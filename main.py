import socket
from colorama import init, Fore
import json
#import _thread as thread

class Colors():
  init()




# function to test a specific port
def test_specified_port(targetIp, port):
	skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	skt.settimeout(0.5)
	status = skt.connect_ex((targetIp, port))
	
	if status == 0:
	  f = open("Open.txt", "a")
	  f.write("[OPEN] Port: " + str(port) + " Host: " + targetIp + "\n")
	  f.close()
	  print(Fore.GREEN + "[OPEN] " + str(port) + " | Made by @Diary & @Doxer")
	else:
	  print(Fore.RED + "[CLOSED] "+str(port)+" | Made by @Diary & Doxer")
	
	skt.close()

# function to handle the range port choice
def get_range_of_ports():
	Prange = input("[S] Port range to scan - e.g, 1-10: ")
		
	lowerPort = int(Prange.split('-')[0])
	upperPort = int(Prange.split('-')[1])
	
	return range(lowerPort, upperPort + 1)

# function to handle the common port choice
def get_common_ports():
	print("[S] Scanning the commonly used ports")
	# array of commonly used ports (Red Team Field Manual)
	commonPorts = [21, 22, 23, 25, 49, 53, 67, 68, 69, 80, 88, 110, 111, 123, 135, 137, 138,
		139, 143, 161, 179, 201, 389, 443, 445, 500, 514, 520, 546, 547, 587, 902, 1080,
		1194, 1433, 1434, 1521, 1629, 2049, 3128, 3306, 3389, 5060, 5222, 5432, 5666, 
		5900, 6000, 6129, 6667, 9001, 9090, 9091, 9100]

	return commonPorts

# function to handle the port input choice
def handle_port_choice(choice):
	if choice == 1:
		return get_range_of_ports()
	elif choice == 2:
		return get_common_ports()
	else:
		return []

# function to handle scanning of target IP (used in multi-threading)
def scan_target_IP(ipAddress, ports):
	print("[S] Scanning target: ", ipAddress)
	for portNumber in ports:
		test_specified_port(ipAddress, portNumber)

# main functionality starts here
def main():
	print(Fore.RED + " Scan Dat Port")
	print("@Diary - @Twirls" + Fore.WHITE)
	print("1 - Single IP \n2 - IP range \n3 - Specific IPs")
	choice = int(input("[I] Select your option: "))
	
	if choice == 1:
		print("Enter the IP address to scan: ")
		target = str(input(""))
		print("1 - Range of Ports \n2 - Common Ports")
		portChoice = int(input("Select your option: "))
		portsToScan = handle_port_choice(portChoice)
	
		scan_target_IP(target, portsToScan)	
			
	elif choice == 2:
		print("[S] Enter the IP addresses to scan between, seperated by a '-'")
		print("e.g, 0.0.0.0-0.0.0.100")
		targets = input("").split('-')
		splitIP = targets[0].split('.')
		ipMask = splitIP[0] + "." + splitIP[1] + "." + splitIP[2]
		
		lowerIP = int(splitIP[3])
		upperIP = int(targets[1].split('.')[3])
	
		print("1 - Range of Ports \n2 - Common Ports")
		portChoice = int(input("[I] Select your option: "))
		portsToScan = handle_port_choice(portChoice)
		
		for ip in range(lowerIP, upperIP + 1):
			currentIp = ipMask + "." + str(ip)
			#thread.start_new_thread(scan_target_IP, (currentIp, portsToScan))
			scan_target_IP(currentIp, portsToScan)
	
	elif choice == 3:
		print("Enter the IP addresses to scan, seperated by a ','")
		print("e.g, 0.0.0.0,0.0.0.1")
		targets = input("").split(',')
		print("1 - Range of Ports \n2 - Commonly used ports")
		portChoice = int(input("Select your option: "))
		portsToScan = handle_port_choice(portChoice)	
		
		for ip in targets:
			#thread.start_new_thread(scan_target_IP, (ip, portsToScan))
			scan_target_IP(ip, portsToScan)
	else:
		print("Command not recognized. Maybe run it again?")
	
	print("Done scanning HOST: " + target)
	# Pog

if __name__ == "__main__":
	main()
