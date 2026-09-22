# -*- coding: utf-8 -*-
"""
Generator for all 15 brand-new, unified theme SVG diagrams for StackSaga Cassandra Support v2.
All diagrams follow a strict minimal-text design with consistent styling and numbered badges.
"""

import os

OUTPUT_DIR = r"c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\images\cassandra"

COMMON_DEFS = """
  <defs>
    <style>
      .canvas-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; font-weight: 700; fill: #0f172a; }
      .group-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11.5px; font-weight: 700; fill: #334155; letter-spacing: 0.5px; }
      .box-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 12px; font-weight: 600; fill: #0f172a; }
      .subtext { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; fill: #475569; }
      .subtext-bold { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; font-weight: 600; fill: #1e293b; }
      .code { font-family: "SFMono-Regular", Consolas, Menlo, monospace; font-size: 10px; fill: #0369a1; }
      .badge-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; font-weight: 700; fill: #ffffff; text-anchor: middle; dominant-baseline: central; }
      
      .box-container { fill: #f8fafc; stroke: #cbd5e1; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 8; }
      .box-white { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1.2; rx: 6; }
      .box-blue { fill: #eff6ff; stroke: #3b82f6; stroke-width: 1.2; rx: 6; }
      .box-amber { fill: #fffbeb; stroke: #f59e0b; stroke-width: 1.2; rx: 6; }
      .box-emerald { fill: #f0fdf4; stroke: #10b981; stroke-width: 1.2; rx: 6; }
      .box-purple { fill: #f5f3ff; stroke: #8b5cf6; stroke-width: 1.2; rx: 6; }
      .box-rose { fill: #fef2f2; stroke: #ef4444; stroke-width: 1.2; rx: 6; }
      
      .badge-blue { fill: #2563eb; stroke: #ffffff; stroke-width: 1.5; }
      .badge-emerald { fill: #16a34a; stroke: #ffffff; stroke-width: 1.5; }
      .badge-amber { fill: #d97706; stroke: #ffffff; stroke-width: 1.5; }
      .badge-purple { fill: #7c3aed; stroke: #ffffff; stroke-width: 1.5; }
      .badge-rose { fill: #dc2626; stroke: #ffffff; stroke-width: 1.5; }
      
      .arrow { stroke: #64748b; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
      .arrow-blue { stroke: #2563eb; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead-blue); }
      .arrow-emerald { stroke: #16a34a; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead-emerald); }
      .arrow-rose { stroke: #dc2626; stroke-width: 1.5; stroke-dasharray: 4,3; fill: none; marker-end: url(#arrowhead-rose); }
    </style>
    <marker id="arrowhead" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="#64748b" />
    </marker>
    <marker id="arrowhead-blue" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="#2563eb" />
    </marker>
    <marker id="arrowhead-emerald" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="#16a34a" />
    </marker>
    <marker id="arrowhead-rose" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="#dc2626" />
    </marker>
  </defs>
"""

diagrams = {}

