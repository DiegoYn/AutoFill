import requests
from bs4 import BeautifulSoup

def fill_survey(url, percentage):
    if not 0 <= percentage <= 10:
        raise ValueError("El porcentaje debe estar entre 0 y 10")
    scaled_percentage = str(percentage + 1)

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"No se pudo acceder a la URL. Código de estado: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    radio_inputs = soup.find_all("input", {"type": "radio", "value": scaled_percentage})
    textareas = soup.find_all("textarea")
    form = soup.find("form")
    
    if not form:
        raise Exception("No se encontró un formulario en la página.")
    
    action_url = form.get("action", url)
    form_data = {
        radio["name"]: scaled_percentage for radio in radio_inputs
    }
    for textarea in textareas:
        form_data[textarea["name"]] = "No opina"

    terminar_data = form_data.copy()
    terminar_data["terminar"] = "terminar"  
    print("\n--- Datos preparados para enviar ---")
    print("URL de acción:", action_url)
    print("Datos del formulario:", terminar_data)
    print("-----------------------------------")

    confirm = input("\n¿Deseas enviar el formulario ahora? (sí/no): ").strip().lower()
    if confirm in ["sí", "si"]:
        response = requests.post(action_url, data=terminar_data)
        if response.status_code == 200:
            print("Formulario enviado exitosamente.")
        else:
            print(f"Error al enviar el formulario. Código de estado: {response.status_code}")
    else:
        print("Formulario no enviado. Revisa los datos antes de proceder.")

if __name__ == "__main__":
    while True:
        survey_url = input("Introduce la URL de la encuesta: ").strip()
        if survey_url:
            break
        print("URL no válida, por favor ingresa una URL válida.")
    while True:
        try:
            percentage = int(input("Introduce el porcentaje (1-10): ").strip())
            if 1 <= percentage <= 10:
                break
            else:
                print("Porcentaje fuera de rango. Debe ser entre 1 y 10.")
        except ValueError:
            print("Por favor ingresa un valor numérico válido para el porcentaje.")
    fill_survey(survey_url, percentage)
