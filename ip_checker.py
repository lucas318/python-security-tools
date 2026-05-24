# Simulated IP blacklist
blacklisted_ips = [
    "192.168.1.10",
    "10.0.0.5",
    "203.0.113.45"
]

def check_ip(ip):
    if ip in blacklisted_ips:
        return "Malicious ❌"
    else:
        return "Clean ✅"


# User input
ip = input("Enter IP address: ")
result = check_ip(ip)

print(f"IP Status: {result}")
