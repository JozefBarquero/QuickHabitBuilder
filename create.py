import json

def read_values():
    with open('valores.json', 'r') as file:
        return json.load(file)

# Comprobar inicio
print("Se inicio")

# Traer datos
valores = read_values()
print(valores)
