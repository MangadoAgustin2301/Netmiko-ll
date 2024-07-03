from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.111',
    'username': 'admin',
    'password': 'agustin',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/ip pool add name=dhcp_pool1 ranges=172.26.24.2-172.26.24.126',
    '/port set 0 name=serial0',
    '/port set 1 name=serial1',
    '/ip address add address=192.168.24.1/30 interface=ether2 network=192.168.24.0',
    '/ip address add address=172.26.24.3/25 interface=ether3 network=172.26.24.0',
    '/ip dhcp-client add interface=ether1',
    '/ip dhcp-server network add address=172.26.24.0/25 gateway=172.26.24.1',
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
    '/ip route add distance=1 dst-address=172.26.24.0/25 gateway=172.26.24.1'
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()