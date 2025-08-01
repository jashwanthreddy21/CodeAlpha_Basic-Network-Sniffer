from scapy.all import sniff, IP, TCP, UDP
import signal
import sys

# Graceful Ctrl+C handling
def signal_handler(sig, frame):
    print("\n[!] Stopping sniffer and exiting cleanly.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        print(f"[+] Packet: {src_ip} --> {dst_ip} | Protocol: {protocol}")

        if TCP in packet:
            print("    TCP | Src Port:", packet[TCP].sport, "| Dst Port:", packet[TCP].dport)
        elif UDP in packet:
            print("    UDP | Src Port:", packet[UDP].sport, "| Dst Port:", packet[UDP].dport)

print("[*] Starting packet sniffer... Press Ctrl+C to stop.\n")

# Sniff packets until Ctrl+C
sniff(prn=packet_callback, store=False)