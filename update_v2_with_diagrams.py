# Script to update stacksaga-cassandra-support-v2.adoc with all diagrams and callouts
import re

doc_path = r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\pages\cassandra-database-support\stacksaga-cassandra-support-v2.adoc'

with open(doc_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Overview Diagram
intro_target = "This guide covers both concerns completely, starting with the setup steps and ending with a deep-dive into the Recovery Engine's internal architecture.\n"
intro_replacement = """This guide covers both concerns completely, starting with the setup steps and ending with a deep-dive into the Recovery Engine's internal architecture.

.StackSaga Cassandra Ecosystem Architecture
image::stacksaga-database-support:cassandra/stacksaga-diagram-stacksaga-components-database-support-cassandra.svg[alt="StackSaga Cassandra Ecosystem Architecture"]

The system operates across three interconnected environments:

<1> **Orchestrator Application Pods:** Live Spring Boot microservices (such as `order-service`) integrating `stacksaga-spring-boot-starter` and `stacksaga-cassandra-reactive-support`.
<2> **Apache Cassandra Event Store:** Distributed cluster holding the primary transactional event ledger (`es_transaction`) and the 5-tier recovery directory.
<3> **StackSaga Agent & Trace Window:** Sidecar agent capturing execution metrics and streaming them to the central observability console (ports 8080/4545).
"""
text = text.replace(intro_target, intro_replacement, 1)

# 2. es_transaction Diagram
es_txn_target = """=== `es_transaction` — The Primary Transaction Record

Every saga transaction has exactly one row in `es_transaction`, keyed by `transaction_id`.

*Why doesn't this cause hot spots?*
`transaction_id` is a UUID — randomly distributed by Cassandra's Murmur3 partitioner across all cluster nodes with zero coordination.
Even 100,000 concurrent writes land on different nodes uniformly.
"""
es_txn_replacement = """=== `es_transaction` — The Primary Transaction Record

Every saga transaction has exactly one row in `es_transaction`, keyed by `transaction_id`.

*Why doesn't this cause hot spots?*
`transaction_id` is a UUID — randomly distributed by Cassandra's Murmur3 partitioner across all cluster nodes with zero coordination.
Even 100,000 concurrent writes land on different nodes uniformly.

.Managing High Write Throughput via Uniform Murmur3 Partitioning
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-managing-throughput.drawio.svg[alt="Managing High Write Throughput via Uniform Murmur3 Partitioning"]

<1> **Concurrent Inflow:** Client requests trigger simultaneous saga transaction starts across horizontally scaled standard nodes.
<2> **Murmur3 Hash Distribution:** The `transaction_id` (UUID) partition key is passed through Cassandra's 64-bit Murmur3 partitioner.
<3> **Even Cluster Scattering:** Writes are uniformly scattered across physical Cassandra nodes, eliminating database hotspots.
"""
text = text.replace(es_txn_target, es_txn_replacement, 1)

# 3. es_transaction_tryout Diagram
es_tryout_target = """=== `es_transaction_tryout` — The Step Execution History

Each saga step attempt (called a "tryout") is stored as a row under the same `transaction_id` partition key.
Because `transaction_id` is the partition key in both tables, a transaction and its complete step history always live on the **same physical Cassandra node** — reading both never requires a network hop.
"""
es_tryout_replacement = """=== `es_transaction_tryout` — The Step Execution History

Each saga step attempt (called a "tryout") is stored as a row under the same `transaction_id` partition key.
Because `transaction_id` is the partition key in both tables, a transaction and its complete step history always live on the **same physical Cassandra node** — reading both never requires a network hop.

.Colocated Transaction Step History (`es_transaction_tryout`)
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-es-transaction-tryout-table.svg[alt="Colocated Transaction Step History"]

<1> **Shared Partition Key:** Both `es_transaction` and `es_transaction_tryout` use the identical composite partition key `((region, cluster, service_name, transaction_id))`.
<2> **Clustering Rows (`tryout_index ASC`):** Individual saga steps (orders, payments, reservations) append as clustered rows inside the same physical Cassandra partition.
<3> **Zero-Hop Colocation:** When an orchestrator reads a transaction and its full step history, both records are fetched from the exact same physical Cassandra node without cross-node network hops.
"""
text = text.replace(es_tryout_target, es_tryout_replacement, 1)

# 4. Write Protection STRICT callouts & RELAXED diagram + callouts
strict_target = """@enduml
----

=== RELAXED_WITH_DEDUP Mode — Lightweight Read Check

`RELAXED_WITH_DEDUP` skips the LWT (Paxos) overhead entirely.
Before executing, the worker performs a simple read: if a committed marker already exists, it skips.
If two pods arrive at the exact same moment and both read "no marker yet", both will execute — but this is acceptable when the saga step is already idempotent by design.

Use `RELAXED_WITH_DEDUP` when:

* Your saga step is inherently idempotent (e.g., setting a value, not incrementing one)
* Throughput is critical and the double-execution risk is analytically acceptable
"""

strict_replacement = """@enduml
----

<1> **Kafka Event Delivery:** Worker receives an incoming event for a saga step execution.
<2> **Atomic LWT Lease:** Executes an atomic Paxos `INSERT ... IF NOT EXISTS USING TTL` against `es_execution_markers`.
<3> **Mutual Exclusion Check:** If another pod holds an active lease (`TTL > 0`), the worker backs off. If already committed (`TTL = 0`), execution safely skips.
<4> **Permanent Commit Marker:** Upon business logic success, the marker is committed permanently (`TTL = 0`) to prevent any duplicate re-execution.

=== RELAXED_WITH_DEDUP Mode — Lightweight Read Check

`RELAXED_WITH_DEDUP` skips the LWT (Paxos) overhead entirely.
Before executing, the worker performs a simple read: if a committed marker already exists, it skips.
If two pods arrive at the exact same moment and both read "no marker yet", both will execute — but this is acceptable when the saga step is already idempotent by design.

.RELAXED_WITH_DEDUP Mode Execution Flow
[plantuml,target=stacksaga-cassandra-write-protection-relaxed-flow,format=svg]
----
@startuml stacksaga-cassandra-write-protection-relaxed-flow
!theme plain
skinparam backgroundColor #FAFAFA
skinparam defaultFontName "DejaVu Sans"
skinparam defaultFontSize 12
skinparam conditionStyle InsideDiamond
skinparam shadowing false

skinparam activity {
  BackgroundColor #EEF4FF
  BorderColor #4A6FA5
  FontColor #1A1A2E
}

skinparam diamond {
  BackgroundColor #FFF9E6
  BorderColor #E0A800
  FontColor #1A1A2E
}

skinparam arrow {
  Color #4A6FA5
  FontColor #1A1A2E
}

start

:Receive Kafka event for saga step;

:Check if ExecutionMarker exists in Cassandra
(Fast read: SELECT FROM es_execution_markers);

if (Marker already exists?) then (YES)
  :Duplicate delivery detected;
  :Skip execution safely without side effects;
  stop

else (NO)
  :Execute saga step business logic;

  repeat
    :Persist event data + permanent ExecutionMarker
    (Atomic logged batch write with TTL = 0);
  backward:Retry batch write;
  repeat while (Batch write\\nsuccessful?) is (NO) not (YES)

  :Dispatch state-changed events to listeners;
  stop

endif

@enduml
----

<1> **Lightweight Read Check:** Fast non-blocking read against `es_execution_markers` without Paxos consensus round-trips.
<2> **Duplicate Skip:** If an existing marker is discovered, the pod immediately terminates the attempt safely.
<3> **Atomic Logged Batch Write:** Step state and execution marker are committed together in a single Cassandra batch.

Use `RELAXED_WITH_DEDUP` when:

* Your saga step is inherently idempotent (e.g., setting a value, not incrementing one)
* Throughput is critical and the double-execution risk is analytically acceptable
"""
text = text.replace(strict_target, strict_replacement, 1)

# 5. 5-Tier Directory Diagram
tier_target = """=== The 5-Tier Directory: The Architecture at a Glance

[source,text]
----
es_days_by_year                            ← Tier 1: Which days have pending work?
  └── es_recovery_windows_by_day           ← Tier 2: Which minute windows on that day?
        └── es_instances_by_recovery_window← Tier 3: Which pods wrote failures in that window?
              └── es_buckets_by_instance   ← Tier 4: Which bucket partitions did that pod create?
                    └── es_recovery_transactions_by_instance  ← Tier 5: The actual transaction IDs.
----

Workers never scan empty tables.
Every query at every tier provides the full composite partition key of the tier above it, descending the tree until they find `transaction_id` values to re-invoke.
"""

tier_replacement = """=== The 5-Tier Directory: The Architecture at a Glance

[source,text]
----
es_days_by_year                            ← Tier 1: Which days have pending work?
  └── es_recovery_windows_by_day           ← Tier 2: Which minute windows on that day?
        └── es_instances_by_recovery_window← Tier 3: Which pods wrote failures in that window?
              └── es_buckets_by_instance   ← Tier 4: Which bucket partitions did that pod create?
                    └── es_recovery_transactions_by_instance  ← Tier 5: The actual transaction IDs.
----

Workers never scan empty tables.
Every query at every tier provides the full composite partition key of the tier above it, descending the tree until they find `transaction_id` values to re-invoke.

.StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-hierarchical-retry-schema.svg[alt="StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store"]

The active directory tree operates through five coordinated tiers:

<1> **Tier 1 (`es_days_by_year`) — Active Calendar Dates:** Tracks which calendar dates contain pending recovery records. Workers query active dates directly, eliminating empty table scans.
<2> **Tier 2 (`es_recovery_windows_by_day`) — Minute Windows per Day:** Divides each 24-hour day into discrete UTC minute windows (`0` to `1439`). Workers traverse windows in ascending order (`minute_of_day ASC`), guaranteeing older failures are retried first.
<3> **Tier 3 (`es_instances_by_recovery_window`) — Token-Partitioned Worker Slicing:** Records which pods registered records in that minute window, clustered by their 64-bit Murmur3 token (`instance_id_token = token(instance_id)`). Enables spatial sector queries without row locks.
<4> **Tier 4 (`es_buckets_by_instance`) — Bucket Allocation Directory:** Records sequential bucket indices per instance. Even indices (0, 2, 4...) represent retry partitions; odd indices (1, 3, 5...) represent restore partitions.
<5> **Tier 5 (`es_recovery_transactions_by_instance`) — Bounded Partitions:** Stores strictly lightweight metadata pointers (~50–100 bytes per row) bounded below 50,000 rows. Dropped in $O(1)$ time via partition tombstones upon completion.
<6> **Primary Event Store (`es_transaction`) — Decoupled Payload:** Stores the heavy business payload and full saga execution history. Hydrated lazily by `transaction_id`, keeping recovery directory partitions tiny.
"""
text = text.replace(tier_target, tier_replacement, 1)

# 6. Instance-Level Local Bucketing Diagram
bucketing_target = """Each 50,000-row partition holds only metadata pointers (~50–100 bytes per row) — never business payloads.
A full 50,000-row partition consumes **~3MB to 5MB on disk**, regardless of saga payload size.
Cassandra's 100MB partition limit is structurally impossible to reach.
"""

bucketing_replacement = """Each 50,000-row partition holds only metadata pointers (~50–100 bytes per row) — never business payloads.
A full 50,000-row partition consumes **~3MB to 5MB on disk**, regardless of saga payload size.
Cassandra's 100MB partition limit is structurally impossible to reach.

.Instance-Level Local Bucketing & Autonomous Worker Re-Distribution
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-instance-bucket-distribution.svg[alt="Instance-Level Local Bucketing & Autonomous Worker Re-Distribution"]

<1> **Ephemeral Orchestrator Pods (Live Writers):** Every live pod independently maintains in-memory `AtomicLong` counters. Checking and incrementing takes ~2 nanoseconds, adding zero read latency to live traffic.
<2> **Isolated Bounded Partitions (Cassandra Tier 5):** Because `instance_id` and `bucket_index` are embedded in the partition key, writes land in dedicated partitions capped at 50,000 rows (~3–5MB), remaining far below Cassandra's 100MB limit.
<3> **Deterministic Spatial Mapping (`instance_id_token = token(instance_id)`):** Pods register their presence in Tier 3 along with their Murmur3 token hash, uniformly distributed across the 64-bit token ring (`-2^63` to `2^63 - 1`).
<4> **Autonomous Worker Discovery:** Retry-Nodes query Tier 3 within their assigned token sector lease (`WHERE instance_id_token >= min AND instance_id_token < max`), claiming instances deterministically without cross-node locking.
<5> **Lifecycle Decoupling (Pod Crash Guarantee):** Writer pods can terminate, restart, or scale to zero immediately after writing failure records without impacting recovery.
"""
text = text.replace(bucketing_target, bucketing_replacement, 1)

# 7. Dual-Window Model Diagram
dual_target = """This also provides a free **cooldown buffer** of up to 70 seconds before a failed step is first retried.
This prevents the Retry-Node from immediately hammering a downstream service that is still rebooting.
"""

dual_replacement = """This also provides a free **cooldown buffer** of up to 70 seconds before a failed step is first retried.
This prevents the Retry-Node from immediately hammering a downstream service that is still rebooting.

.Dual-Window Synchronization Timeline: Writer & Reader Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-dual-window-timeline.svg[alt="Dual-Window Synchronization Timeline"]

<1> **Active Write Window ($W+1$):** Live Standard-Nodes append transient failures exclusively into the future minute window ($W+1$), completely isolated from active reader queries.
<2> **Sealed Read Windows ($\le W$):** Retry-Nodes scan only completed, sealed windows ($\le W$). Because writers never touch windows $\le W$, readers experience zero lock contention or phantom reads.
<3> **Natural Cooldown Buffer:** Writing ahead into $W+1$ introduces an automatic buffer (up to 70 seconds) before the first retry attempt, preventing workers from hammering a downstream service that is still rebooting.
<4> **UTC Midnight Rollover:** When the current window reaches 1439, the target write window seamlessly wraps around to minute 0 of the next calendar day (`date_of_year + 1`).
"""
text = text.replace(dual_target, dual_replacement, 1)

# 8. Spatial Isolation via Murmur3 Diagram
spatial_target = """Every query and every step execution verifies that the current timestamp is within the lease validity window.
If a lease expires (e.g., network partition), execution stops immediately — preventing split-brain processing while the coordinator redistributes leases.
"""

spatial_replacement = """Every query and every step execution verifies that the current timestamp is within the lease validity window.
If a lease expires (e.g., network partition), execution stops immediately — preventing split-brain processing while the coordinator redistributes leases.

.Murmur3 Token Ring Slicing & Spatial Worker Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-token-ring-instance-mapping.svg[alt="Murmur3 Token Ring Slicing & Spatial Worker Isolation"]

<1> **64-bit Murmur3 Token Ring:** The continuous token ring spans `-9,223,372,036,854,775,808` to `+9,223,372,036,854,775,807`.
<2> **Non-Overlapping Sector Leases:** The RSocket Ring Coordinator divides the ring into non-overlapping sectors and issues time-bounded leases to active Retry-Nodes.
<3> **Instance Token Clustering:** Standard-Node tokens stored in Tier 3 map deterministically into exactly one worker's leased range.
<4> **Autonomous Slicing:** Each Retry-Node sweeps only its assigned token sector, ensuring zero duplicate processing without database row locks.
"""
text = text.replace(spatial_target, spatial_replacement, 1)

# 9. Traversal Pipeline & Safe Shutdown Diagram
shutdown_target = """When a Retry-Node is killed mid-bucket, the partition stays intact in Cassandra.
The next Retry-Node (or the restarted one) picks it up from row 1.
Execution markers (`es_execution_markers`) ensure that already-completed saga steps are detected as `COMMITTED` and skipped — so only the genuinely unprocessed transactions (e.g., rows #25,001 through #50,000) actually execute again.
"""

shutdown_replacement = """When a Retry-Node is killed mid-bucket, the partition stays intact in Cassandra.
The next Retry-Node (or the restarted one) picks it up from row 1.
Execution markers (`es_execution_markers`) ensure that already-completed saga steps are detected as `COMMITTED` and skipped — so only the genuinely unprocessed transactions (e.g., rows #25,001 through #50,000) actually execute again.

.Top-Down Traversal & Compaction Lifecycle Pipeline
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-traversal-pipeline.svg[alt="Top-Down Traversal & Compaction Lifecycle Pipeline"]

The complete traversal and execution pipeline operates across five stages:

<1> **Top-Down Directory Discovery:** Workers traverse Tier 1 (calendar day) → Tier 2 (minute window) → Tier 3 (token-filtered instances) → Tier 4 (bucket indices).
<2> **Tier 5 Stream & Lazy Payload Hydration:** Worker streams lightweight `transaction_id` rows from Tier 5 and lazily fetches the business payload from `es_transaction`.
<3> **Controlled Concurrent Dispatch:** Transactions are dispatched for step execution up to `recovery.concurrency` (default: 100).
<4> **Safe Shutdown Barrier:** If a pod is killed mid-bucket, the partition is preserved in Cassandra. Upon restart, execution markers ensure already-completed steps are skipped.
<5> **O(1) Partition Compaction:** When all transactions in a bucket are dispatched, the worker drops the entire partition with a single partition tombstone.
"""
text = text.replace(shutdown_target, shutdown_replacement, 1)

# 10. Deep Historical Recovery Diagram
history_target = """If the entire service was offline for a weekend, all of Friday's, Saturday's, and Sunday's pending retry windows are systematically discovered and processed on Monday morning — oldest first.
"""

history_replacement = """If the entire service was offline for a weekend, all of Friday's, Saturday's, and Sunday's pending retry windows are systematically discovered and processed on Monday morning — oldest first.

.Deep Historical Lookback Across Calendar Days
image::stacksaga-database-support:cassandra/stacksaga-diagram-stacksaga-cassandra-how-transactions-saved-for-recovery.svg[alt="Deep Historical Lookback Across Calendar Days"]

<1> **Lookback Window Calculation:** On startup, workers calculate candidate lookback dates based on `recovery.retry.lookback-days` (e.g. `[today - 2 days .. today]`).
<2> **Ascending Date Traversal:** Workers query Tier 1 (`es_days_by_year`) in ascending order (`date_of_year ASC`), processing older calendar days first.
<3> **Sequential Minute Window Sweep:** Pending minute windows are swept chronologically, recovering transactions from extended outages (e.g. over a weekend).
<4> **Seamless Live Transition:** Once historical windows are cleared, workers seamlessly transition to the live stream.
"""
text = text.replace(history_target, history_replacement, 1)

# 11. Restore Dead-Man's Switch Diagram
restore_target = """| **JVM crashes mid-transaction**
| The watchdog row was never deleted.
600 minutes later, a Retry-Node traverses the directory, reaches that restore window, finds the watchdog row in the odd bucket, and re-invokes the transaction.
The transaction is recovered automatically — with zero developer action.
|===
"""

restore_replacement = """| **JVM crashes mid-transaction**
| The watchdog row was never deleted.
600 minutes later, a Retry-Node traverses the directory, reaches that restore window, finds the watchdog row in the odd bucket, and re-invokes the transaction.
The transaction is recovered automatically — with zero developer action.
|===

.The Restore Feature: Dead-Man's Switch Lifecycle
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-restore-dead-mans-switch.svg[alt="The Restore Feature: Dead-Man's Switch Lifecycle"]

<1> **Watchdog Registration:** On transaction start, the Standard-Node computes the far-future restore window ($W + \\text{delay}$) and writes a watchdog row into an odd bucket.
<2> **Path Stored in Primary Ledger:** The partition path `(date, window, instance_id, odd_bucket)` is durably saved in `es_transaction`.
<3> **Path A (Normal Completion):** Upon success or compensation, the pod issues an immediate targeted $O(1)$ delete of the watchdog row. The restore window remains clean.
<4> **Path B (Silent Pod Crash):** If the pod dies mid-flight (power outage, OOM kill), the watchdog row is never deleted and persists safely in Cassandra.
<5> **Restore Window Discovery:** When the restore window arrives and becomes sealed ($\\le W$), a Retry-Node discovers the odd bucket via its token lease.
<6> **Mandatory Status Check:** The engine reads `es_transaction.running_status`. If already completed, the row is deleted and skipped.
<7> **Automatic Resumption:** If still in-flight, the transaction is automatically re-invoked with zero data loss.
"""
text = text.replace(restore_target, restore_replacement, 1)

# 12. Odd vs Even Bucket Segregation Diagram
odd_even_target = """3. **Independent window schedules.**
   Retry windows are 1 window ahead (W+1).
   Restore windows are hundreds of windows ahead (W + 600).
   These are entirely different points in time.
   A single shared counter spanning both would make it impossible to bound either type's partitions correctly.
"""

odd_even_replacement = """3. **Independent window schedules.**
   Retry windows are 1 window ahead (W+1).
   Restore windows are hundreds of windows ahead (W + 600).
   These are entirely different points in time.
   A single shared counter spanning both would make it impossible to bound either type's partitions correctly.

.Odd vs. Even Bucket Segregation & Tombstone Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-odd-even-bucket-segregation.svg[alt="Odd vs. Even Bucket Segregation & Tombstone Isolation"]

<1> **Dual In-Memory Counters:** Standard-Nodes maintain independent `AtomicLong` counters for retry (even) and restore (odd) in local JVM memory.
<2> **Even Buckets (Pure Retry Lane):** Written only on transient failure. Zero row-by-row deletions occur, meaning partitions contain 0% cell tombstones and drop cleanly via single partition tombstones.
<3> **Odd Buckets (Restore Watchdog Lane):** Written on every transaction start and deleted on success. High-frequency cell tombstones are strictly quarantined inside odd partitions.
<4> **Cassandra Read Protection:** Retry-Nodes scanning retry buckets never encounter cell tombstones, completely preventing Cassandra `ReadFailureException` (>100,000 tombstones).
"""
text = text.replace(odd_even_target, odd_even_replacement, 1)

# 13. Virtual Clusters Diagram
virtual_target = """For 99.9% of deployments, the default single cluster is sufficient.
Virtual clusters exist for the rare hyperscale case where even 10,000 pods per cluster is not enough.
----
"""

virtual_replacement = """For 99.9% of deployments, the default single cluster is sufficient.
Virtual clusters exist for the rare hyperscale case where even 10,000 pods per cluster is not enough.
----

.Horizontal Scaling via Virtual Clusters & Regional Cell Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-virtual-clusters.svg[alt="Horizontal Scaling via Virtual Clusters & Regional Cell Isolation"]

<1> **Shared Physical Cassandra Cluster:** All virtual clusters reside within the same physical Cassandra cluster and share the exact same keyspace.
<2> **Virtual Cluster Cell 1 (`cluster = cluster-1`):** Autonomous deployment cell with its own dedicated Ring Coordinator and Retry-Nodes.
<3> **Virtual Cluster Cell 2 (`cluster = cluster-2`):** Second autonomous deployment cell operating independently within the same region.
<4> **Tier 3 Partition Key Isolation:** Because `cluster` is embedded in the composite partition key `((region, cluster, service_name, date_of_year, minute_of_day))`, each cell's pod count stays strictly bounded below the 50,000 pod ceiling.
"""
text = text.replace(virtual_target, virtual_replacement, 1)

# 14. Node-0 Two-Gate Protocol Diagram
node0_target = """Only when **both gates pass** does Node-0 safely delete the minute window from Tier 2.
After all windows for a given date are cleared, it deletes the date from Tier 1.

This protocol eliminates the premature deletion race condition without any distributed locking.
"""

node0_replacement = """Only when **both gates pass** does Node-0 safely delete the minute window from Tier 2.
After all windows for a given date are cleared, it deletes the date from Tier 1.

This protocol eliminates the premature deletion race condition without any distributed locking.

.Directory Compaction: Node-0 Compactor Overseer Two-Gate Verification Protocol
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-node0-compaction-gates.svg[alt="Node-0 Compactor Overseer Two-Gate Verification Protocol"]

<1> **Worker Compaction:** Normal Retry-Nodes (Node-1, Node-2) drop only their own Tier 5 bucket partitions and their own Tier 3 instance markers.
<2> **The Premature Deletion Hazard:** If a fast worker (5 transactions) could delete Tier 2 minute windows directly, it would orphan transactions still being processed by a slower peer worker (40,000 transactions).
<3> **Node-0 Compactor Overseer:** Node-0 (anchor token lease holder) is the sole authority permitted to prune shared upper tiers (Tier 2 and Tier 1).
<4> **Gate 1 (Cluster-Wide Completion):** Node-0 queries Tier 3 across the entire cluster without token filtering. It must return 0 rows before proceeding.
<5> **Gate 2 (Wall-Clock Time Barrier):** Node-0 verifies that the current UTC time is past the window end time, ensuring live Standard-Nodes have progressed to subsequent write windows ($W+1$).
<6> **Safe Upper Pruning:** Once both gates pass, Node-0 deletes the completed minute window from Tier 2, and deletes the calendar date from Tier 1 once all windows are cleared.
"""
text = text.replace(node0_target, node0_replacement, 1)

with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated stacksaga-cassandra-support-v2.adoc successfully!")
