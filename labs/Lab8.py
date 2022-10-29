import requests
import socket
import re

print("IP Address Information!")
address = input("Please enter a website or valid IP address to query: ")

validateIP = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
validateWebsite = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

if(re.match(validateIP, address)):
    print("IP address entered")
    ip = address
elif(re.match(validateWebsite, address)):
    print("Website entered")
    ip = socket.gethostbyname(address)
else:
    print("Invalid entry, exiting program")
    exit()

ipInfo = requests.get(f"https://ipinfo.io/{ip}/geo").json()

try:
    print(f"\nReturned Information on {address}")
    print(f"IP Address: {ipInfo['ip']}")
    print(f"City: {ipInfo['city']}")
    print(f"Region: {ipInfo['region']}")
    print(f"Country: {ipInfo['country']}")
    print(f"Location: {ipInfo['loc']}")
    print(f"Organization: {ipInfo['org']}")
    print(f"Postal Code: {ipInfo['postal']}")
    print(f"Timezone: {ipInfo['timezone']}")
    print(f"Readme: {ipInfo['readme']}\n")
except:
    print("Ipinfo.io failed to return data for this address")

