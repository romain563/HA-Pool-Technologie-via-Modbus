from pymodbus.client import ModbusTcpClient
import csv
from pymodbus.exceptions import ModbusException

# Configuration de la connexion Modbus TCP
ip = "192.168.0.26"
port = 4196
slave_id = 1  # ID de l'esclave

# Fichiers
input_file = "valid_registers.txt"  # 1 adresse par ligne
output_file = "modbus_scan_results.csv"

client = ModbusTcpClient(ip, port=port)

def scan_address(address):
    results = []
    for reg_type in ["Holding", "Input", "Coil", "Discrete"]:
        try:
            if reg_type == "Holding":
                response = client.read_holding_registers(address, count=1, slave=slave_id)
            elif reg_type == "Input":
                response = client.read_input_registers(address, count=1, slave=slave_id)
            elif reg_type == "Coil":
                response = client.read_coils(address, count=1, slave=slave_id)
            elif reg_type == "Discrete":
                response = client.read_discrete_inputs(address, count=1, slave=slave_id)

            if not response.isError():
                if reg_type in ["Holding", "Input"]:
                    value = response.registers[0] if response.registers else "N/A"
                else:
                    value = response.bits[0] if response.bits else "N/A"
                results.append((reg_type, address, "R", value))
            else:
                results.append((reg_type, address, "N/A", "N/A"))
        except ModbusException as e:
            results.append((reg_type, address, "Erreur", str(e)))
    return results

# Lire les adresses depuis le fichier
with open(input_file, "r") as f:
    addresses = [int(line.strip()) for line in f if line.strip()]

# Scanner chaque adresse
all_results = []
for address in addresses:
    print(f"Scanning address {address}...")
    all_results.extend(scan_address(address))

# Écrire les résultats dans le CSV
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Type", "Adresse", "Accès", "Valeur"])
    for result in all_results:
        writer.writerow(result)

client.close()
print(f"Scan terminé. Résultats enregistrés dans {output_file}.")
