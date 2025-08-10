import ipaddress

try:
    with (
        open('ips.txt', 'r') as file_entrada,
        open('ips_validas.txt', 'w') as file_validas,
        open('ips_invalidas.txt', 'w') as file_invalidas
    ):
        lineas = file_entrada.readlines()

        for linea in lineas:
            linea_limpia = linea.strip()
            
            if linea_limpia:
                try:
                    # Intentamos convertir la línea en un objeto IP.
                    # Si no es una IP válida, esta línea lanzará un error.
                    ip_objeto = ipaddress.ip_address(linea_limpia)
                    
                    # Si llega aquí, la IP es válida.
                    file_validas.write(linea_limpia + '\n')
                
                except ValueError:
                    # Si se produce un error, la IP no es válida.
                    file_invalidas.write(linea_limpia + '\n')
                    
except FileNotFoundError:
    print("Error: El archivo 'ips.txt' no se encontró.")