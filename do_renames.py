path = r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\pages\cassandra-database-support\stacksaga-cassandra-support.adoc'

with open(path, encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Table name renames
    ('es_retry_windows_by_day',           'es_recovery_windows_by_day'),
    ('es_instances_by_retry_window',      'es_instances_by_recovery_window'),
    ('es_retry_transactions_by_instance', 'es_recovery_transactions_by_instance'),
    # CQL comment header
    ('5-TIER HIERARCHICAL RETRY ENGINE TABLES', '5-TIER HIERARCHICAL RECOVERY ENGINE TABLES'),
    # Section headings and labels
    ('5-Tier Retry Engine',  '5-Tier Recovery Engine'),
    ('5-tier retry engine',  '5-tier recovery engine'),
    ('5-Tier Retry',         '5-Tier Recovery'),
    ('Retry Engine',         'Recovery Engine'),
    ('retry engine',         'recovery engine'),
    # Properties
    ('transaction.retry.delay-in-minutes',        'recovery.window-interval-minutes'),
    ('transaction.retry.concurrency',             'recovery.concurrency'),
    ('transaction.retry.start-digging-in-advance','recovery.retry.lookback-days'),
    ('transaction.retry.maximum-retry-bucket-size','recovery.bucket-size'),
]

for old, new in replacements:
    before = content.count(old)
    content = content.replace(old, new)
    after = content.count(new)
    print(f'  {old!r} -> {new!r}  ({before} replaced)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone.')
