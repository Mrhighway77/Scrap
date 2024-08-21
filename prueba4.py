#ESTE CÓDIGO PUDO SACAR LOS DATOS DE LA PÁGINA COMPLETA 1 SOLA 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configuración del WebDriver (asegúrate de tener el driver adecuado para tu navegador)
driver = webdriver.Chrome()  # O usa el driver correspondiente para Firefox, Edge, etc.

# URL de la página que quieres raspar
url = 'https://www.toctoc.com/venta/departamento/metropolitana/santiago?o=menu_compradepto'
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(5)

# Lista para almacenar los datos
data = []

# Encuentra todas las tarjetas de propiedades
cards = driver.find_elements(By.CSS_SELECTOR, '.card-body-ds')

# Extraer datos de cada tarjeta
for card in cards:
    try:
        comuna = card.find_element(By.CSS_SELECTOR, '.comuna-ds').text
        tipo = card.find_element(By.CSS_SELECTOR, '.infoTipo-ds').text
        nombre = card.find_element(By.CSS_SELECTOR, '.nombre-ds').text
        
        # Extraer características
        caracteristicas = card.find_elements(By.CSS_SELECTOR, '.caracteristicas-ds')
        caracteristicas_text = [c.find_element(By.TAG_NAME, 'p').text for c in caracteristicas]
        
        superficie = card.find_element(By.CSS_SELECTOR, '.superficie-ds').text
        precio_uf = card.find_element(By.CSS_SELECTOR, '.txtPrecioA-ds').text
        precio_clp = card.find_element(By.CSS_SELECTOR, '.txtPrecioB-ds').text
        
        # Agregar datos a la lista
        data.append({
            'Comuna': comuna,
            'Tipo': tipo,
            'Nombre': nombre,
            'Caracteristicas': ', '.join(caracteristicas_text),
            'Superficie': superficie,
            'Precio UF': precio_uf,
            'Precio CLP': precio_clp
        })
    except Exception as e:
        print(f'Error al extraer datos de una tarjeta: {e}')

# Cerrar el navegador
driver.quit()

# Crear un DataFrame y guardarlo en un archivo Excel
df = pd.DataFrame(data)
df.to_excel('datos_propiedades.xlsx', index=False)
