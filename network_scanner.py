import subprocess
import platform
import ipaddress
from scapy.all import ARP, Ether, srp

def arp_scan(subnet):
    print(f"\n🔍 ARP Scan on: {subnet}")
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []
    for _, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def ping_sweep(subnet):
    print(f"\n📡 Ping Sweep on: {subnet}")
    live_hosts = []
    for ip in ipaddress.IPv4Network(subnet, strict=False):
        ip = str(ip)
        # Skip network address
        if ip.endswith(".0"):
            continue
        param = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            live_hosts.append(ip)
    return live_hosts

def nmap_scan(ip):
    print(f"\n🔎 Nmap scan on {ip} ...")
    try:
        result = subprocess.check_output(["nmap", "-O", ip], stderr=subprocess.DEVNULL).decode()
        print(result)
    except FileNotFoundError:
        print("⚠️ Nmap not found. Please install Nmap for this feature.")
    except Exception as e:
        print(f"❌ Error running Nmap on {ip}: {e}")

def main():
    subnet = input("Enter subnet (e.g. 192.168.1.0/24): ").strip()
    
    # Step 1: ARP scan
    arp_devices = arp_scan(subnet)
    print("\n[ARP Scan Results]")
    for dev in arp_devices:
        print(f"IP: {dev['ip']}\tMAC: {dev['mac']}")

    # Step 2: Ping sweep
    live_ips = ping_sweep(subnet)
    print("\n[Ping Sweep Results]")
    for ip in live_ips:
        print(f"Live IP: {ip}")

    # Step 3: Nmap Scan
    scan_choice = input("\nDo you want to run Nmap on all live IPs? (y/n): ").lower()
    if scan_choice == 'y':
        for ip in live_ips:
            nmap_scan(ip)

if __name__ == "__main__":
    main()
