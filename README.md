Network Scanner

This Python script provides a user-friendly tool for scanning networks. It offers two types of scans:

 ARP scan and TCP scan.

ARP Scan

    Identifies devices connected to a network by discovering their Media Access Control (MAC) addresses.
    Creates an ARP (Address Resolution Protocol) request packet and broadcasts it on the network.
    Listens for ARP response packets from devices, which reveal their IP and MAC addresses.
    Provides a table showing the IP address and corresponding MAC address of each discovered device.

TCP Scan

    Checks for open ports on a specific IP address.
    Allows you to specify a range of ports to scan.
    Sends TCP SYN (synchronize) packets to each port in the range.
    Analyzes the responses to identify ports that accept the connection (open ports).
    Reports the open ports on the target IP address.

User Interface

    The script prompts the user to enter the target IP address.
    It asks the user to choose the scan type (ARP or TCP).
    For TCP scans, it allows the user to define a range of ports to scan.
    It displays scan results in a clear format.
    It asks the user if they want to perform another scan after each scan is complete.

Requirements

This script relies on the scapy library, a powerful network packet manipulation and analysis tool for Python. You'll need to install it using pip install scapy before running the script.

How to Use

    Install scapy using pip install scapy.
    Save the script as a Python file (e.g., network_scanner.py).
    Run the script from the command line using python network_scanner.py.
    Follow the on-screen prompts to enter the target IP address and choose the scan type (ARP or TCP).
    For TCP scans, provide the range of ports you want to scan when prompted.
