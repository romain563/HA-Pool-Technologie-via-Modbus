from pymodbus.client import ModbusTcpClient
import csv
from pymodbus.exceptions import ModbusException

# Configuration de la connexion Modbus TCP
ip = "192.168.0.26"
port = 4196
slave_id = 1  # ID de l'esclave

# Fichiers
input_file = "valid_registers.txt"  # 1 adresse par ligne
output_file = "modbus_values.csv"    # Adresse + Valeur uniquement

client = ModbusTcpClient(ip, port=port)

def scan_address(address):
    # Teste d'abord comme Holding Register (le plus courant pour les paramètres)
    try:
        response = client.read_holding_registers(address, count=1, slave=slave_id)
        if not response.isError() and response.registers:
            return (address, response.registers[0])
    except ModbusException:
        pass

    # Puis comme Input Register (pour les valeurs de capteurs)
    try:
        response = client.read_input_registers(address, count=1, slave=slave_id)
        if not response.isError() and response.registers:
            return (address, response.registers[0])
    except ModbusException:
        pass

    return None  # Aucun registre accessible à cette adresse

# Lire les adresses depuis le fichier
with open(input_file, "r") as f:
    addresses = [int(line.strip()) for line in f if line.strip()]

# Scanner chaque adresse
results = []
for address in addresses:
    print(f"Scanning address {address}...")
    result = scan_address(address)
    if result:
        results.append(result)

# Écrire les résultats dans le CSV
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Adresse", "Valeur"])
    for addr, value in results:
        writer.writerow([addr, value])

client.close()
print(f"Scan terminé. {len(results)} valeurs enregistrées dans {output_file}.")
