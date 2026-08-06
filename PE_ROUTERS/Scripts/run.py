import ConnectHandler
import ShowInterfaceBrief
import os
import pathlib


CREDENTIALS="../../CREDENTIALS/mpl3_vpn_credentials.txt"

def __main__():

    handlers = []

    with open(CREDENTIALS) as f:
        lines = f.readlines()

        for line in lines:
            device_type = line.split(',')[0].strip()
            ip = line.split(',')[1].strip()
            username = line.split(',')[2].strip()
            password = line.split(',')[3].strip()

        handlers.append(ConnectHandler.connect_to_device(device_type,ip,username,password))

        ShowInterfaceBrief.Show_interface_config(handlers)



