from scapy.all import *


def arp_scan(ip):

    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result


def tcp_scan(ip, ports):

    try:
        syn = IP(dst=ip) / TCP(dport=ports, flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))

    ans, unans = sr(syn, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        if received[TCP].flags == "SA":
            result.append(received[TCP].sport)

    return result


def main():
    while True:
        ip = input("Enter the IP address: ")

        print("Enter The Type of Scan(Arp or Tcp): ")
        command = input().lower()

        if command == 'arp' or command == 'a':
            result = arp_scan(ip)

            for mapping in result:
                print('{} ==> {}'.format(mapping['IP'], mapping['MAC']))

        elif command == 'tcp' or command == 't':
            print("Enter the ports to scan, delimited by spaces:")
            m,n=map(int,input().split())
            ports = []
            for i in range (m,n+1):
                ports.append(i)

            try:
                result = tcp_scan(ip, ports)
            except ValueError as error:
                print(error)
                continue

            for port in result:
                print('Port {} is open.'.format(port))

        else:
            print("Invalid command. Please enter 'tcp' or 'arp'.")
        p=input("Do you want to perform another scan(Y/N)").lower()
        if p=="n":
            break


if __name__ == '__main__':
    main()