# -------------------------------------------------------------
# 01. Ecosystem & Component Architecture
# -------------------------------------------------------------
diagrams["stacksaga-v2-01-ecosystem-overview.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>
  
  <!-- Container: App Environment -->
  <rect x="20" y="20" width="400" height="300" class="box-container"/>
  <circle cx="40" cy="42" r="11" class="badge-blue"/>
  <text x="40" y="42" class="badge-text">1</text>
  <text x="60" y="46" class="group-title">MICROSERVICE APPLICATION POD</text>
  
  <g transform="translate(45, 70)">
    <rect width="350" height="60" class="box-white"/>
    <text x="20" y="28" class="box-title">Spring Boot Service (e.g. order-service)</text>
    <text x="20" y="48" class="code">stacksaga-spring-boot-starter</text>
  </g>
  
  <g transform="translate(45, 150)">
    <rect width="350" height="60" class="box-blue"/>
    <text x="20" y="28" class="box-title">StackSaga Cassandra Reactive Support</text>
    <text x="20" y="48" class="code">stacksaga-cassandra-reactive-support</text>
  </g>

  <g transform="translate(45, 230)">
    <rect width="350" height="60" class="box-purple"/>
    <text x="20" y="28" class="box-title">StackSaga Agent (Metrics &amp; Tracing Sidecar)</text>
    <text x="20" y="48" class="code">Port 4545 (Internal RPC)</text>
  </g>
  
  <!-- Arrow to DB -->
  <path d="M 395 180 L 490 180" class="arrow-blue"/>
  
  <!-- Container: Cassandra Cluster -->
  <rect x="500" y="20" width="390" height="180" class="box-container"/>
  <circle cx="520" cy="42" r="11" class="badge-amber"/>
  <text x="520" y="42" class="badge-text">2</text>
  <text x="540" y="46" class="group-title">APACHE CASSANDRA CLUSTER</text>
  
  <g transform="translate(525, 70)">
    <rect width="340" height="50" class="box-amber"/>
    <text x="15" y="25" class="box-title">Core Event Store</text>
    <text x="15" y="42" class="code">es_transaction, es_transaction_tryout</text>
  </g>
  
  <g transform="translate(525, 130)">
    <rect width="340" height="50" class="box-amber"/>
    <text x="15" y="25" class="box-title">5-Tier Recovery Directory</text>
    <text x="15" y="42" class="code">es_days, es_recovery_windows, es_instances, es_buckets, es_recovery_tx</text>
  </g>
  
  <!-- Arrow to Trace Window -->
  <path d="M 395 260 L 515 260" class="arrow"/>

  <!-- Box: Trace Window -->
  <g transform="translate(525, 220)">
    <rect width="340" height="80" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="box-title">StackSaga Trace Window Console</text>
    <text x="15" y="50" class="subtext">Central dashboard for transaction visual tracing</text>
    <text x="15" y="68" class="code">Port 8080 (Web UI)</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 02. Event Store: Transaction Throughput & Murmur3 Hashing
# -------------------------------------------------------------
diagrams["stacksaga-v2-02-transaction-throughput.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>
  
  <!-- Left Box: Inflow -->
  <g transform="translate(30, 40)">
    <rect width="230" height="240" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">High Inflow Requests</text>
    <text x="15" y="65" class="subtext">100,000+ Concurrent</text>
    <text x="15" y="82" class="subtext">Saga Transactions</text>
    <rect x="15" y="110" width="200" height="35" class="box-white"/>
    <text x="25" y="132" class="code">Txn-1: 9b1deb4d-3b7d...</text>
    <rect x="15" y="155" width="200" height="35" class="box-white"/>
    <text x="25" y="177" class="code">Txn-2: 4a2fe9c1-8d2a...</text>
    <rect x="15" y="200" width="200" height="35" class="box-white"/>
    <text x="25" y="222" class="code">Txn-3: f1c0e3b9-5e11...</text>
  </g>
  
  <!-- Middle Box: Murmur3 Partitioner -->
  <path d="M 260 160 L 330 160" class="arrow-blue"/>
  <g transform="translate(340, 75)">
    <rect width="220" height="170" class="box-purple"/>
    <circle cx="20" cy="22" r="11" class="badge-purple"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">Murmur3 Partitioner</text>
    <text x="15" y="60" class="subtext">64-bit Uniform Hash</text>
    <text x="15" y="80" class="code">token(transaction_id)</text>
    <text x="15" y="110" class="subtext">• Zero coordination</text>
    <text x="15" y="128" class="subtext">• Uniform scatter</text>
    <text x="15" y="146" class="subtext">• Eliminates hot spots</text>
  </g>
  
  <!-- Right Box: Cassandra Nodes -->
  <path d="M 560 110 L 630 80" class="arrow"/>
  <path d="M 560 160 L 630 160" class="arrow"/>
  <path d="M 560 210 L 630 240" class="arrow"/>
  
  <g transform="translate(640, 30)">
    <rect width="250" height="80" class="box-amber"/>
    <circle cx="20" cy="20" r="11" class="badge-amber"/>
    <text x="20" y="20" class="badge-text">3</text>
    <text x="40" y="24" class="box-title">Cassandra Node 1</text>
    <text x="15" y="50" class="code">Partition: Txn-1 (Hash: -4.81e18)</text>
    <text x="15" y="68" class="subtext">Even CPU &amp; Disk Distribution</text>
  </g>

  <g transform="translate(640, 120)">
    <rect width="250" height="80" class="box-amber"/>
    <circle cx="20" cy="20" r="11" class="badge-amber"/>
    <text x="20" y="20" class="badge-text">3</text>
    <text x="40" y="24" class="box-title">Cassandra Node 2</text>
    <text x="15" y="50" class="code">Partition: Txn-2 (Hash: +1.24e18)</text>
    <text x="15" y="68" class="subtext">Even CPU &amp; Disk Distribution</text>
  </g>

  <g transform="translate(640, 210)">
    <rect width="250" height="80" class="box-amber"/>
    <circle cx="20" cy="20" r="11" class="badge-amber"/>
    <text x="20" y="20" class="badge-text">3</text>
    <text x="40" y="24" class="box-title">Cassandra Node 3</text>
    <text x="15" y="50" class="code">Partition: Txn-3 (Hash: +7.92e18)</text>
    <text x="15" y="68" class="subtext">Even CPU &amp; Disk Distribution</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 03. Event Store: Colocated Tryout History
# -------------------------------------------------------------
diagrams["stacksaga-v2-03-tryout-colocation.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 300" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>
  
  <!-- Outer Node Box -->
  <rect x="30" y="20" width="860" height="260" class="box-container"/>
  <circle cx="50" cy="42" r="11" class="badge-amber"/>
  <text x="50" y="42" class="badge-text">1</text>
  <text x="70" y="46" class="group-title">PHYSICAL CASSANDRA NODE (Same Partition Key: transaction_id = T-1001)</text>

  <!-- Left Table: es_transaction -->
  <g transform="translate(50, 70)">
    <rect width="360" height="180" class="box-amber"/>
    <text x="15" y="25" class="box-title">Primary Record: es_transaction</text>
    <text x="15" y="45" class="code">PK: ((region, cluster, svc, transaction_id))</text>
    <rect x="15" y="60" width="330" height="100" class="box-white"/>
    <text x="25" y="80" class="subtext-bold">transaction_id: T-1001</text>
    <text x="25" y="98" class="subtext">running_status: IN_FLIGHT</text>
    <text x="25" y="116" class="subtext">created_at: 2026-09-23T01:00:00Z</text>
    <text x="25" y="134" class="subtext">payload: [Saga State Binary Blob]</text>
  </g>

  <!-- Zero Hop Bridge -->
  <g transform="translate(420, 140)">
    <circle cx="20" cy="20" r="11" class="badge-emerald"/>
    <text x="20" y="20" class="badge-text">3</text>
    <path d="M 0 20 L 35 20" class="arrow-emerald"/>
    <text x="8" y="48" class="subtext-bold" fill="#16a34a">Zero Hop</text>
    <text x="6" y="62" class="subtext">Colocated</text>
  </g>

  <!-- Right Table: es_transaction_tryout -->
  <g transform="translate(470, 70)">
    <rect width="400" height="180" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">Execution Steps: es_transaction_tryout</text>
    <text x="15" y="45" class="code">Clustering: (..., tryout_index ASC)</text>
    
    <rect x="15" y="55" width="370" height="35" class="box-white"/>
    <text x="25" y="73" class="code">tryout_index: 0 | CreateOrderStep | SUCCESS</text>
    
    <rect x="15" y="95" width="370" height="35" class="box-white"/>
    <text x="25" y="113" class="code">tryout_index: 1 | MakePaymentStep | SUCCESS</text>
    
    <rect x="15" y="135" width="370" height="35" class="box-white"/>
    <text x="25" y="153" class="code">tryout_index: 2 | ReserveInventoryStep | FAILED</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 04. Write Protection: STRICT Mode Flow
# -------------------------------------------------------------
diagrams["stacksaga-v2-04-write-protection-strict.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Step 1: Kafka Delivery -->
  <g transform="translate(30, 80)">
    <rect width="180" height="160" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">Kafka Event Inflow</text>
    <text x="15" y="60" class="subtext">Saga step triggered</text>
    <text x="15" y="80" class="subtext">by message broker.</text>
    <text x="15" y="110" class="subtext" fill="#ef4444">Risk: At-least-once</text>
    <text x="15" y="128" class="subtext" fill="#ef4444">duplicate delivery</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 210 160 L 265 160" class="arrow-blue"/>

  <!-- Step 2: LWT Lease -->
  <g transform="translate(275, 40)">
    <rect width="250" height="240" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">Cassandra Paxos LWT Lease</text>
    <text x="15" y="55" class="code">INSERT INTO es_execution_markers</text>
    <text x="15" y="70" class="code">IF NOT EXISTS USING TTL 5s</text>
    
    <rect x="15" y="85" width="220" height="60" class="box-white"/>
    <text x="10" y="105" class="subtext-bold" fill="#16a34a">✓ Row did NOT exist:</text>
    <text x="10" y="125" class="subtext">Lease acquired! Proceed to step 3</text>
    
    <rect x="15" y="155" width="220" height="70" class="box-rose"/>
    <circle cx="10" cy="172" r="8" class="badge-rose"/>
    <text x="10" y="172" class="badge-text" font-size="9px">!</text>
    <text x="25" y="176" class="subtext-bold" fill="#dc2626">Row ALREADY existed:</text>
    <text x="10" y="196" class="subtext">• TTL &gt; 0: In-flight by peer → wait</text>
    <text x="10" y="214" class="subtext">• TTL = 0: Committed → skip safely</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 525 120 L 595 120" class="arrow-emerald"/>

  <!-- Step 3: Business Execution -->
  <g transform="translate(605, 50)">
    <rect width="280" height="100" class="box-white"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="box-title">Execute Business Logic</text>
    <text x="15" y="55" class="subtext">• Invoke downstream API / Payment</text>
    <text x="15" y="75" class="subtext">• Strictly mutual-exclusive execution</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 745 150 L 745 175" class="arrow-emerald"/>

  <!-- Step 4: Permanent Marker Commit -->
  <g transform="translate(605, 185)">
    <rect width="280" height="100" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">4</text>
    <text x="40" y="26" class="box-title">Commit Permanent Marker</text>
    <text x="15" y="55" class="code">UPDATE es_execution_markers</text>
    <text x="15" y="70" class="code">SET state='COMMITTED', TTL=0</text>
    <text x="15" y="90" class="subtext-bold" fill="#16a34a">✓ Permanent duplicate immunity</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 05. Write Protection: RELAXED_WITH_DEDUP Flow
# -------------------------------------------------------------
diagrams["stacksaga-v2-05-write-protection-relaxed.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Step 1: Kafka Delivery -->
  <g transform="translate(30, 60)">
    <rect width="200" height="160" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">Kafka Event Inflow</text>
    <text x="15" y="60" class="subtext">Incoming saga event</text>
    <text x="15" y="80" class="subtext">High-throughput path</text>
    <text x="15" y="110" class="subtext-bold">Optimized for idempotent</text>
    <text x="15" y="128" class="subtext-bold">downstream actions</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 230 140 L 290 140" class="arrow-blue"/>

  <!-- Step 2: Read Check -->
  <g transform="translate(300, 45)">
    <rect width="270" height="190" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">Non-Blocking Read Check</text>
    <text x="15" y="55" class="code">SELECT FROM es_execution_markers</text>
    <text x="15" y="70" class="subtext">(Fast standard read, NO Paxos LWT)</text>
    
    <rect x="15" y="90" width="240" height="40" class="box-white"/>
    <text x="10" y="115" class="subtext" fill="#16a34a">✓ No marker found → Proceed to execute</text>
    
    <rect x="15" y="135" width="240" height="40" class="box-rose"/>
    <text x="10" y="160" class="subtext" fill="#dc2626">⚠ Marker exists → Duplicate! Skip safely</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 570 140 L 630 140" class="arrow-emerald"/>

  <!-- Step 3: Batch Write -->
  <g transform="translate(640, 50)">
    <rect width="250" height="180" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="box-title">Atomic Batch Write</text>
    <text x="15" y="55" class="subtext">• Executes business logic</text>
    <text x="15" y="80" class="code">BATCH WRITE:</text>
    <text x="15" y="98" class="code">1. Append step result</text>
    <text x="15" y="115" class="code">2. Write permanent marker</text>
    <text x="15" y="145" class="subtext-bold" fill="#16a34a">Maximum Throughput</text>
    <text x="15" y="162" class="subtext">Zero Paxos round-trip latency</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 06. 5-Tier Directory Hierarchy
# -------------------------------------------------------------
diagrams["stacksaga-v2-06-5tier-recovery-hierarchy.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 440" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left: 5-Tier Tree -->
  <rect x="20" y="20" width="560" height="400" class="box-container"/>
  <text x="40" y="46" class="group-title">5-TIER HIERARCHICAL RECOVERY ACTIVE DIRECTORY</text>

  <!-- Tier 1 -->
  <g transform="translate(40, 65)">
    <rect width="520" height="55" class="box-amber"/>
    <circle cx="20" cy="27" r="11" class="badge-amber"/>
    <text x="20" y="27" class="badge-text">1</text>
    <text x="40" y="24" class="box-title">Tier 1: es_days_by_year (Active Calendar Dates)</text>
    <text x="40" y="42" class="code">PK: ((region, cluster, service_name, year), date_of_year)</text>
  </g>
  <path d="M 80 120 L 80 135" class="arrow"/>

  <!-- Tier 2 -->
  <g transform="translate(40, 135)">
    <rect width="520" height="55" class="box-amber"/>
    <circle cx="20" cy="27" r="11" class="badge-amber"/>
    <text x="20" y="27" class="badge-text">2</text>
    <text x="40" y="24" class="box-title">Tier 2: es_recovery_windows_by_day (UTC Minute Windows: 0..1439)</text>
    <text x="40" y="42" class="code">PK: ((region, cluster, service_name, date_of_year), minute_of_day)</text>
  </g>
  <path d="M 80 190 L 80 205" class="arrow"/>

  <!-- Tier 3 -->
  <g transform="translate(40, 205)">
    <rect width="520" height="55" class="box-amber"/>
    <circle cx="20" cy="27" r="11" class="badge-amber"/>
    <text x="20" y="27" class="badge-text">3</text>
    <text x="40" y="24" class="box-title">Tier 3: es_instances_by_recovery_window (Token-Clustered Pods)</text>
    <text x="40" y="42" class="code">PK: ((region, cluster, service_name, date, window), token(instance_id), instance_id)</text>
  </g>
  <path d="M 80 260 L 80 275" class="arrow"/>

  <!-- Tier 4 -->
  <g transform="translate(40, 275)">
    <rect width="520" height="55" class="box-amber"/>
    <circle cx="20" cy="27" r="11" class="badge-amber"/>
    <text x="20" y="27" class="badge-text">4</text>
    <text x="40" y="24" class="box-title">Tier 4: es_buckets_by_instance (Even=Retry, Odd=Restore)</text>
    <text x="40" y="42" class="code">PK: ((region, cluster, service_name, date, window, instance_id), bucket_index)</text>
  </g>
  <path d="M 80 330 L 80 345" class="arrow"/>

  <!-- Tier 5 -->
  <g transform="translate(40, 345)">
    <rect width="520" height="60" class="box-emerald"/>
    <circle cx="20" cy="30" r="11" class="badge-emerald"/>
    <text x="20" y="30" class="badge-text">5</text>
    <text x="40" y="24" class="box-title">Tier 5: es_recovery_transactions_by_instance (Bounded &lt; 50K rows)</text>
    <text x="40" y="42" class="code">PK: ((region, cluster, service_name, date, window, instance_id, bucket_index), txn_id)</text>
  </g>

  <!-- Right: Primary Store Connection -->
  <path d="M 560 375 L 610 375 L 610 220 L 640 220" class="arrow-blue"/>
  
  <g transform="translate(640, 110)">
    <rect width="250" height="220" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">6</text>
    <text x="40" y="26" class="box-title">Primary Event Store</text>
    <text x="15" y="55" class="code">es_transaction</text>
    <text x="15" y="85" class="subtext">• Holds business payload</text>
    <text x="15" y="105" class="subtext">• Heavy state decoupled</text>
    <text x="15" y="125" class="subtext">• Lazy payload hydration</text>
    <text x="15" y="145" class="subtext">  by transaction_id</text>
    <text x="15" y="175" class="subtext-bold" fill="#2563eb">Tier 5 rows are only ~50B</text>
    <text x="15" y="195" class="subtext-bold" fill="#2563eb">50,000 rows = ~3-5MB disk</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 07. Instance-Level Local Bucketing
# -------------------------------------------------------------
diagrams["stacksaga-v2-07-instance-local-bucketing.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left: Pods -->
  <g transform="translate(20, 20)">
    <rect width="260" height="300" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="group-title">LIVE WRITER PODS</text>
    
    <rect x="15" y="50" width="230" height="70" class="box-blue"/>
    <text x="10" y="22" class="box-title">Pod: order-service-a</text>
    <text x="10" y="42" class="code">AtomicLong counter: 14,200</text>
    <text x="10" y="60" class="subtext">→ Writes to Bucket 0</text>
    
    <rect x="15" y="130" width="230" height="75" class="box-blue"/>
    <text x="10" y="22" class="box-title">Pod: order-service-b</text>
    <text x="10" y="42" class="code">AtomicLong counter: 70,586</text>
    <text x="10" y="58" class="subtext">• 50,000 in Bucket 0 (Full)</text>
    <text x="10" y="72" class="subtext">• 20,586 rolled to Bucket 2</text>
    
    <rect x="15" y="215" width="230" height="70" class="box-blue"/>
    <text x="10" y="22" class="box-title">Pod: order-service-c</text>
    <text x="10" y="42" class="code">AtomicLong counter: 8,110</text>
    <text x="10" y="60" class="subtext">→ Writes to Bucket 0</text>
  </g>

  <!-- Middle: Isolated Partitions -->
  <path d="M 280 85 L 340 85" class="arrow-blue"/>
  <path d="M 280 167 L 340 167" class="arrow-blue"/>
  <path d="M 280 250 L 340 250" class="arrow-blue"/>

  <g transform="translate(340, 20)">
    <rect width="280" height="300" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="group-title">TIER 5 BOUNDED PARTITIONS</text>
    
    <rect x="15" y="50" width="250" height="50" class="box-amber"/>
    <text x="10" y="20" class="code">((..., pod-a, bucket: 0))</text>
    <text x="10" y="38" class="subtext">14,200 rows (~1.2MB)</text>

    <rect x="15" y="110" width="250" height="50" class="box-amber"/>
    <text x="10" y="20" class="code">((..., pod-b, bucket: 0))</text>
    <text x="10" y="38" class="subtext">50,000 rows (~4.2MB - CAPPED)</text>

    <rect x="15" y="170" width="250" height="50" class="box-amber"/>
    <text x="10" y="20" class="code">((..., pod-b, bucket: 2))</text>
    <text x="10" y="38" class="subtext">20,586 rollover rows (~1.8MB)</text>

    <rect x="15" y="230" width="250" height="50" class="box-amber"/>
    <text x="10" y="20" class="code">((..., pod-c, bucket: 0))</text>
    <text x="10" y="38" class="subtext">8,110 rows (~0.7MB)</text>
  </g>

  <!-- Right: Murmur3 Mapping & Workers -->
  <path d="M 620 160 L 670 160" class="arrow"/>

  <g transform="translate(670, 20)">
    <rect width="230" height="300" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-purple"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="group-title">SPATIAL MAPPING</text>

    <rect x="15" y="50" width="200" height="60" class="box-purple"/>
    <text x="10" y="20" class="box-title">Tier 3 Token Hashing</text>
    <text x="10" y="38" class="code">token(instance_id)</text>
    <text x="10" y="52" class="subtext">Scattered across 64-bit ring</text>

    <rect x="15" y="125" width="200" height="75" class="box-emerald"/>
    <circle cx="10" cy="140" r="8" class="badge-emerald"/>
    <text x="10" y="140" class="badge-text" font-size="9px">4</text>
    <text x="25" y="144" class="box-title">Retry-Node 0</text>
    <text x="10" y="165" class="subtext">Sector Lease: [-2^63 .. 0)</text>
    <text x="10" y="182" class="subtext">• Sweeps pod-a &amp; pod-c</text>

    <rect x="15" y="210" width="200" height="75" class="box-emerald"/>
    <circle cx="10" cy="225" r="8" class="badge-emerald"/>
    <text x="10" y="225" class="badge-text" font-size="9px">4</text>
    <text x="25" y="229" class="box-title">Retry-Node 1</text>
    <text x="10" y="250" class="subtext">Sector Lease: [0 .. 2^63 - 1]</text>
    <text x="10" y="267" class="subtext">• Sweeps pod-b (both buckets)</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 08. Dual-Window Synchronization Timeline
# -------------------------------------------------------------
diagrams["stacksaga-v2-08-dual-window-timeline.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 300" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Timeline Line -->
  <line x1="50" y1="120" x2="870" y2="120" stroke="#cbd5e1" stroke-width="4"/>

  <!-- Past Windows (Sealed) -->
  <circle cx="150" cy="120" r="16" class="box-emerald"/>
  <text x="150" y="120" class="badge-text" fill="#16a34a">1421</text>
  <text x="150" y="90" class="subtext" text-anchor="middle">Window W-2</text>

  <circle cx="330" cy="120" r="16" class="box-emerald"/>
  <text x="330" y="120" class="badge-text" fill="#16a34a">1422</text>
  <text x="330" y="90" class="subtext" text-anchor="middle">Window W-1</text>

  <!-- Current Read Window (W) -->
  <circle cx="510" cy="120" r="20" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
  <text x="510" y="120" class="badge-text">1423</text>
  <text x="510" y="85" class="box-title" text-anchor="middle" fill="#047857">Current Window (W)</text>
  <text x="510" y="160" class="subtext" text-anchor="middle">Time: 14:23 UTC</text>

  <!-- Future Write Window (W+1) -->
  <circle cx="730" cy="120" r="20" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
  <text x="730" y="120" class="badge-text">1424</text>
  <text x="730" y="85" class="box-title" text-anchor="middle" fill="#1d4ed8">Write Window (W+1)</text>
  <text x="730" y="160" class="subtext" text-anchor="middle">Future Target</text>

  <!-- Reader Zone Box -->
  <rect x="50" y="190" width="500" height="90" class="box-emerald"/>
  <circle cx="70" cy="212" r="11" class="badge-emerald"/>
  <text x="70" y="212" class="badge-text">2</text>
  <text x="90" y="216" class="box-title" fill="#047857">SEALED READ WINDOWS (&lt;= W)</text>
  <text x="25" y="242" class="subtext">• Processed strictly by Retry-Nodes</text>
  <text x="25" y="260" class="subtext">• Live writers never append here anymore → Zero phantom reads, zero row locks</text>

  <!-- Writer Zone Box -->
  <rect x="590" y="190" width="280" height="90" class="box-blue"/>
  <circle cx="610" cy="212" r="11" class="badge-blue"/>
  <text x="610" y="212" class="badge-text">1</text>
  <text x="630" y="216" class="box-title" fill="#1d4ed8">ACTIVE WRITE WINDOW (W+1)</text>
  <text x="605" y="242" class="subtext">• Standard-Nodes append failures here</text>
  <text x="605" y="260" class="subtext">• Up to 70s cooldown buffer before retry</text>

  <!-- Rollover Note -->
  <g transform="translate(680, 20)">
    <rect width="190" height="45" class="box-white"/>
    <circle cx="15" cy="22" r="8" class="badge-amber"/>
    <text x="15" y="22" class="badge-text" font-size="9px">4</text>
    <text x="30" y="20" class="subtext-bold">Midnight Rollover</text>
    <text x="30" y="36" class="code">W=1439 → W+1 = Min 0 (Day+1)</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 09. Spatial Token Ring Slicing
# -------------------------------------------------------------
diagrams["stacksaga-v2-09-spatial-token-ring.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left: Ring Diagram Representation -->
  <g transform="translate(40, 30)">
    <rect width="360" height="280" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-purple"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="group-title">64-BIT MURMUR3 TOKEN RING</text>
    
    <circle cx="180" cy="160" r="90" fill="none" stroke="#8b5cf6" stroke-width="4"/>
    <line x1="180" y1="70" x2="180" y2="250" stroke="#cbd5e1" stroke-dasharray="3,3"/>
    
    <text x="180" y="60" class="code" text-anchor="middle">-9,223,372,036,854,775,808 (-2^63)</text>
    <text x="180" y="270" class="code" text-anchor="middle">+9,223,372,036,854,775,807 (+2^63 - 1)</text>
    <text x="280" y="165" class="code">Token: 0</text>

    <!-- Ring coordinator badge -->
    <rect x="110" y="135" width="140" height="50" class="box-white"/>
    <circle cx="125" cy="160" r="9" class="badge-purple"/>
    <text x="125" y="160" class="badge-text" font-size="10px">2</text>
    <text x="140" y="155" class="box-title">Ring Coordinator</text>
    <text x="140" y="172" class="subtext">Issues Sector Leases</text>
  </g>

  <!-- Arrow -->
  <path d="M 400 170 L 460 170" class="arrow"/>

  <!-- Right: Worker Leases -->
  <g transform="translate(460, 30)">
    <rect width="420" height="280" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="group-title">AUTONOMOUS RETRY-NODE LEASES</text>

    <!-- Worker 0 -->
    <g transform="translate(20, 50)">
      <rect width="380" height="95" class="box-emerald"/>
      <circle cx="20" cy="20" r="10" class="badge-emerald"/>
      <text x="20" y="20" class="badge-text">4</text>
      <text x="38" y="24" class="box-title">Retry-Node 0 (Sector Lease: [-2^63 .. 0))</text>
      <text x="15" y="48" class="code">SELECT FROM es_instances WHERE token &gt;= -2^63 AND token &lt; 0</text>
      <text x="15" y="68" class="subtext">• Claims: </text>
      <text x="75" y="68" class="code">pod-order-a (-4.81e18)</text>
      <text x="215" y="68" class="subtext">and</text>
      <text x="245" y="68" class="code">pod-order-c (-1.29e18)</text>
      <text x="15" y="86" class="subtext-bold" fill="#047857">✓ Zero contention with Retry-Node 1</text>
    </g>

    <!-- Worker 1 -->
    <g transform="translate(20, 160)">
      <rect width="380" height="95" class="box-emerald"/>
      <circle cx="20" cy="20" r="10" class="badge-emerald"/>
      <text x="20" y="20" class="badge-text">4</text>
      <text x="38" y="24" class="box-title">Retry-Node 1 (Sector Lease: [0 .. +2^63 - 1])</text>
      <text x="15" y="48" class="code">SELECT FROM es_instances WHERE token &gt;= 0 AND token &lt;= 2^63-1</text>
      <text x="15" y="68" class="subtext">• Claims: </text>
      <text x="75" y="68" class="code">pod-order-b (+3.19e18)</text>
      <text x="15" y="86" class="subtext-bold" fill="#047857">✓ Linear horizontal throughput scaling</text>
    </g>
  </g>
</svg>"""

# -------------------------------------------------------------
# 10. Traversal Pipeline & Safe Shutdown
# -------------------------------------------------------------
diagrams["stacksaga-v2-10-traversal-pipeline.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Step 1: Discover -->
  <g transform="translate(20, 50)">
    <rect width="160" height="220" class="box-white"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">1. Discovery</text>
    <text x="15" y="60" class="subtext">Top-down sweep:</text>
    <text x="15" y="80" class="code">Tier 1: Date</text>
    <text x="15" y="100" class="code">Tier 2: Window</text>
    <text x="15" y="120" class="code">Tier 3: Instance</text>
    <text x="15" y="140" class="code">Tier 4: Bucket</text>
    <text x="15" y="180" class="subtext">Zero empty scans</text>
  </g>
  <path d="M 180 160 L 205 160" class="arrow"/>

  <!-- Step 2: Fetch & Hydrate -->
  <g transform="translate(215, 50)">
    <rect width="170" height="220" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">2. Hydration</text>
    <text x="15" y="55" class="subtext">Read Tier 5 rows:</text>
    <text x="15" y="75" class="code">transaction_id</text>
    <text x="15" y="105" class="subtext">Lazy fetch payload:</text>
    <text x="15" y="125" class="code">es_transaction</text>
    <text x="15" y="160" class="subtext">Decoupled memory</text>
    <text x="15" y="178" class="subtext">Low heap footprint</text>
  </g>
  <path d="M 385 160 L 410 160" class="arrow"/>

  <!-- Step 3: Concurrent Dispatch -->
  <g transform="translate(420, 50)">
    <rect width="160" height="220" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="box-title">3. Dispatch</text>
    <text x="15" y="55" class="subtext">Re-invoke step:</text>
    <text x="15" y="80" class="code">concurrency=100</text>
    <text x="15" y="110" class="subtext">Controlled async</text>
    <text x="15" y="130" class="subtext">dispatch avoiding</text>
    <text x="15" y="150" class="subtext">downstream overload</text>
  </g>
  <path d="M 580 160 L 605 160" class="arrow"/>

  <!-- Step 4: Safe Shutdown Barrier -->
  <g transform="translate(615, 50)">
    <rect width="140" height="220" class="box-rose"/>
    <circle cx="20" cy="22" r="11" class="badge-rose"/>
    <text x="20" y="22" class="badge-text">4</text>
    <text x="40" y="26" class="box-title">4. Barrier</text>
    <text x="12" y="55" class="subtext-bold">Pod kill / crash?</text>
    <text x="12" y="75" class="subtext">Partial batch:</text>
    <text x="12" y="95" class="code">KEEP PARTITION</text>
    <text x="12" y="130" class="subtext">Never delete</text>
    <text x="12" y="148" class="subtext">unless 100%</text>
    <text x="12" y="166" class="subtext">dispatched!</text>
  </g>
  <path d="M 755 160 L 780 160" class="arrow-emerald"/>

  <!-- Step 5: O(1) Drop -->
  <g transform="translate(790, 50)">
    <rect width="115" height="220" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">5</text>
    <text x="40" y="26" class="box-title">5. Drop</text>
    <text x="10" y="60" class="subtext-bold" fill="#047857">100% Complete:</text>
    <text x="10" y="90" class="code">DELETE</text>
    <text x="10" y="110" class="code">bucket=B</text>
    <text x="10" y="150" class="subtext">O(1) partition</text>
    <text x="10" y="170" class="subtext">tombstone</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 11. Deep Historical Recovery
# -------------------------------------------------------------
diagrams["stacksaga-v2-11-deep-historical-recovery.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Timeline Box -->
  <rect x="30" y="30" width="860" height="220" class="box-container"/>
  <text x="50" y="56" class="group-title">CHRONOLOGICAL LOOKBACK TIMELINE (recovery.retry.lookback-days = 2)</text>

  <!-- Step 1: Lookback Range -->
  <g transform="translate(50, 80)">
    <rect width="230" height="140" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">1. Lookback Calculation</text>
    <text x="15" y="55" class="subtext">Startup scans:</text>
    <text x="15" y="75" class="code">[Today - 2 Days .. Today]</text>
    <text x="15" y="105" class="subtext">• Friday: Day 264</text>
    <text x="15" y="122" class="subtext">• Saturday: Day 265</text>
  </g>

  <!-- Arrow -->
  <path d="M 280 150 L 330 150" class="arrow"/>

  <!-- Step 2: Ascending Date Traversal -->
  <g transform="translate(340, 80)">
    <rect width="250" height="140" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">2. Ascending Day Sweep</text>
    <text x="15" y="55" class="code">ORDER BY date_of_year ASC</text>
    <text x="15" y="80" class="subtext">1. Sweeps Day 264 (Friday)</text>
    <text x="15" y="100" class="subtext">2. Sweeps Day 265 (Saturday)</text>
    <text x="15" y="120" class="subtext">3. Sweeps Day 266 (Today)</text>
  </g>

  <!-- Arrow -->
  <path d="M 590 150 L 640 150" class="arrow-emerald"/>

  <!-- Step 3: Transition to Live -->
  <g transform="translate(650, 80)">
    <rect width="220" height="140" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">3</text>
    <text x="40" y="26" class="box-title">3. Live Transition</text>
    <text x="15" y="55" class="subtext">Once historical backlog</text>
    <text x="15" y="75" class="subtext">is fully retried,</text>
    <text x="15" y="105" class="subtext-bold" fill="#047857">Seamless handoff to</text>
    <text x="15" y="125" class="subtext-bold" fill="#047857">live minute stream (W)</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 12. Restore Feature: Dead-Man's Switch Lifecycle
# -------------------------------------------------------------
diagrams["stacksaga-v2-12-restore-dead-mans-switch.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Top Swimlane: Txn Start -->
  <rect x="20" y="20" width="880" height="140" class="box-container"/>
  <circle cx="40" cy="40" r="11" class="badge-blue"/>
  <text x="40" y="40" class="badge-text">1</text>
  <text x="60" y="44" class="group-title">TRANSACTION START (Standard-Node)</text>

  <g transform="translate(45, 60)">
    <rect width="250" height="80" class="box-blue"/>
    <text x="15" y="25" class="box-title">Start Transaction</text>
    <text x="15" y="45" class="subtext">• Computes restore window:</text>
    <text x="15" y="62" class="code">W + 600 min (Far Future)</text>
  </g>
  <path d="M 295 100 L 335 100" class="arrow-blue"/>

  <g transform="translate(345, 60)">
    <rect width="260" height="80" class="box-amber"/>
    <circle cx="20" cy="20" r="10" class="badge-amber"/>
    <text x="20" y="20" class="badge-text">2</text>
    <text x="38" y="24" class="box-title">Write Watchdog Row</text>
    <text x="15" y="45" class="subtext">Inserted into Tier 5 ODD bucket</text>
    <text x="15" y="62" class="code">((..., W+600, odd_bucket, txn_id))</text>
  </g>
  <path d="M 605 100 L 645 100" class="arrow-blue"/>

  <g transform="translate(655, 60)">
    <rect width="225" height="80" class="box-white"/>
    <circle cx="20" cy="20" r="10" class="badge-blue"/>
    <text x="20" y="20" class="badge-text">3</text>
    <text x="38" y="24" class="box-title">Store Partition Path</text>
    <text x="15" y="45" class="code">es_transaction</text>
    <text x="15" y="62" class="subtext">Saved for O(1) targeted delete</text>
  </g>

  <!-- Bottom: Outcomes -->
  <g transform="translate(20, 180)">
    <!-- Normal Path -->
    <rect x="0" y="0" width="430" height="140" class="box-emerald"/>
    <circle cx="20" cy="22" r="11" class="badge-emerald"/>
    <text x="20" y="22" class="badge-text">4</text>
    <text x="40" y="26" class="box-title" fill="#047857">PATH A: Normal Completion (Success/Revert)</text>
    <text x="15" y="55" class="subtext">Pod issues targeted partition-key delete:</text>
    <text x="15" y="75" class="code">DELETE FROM es_recovery_tx WHERE path = stored_path</text>
    <text x="15" y="105" class="subtext-bold" fill="#047857">✓ Watchdog row deleted in O(1) time.</text>
    <text x="15" y="122" class="subtext">Far-future window remains completely clean.</text>

    <!-- Crash Path -->
    <rect x="450" y="0" width="430" height="140" class="box-rose"/>
    <circle cx="470" cy="22" r="11" class="badge-rose"/>
    <text x="470" y="22" class="badge-text">5</text>
    <text x="490" y="26" class="box-title" fill="#b91c1c">PATH B: Pod Crash / Power Outage</text>
    <text x="465" y="55" class="subtext">Pod terminates abruptly. Watchdog is NOT deleted.</text>
    <text x="465" y="75" class="subtext-bold" fill="#b91c1c">600 min later: Window W+600 arrives!</text>
    <text x="465" y="98" class="code">1. Retry-Node reads status from es_transaction</text>
    <text x="465" y="118" class="code">2. IN-FLIGHT detected → Re-invoke automatically!</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 13. Odd vs Even Bucket Segregation
# -------------------------------------------------------------
diagrams["stacksaga-v2-13-odd-even-bucket-segregation.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left: Pod JVM Dual Counters -->
  <g transform="translate(20, 20)">
    <rect width="280" height="280" class="box-container"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="group-title">POD JVM MEMORY (Dual Counters)</text>
    
    <rect x="15" y="55" width="250" height="95" class="box-blue"/>
    <text x="10" y="22" class="box-title" fill="#1d4ed8">retryCounter : AtomicLong</text>
    <text x="10" y="42" class="subtext">• Incremented ONLY on failure</text>
    <text x="10" y="60" class="code">Formula: (slot / 50K) * 2</text>
    <text x="10" y="80" class="subtext-bold" fill="#1d4ed8">EVEN: 0, 2, 4, 6 ...</text>

    <rect x="15" y="165" width="250" height="95" class="box-amber"/>
    <text x="10" y="22" class="box-title" fill="#b45309">restoreCounter : AtomicLong</text>
    <text x="10" y="42" class="subtext">• Incremented on EVERY transaction</text>
    <text x="10" y="60" class="code">Formula: (slot / 50K) * 2 + 1</text>
    <text x="10" y="80" class="subtext-bold" fill="#b45309">ODD: 1, 3, 5, 7 ...</text>
  </g>

  <!-- Middle Arrows -->
  <path d="M 300 100 L 360 100" class="arrow-blue"/>
  <path d="M 300 215 L 360 215" class="arrow-amber" style="stroke: #d97706; marker-end: url(#arrowhead);"/>

  <!-- Right: Storage Partitions -->
  <g transform="translate(370, 20)">
    <rect width="530" height="280" class="box-container"/>
    <text x="20" y="26" class="group-title">TIER 5 STORAGE ISOLATION</text>

    <!-- Even Lane -->
    <g transform="translate(15, 45)">
      <rect width="500" height="105" class="box-emerald"/>
      <circle cx="20" cy="20" r="10" class="badge-emerald"/>
      <text x="20" y="20" class="badge-text">2</text>
      <text x="38" y="24" class="box-title" fill="#047857">EVEN BUCKETS (0, 2, 4...) — Pure Retry Lane</text>
      <text x="15" y="50" class="subtext-bold">✓ 0% Cell Tombstones | High read performance</text>
      <text x="15" y="70" class="subtext">• Dropped via single O(1) Partition Tombstone upon completion</text>
      <text x="15" y="88" class="subtext">• Retry workers never scan deleted rows</text>
    </g>

    <!-- Odd Lane -->
    <g transform="translate(15, 160)">
      <rect width="500" height="105" class="box-rose"/>
      <circle cx="20" cy="20" r="10" class="badge-rose"/>
      <text x="20" y="20" class="badge-text">3</text>
      <text x="38" y="24" class="box-title" fill="#b91c1c">ODD BUCKETS (1, 3, 5...) — Restore Watchdog Lane</text>
      <text x="15" y="50" class="subtext-bold" fill="#b91c1c">⚠ Quarantines Cell Tombstones from normal deletes</text>
      <text x="15" y="70" class="subtext">• Isolates delete markers away from retry worker reads</text>
      <text x="15" y="88" class="subtext">• Eliminates Cassandra ReadFailureException (>100K tombstones)</text>
    </g>
  </g>
</svg>"""

# -------------------------------------------------------------
# 14. Virtual Clusters & Cell Isolation
# -------------------------------------------------------------
diagrams["stacksaga-v2-14-virtual-clusters.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left: Shared Cassandra -->
  <g transform="translate(30, 40)">
    <rect width="280" height="240" class="box-amber"/>
    <circle cx="20" cy="22" r="11" class="badge-amber"/>
    <text x="20" y="22" class="badge-text">1</text>
    <text x="40" y="26" class="box-title">Shared Cassandra Keyspace</text>
    <text x="15" y="60" class="subtext">Single physical cluster</text>
    <text x="15" y="80" class="code">stacksaga_event_store</text>
    
    <rect x="15" y="110" width="250" height="100" class="box-white"/>
    <text x="10" y="25" class="subtext-bold">Tier 3 Partition Key:</text>
    <text x="10" y="45" class="code">((region, cluster, svc, ...))</text>
    <text x="10" y="70" class="subtext">Partition bounds isolated by</text>
    <text x="10" y="88" class="code">cluster</text>
    <text x="55" y="88" class="subtext">column!</text>
  </g>

  <!-- Middle Arrow -->
  <path d="M 310 160 L 370 160" class="arrow"/>

  <!-- Right: 2 Virtual Clusters -->
  <g transform="translate(380, 20)">
    <!-- Virtual Cluster 1 -->
    <rect x="0" y="0" width="510" height="130" class="box-blue"/>
    <circle cx="20" cy="22" r="11" class="badge-blue"/>
    <text x="20" y="22" class="badge-text">2</text>
    <text x="40" y="26" class="box-title">Virtual Cluster 1 (cluster = 'cluster-1')</text>
    <text x="15" y="55" class="subtext">• Dedicated Ring Coordinator 1</text>
    <text x="15" y="75" class="subtext">• Dedicated Retry-Nodes for cluster-1</text>
    <text x="15" y="95" class="subtext">• Manages up to 50,000 pods independently</text>

    <!-- Virtual Cluster 2 -->
    <rect x="0" y="150" width="510" height="130" class="box-purple"/>
    <circle cx="20" cy="172" r="11" class="badge-purple"/>
    <text x="20" y="172" class="badge-text">3</text>
    <text x="40" y="176" class="box-title">Virtual Cluster 2 (cluster = 'cluster-2')</text>
    <text x="15" y="205" class="subtext">• Dedicated Ring Coordinator 2</text>
    <text x="15" y="225" class="subtext">• Dedicated Retry-Nodes for cluster-2</text>
    <text x="15" y="245" class="subtext">• Zero cross-cluster communication</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 15. Node-0 Compaction Two-Gate Protocol
# -------------------------------------------------------------
diagrams["stacksaga-v2-15-node0-compaction-gates.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" height="100%">
  {COMMON_DEFS}
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Top: Danger Scenario -->
  <rect x="20" y="20" width="880" height="110" class="box-rose"/>
  <circle cx="40" cy="40" r="11" class="badge-rose"/>
  <text x="40" y="40" class="badge-text">1</text>
  <text x="60" y="44" class="box-title" fill="#b91c1c">THE DANGER: UNCOORDINATED WORKER DELETION</text>
  <text x="20" y="70" class="subtext">If Node-1 (finishing 5 txns in 100ms) could delete minute window 500 from Tier 2 immediately,</text>
  <text x="20" y="90" class="subtext">Node-2 (still busy processing 40,000 txns) would lose its window if it restarts → </text>
  <text x="500" y="90" class="subtext-bold" fill="#b91c1c">40,000 transactions orphaned!</text>

  <!-- Bottom: Node-0 Protocol -->
  <rect x="20" y="150" width="880" height="170" class="box-container"/>
  <circle cx="40" cy="172" r="11" class="badge-emerald"/>
  <text x="40" y="172" class="badge-text">2</text>
  <text x="60" y="176" class="group-title">NODE-0 TWO-GATE VERIFICATION PROTOCOL</text>

  <!-- Gate 1 -->
  <g transform="translate(45, 195)">
    <rect width="250" height="105" class="box-amber"/>
    <circle cx="18" cy="18" r="10" class="badge-amber"/>
    <text x="18" y="18" class="badge-text">3</text>
    <text x="35" y="22" class="box-title">GATE 1: Quorum Check</text>
    <text x="10" y="45" class="code">SELECT instance_id FROM Tier 3</text>
    <text x="10" y="62" class="subtext">(Cluster-wide scan, no token filter)</text>
    <text x="10" y="85" class="subtext-bold" fill="#047857">✓ Must return 0 rows</text>
  </g>
  <path d="M 295 245 L 335 245" class="arrow"/>

  <!-- Gate 2 -->
  <g transform="translate(345, 195)">
    <rect width="250" height="105" class="box-amber"/>
    <circle cx="18" cy="18" r="10" class="badge-amber"/>
    <text x="18" y="18" class="badge-text">4</text>
    <text x="35" y="22" class="box-title">GATE 2: Wall-Clock Check</text>
    <text x="10" y="45" class="code">UTC_NOW &gt; Window_End_Time</text>
    <text x="10" y="68" class="subtext">Guarantees live Standard-Nodes</text>
    <text x="10" y="85" class="subtext">have advanced to write window W+1</text>
  </g>
  <path d="M 595 245 L 635 245" class="arrow-emerald"/>

  <!-- Action -->
  <g transform="translate(645, 195)">
    <rect width="235" height="105" class="box-emerald"/>
    <circle cx="18" cy="18" r="10" class="badge-emerald"/>
    <text x="18" y="18" class="badge-text">5</text>
    <text x="35" y="22" class="box-title" fill="#047857">SAFE UPPER PRUNING</text>
    <text x="10" y="45" class="code">DELETE Tier 2 Window</text>
    <text x="10" y="65" class="code">DELETE Tier 1 Date</text>
    <text x="10" y="90" class="subtext-bold" fill="#047857">✓ Zero Orphaned Records</text>
  </g>
</svg>"""

for name, content in diagrams.items():
    file_path = os.path.join(OUTPUT_DIR, name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {name}")

print(f"\\nAll {len(diagrams)} diagrams generated successfully!")
