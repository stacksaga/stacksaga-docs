# Create stacksaga-diagram-cassandra-odd-even-bucket-segregation.svg
svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; fill: #1a202c; }
      .section-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #2d3748; }
      .node-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #1a202c; }
      .sub-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 10.5px; fill: #4a5568; }
      .code-text { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; font-size: 10px; fill: #2b6cb0; }
      .badge-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 11px; font-weight: bold; fill: #ffffff; text-anchor: middle; dominant-baseline: central; }
      .badge-circle { fill: #2b6cb0; stroke: #ffffff; stroke-width: 1.5; }
      .badge-green { fill: #2f855a; stroke: #ffffff; stroke-width: 1.5; }
      .badge-orange { fill: #dd6b20; stroke: #ffffff; stroke-width: 1.5; }
      .arrow { stroke: #4a5568; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
      .arrow-blue { stroke: #2b6cb0; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead-blue); }
      .arrow-orange { stroke: #dd6b20; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead-orange); }
      .box-container { fill: #f7fafc; stroke: #cbd5e0; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 8; ry: 8; }
      .box-node { fill: #ffffff; stroke: #cbd5e0; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-retry { fill: #ebf8ff; stroke: #3182ce; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-restore { fill: #fffaf0; stroke: #dd6b20; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-db { fill: #feebc8; stroke: #f6ad55; stroke-width: 1.2; rx: 6; ry: 6; }
      .cell-live { fill: #c6f6d5; stroke: #38a169; stroke-width: 1; rx: 3; ry: 3; }
      .cell-tombstone { fill: #fed7d7; stroke: #e53e3e; stroke-width: 1; stroke-dasharray: 2,2; rx: 3; ry: 3; }
    </style>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4a5568" />
    </marker>
    <marker id="arrowhead-blue" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#2b6cb0" />
    </marker>
    <marker id="arrowhead-orange" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#dd6b20" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Left Container: Standard-Node JVM Memory -->
  <rect x="20" y="20" width="310" height="580" class="box-container" />
  <circle cx="40" cy="42" r="11" class="badge-circle"/>
  <text x="40" y="42" class="badge-text">1</text>
  <text x="60" y="46" class="section-title">STANDARD-NODE (JVM Memory)</text>

  <!-- Node: pod instance -->
  <g transform="translate(35, 70)">
    <rect width="280" height="110" class="box-node" />
    <text x="15" y="25" class="node-text">Pod Instance: pod-order-a</text>
    <text x="15" y="45" class="sub-text">• Independent in-memory counters</text>
    <text x="15" y="65" class="sub-text">• Increment takes ~2 nanoseconds</text>
    <text x="15" y="85" class="sub-text">• Zero database lock, zero read overhead</text>
    <text x="15" y="102" class="sub-text">• Unique instance_id per JVM startup</text>
  </g>

  <!-- Counter 1: Retry Counter (Even) -->
  <g transform="translate(35, 200)">
    <rect width="280" height="170" class="box-retry" />
    <text x="15" y="25" class="node-text" fill="#2b6cb0">retryCounter : AtomicLong</text>
    <text x="15" y="45" class="sub-text">• Incremented ONLY on transient error</text>
    <text x="15" y="65" class="sub-text">• Target window: </text>
    <text x="105" y="65" class="code-text">W + 1 (Write window)</text>
    <text x="15" y="85" class="sub-text">• Index formula: </text>
    <text x="100" y="85" class="code-text">(slot / 50K) * 2</text>
    <rect x="15" y="105" width="250" height="50" fill="#ffffff" stroke="#bee3f8" rx="4" ry="4"/>
    <text x="25" y="125" class="code-text" font-weight="bold">EVEN INDEXES: 0, 2, 4, 6 ...</text>
    <text x="25" y="143" class="sub-text">Produces clean, sparse partitions</text>
  </g>

  <!-- Counter 2: Restore Counter (Odd) -->
  <g transform="translate(35, 390)">
    <rect width="280" height="190" class="box-restore" />
    <text x="15" y="25" class="node-text" fill="#c05621">restoreCounter : AtomicLong</text>
    <text x="15" y="45" class="sub-text">• Incremented on EVERY transaction start</text>
    <text x="15" y="65" class="sub-text">• Target window: </text>
    <text x="105" y="65" class="code-text">W + delay (e.g. +600)</text>
    <text x="15" y="85" class="sub-text">• Index formula: </text>
    <text x="100" y="85" class="code-text">(slot / 50K) * 2 + 1</text>
    <rect x="15" y="105" width="250" height="70" fill="#ffffff" stroke="#feebc8" rx="4" ry="4"/>
    <text x="25" y="125" class="code-text" font-weight="bold">ODD INDEXES: 1, 3, 5, 7 ...</text>
    <text x="25" y="143" class="sub-text">Quarantines high-frequency deletions</text>
    <text x="25" y="160" class="sub-text">and isolates all cell tombstones</text>
  </g>

  <!-- Arrows from JVM to Cassandra -->
  <path d="M 315 285 L 365 240" class="arrow-blue" />
  <path d="M 315 485 L 365 485" class="arrow-orange" />

  <!-- Right Container: Cassandra Storage Tier 5 -->
  <rect x="350" y="20" width="590" height="580" class="box-container" />
  <text x="370" y="42" class="section-title">CASSANDRA STORAGE TIER 5 (es_recovery_transactions_by_instance)</text>

  <!-- Lane 1: Even Buckets (Retry) -->
  <g transform="translate(370, 60)">
    <rect width="550" height="230" class="box-retry" fill="#f7fafc" />
    <circle cx="20" cy="20" r="11" class="badge-circle"/>
    <text x="20" y="20" class="badge-text">2</text>
    <text x="40" y="24" class="node-text" fill="#2b6cb0">EVEN BUCKETS (0, 2, 4...) — Pure Retry Lane</text>
    
    <!-- Partition Box -->
    <g transform="translate(15, 45)">
      <rect width="250" height="120" class="box-node" stroke="#3182ce" />
      <text x="10" y="20" class="code-text" font-weight="bold">Partition: ((..., pod-order-a, 0))</text>
      <!-- Rows inside -->
      <rect x="10" y="30" width="110" height="22" class="cell-live"/>
      <text x="18" y="45" class="sub-text">tx-101 [LIVE]</text>
      <rect x="130" y="30" width="110" height="22" class="cell-live"/>
      <text x="138" y="45" class="sub-text">tx-102 [LIVE]</text>
      <rect x="10" y="60" width="110" height="22" class="cell-live"/>
      <text x="18" y="75" class="sub-text">tx-103 [LIVE]</text>
      <rect x="130" y="60" width="110" height="22" class="cell-live"/>
      <text x="138" y="75" class="sub-text">tx-104 [LIVE]</text>
      <text x="10" y="105" class="sub-text" fill="#2b6cb0" font-weight="bold">✓ 0% Cell Tombstones (All rows live)</text>
    </g>

    <!-- Partition Rollover Box -->
    <g transform="translate(280, 45)">
      <rect width="255" height="120" class="box-node" stroke="#3182ce" />
      <text x="10" y="20" class="code-text" font-weight="bold">Partition: ((..., pod-order-a, 2))</text>
      <text x="10" y="45" class="sub-text">• Rollover when Bucket 0 hits 50K</text>
      <text x="10" y="65" class="sub-text">• Capped at max 50,000 rows (~3-5MB)</text>
      <text x="10" y="85" class="sub-text">• On completion: Worker issues single</text>
      <text x="10" y="105" class="code-text">DELETE WHERE bucket_index = 0</text>
    </g>

    <text x="15" y="195" class="sub-text" font-weight="bold" fill="#2f855a">
      ✓ O(1) PARTITION TOMBSTONE: Entire partition dropped in one operation during SSTable compaction.
    </text>
    <text x="15" y="215" class="sub-text">
      Zero row-by-row deletions. Retry worker never scans dead records.
    </text>
  </g>

  <!-- Lane 2: Odd Buckets (Restore) -->
  <g transform="translate(370, 310)">
    <rect width="550" height="270" class="box-restore" fill="#f7fafc" />
    <circle cx="20" cy="20" r="11" class="badge-orange"/>
    <text x="20" y="20" class="badge-text">3</text>
    <text x="40" y="24" class="node-text" fill="#c05621">ODD BUCKETS (1, 3, 5...) — Restore Watchdog Lane</text>

    <!-- Partition Box -->
    <g transform="translate(15, 45)">
      <rect width="250" height="135" class="box-node" stroke="#dd6b20" />
      <text x="10" y="20" class="code-text" font-weight="bold">Partition: ((..., pod-order-a, 1))</text>
      <!-- Rows inside: mix of tombstones and rare live -->
      <rect x="10" y="30" width="110" height="22" class="cell-tombstone"/>
      <text x="18" y="45" class="sub-text">tx-001 [DELETED]</text>
      <rect x="130" y="30" width="110" height="22" class="cell-tombstone"/>
      <text x="138" y="45" class="sub-text">tx-002 [DELETED]</text>
      <rect x="10" y="60" width="110" height="22" class="cell-live"/>
      <text x="18" y="75" class="sub-text">tx-003 [CRASHED]</text>
      <rect x="130" y="60" width="110" height="22" class="cell-tombstone"/>
      <text x="138" y="75" class="sub-text">tx-004 [DELETED]</text>
      <rect x="10" y="90" width="110" height="22" class="cell-tombstone"/>
      <text x="18" y="105" class="sub-text">tx-005 [DELETED]</text>
      <rect x="130" y="90" width="110" height="22" class="cell-tombstone"/>
      <text x="138" y="105" class="sub-text">tx-006 [DELETED]</text>
      <text x="10" y="125" class="sub-text" fill="#c05621">⚠ 99.9% Cell Tombstones</text>
    </g>

    <!-- Explanation Box -->
    <g transform="translate(280, 45)">
      <rect width="255" height="135" class="box-node" stroke="#dd6b20" />
      <circle cx="18" cy="18" r="10" class="badge-circle"/>
      <text x="18" y="18" class="badge-text">4</text>
      <text x="35" y="22" class="node-text" fill="#2d3748">Tombstone Quarantine</text>
      <text x="10" y="45" class="sub-text">• Normal transactions delete their</text>
      <text x="10" y="60" class="sub-text">  watchdog row upon completion.</text>
      <text x="10" y="80" class="sub-text">• Leaves behind cell tombstones.</text>
      <text x="10" y="100" class="sub-text" font-weight="bold">• By isolating to ODD buckets,</text>
      <text x="10" y="115" class="sub-text" font-weight="bold">  EVEN buckets remain 100% clean!</text>
    </g>

    <text x="15" y="205" class="sub-text" font-weight="bold" fill="#c05621">
      ✓ WHY SEGREGATION MATTERS:
    </text>
    <text x="15" y="225" class="sub-text">
      1. Retry workers never scan past thousands of delete markers → eliminates ReadFailureException.
    </text>
    <text x="15" y="242" class="sub-text">
      2. In-memory AtomicLong counters stay accurate (separate live counts for retry vs restore).
    </text>
    <text x="15" y="259" class="sub-text">
      3. Independent time windows (W+1 vs W+600) never collide or corrupt each other's partition bounds.
    </text>
  </g>
</svg>
"""

with open(r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\images\cassandra\stacksaga-diagram-cassandra-odd-even-bucket-segregation.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print("Saved stacksaga-diagram-cassandra-odd-even-bucket-segregation.svg successfully!")
