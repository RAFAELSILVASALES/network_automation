from netmiko import ConnectHandler
from getpass import getpass

##  Dictionary for defining device parameters
def router_connect():
   while True:
      routers = {'device_type': 'cisco_xe',
        'ip': '',
        'username': '',
        'password':'',
   
        }
      routers['ip'] = input("Digite o endereço IP:")
      routers['username'] = input("Digite usuário:")
      routers['password']= getpass()
     ## Connect via SSH
      connect = ConnectHandler(**routers)

      print(connect.find_prompt())
   
      config_commands = [
           "interface loopback 0",
           "ip address 200.168.0.1 255.255.255.255",
           "do show ip interface brief | exclude una"
      ]
      cfg_output = connect.send_config_set(config_commands)
      print(cfg_output)
      cfg_output_save = connect.save_config()
      print(cfg_output_save)
      stop = str(input("Digite N para continuar: Y para sair: '-': ")).upper()
      if (stop == "Y"):
         break


router_connect()
