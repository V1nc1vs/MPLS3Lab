import run

def Show_interface_config(handlers):


    for handler in handlers:

        print(f"######################## {handler.ip}  INTERFACES CONFIGURATION ########################\n\n")
        print(handler.send_command("show ip interface brief\n\n"))
        print("#########################################################################################\n\n")