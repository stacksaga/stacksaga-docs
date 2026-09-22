with open(r'c:\Users\mafei\STACKSAGA-PROJECT\stacksaga-docs\docs\modules\stacksaga-database-support\pages\cassandra-database-support\stacksaga-cassandra-support.adoc', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines, 1):
    if 'restart' in l.lower() or 'overwrite' in l.lower() or 'prior window' in l.lower() or 'in-memory' in l.lower():
        print(f'L{i}: {l.rstrip()}')
