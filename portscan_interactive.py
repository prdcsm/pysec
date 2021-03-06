#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

host = []
ports = []
s = socket.socket()

#----------------------------------------------------------------
# --- Input queries ---------------------------------------------
print("######### Interactive Python Port Scanner #####################\n")
method = input("What type of port scan do you want to use?\n"
               "For port range scan, type 1.\n"
               "For specific ports scan, type 2. ")
host = input("Type in the target host address. ")

#----------------------------------------------------------------
# --- Port range scan -------------------------------------------
if method == "1":
    print("\n######### Port Range Scanner #####################\n")
    minport = int(input("Minimum port number:"))
    maxport = int(input("Maximum port number:"))
    
    for port in range(minport, maxport):
        try:
            s.connect((host, port))
            banner = s.recv(1024)
            decodedBanner = banner.decode('utf-8')
            if banner:
                print(">>> Port "+str(port)+" open: "+decodedBanner)
            s.close()

        except:
            pass

#----------------------------------------------------------------
# --- Specific ports scan ---------------------------------------
if method == "2":
    print("\n######### Specific ports scanner #####################\n")
    print("Type in the specific port numbers one by one.\n"
      "When you finished, type \"S\" to start the scan.\n")
    
    while True:
        inputPort = input("Port number: ")
        if inputPort != "S":
            ports.append(int(inputPort))
        else:
            break

    for port in ports:
        try:
            s.connect((host, port))
            banner = s.recv(1024)
            decodedBanner = banner.decode('utf-8')
            if banner:
                print(">>> Port "+str(port)+" open: "+decodedBanner)
            s.close()
            
        except:
            pass
