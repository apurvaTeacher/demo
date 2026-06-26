from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.10.10.1",
    "username": "sam",
    "password": "cisco123",
    "port": 22,
}

with ConnectHandler(**device) as conn:
    output = conn.send_command("show ip int br")
    print(output)

with ConnectHandler(**device) as conn:
    output = conn.send_command("sh version")
    print(output)
