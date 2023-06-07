
from netmiko import ConnectHandler

r1_11 = {
    'device_type': 'cisco_xe',
    'ip': '',
    'username': '',
    'password': ''
}

connect = ConnectHandler(**r1_11)

print(connect.find_prompt())

### configuração do modo privilegiado no dispositivo#
output = connect.send_command("show ip arp")
config_commands = [
        "enable",
        "configure t",
        "line console 0", 
        "password cisco", 
        "login",
        "exit", 
        "enable secret cisco", 
        "banner motd # ACESSO PROIBIDO # ",
        "line vty 0 4",
        "password cisco", 
        "login ",
        "exit", 
        "service password-encryption",
        "security passwords min-length 5",
        "login block-for 120 attempts 3 within 30",
]

# configuração global do dispositivo #
cfg_output = connect.send_config_set(config_commands)

print(cfg_output)



r1_12 = {
    'device_type': 'cisco_xe',
    'ip': '',
    'username': '',
    'password': ''
}

connect = ConnectHandler(**r1_12)

print(connect.find_prompt())

### configuração do modo privilegiado no dispositivo#
output = connect.send_command("show ip arp")
config_commands = [
        "enable",
        "configure t",
        "line console 0", 
        "password cisco", 
        "login",
        "exit", 
        "enable secret cisco", 
        "banner motd # ACESSO PROIBIDO # ",
        "line vty 0 4",
        "password cisco", 
        "login ",
        "exit", 
        "service password-encryption",
        "security passwords min-length 5",
        "login block-for 120 attempts 3 within 30",
]

# configuração global do dispositivo #
cfg_output = connect.send_config_set(config_commands)

print(cfg_output)



r1_13 = {
    'device_type': 'cisco_xe',
    'ip': '',
    'username': '',
    'password': ''
}

connect = ConnectHandler(**r1_13)

print(connect.find_prompt())

### configuração do modo privilegiado no dispositivo#
output = connect.send_command("show ip arp")
config_commands = [
        "enable",
        "configure t",
        "line console 0", 
        "password cisco", 
        "login",
        "exit", 
        "enable secret cisco", 
        "banner motd # ACESSO PROIBIDO # ",
        "line vty 0 4",
        "password cisco", 
        "login ",
        "exit", 
        "service password-encryption",
        "security passwords min-length 5",
        "login block-for 120 attempts 3 within 30",
]

# configuração global do dispositivo #
cfg_output = connect.send_config_set(config_commands)

print(cfg_output)

         
