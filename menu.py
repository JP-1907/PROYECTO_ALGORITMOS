import requests
from producto import Perro

def obtener_menu():
    url = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-1/main/menu.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def lista_perros_calientes(menu):
    lista_perros = []
    for item in menu:
        nombre = item.get("nombre", "Sin nombre")
        pan = item.get("Pan", "Sin pan")
        salchicha = item.get("Salchicha", "Sin salchicha")
        toppings = item.get("toppings", [])
        salsas = item.get("salsas", [])
        acompañante = item.get("Acompañante", "Sin acompañante")
        toppings = toppings if toppings else []
        salsas = salsas if salsas else []
        acompañantes = [acompañante] if acompañante else []
        perro = Perro(nombre, pan, salchicha, toppings, salsas, acompañantes)
        lista_perros.append(perro)
    return lista_perros

# Ejecutar
try:
    menu = obtener_menu()
    lista = lista_perros_calientes(menu)
    for perro in lista:
        print(perro)
except Exception as e:
    print("❌ Ocurrió un error:", e)