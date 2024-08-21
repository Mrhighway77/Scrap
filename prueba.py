from bs4 import BeautifulSoup
import pandas as pd

html = '''
<!-- Aquí agregas el HTML completo con múltiples propiedades -->
<div class="properties">
    <!-- Propiedad 1 -->
    <div class="card-body-ds MuiBox-root css-0">
        <div class="contenedorTTimg-ds MuiBox-root css-0">
            <div class="infoPrincipal-ds">
                <p class="MuiTypography-root MuiTypography-body1 comuna-ds css-15lzst4">Santiago</p>
                <p class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap infoTipo-ds css-9l4rpz">Departamento | Venta Nuevo</p>
                <h5 class="MuiTypography-root MuiTypography-h5 nombre-ds css-11a2mf6">Edificio Parque Quinta</h5>
            </div>
        </div>
        <div class="MuiBox-root css-0">
            <ul class="programa-ds">
                <li class="caracteristicas-ds"><p>Studio a 1</p></li>
                <div class="espaciador-ds">|</div>
                <li class="caracteristicas-ds"><p>1</p></li>
                <div class="espaciador-ds">|</div>
                <li class="caracteristicas-ds superficie"><p>22,98 a 40,51 m²</p></li>
            </ul>
        </div>
        <div class="MuiBox-root css-2n8o0q">
            <p class="txtLabel-ds ">Desde</p>
            <div class="cardPrices">
                <p class="txtPrecioA-ds">UF 2.719</p>
                <p class="txtPrecioEspaciadorAB-ds">/</p>
                <p class="txtPrecioB-ds">$ 102.377.583</p>
            </div>
        </div>
    </div>
    
    <!-- Propiedad 2 -->
    <div class="card-body-ds MuiBox-root css-0">
        <div class="contenedorTTimg-ds MuiBox-root css-0">
            <div class="infoPrincipal-ds">
                <p class="MuiTypography-root MuiTypography-body1 comuna-ds css-15lzst4">Santiago</p>
                <p class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap infoTipo-ds css-9l4rpz">Departamento | Venta Nuevo</p>
                <h5 class="MuiTypography-root MuiTypography-h5 nombre-ds css-11a2mf6">Edificio Prat 631</h5>
            </div>
        </div>
        <div class="MuiBox-root css-0">
            <ul class="programa-ds">
                <li class="caracteristicas-ds"><p>2</p></li>
                <div class="espaciador-ds">|</div>
                <li class="caracteristicas-ds"><p>2</p></li>
                <div class="espaciador-ds">|</div>
                <li class="caracteristicas-ds superficie"><p>46,05 m²</p></li>
            </ul>
        </div>
        <div class="MuiBox-root css-2n8o0q">
            <p class="txtLabel-ds ">Desde</p>
            <div class="cardPrices">
                <p class="txtPrecioA-ds">UF 2.800</p>
                <p class="txtPrecioEspaciadorAB-ds">/</p>
                <p class="txtPrecioB-ds">$ 105.427.448</p>
            </div>
        </div>
    </div>
</div>

<div class="card-body-ds MuiBox-root css-0">
    <div class="contenedorTTimg-ds MuiBox-root css-0">
        <div class="infoPrincipal-ds">
            <p class="MuiTypography-root MuiTypography-body1 comuna-ds css-15lzst4">Santiago</p>
            <p class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap infoTipo-ds css-9l4rpz">Departamento | Venta Nuevo</p>
            <h5 class="MuiTypography-root MuiTypography-h5 nombre-ds css-11a2mf6">Edificio Santa Elena 1670</h5>
        </div>
    </div>
    <div class="MuiBox-root css-0">
        <ul class="programa-ds">
            <li class="caracteristicas-ds">
                <svg viewBox="0 0 16 16" width="16" height="16" stroke="#666" stroke-width="1" fill="none" stroke-linecap="round" stroke-linejoin="round" class="ico ico-room">
                    <path d="M2.167 7.23V4.122C2.167 3.503 2.669 3 3.29 3h9.348c.62 0 1.123.503 1.123 1.123v3.106M1 12.698V8.425c0-.62.503-1.123 1.123-1.123h11.754c.62 0 1.123.503 1.123 1.123v4.273M1 9.745h14M1 11.531h14"></path>
                    <path d="M3.906 5.284a.561.561 0 0 1 .552-.461h2.106c.31 0 .561.251.561.561v1.284c0 .31-.251.561-.561.561h-2.34a.561.561 0 0 1-.551-.662l.233-1.283ZM12.094 5.284a.561.561 0 0 0-.552-.461H9.436a.561.561 0 0 0-.56.561v1.284c0 .31.25.561.56.561h2.34c.35 0 .614-.317.552-.662l-.234-1.283Z"></path>
                </svg>
                <p>1 a 2</p>
            </li>
            <div class="espaciador-ds">|</div>
            <li class="caracteristicas-ds">
                <svg viewBox="0 0 16 16" width="16" height="16" stroke="#666" stroke-width="1" fill="none" stroke-linecap="round" stroke-linejoin="round" class="ico ico-bathrooms">
                    <path d="M12.718 8.973V3.472a1.472 1.472 0 1 0-2.943 0v.537M9.775 5.594v.34M9.775 7.406v.34"></path>
                    <path d="M5.35 12.605c-2.336-.39-3.044-2.496-3.096-3.602h11.492c-.052 1.106-.76 3.211-3.096 3.602m-5.3 0a4.8 4.8 0 0 0 .792.064h3.716a4.8 4.8 0 0 0 .792-.064m-5.3 0c-.368.059-1.102.408-1.102 1.34m6.402-1.34c.368.063 1.102.418 1.102 1.34"></path>
                </svg>
                <p>1 a 2</p>
            </li>
            <div class="espaciador-ds">|</div>
            <li class="caracteristicas-ds superficie">
                <svg viewBox="0 0 16 16" width="16" height="16" stroke="#666" stroke-width="1" fill="none" stroke-linecap="round" stroke-linejoin="round" class="ico ico-meters">
                    <path d="M13.9337 1.53331H5.45692C5.20262 1.53331 5.03308 1.70285 5.03308 1.95715V10.4339C5.03308 10.6882 5.20262 10.8578 5.45692 10.8578H13.9337C14.188 10.8578 14.3575 10.6882 14.3575 10.4339V1.95715C14.3575 1.70285 14.188 1.53331 13.9337 1.53331Z"></path>
                    <path d="M2.6004 1.53331V11.9809"></path>
                    <path d="M1.64233 11.1672L2.60445 12.1293L3.56232 11.1714"></path>
                    <path d="M1.64233 2.49543L2.60445 1.53332L3.56232 2.49119"></path>
                    <path d="M14.3575 13.2906H3.90991"></path>
                    <path d="M4.72371 12.3285L3.7616 13.2906L4.71947 14.2485"></path>
                    <path d="M13.3955 12.3285L14.3576 13.2906L13.3997 14.2485"></path>
                </svg>
                <p class="superficie-ds">29,60 a 50,95 m²</p>
            </li>
        </ul>
    </div>
    <div class="MuiBox-root css-2n8o0q">
        <p class="txtLabel-ds">Desde</p>
        <div class="cardPrices">
            <p class="txtPrecioA-ds">UF 2.686</p>
            <p class="txtPrecioEspaciadorAB-ds">/</p>
            <p class="txtPrecioB-ds">$ 101.135.045</p>
        </div>
        <div class="cardPrices cardPricesSecond "></div>
    </div>
    <div class="infoInferior-ds">
        <p></p>
    </div>
</div>

'''

