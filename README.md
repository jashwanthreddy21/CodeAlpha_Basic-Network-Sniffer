# 🛡️ CodeAlpha - Network Sniffer Task

This project is a simple network packet sniffer written in Python using the **Scapy** library. It was developed as part of the **CodeAlpha Cyber Security Internship** to demonstrate understanding of basic networking, protocols, and packet inspection.

---

## 📌 Project Objectives

- Capture real-time packets using Python
- Display source/destination IPs and protocols (TCP/UDP)
- Understand how data moves through a network
- Build a basic tool that demonstrates ethical packet sniffing

---

## 🔧 Features

- Captures live packets from the network interface
- Displays:
  - Source & destination IP addresses
  - Protocol types (TCP/UDP)
  - Port numbers
- Graceful exit using `Ctrl+C`

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

Make sure Python 3 is installed.

Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate
pip install scapy
