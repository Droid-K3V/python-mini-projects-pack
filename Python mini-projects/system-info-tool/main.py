import platform
import psutil
import socket
import shutil

print("=== System Information Tool ===\n")

# OS Information
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"OS Version: {platform.version()}")

# Hostname and IP
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# CPU Information
print(f"Processor: {platform.processor()}")
print(f"CPU Cores: {psutil.cpu_count(logical=False)} physical / {psutil.cpu_count(logical=True)} logical")

# RAM Information
ram = psutil.virtual_memory()
print(f"Total RAM: {round(ram.total / (1024**3), 2)} GB")
print(f"Available RAM: {round(ram.available / (1024**3), 2)} GB")

# Disk Information
total, used, free = shutil.disk_usage("/")
print(f"Disk Total: {round(total / (1024**3), 2)} GB")
print(f"Disk Used: {round(used / (1024**3), 2)} GB")
print(f"Disk Free: {round(free / (1024**3), 2)} GB")

print("\nSystem scan complete!")
