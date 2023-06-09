from netmiko import ConnectHandler
from getpass import getpass

router = {'device_type': 'cisco_xe',
        'ip': '',
        'username': '',
        'password':'',
   
}

router['ip'] = input("Digite o endereço IP:")
router['username'] = input("Digite usuário:")
router['password']= getpass()
     ## Connect via SSH
connect = ConnectHandler(**router)

print(connect.find_prompt())

print("Iniciando configuração de Backup")   

output = connect.send_command("show run")
print(output)

save_file_backup = open("backup.txt", "w")
save_file_backup.write(output)
save_file_backup.close()

print ('finalizado o backup')