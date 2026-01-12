import pandas as pd
import os

# ==============================
# Configuración de archivos
# ==============================
INPUT_FILE = "datos_entrada.xlsx"
OUTPUT_FILE = "datos_categorizados.xlsx"

# ==============================
# Diccionario de categorías
# ==============================
CATEGORIES = {
    "tinta": "Insumos de impresión",
    "toner": "Insumos de impresión",
    "impresora": "Equipos de impresión",
    "laptop": "Equipos informáticos",
    "notebook": "Equipos informáticos",
    "router": "Redes y conectividad",
    "cable": "Cables y conectores",
    "mouse": "Accesorios informáticos",
    "teclado": "Accesorios informáticos",
    "monitor": "Periféricos",
    "memoria": "Componentes de hardware",
    "disco": "Componentes de hardware",
    "procesador": "Componentes de hardware",
    "servicio": "Servicios",
    # El diccionario puede ampliarse según el negocio
}

def categorize_product(product_name):
    """
    Asigna una categoría a un producto según palabras clave.
    """
    product_name = str(product_name).lower()
    for keyword, category in CATEGORIES.items():
        if keyword in product_name:
            return category
    return "Otros"

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: No se encontró el archivo {INPUT_FILE}")
        return

    try:
        df = pd.read_excel(INPUT_FILE)

        if 'Producto' not in df.columns:
            print("Error: El archivo debe contener una columna llamada 'Producto'")
            return

        df['Categoría'] = df['Producto'].apply(categorize_product)

        df.to_excel(OUTPUT_FILE, index=False)
        print(f"Archivo categorizado generado correctamente: {OUTPUT_FILE}")

    except Exception as e:
        print(f"Error durante el procesamiento: {e}")

if __name__ == "__main__":
    main()
