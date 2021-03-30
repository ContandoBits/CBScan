#!/usr/bin/python3

import nmap

print()
print("   ____   ____    _   _          ")
print("  / ___| | __ )  (_) | |_   ___  ")
print(" | |     |  _ \  | | | __| / __| ")
print(" | |___  | |_) | | | | |_  \__ \ ")
print("  \____| |____/  |_|  \__| |___/ ")
print()

print("[Info] Herramienta para escanear los puertos abiertos en una dirección IP")
print("  ||   Escrito en Python y utiliza Nmap")
print("  ||   Más Herramientas y Tutoriales en >> youtube.com/c/ContandoBits\n")


ip=input("[+] IP Objetivo ==> ")
nm = nmap.PortScanner()
puertos_abiertos="-p "
results = nm.scan(hosts=ip,arguments="-sS -n -Pn -T4")
count=0
#print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
	print("Protocol : %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			puertos_abiertos=puertos_abiertos+str(port)
			count=1
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)

print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip))