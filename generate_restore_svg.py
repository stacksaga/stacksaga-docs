# Create stacksaga-diagram-cassandra-restore-dead-mans-switch.svg
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
      .badge-red { fill: #c53030; stroke: #ffffff; stroke-width: 1.5; }
      .arrow { stroke: #4a5568; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
      .arrow-green { stroke: #2f855a; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead-green); }
      .arrow-red { stroke: #c53030; stroke-width: 1.5; stroke-dasharray: 4,3; fill: none; marker-end: url(#arrowhead-red); }
      .box-container { fill: #f7fafc; stroke: #cbd5e0; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 8; ry: 8; }
      .box-node { fill: #ffffff; stroke: #cbd5e0; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-app { fill: #ebf8ff; stroke: #63b3ed; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-db { fill: #feebc8; stroke: #f6ad55; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-worker { fill: #e6fffa; stroke: #4fd1c5; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-crash { fill: #fff5f5; stroke: #feb2b2; stroke-width: 1.2; rx: 6; ry: 6; }
      .box-success { fill: #f0fff4; stroke: #9ae6b4; stroke-width: 1.2; rx: 6; ry: 6; }
    </style>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4a5568" />
    </marker>
    <marker id="arrowhead-green" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#2f855a" />
    </marker>
    <marker id="arrowhead-red" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#c53030" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Top Container: Transaction Initiation -->
  <rect x="20" y="20" width="920" height="150" class="box-container" />
  <text x="35" y="42" class="section-title">PHASE 1: TRANSACTION START (Standard-Node)</text>

  <!-- Node 1: Live Pod Starts Txn -->
  <g transform="translate(45, 55)">
    <rect width="240" height="90" class="box-app" />
    <circle cx="18" cy="18" r="11" class="badge-circle"/>
    <text x="18" y="18" class="badge-text">1</text>
    <text x="38" y="22" class="node-text">Standard-Node (Live Pod)</text>
    <text x="15" y="48" class="sub-text">• Receives live saga request</text>
    <text x="15" y="65" class="sub-text">• Computes restore window: </text>
    <text x="155" y="65" class="code-text">W + delay</text>
    <text x="15" y="82" class="sub-text">• Increments odd </text>
    <text x="100" y="82" class="code-text">restoreCounter</text>
  </g>

  <!-- Arrow 1 -> DB -->
  <path d="M 285 100 L 350 100" class="arrow" />

  <!-- Node 2: Write Watchdog into Tier 5 -->
  <g transform="translate(360, 55)">
    <rect width="260" height="90" class="box-db" />
    <circle cx="18" cy="18" r="11" class="badge-circle"/>
    <text x="18" y="18" class="badge-text">2</text>
    <text x="38" y="22" class="node-text">Tier 5 (Odd Bucket Watchdog)</text>
    <text x="15" y="48" class="sub-text">• Partition: </text>
    <text x="75" y="48" class="code-text">((..., window, odd_bucket))</text>
    <text x="15" y="65" class="sub-text">• Lightweight metadata pointer</text>
    <text x="15" y="82" class="sub-text">• Far-future deadline (e.g. +600 min)</text>
  </g>

  <!-- Arrow DB -> Ledger -->
  <path d="M 620 100 L 685 100" class="arrow" />

  <!-- Node 3: Save Path in es_transaction -->
  <g transform="translate(695, 55)">
    <rect width="225" height="90" class="box-node" />
    <circle cx="18" cy="18" r="11" class="badge-circle"/>
    <text x="18" y="18" class="badge-text">3</text>
    <text x="38" y="22" class="node-text">Primary Event Store</text>
    <text x="15" y="48" class="code-text">es_transaction</text>
    <text x="15" y="68" class="sub-text">Stores exact partition path for</text>
    <text x="15" y="83" class="sub-text">fast O(1) targeted deletion</text>
  </g>

  <!-- Middle Container: Two Divergent Outcomes -->
  <rect x="20" y="190" width="920" height="190" class="box-container" />
  <text x="35" y="212" class="section-title">PHASE 2: EXECUTION OUTCOMES (Normal Success vs. Silent Pod Crash)</text>

  <!-- Path A: Normal Completion -->
  <g transform="translate(45, 230)">
    <rect width="415" height="130" class="box-success" />
    <circle cx="20" cy="20" r="11" class="badge-green"/>
    <text x="20" y="20" class="badge-text">4A</text>
    <text x="40" y="24" class="node-text" fill="#22543d">PATH A: Transaction Completed Normally</text>
    <text x="18" y="52" class="sub-text">• Saga completes all steps successfully (or finishes compensation).</text>
    <text x="18" y="70" class="sub-text">• Standard-Node reads restore path from </text>
    <text x="235" y="70" class="code-text">es_transaction</text>
    <text x="18" y="90" class="sub-text">• Issues targeted </text>
    <text x="105" y="90" class="code-text">DELETE FROM es_recovery_transactions...</text>
    <text x="18" y="112" class="sub-text" font-weight="bold" fill="#22543d">✓ Watchdog row deleted in O(1) time. Restore window stays clean.</text>
  </g>

  <!-- Path B: Pod Crash -->
  <g transform="translate(500, 230)">
    <rect width="420" height="130" class="box-crash" />
    <circle cx="20" cy="20" r="11" class="badge-red"/>
    <text x="20" y="20" class="badge-text">4B</text>
    <text x="40" y="24" class="node-text" fill="#742a2a">PATH B: Unexpected Pod Crash / Power Outage</text>
    <text x="18" y="52" class="sub-text">• Server dies mid-flight (OOM kill, node eviction, power cut).</text>
    <text x="18" y="70" class="sub-text">• In-flight transaction was never committed and never aborted.</text>
    <text x="18" y="90" class="sub-text">• Pod terminates abruptly — </text>
    <text x="175" y="90" class="sub-text" font-weight="bold">Watchdog row is NOT deleted.</text>
    <text x="18" y="112" class="sub-text" font-weight="bold" fill="#742a2a">⚠ Watchdog row persists safely in Cassandra until window arrives.</text>
  </g>

  <!-- Bottom Container: Restore Window Arrival -->
  <rect x="20" y="400" width="920" height="200" class="box-container" />
  <text x="35" y="422" class="section-title">PHASE 3: RESTORE WINDOW ARRIVAL (Automatic Recovery Worker)</text>

  <!-- Node 5: Window Becomes Sealed -->
  <g transform="translate(45, 440)">
    <rect width="250" height="140" class="box-worker" />
    <circle cx="18" cy="18" r="11" class="badge-circle"/>
    <text x="18" y="18" class="badge-text">5</text>
    <text x="38" y="22" class="node-text">Window Arrival & Discovery</text>
    <text x="15" y="48" class="sub-text">• Clock reaches </text>
    <text x="95" y="48" class="code-text">W + delay</text>
    <text x="15" y="66" class="sub-text">• Window becomes sealed (≤ W)</text>
    <text x="15" y="84" class="sub-text">• Retry-Node scans Tier 3 token lease</text>
    <text x="15" y="102" class="sub-text">• Discovers odd bucket </text>
    <text x="135" y="102" class="code-text">(bucket_index % 2 == 1)</text>
    <text x="15" y="120" class="sub-text">• Streams pending </text>
    <text x="105" y="120" class="code-text">transaction_id</text>
  </g>

  <!-- Arrow 5 -> 6 -->
  <path d="M 295 510 L 355 510" class="arrow" />

  <!-- Node 6: Status Check -->
  <g transform="translate(365, 440)">
    <rect width="265" height="140" class="box-db" />
    <circle cx="18" cy="18" r="11" class="badge-circle"/>
    <text x="18" y="18" class="badge-text">6</text>
    <text x="38" y="22" class="node-text">Mandatory Status Check</text>
    <text x="15" y="48" class="sub-text">• Reads: </text>
    <text x="60" y="48" class="code-text">es_transaction.running_status</text>
    <text x="15" y="70" class="sub-text" fill="#2f855a">✓ If COMPLETED / REVERTED:</text>
    <text x="25" y="86" class="sub-text">Watchdog delete failed earlier.</text>
    <text x="25" y="102" class="sub-text">Silently delete watchdog & skip.</text>
    <text x="15" y="124" class="sub-text" fill="#c53030" font-weight="bold">⚠ If IN-FLIGHT / UNKNOWN → Proceed</text>
  </g>

  <!-- Arrow 6 -> 7 -->
  <path d="M 630 510 L 690 510" class="arrow-green" />

  <!-- Node 7: Re-invoke -->
  <g transform="translate(700, 440)">
    <rect width="220" height="140" class="box-success" />
    <circle cx="18" cy="18" r="11" class="badge-green"/>
    <text x="18" y="18" class="badge-text">7</text>
    <text x="38" y="22" class="node-text" fill="#22543d">Resumption & Re-invoke</text>
    <text x="15" y="48" class="sub-text">• Hydrates state from </text>
    <text x="125" y="48" class="code-text">es_transaction</text>
    <text x="15" y="68" class="sub-text">• Dispatches unexecuted step</text>
    <text x="15" y="86" class="sub-text">• Idempotency markers protect</text>
    <text x="15" y="102" class="sub-text">already-committed steps</text>
    <text x="15" y="124" class="sub-text" font-weight="bold" fill="#22543d">✓ 100% Zero Data Loss</text>
  </g>
</svg>
"""

with open(r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\images\cassandra\stacksaga-diagram-cassandra-restore-dead-mans-switch.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print("Saved stacksaga-diagram-cassandra-restore-dead-mans-switch.svg successfully!")
