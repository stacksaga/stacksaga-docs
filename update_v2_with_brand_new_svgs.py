# -*- coding: utf-8 -*-
"""
Script to update stacksaga-cassandra-support-v2.adoc with the 15 brand-new, unified SVGs.
Replaces all old diagram references and PlantUML diagrams with the new stacksaga-v2-XX SVGs and exact callouts.
"""

doc_path = r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\pages\cassandra-database-support\stacksaga-cassandra-support-v2.adoc'

with open(doc_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace Overview Diagram
old_01 = """.StackSaga Cassandra Ecosystem Architecture
image::stacksaga-database-support:cassandra/stacksaga-diagram-stacksaga-components-database-support-cassandra.svg[alt="StackSaga Cassandra Ecosystem Architecture"]

The system operates across three interconnected environments:

<1> **Orchestrator Application Pods:** Live Spring Boot microservices (such as `order-service`) integrating `stacksaga-spring-boot-starter` and `stacksaga-cassandra-reactive-support`.
<2> **Apache Cassandra Event Store:** Distributed cluster holding the primary transactional event ledger (`es_transaction`) and the 5-tier recovery directory.
<3> **StackSaga Agent & Trace Window:** Sidecar agent capturing execution metrics and streaming them to the central observability console (ports 8080/4545)."""

new_01 = """.StackSaga Cassandra Ecosystem Architecture
image::stacksaga-database-support:cassandra/stacksaga-v2-01-ecosystem-overview.svg[alt="StackSaga Cassandra Ecosystem Architecture"]

The system operates across three interconnected environments:

<1> **Microservice Application Pod:** Live Spring Boot microservices (such as `order-service`) integrating `stacksaga-spring-boot-starter` and `stacksaga-cassandra-reactive-support`.
<2> **Apache Cassandra Cluster:** Distributed data tier storing both the Core Event Store (`es_transaction`, `es_transaction_tryout`) and the 5-Tier Recovery Directory.
<3> **StackSaga Trace Window:** Central web observability console connected via the StackSaga Agent sidecar (port 4545/8080) for real-time visualization of saga state."""

text = text.replace(old_01, new_01, 1)

# 2. Replace es_transaction Diagram
old_02 = """.Managing High Write Throughput via Uniform Murmur3 Partitioning
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-managing-throughput.drawio.svg[alt="Managing High Write Throughput via Uniform Murmur3 Partitioning"]

<1> **Concurrent Inflow:** Client requests trigger simultaneous saga transaction starts across horizontally scaled standard nodes.
<2> **Murmur3 Hash Distribution:** The `transaction_id` (UUID) partition key is passed through Cassandra's 64-bit Murmur3 partitioner.
<3> **Even Cluster Scattering:** Writes are uniformly scattered across physical Cassandra nodes, eliminating database hotspots."""

new_02 = """.Managing High Write Throughput via Uniform Murmur3 Partitioning
image::stacksaga-database-support:cassandra/stacksaga-v2-02-transaction-throughput.svg[alt="Managing High Write Throughput via Uniform Murmur3 Partitioning"]

<1> **High Inflow Requests:** Over 100,000 concurrent saga transactions initiated simultaneously across horizontally scaled standard nodes.
<2> **Murmur3 Partitioner:** Cassandra's 64-bit Murmur3 hash uniformly scatters `transaction_id` (UUID) across the token space with zero coordination and zero lock contention.
<3> **Even Cluster Scattering:** Writes land uniformly across physical nodes, ensuring CPU, memory, and disk I/O remain balanced without hot spots."""

text = text.replace(old_02, new_02, 1)

# 3. Replace es_transaction_tryout Diagram
old_03 = """.Colocated Transaction Step History (`es_transaction_tryout`)
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-es-transaction-tryout-table.svg[alt="Colocated Transaction Step History"]

<1> **Shared Partition Key:** Both `es_transaction` and `es_transaction_tryout` use the identical composite partition key `((region, cluster, service_name, transaction_id))`.
<2> **Clustering Rows (`tryout_index ASC`):** Individual saga steps (orders, payments, reservations) append as clustered rows inside the same physical Cassandra partition.
<3> **Zero-Hop Colocation:** When an orchestrator reads a transaction and its full step history, both records are fetched from the exact same physical Cassandra node without cross-node network hops."""

new_03 = """.Colocated Transaction Step History (`es_transaction_tryout`)
image::stacksaga-database-support:cassandra/stacksaga-v2-03-tryout-colocation.svg[alt="Colocated Transaction Step History"]

<1> **Physical Cassandra Node Colocation:** Because `es_transaction` and `es_transaction_tryout` share the identical composite partition key `((region, cluster, service_name, transaction_id))`, all records for a given transaction reside on the exact same physical node.
<2> **Step Execution Clustering Rows:** Individual saga attempts append as ordered clustering rows (`tryout_index ASC`) within the partition.
<3> **Zero-Hop Colocated Read:** Fetching a transaction and its full step history requires zero cross-node network hops, maximizing read performance."""

text = text.replace(old_03, new_03, 1)

# 4. Replace STRICT Mode PlantUML with SVG 04
old_04_target = """[plantuml,target=stacksaga-cassandra-write-protection-flow,format=svg]
----
@startuml stacksaga-cassandra-write-protection-flow
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

repeat
  :Attempt to acquire temporary lease in Cassandra
  (INSERT IF NOT EXISTS USING TTL);

  if (Lease acquired?) then (yes — row did not exist)
    :Execute saga step business logic;
    :Commit permanent marker (TTL = 0);
    stop
  else (no)
    if (Existing marker TTL = 0?) then (yes — already committed)
      :Skip — step already completed by another pod;
      stop
    else (no — TTL > 0, still in-flight)
      :Back off and wait for TTL to expire;
    endif
  endif
repeat while (Retrying)

@enduml
----

<1> **Kafka Event Delivery:** Worker receives an incoming event for a saga step execution.
<2> **Atomic LWT Lease:** Executes an atomic Paxos `INSERT ... IF NOT EXISTS USING TTL` against `es_execution_markers`.
<3> **Mutual Exclusion Check:** If another pod holds an active lease (`TTL > 0`), the worker backs off. If already committed (`TTL = 0`), execution safely skips.
<4> **Permanent Commit Marker:** Upon business logic success, the marker is committed permanently (`TTL = 0`) to prevent any duplicate re-execution."""

new_04 = """.STRICT Mode Write Protection Flow
image::stacksaga-database-support:cassandra/stacksaga-v2-04-write-protection-strict.svg[alt="STRICT Mode Write Protection Flow"]

<1> **Kafka Event Inflow:** A saga step execution event arrives from Kafka with potential at-least-once duplicate delivery.
<2> **Paxos LWT Lease Acquisition:** The pod executes an atomic `INSERT ... IF NOT EXISTS USING TTL 5s` into `es_execution_markers`. If a lease exists with `TTL > 0`, the pod backs off; if `TTL = 0`, it skips.
<3> **Mutual Exclusive Execution:** The single pod holding the active lease executes the saga business logic.
<4> **Permanent Marker Commit:** On success, the marker is committed with `TTL = 0`, conferring permanent duplicate immunity."""

text = text.replace(old_04_target, new_04, 1)

# 5. Replace RELAXED Mode PlantUML with SVG 05
old_05_target = """.RELAXED_WITH_DEDUP Mode Execution Flow
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
<3> **Atomic Logged Batch Write:** Step state and execution marker are committed together in a single Cassandra batch."""

new_05 = """.RELAXED_WITH_DEDUP Mode Execution Flow
image::stacksaga-database-support:cassandra/stacksaga-v2-05-write-protection-relaxed.svg[alt="RELAXED_WITH_DEDUP Mode Execution Flow"]

<1> **Kafka Event Inflow:** Event received on high-throughput streaming pipelines where operations are inherently idempotent.
<2> **Non-Blocking Read Check:** Executes a fast read against `es_execution_markers` without Paxos consensus overhead. If a marker exists, execution terminates immediately.
<3> **Atomic Batch Write:** Step results and execution markers are committed together in a single logged batch write."""

text = text.replace(old_05_target, new_05, 1)

# 6. Replace 5-Tier Directory Diagram
old_06 = """.StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-hierarchical-retry-schema.svg[alt="StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store"]

The active directory tree operates through five coordinated tiers:

<1> **Tier 1 (`es_days_by_year`) — Active Calendar Dates:** Tracks which calendar dates contain pending recovery records. Workers query active dates directly, eliminating empty table scans.
<2> **Tier 2 (`es_recovery_windows_by_day`) — Minute Windows per Day:** Divides each 24-hour day into discrete UTC minute windows (`0` to `1439`). Workers traverse windows in ascending order (`minute_of_day ASC`), guaranteeing older failures are retried first.
<3> **Tier 3 (`es_instances_by_recovery_window`) — Token-Partitioned Worker Slicing:** Records which pods registered records in that minute window, clustered by their 64-bit Murmur3 token (`instance_id_token = token(instance_id)`). Enables spatial sector queries without row locks.
<4> **Tier 4 (`es_buckets_by_instance`) — Bucket Allocation Directory:** Records sequential bucket indices per instance. Even indices (0, 2, 4...) represent retry partitions; odd indices (1, 3, 5...) represent restore partitions.
<5> **Tier 5 (`es_recovery_transactions_by_instance`) — Bounded Partitions:** Stores strictly lightweight metadata pointers (~50–100 bytes per row) bounded below 50,000 rows. Dropped in $O(1)$ time via partition tombstones upon completion.
<6> **Primary Event Store (`es_transaction`) — Decoupled Payload:** Stores the heavy business payload and full saga execution history. Hydrated lazily by `transaction_id`, keeping recovery directory partitions tiny."""

new_06 = """.StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store
image::stacksaga-database-support:cassandra/stacksaga-v2-06-5tier-recovery-hierarchy.svg[alt="StackSaga 5-Tier Recovery Directory Hierarchy & Primary Event Store"]

The active directory tree operates through five coordinated tiers:

<1> **Tier 1 (`es_days_by_year`):** Active calendar dates index preventing empty table scans.
<2> **Tier 2 (`es_recovery_windows_by_day`):** UTC minute windows (`0` to `1439`) processed in ascending order (`minute_of_day ASC`).
<3> **Tier 3 (`es_instances_by_recovery_window`):** Pod instance tokens clustered by `token(instance_id)` for spatial worker slicing.
<4> **Tier 4 (`es_buckets_by_instance`):** Bucket index directory (even = retry, odd = restore).
<5> **Tier 5 (`es_recovery_transactions_by_instance`):** Bounded metadata partitions (< 50,000 rows, ~3–5MB) dropped via single partition tombstones in $O(1)$ time.
<6> **Primary Event Store (`es_transaction`):** Decoupled heavy state hydrated lazily by `transaction_id`."""

text = text.replace(old_06, new_06, 1)

# 7. Replace Local Bucketing Diagram
old_07 = """.Instance-Level Local Bucketing & Autonomous Worker Re-Distribution
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-instance-bucket-distribution.svg[alt="Instance-Level Local Bucketing & Autonomous Worker Re-Distribution"]

<1> **Ephemeral Orchestrator Pods (Live Writers):** Every live pod independently maintains in-memory `AtomicLong` counters. Checking and incrementing takes ~2 nanoseconds, adding zero read latency to live traffic.
<2> **Isolated Bounded Partitions (Cassandra Tier 5):** Because `instance_id` and `bucket_index` are embedded in the partition key, writes land in dedicated partitions capped at 50,000 rows (~3–5MB), remaining far below Cassandra's 100MB limit.
<3> **Deterministic Spatial Mapping (`instance_id_token = token(instance_id)`):** Pods register their presence in Tier 3 along with their Murmur3 token hash, uniformly distributed across the 64-bit token ring (`-2^63` to `2^63 - 1`).
<4> **Autonomous Worker Discovery:** Retry-Nodes query Tier 3 within their assigned token sector lease (`WHERE instance_id_token >= min AND instance_id_token < max`), claiming instances deterministically without cross-node locking.
<5> **Lifecycle Decoupling (Pod Crash Guarantee):** Writer pods can terminate, restart, or scale to zero immediately after writing failure records without impacting recovery."""

new_07 = """.Instance-Level Local Bucketing & Autonomous Worker Re-Distribution
image::stacksaga-database-support:cassandra/stacksaga-v2-07-instance-local-bucketing.svg[alt="Instance-Level Local Bucketing & Autonomous Worker Re-Distribution"]

<1> **Live Writer Pods:** Each pod maintains JVM-local `AtomicLong` counters. Checking and incrementing takes ~2 nanoseconds without database locks.
<2> **Tier 5 Bounded Partitions:** Partitions are scoped by `instance_id` and bounded to 50,000 rows. When full, the pod atomically rolls to the next even index (e.g. Bucket 0 → Bucket 2).
<3> **Spatial Mapping in Tier 3:** Pods register their token hash `token(instance_id)` uniformly across the 64-bit token ring.
<4> **Autonomous Worker Discovery:** Retry-Nodes sweep assigned token sector leases, discovering instances deterministically without cross-worker locking.
<5> **Lifecycle Decoupling:** Writer pods can terminate, restart, or scale to zero immediately after writing failure records without impacting recovery."""

text = text.replace(old_07, new_07, 1)

# 8. Replace Dual-Window Diagram
old_08 = """.Dual-Window Synchronization Timeline: Writer & Reader Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-dual-window-timeline.svg[alt="Dual-Window Synchronization Timeline"]

<1> **Active Write Window ($W+1$):** Live Standard-Nodes append transient failures exclusively into the future minute window ($W+1$), completely isolated from active reader queries.
<2> **Sealed Read Windows ($\le W$):** Retry-Nodes scan only completed, sealed windows ($\le W$). Because writers never touch windows $\le W$, readers experience zero lock contention or phantom reads.
<3> **Natural Cooldown Buffer:** Writing ahead into $W+1$ introduces an automatic buffer (up to 70 seconds) before the first retry attempt, preventing workers from hammering a downstream service that is still rebooting.
<4> **UTC Midnight Rollover:** When the current window reaches 1439, the target write window seamlessly wraps around to minute 0 of the next calendar day (`date_of_year + 1`)."""

new_08 = """.Dual-Window Synchronization Timeline: Writer & Reader Isolation
image::stacksaga-database-support:cassandra/stacksaga-v2-08-dual-window-timeline.svg[alt="Dual-Window Synchronization Timeline"]

<1> **Active Write Window ($W+1$):** Standard-Nodes write transient failures into the future window, completely isolated from active reader queries.
<2> **Sealed Read Windows ($\le W$):** Retry-Nodes read only completed, sealed windows. Zero phantom reads, zero lock contention.
<3> **Cooldown Buffer:** Writing to $W+1$ provides an automatic buffer (up to 70 seconds) before the first retry attempt.
<4> **Midnight Rollover:** Window 1439 wraps smoothly to minute 0 of the next calendar day (`date_of_year + 1`)."""

text = text.replace(old_08, new_08, 1)

# 9. Replace Spatial Ring Diagram
old_09 = """.Murmur3 Token Ring Slicing & Spatial Worker Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-token-ring-instance-mapping.svg[alt="Murmur3 Token Ring Slicing & Spatial Worker Isolation"]

<1> **64-bit Murmur3 Token Ring:** The continuous token ring spans `-9,223,372,036,854,775,808` to `+9,223,372,036,854,775,807`.
<2> **Non-Overlapping Sector Leases:** The RSocket Ring Coordinator divides the ring into non-overlapping sectors and issues time-bounded leases to active Retry-Nodes.
<3> **Instance Token Clustering:** Standard-Node tokens stored in Tier 3 map deterministically into exactly one worker's leased range.
<4> **Autonomous Slicing:** Each Retry-Node sweeps only its assigned token sector, ensuring zero duplicate processing without database row locks."""

new_09 = """.Murmur3 Token Ring Slicing & Spatial Worker Isolation
image::stacksaga-database-support:cassandra/stacksaga-v2-09-spatial-token-ring.svg[alt="Murmur3 Token Ring Slicing & Spatial Worker Isolation"]

<1> **64-bit Murmur3 Token Ring:** Spans `-2^63` to `+2^63 - 1`.
<2> **Ring Coordinator:** Divides the token ring into non-overlapping sectors and issues time-bounded leases.
<3> **Worker Leases:** Each Retry-Node queries Tier 3 using its leased sector bounds (`WHERE token >= min AND token < max`).
<4> **Autonomous Slicing:** Linear horizontal scaling with zero duplicate processing and zero database row locks."""

text = text.replace(old_09, new_09, 1)

# 10. Replace Traversal Pipeline Diagram
old_10 = """.Top-Down Traversal & Compaction Lifecycle Pipeline
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-traversal-pipeline.svg[alt="Top-Down Traversal & Compaction Lifecycle Pipeline"]

The complete traversal and execution pipeline operates across five stages:

<1> **Top-Down Directory Discovery:** Workers traverse Tier 1 (calendar day) → Tier 2 (minute window) → Tier 3 (token-filtered instances) → Tier 4 (bucket indices).
<2> **Tier 5 Stream & Lazy Payload Hydration:** Worker streams lightweight `transaction_id` rows from Tier 5 and lazily fetches the business payload from `es_transaction`.
<3> **Controlled Concurrent Dispatch:** Transactions are dispatched for step execution up to `recovery.concurrency` (default: 100).
<4> **Safe Shutdown Barrier:** If a pod is killed mid-bucket, the partition is preserved in Cassandra. Upon restart, execution markers ensure already-completed steps are skipped.
<5> **O(1) Partition Compaction:** When all transactions in a bucket are dispatched, the worker drops the entire partition with a single partition tombstone."""

new_10 = """.Top-Down Traversal & Compaction Lifecycle Pipeline
image::stacksaga-database-support:cassandra/stacksaga-v2-10-traversal-pipeline.svg[alt="Top-Down Traversal & Compaction Lifecycle Pipeline"]

<1> **Discovery:** Top-down sweep from Tier 1 down to Tier 4 without empty table scans.
<2> **Hydration:** Stream lightweight pointers from Tier 5 and lazily fetch payloads from `es_transaction`.
<3> **Dispatch:** Concurrent re-invocation up to `recovery.concurrency` (default: 100).
<4> **Safe Shutdown Barrier:** If a pod is killed mid-bucket, the partition is preserved in Cassandra; completed steps are skipped upon restart.
<5> **O(1) Compaction Drop:** When 100% dispatched, the entire bucket partition is dropped with a single partition tombstone."""

text = text.replace(old_10, new_10, 1)

# 11. Replace Historical Recovery Diagram
old_11 = """.Deep Historical Lookback Across Calendar Days
image::stacksaga-database-support:cassandra/stacksaga-diagram-stacksaga-cassandra-how-transactions-saved-for-recovery.svg[alt="Deep Historical Lookback Across Calendar Days"]

<1> **Lookback Window Calculation:** On startup, workers calculate candidate lookback dates based on `recovery.retry.lookback-days` (e.g. `[today - 2 days .. today]`).
<2> **Ascending Date Traversal:** Workers query Tier 1 (`es_days_by_year`) in ascending order (`date_of_year ASC`), processing older calendar days first.
<3> **Sequential Minute Window Sweep:** Pending minute windows are swept chronologically, recovering transactions from extended outages (e.g. over a weekend).
<4> **Seamless Live Transition:** Once historical windows are cleared, workers seamlessly transition to the live stream."""

new_11 = """.Deep Historical Lookback Across Calendar Days
image::stacksaga-database-support:cassandra/stacksaga-v2-11-deep-historical-recovery.svg[alt="Deep Historical Lookback Across Calendar Days"]

<1> **Lookback Range Calculation:** On startup, workers calculate candidate dates based on `recovery.retry.lookback-days`.
<2> **Ascending Day Sweep:** Workers traverse Tier 1 in ascending order (`date_of_year ASC`), recovering older backlog first.
<3> **Live Transition:** Once historical windows are processed, workers transition smoothly to the live minute stream ($W$)."""

text = text.replace(old_11, new_11, 1)

# 12. Replace Restore Dead-Man's Switch Diagram
old_12 = """.The Restore Feature: Dead-Man's Switch Lifecycle
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-restore-dead-mans-switch.svg[alt="The Restore Feature: Dead-Man's Switch Lifecycle"]

<1> **Watchdog Registration:** On transaction start, the Standard-Node computes the far-future restore window ($W + \\text{delay}$) and writes a watchdog row into an odd bucket.
<2> **Path Stored in Primary Ledger:** The partition path `(date, window, instance_id, odd_bucket)` is durably saved in `es_transaction`.
<3> **Path A (Normal Completion):** Upon success or compensation, the pod issues an immediate targeted $O(1)$ delete of the watchdog row. The restore window remains clean.
<4> **Path B (Silent Pod Crash):** If the pod dies mid-flight (power outage, OOM kill), the watchdog row is never deleted and persists safely in Cassandra.
<5> **Restore Window Discovery:** When the restore window arrives and becomes sealed ($\\le W$), a Retry-Node discovers the odd bucket via its token lease.
<6> **Mandatory Status Check:** The engine reads `es_transaction.running_status`. If already completed, the row is deleted and skipped.
<7> **Automatic Resumption:** If still in-flight, the transaction is automatically re-invoked with zero data loss."""

new_12 = """.The Restore Feature: Dead-Man's Switch Lifecycle
image::stacksaga-database-support:cassandra/stacksaga-v2-12-restore-dead-mans-switch.svg[alt="The Restore Feature: Dead-Man's Switch Lifecycle"]

<1> **Transaction Start:** Standard-Node registers watchdog row at far-future window $W + \text{delay}$ (e.g. +600 min).
<2> **Watchdog in Odd Bucket:** Written into Tier 5 odd bucket partition.
<3> **Path Stored in Ledger:** Partition path stored in `es_transaction` for targeted deletion.
<4> **Path A (Normal Completion):** Targeted $O(1)$ delete removes watchdog row; window stays clean.
<5> **Path B (Pod Crash):** Watchdog row persists in Cassandra. When window arrives, Retry-Node checks status and automatically re-invokes."""

text = text.replace(old_12, new_12, 1)

# 13. Replace Odd/Even Bucket Segregation Diagram
old_13 = """.Odd vs. Even Bucket Segregation & Tombstone Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-odd-even-bucket-segregation.svg[alt="Odd vs. Even Bucket Segregation & Tombstone Isolation"]

<1> **Dual In-Memory Counters:** Standard-Nodes maintain independent `AtomicLong` counters for retry (even) and restore (odd) in local JVM memory.
<2> **Even Buckets (Pure Retry Lane):** Written only on transient failure. Zero row-by-row deletions occur, meaning partitions contain 0% cell tombstones and drop cleanly via single partition tombstones.
<3> **Odd Buckets (Restore Watchdog Lane):** Written on every transaction start and deleted on success. High-frequency cell tombstones are strictly quarantined inside odd partitions.
<4> **Cassandra Read Protection:** Retry-Nodes scanning retry buckets never encounter cell tombstones, completely preventing Cassandra `ReadFailureException` (>100,000 tombstones)."""

new_13 = """.Odd vs. Even Bucket Segregation & Tombstone Isolation
image::stacksaga-database-support:cassandra/stacksaga-v2-13-odd-even-bucket-segregation.svg[alt="Odd vs. Even Bucket Segregation & Tombstone Isolation"]

<1> **Dual In-Memory Counters:** Independent `AtomicLong` counters for retry (even) and restore (odd).
<2> **Even Buckets (Pure Retry):** 0% cell tombstones. High read performance, dropped via single partition tombstones.
<3> **Odd Buckets (Restore Watchdog):** Quarantines high-frequency cell tombstones from completed transactions away from retry reads, eliminating `ReadFailureException`."""

text = text.replace(old_13, new_13, 1)

# 14. Replace Virtual Clusters Diagram
old_14 = """.Horizontal Scaling via Virtual Clusters & Regional Cell Isolation
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-virtual-clusters.svg[alt="Horizontal Scaling via Virtual Clusters & Regional Cell Isolation"]

<1> **Shared Physical Cassandra Cluster:** All virtual clusters reside within the same physical Cassandra cluster and share the exact same keyspace.
<2> **Virtual Cluster Cell 1 (`cluster = cluster-1`):** Autonomous deployment cell with its own dedicated Ring Coordinator and Retry-Nodes.
<3> **Virtual Cluster Cell 2 (`cluster = cluster-2`):** Second autonomous deployment cell operating independently within the same region.
<4> **Tier 3 Partition Key Isolation:** Because `cluster` is embedded in the composite partition key `((region, cluster, service_name, date_of_year, minute_of_day))`, each cell's pod count stays strictly bounded below the 50,000 pod ceiling."""

new_14 = """.Horizontal Scaling via Virtual Clusters & Regional Cell Isolation
image::stacksaga-database-support:cassandra/stacksaga-v2-14-virtual-clusters.svg[alt="Horizontal Scaling via Virtual Clusters & Regional Cell Isolation"]

<1> **Shared Cassandra Keyspace:** Single physical Cassandra cluster and keyspace `stacksaga_event_store`.
<2> **Virtual Cluster 1 (`cluster = cluster-1`):** Autonomous deployment cell with dedicated Ring Coordinator managing up to 50,000 pods.
<3> **Virtual Cluster 2 (`cluster = cluster-2`):** Second autonomous cell isolated via composite partition key `((region, cluster, ...))`."""

text = text.replace(old_14, new_14, 1)

# 15. Replace Node-0 Compaction Diagram
old_15 = """.Directory Compaction: Node-0 Compactor Overseer Two-Gate Verification Protocol
image::stacksaga-database-support:cassandra/stacksaga-diagram-cassandra-node0-compaction-gates.svg[alt="Node-0 Compactor Overseer Two-Gate Verification Protocol"]

<1> **Worker Compaction:** Normal Retry-Nodes (Node-1, Node-2) drop only their own Tier 5 bucket partitions and their own Tier 3 instance markers.
<2> **The Premature Deletion Hazard:** If a fast worker (5 transactions) could delete Tier 2 minute windows directly, it would orphan transactions still being processed by a slower peer worker (40,000 transactions).
<3> **Node-0 Compactor Overseer:** Node-0 (anchor token lease holder) is the sole authority permitted to prune shared upper tiers (Tier 2 and Tier 1).
<4> **Gate 1 (Cluster-Wide Completion):** Node-0 queries Tier 3 across the entire cluster without token filtering. It must return 0 rows before proceeding.
<5> **Gate 2 (Wall-Clock Time Barrier):** Node-0 verifies that the current UTC time is past the window end time, ensuring live Standard-Nodes have progressed to subsequent write windows ($W+1$).
<6> **Safe Upper Pruning:** Once both gates pass, Node-0 deletes the completed minute window from Tier 2, and deletes the calendar date from Tier 1 once all windows are cleared."""

new_15 = """.Directory Compaction: Node-0 Compactor Overseer Two-Gate Verification Protocol
image::stacksaga-database-support:cassandra/stacksaga-v2-15-node0-compaction-gates.svg[alt="Node-0 Compactor Overseer Two-Gate Verification Protocol"]

<1> **Premature Deletion Hazard:** Uncoordinated worker deletion causes peer active transactions to be orphaned.
<2> **Node-0 Compactor Overseer:** Sole authority to delete shared upper tiers (Tier 2 and Tier 1).
<3> **Gate 1 (Cluster-Wide Quorum):** Full cluster query on Tier 3 must return 0 rows.
<4> **Gate 2 (Wall-Clock Check):** Verifies current UTC time has progressed past window end.
<5> **Safe Upper Pruning:** Safely deletes Tier 2 minute window and Tier 1 calendar date."""

text = text.replace(old_15, new_15, 1)

with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated stacksaga-cassandra-support-v2.adoc with all 15 new SVGs successfully!")