soup = BeautifulSoup(html, 'html.parser')

# Función para extraer los datos de una propiedad
def extraer_datos_propiedad(prop):
    try:
        nombre = prop.find('h5', class_='nombre-ds').text.strip()
        ubicacion = prop.find('p', class_='comuna-ds').text.strip()
        tipo_propiedad = prop.find('p', class_='infoTipo-ds').text.strip()
        caracteristicas = [li.text.strip() for li in prop.find_all('li', class_='caracteristicas-ds')]
        precio = prop.find('p', class_='txtPrecioA-ds').text.strip()
        return {
            'Nombre del Edificio': nombre,
            'Ubicación': ubicacion,
            'Tipo de Propiedad': tipo_propiedad,
            'Características': ', '.join(caracteristicas),
            'Precio': precio
        }
    except AttributeError:
        return None

# Lista para guardar los datos de todas las propiedades
datos_propiedades = []

# Encontrar todas las propiedades en el HTML
propiedad_elements = soup.find_all('div', class_='card-body-ds')

for prop in propiedad_elements:
    datos = extraer_datos_propiedad(prop)
    if datos:
        datos_propiedades.append(datos)

# Crear un DataFrame con los datos
df = pd.DataFrame(datos_propiedades)

# Guardar en un archivo Excel
df.to_excel('propiedades.xlsx', index=False)

print("Datos guardados en 'propiedades.xlsx'.")
