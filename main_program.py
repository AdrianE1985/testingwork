import pandas as pd
import openpyxl
from jinja2 import Template, Environment, FileSystemLoader
import os
import numpy as np
import csv
from ncclient import manager
tbe=[]

available_choises=["Abort","build_new_interface","build_new_ospf_neighbor","build_new_bgp_neighbor","update_prefix_list","update_route_map","end_choises"]
print("Which router would you like to build today ?")
router=input()

print("What will you want to build or edit today ? \n 0.Abort  \n 1.build new interface \n 2.build new ospf neighbors \n 3.build new bgp neighbors \n 4.update prefix_list \n 5.update route-map \n 6.exit choise list \n")

user_choise=int(input())
tbe.append(available_choises[user_choise])
while user_choise !=0 and available_choises[user_choise]!="end_choise":
    print("Which is your other wish ?")
    user_choise=int(input())
    if user_choise != 6:
        if available_choises[user_choise] not in tbe:
            print("Ok added:",available_choises[user_choise])
            tbe.append(available_choises[user_choise])
        else:
            print("You already choosed this option")
            continue
    else:
        print ("OK. You have chosen to: ", tbe)
        break
else:
    print("Program aborted by you. Goodbye !")
    exit()

#print(tbe)

def check_hostname(node):
    data = pd.read_csv(r"CORE.csv", header=0)
    print(data)
    presence="False"
    for index in data.index:
        host_value = data.loc[index]['A_host']
        interface_type = data.loc[index]['tip_interfata']
        adresa_ip = data.loc[index]['A_int_address']
        if host_value == node and interface_type=="MGMT":
            presence="True"
            print("Your host MGMT details were found in the repos and here are the capabilities")
            m = manager.connect(host=adresa_ip, port=830, username="adrian", password="adrian")
            for capacitati in m.server_capabilities:
                print(capacitati)
    if presence != "True":
            print("Please check again your hostname")
check_hostname(router)
#
#    #print(data)
#    def new_link_config():
#        data = pd.read_csv(r"C:\Users\adria\Desktop\work automation test\CORE.csv", header=0)
#        with open("newconfig.txt", "a") as f:
#            
#
#        for index in data.index:
#            if data.loc[index]['A host']==hostname:
#            print("Your host was found in the repos")
#
#
#
#    print(data)
#    print(data.loc[4]['A host'])
#    #def ospf_config():
#    data = pd.read_csv(r"C:\Users\adria\Desktop\work automation test\CORE.csv")
#    #def bgp_peering():
#    data = pd.read_csv(r"C:\Users\adria\Desktop\work automation test\CORE.csv")
#    #def prefix_list():
#    data = pd.read_csv(r"C:\Users\adria\Desktop\work automation test\CORE.csv")
#    #def edit_link():
#    data = pd.read_csv(r"C:\Users\adria\Desktop\work automation test\CORE.csv")
#