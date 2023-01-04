# import netmiko and getpass
from netmiko import Netmiko
from getpass import getpass

# get a hostname of the core switch to check
host = input("Enter the core switches hostname: ")

# get the core interface to be configured
interface = input("Enter the core interface to be configured: ")

# get the routed vlan number
vlanNumber = input("Enter the routed VLAN number: ")

# get the 
ipAddress = input("Enter the IP Address for the core routed VLAN: ")

# get users username and password using getpass
user = input("Enter your username: ")
passwd = getpass("Enter your password: ")

# Netmiko connection string
netConnect = Netmiko(host,username=user,password=passwd,device_type="cisco_ios")

# show run int command
showRunInt = netConnect.send_command("show run int " + interface)

# show vlan id command
showVlanId = netConnect.send_command("show vlan id " + vlanNumber)

# show ip route command
showIpRoute = netConnect.send_command("sh ip route " + ipAddress)

# print the commands output
print("\n")
print("Show Run Interface config")
print("<<---------------------->> \n")
print(showRunInt)
print("Show VLAN ID config")
print("<<---------------------->> \n")
print(showVlanId)
print("Show IP Route config")
print("<<-------------------->> \n")
print(showIpRoute)
