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
        ingredientes = item.get("ingredientes", {})
        pan = ingredientes.get("pan", "Sin pan")
        salchicha = ingredientes.get("salchicha", "Sin salchicha")
        toppings = ingredientes.get("toppings", [])
        salsas = ingredientes.get("salsas", [])
        acompañantes = ingredientes.get("acompanantes", [])  
        perro = Perro(nombre, pan, salchicha, toppings, salsas, acompañantes)
        lista_perros.append(perro)
    return lista_perros
menu = obtener_menu()
lista = lista_perros_calientes(menu)

try:
    menu = obtener_menu()
    lista = lista_perros_calientes(menu)
    for perro in lista:
        print(perro)
except Exception as e:
    print(" Ocurrió un error:", e)