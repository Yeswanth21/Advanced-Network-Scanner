# 🔎 Advanced Network Scanner (ARP + Ping Sweep + Nmap)

This Python-based network scanner combines **ARP scanning**, **ICMP ping sweep**, and optional **Nmap scanning** to identify active devices on a given subnet. It is designed for cybersecurity students and professionals who need a quick overview of network activity and connected hosts.

---

## 📌 Features

- ✅ ARP Scan: Detect devices using MAC/IP pairing on your LAN.
- ✅ Ping Sweep: Identify live IPs on the subnet using ICMP echo requests.
- ✅ Optional Nmap Scan: Run OS and port scanning on selected devices (if Nmap is installed).
- 🖥️ Works cross-platform (Windows, Linux, macOS).

---

## 🚀 Usage

### 1. Install Requirements

```bash
pip install scapy
```

Note: This tool uses subprocess to run ping and nmap. Make sure they are available in your system path.

### 2. Run the Tool

```bash
python network_scanner.py
```

You will be prompted to enter the subnet (e.g., 192.168.1.0/24), and the scanner will:
- Perform an ARP scan to detect devices and their MAC addresses.
- Sweep the subnet using ICMP ping.
- Optionally run an Nmap scan on all live IPs for detailed information.

---

## 🧪 Example Output

```bash
Enter subnet (e.g. 192.168.1.0/24): 192.168.1.0/24

🔍 ARP Scan on: 192.168.1.0/24
IP: 192.168.1.1     MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.5     MAC: 11:22:33:44:55:66

📡 Ping Sweep on: 192.168.1.0/24
Live IP: 192.168.1.1
Live IP: 192.168.1.5

🔎 Nmap scan on 192.168.1.1 ...
Starting Nmap 7.91 ...
OS details: Linux 3.x | Port 80 open
```

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical** use only. Do not use it on networks without proper authorization.

---

## 📚 Tech Stack

- Python
- Scapy (for ARP)
- subprocess (for ping and Nmap)
- ipaddress
- Nmap (external tool)

