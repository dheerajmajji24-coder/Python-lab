import re
log = """2024-06-01 08:15:32 INFO user=john msg=Login successful
2024-06-01 08:20:10 ERROR user=alice msg=Database connection failed
2024-06-01 08:25:45 WARN user=john msg=Password expires soon
2024-06-01 08:30:20 ERROR user=bob msg=File not found
2024-06-01 08:35:12 INFO user=alice msg=Login successful
2024-06-01 08:40:05 ERROR user=john msg=Access denied
2024-06-01 08:45:30 WARN user=bob msg=Low disk space"""
pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|WARN|INFO) user=(?P<user>\w+) msg=(?P<msg>.*)'
entries = []
for match in re.finditer(pattern, log):
    entries.append(match.groupdict())
print("Parsed Entries:")
for entry in entries:
    print(entry)
counts = {
    "ERROR": 0,
    "WARN": 0,
    "INFO": 0
}
for entry in entries:
    counts[entry["level"]] += 1
print("\nSummary:")
print("ERROR:", counts["ERROR"])
print("WARN :", counts["WARN"])
print("INFO :", counts["INFO"])
redacted_log = re.sub(
    r'user=\w+',
    'user=<hidden>',
    log
)
print("\nRedacted Log:")
print(redacted_log)
sorted_entries = sorted(entries, key=lambda x: x["user"])
print("\nERROR entries for each user:")
current_user = None
for entry in sorted_entries:
    if entry["level"] == "ERROR":
        if entry["user"] != current_user:
            current_user = entry["user"]
            print("\nUser:", current_user)

        print(entry["timestamp"], "->", entry["msg"])
#output:
# Parsed Entries:
# {'timestamp': '2024-06-01 08:15:32', 'level': 'INFO', 'user': 'john', 'msg': 'Login successful'}
# {'timestamp': '2024-06-01 08:20:10', 'level': 'ERROR', 'user': 'alice', 'msg': 'Database connection failed'}
# {'timestamp': '2024-06-01 08:25:45', 'level': 'WARN', 'user': 'john', 'msg': 'Password expires soon'}
# {'timestamp': '2024-06-01 08:30:20', 'level': 'ERROR', 'user': 'bob', 'msg': 'File not found'}
# {'timestamp': '2024-06-01 08:35:12', 'level': 'INFO', 'user': 'alice', 'msg': 'Login successful'}
# {'timestamp': '2024-06-01 08:40:05', 'level': 'ERROR', 'user': 'john', 'msg': 'Access denied'}
# {'timestamp': '2024-06-01 08:45:30', 'level': 'WARN', 'user': 'bob', 'msg': 'Low disk space'}
# Summary:
# ERROR: 3
# WARN : 2
# INFO : 2
# Redacted Log:
2024-06-01 08:15:32 INFO user=<hidden> msg=Login successful
2024-06-01 08:20:10 ERROR user=<hidden> msg=Database connection failed
2024-06-01 08:25:45 WARN user=<hidden> msg=Password expires soon
2024-06-01 08:30:20 ERROR user=<hidden> msg=File not found
2024-06-01 08:35:12 INFO user=<hidden> msg=Login successful
2024-06-01 08:40:05 ERROR user=<hidden> msg=Access denied
2024-06-01 08:45:30 WARN user=<hidden> msg=Low disk space
# ERROR entries for each user:
User: alice
2024-06-01 08:20:10 -> Database connection failed
User: bob
2024-06-01 08:30:20 -> File not found
User: john
2024-06-01 08:40:05 -> Access denied
