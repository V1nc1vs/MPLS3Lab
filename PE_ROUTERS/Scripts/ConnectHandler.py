from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException



def connect_to_device(device_type,ip,username,password):


    device={

        "device_type": device_type,
        "ip": ip,
        "username":username,
        "password":password

    }

    try:

        with ConnectHandler(**device) as net_connect:

            print(f"CONNECTION SUCCESS TO DEVICE: {device['ip']}\n\n")

    except NetmikoTimeoutException as e:
        print(f"ERROR: connection to device {device['ip']} timed out: {e}\n\n")
    except NetmikoAuthenticationException as e:
        print(f"ERROR: authetnitcation failed to device {device['ip']}: {e}\n\n")
    except Exception as e:
        print(f"ERROR: unexpected error occured while connecting to device {device['ip']}: {e}\n\n")


    return net_connect

