# Simple log analyzer

suspicious_keywords = ["failed", "error", "unauthorized", "denied"]

log_entries = [
    "User login successful",
    "Failed login attempt",
    "Connection denied",
    "File accessed",
    "Unauthorized access detected"
]

for log in log_entries:
    for keyword in suspicious_keywords:
        if keyword.lower() in log.lower():
            print(f"🚨 ALERT: {log}")
            break
    else:
        print(f"✅ OK: {log}")
