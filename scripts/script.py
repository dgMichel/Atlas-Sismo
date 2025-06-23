import PyPDF2
import requests
import os
import json
from pprint import pprint
import re
from dotenv import load_dotenv
load_dotenv()

def clean_json_string(json_str):
    """Improved JSON cleaner with more robust fixes"""
    # Remueve los tag de markdown en los JSON si estan presentes
    json_str = re.sub(r'^```(json)?|```$', '', json_str, flags=re.MULTILINE).strip()
    
    # Arreglos comunes a los JSON
    json_str = (json_str
                .replace("'", '"')  # Sencillo para comillas dobles
                .replace('\\"', '"')  # Deshace las comillas
                .replace('\\n', ' ')  # Remueve las lineas nuevas en los string
                )
    
    # Remueve las comas arrastradas
    json_str = re.sub(r',\s*([}\]])', r'\1', json_str)
    
    # Añade las comas faltantes entre objetos
    json_str = re.sub(r'}\s*{', '},{', json_str)
    
    # Se asegura de que es un array formateado
    json_str = re.sub(r'\[\s*{', '[{', json_str)
    json_str = re.sub(r'}\s*]', '}]', json_str)
    
    # Encuentra los objetos o array JSON externos 
    for wrapper in ['{', '[']:
        start_idx = json_str.find(wrapper)
        if start_idx != -1:
            end_idx = json_str.rfind('}' if wrapper == '{' else ']')
            if end_idx > start_idx:
                json_str = json_str[start_idx:end_idx+1]
                break
    
    return json_str

def validate_and_repair_json(json_str):
    """Try multiple strategies to validate and repair JSON"""
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Initial parse failed: {e}")
        
        # Estrategia 1: Intenta envolver en un array si son múltiples objetos
        if re.search(r'^\s*{', json_str) and re.search(r'}\s*$', json_str):
            try:
                return json.loads(f'[{json_str}]')
            except json.JSONDecodeError:
                pass
        
        # Estrategia 2: TIntenta extraer un fragmento del array
        array_match = re.search(r'\[.*\]', json_str, re.DOTALL)
        if array_match:
            try:
                return json.loads(array_match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Estrategia 3: Intenta arreglaar línea por línea los array
        if '[' in json_str and ']' in json_str:
            lines = [line.strip() for line in json_str.split('\n') if line.strip()]
            repaired = []
            for line in lines:
                if line.startswith('{') and line.endswith('}'):
                    try:
                        json.loads(line)  # Comprueba si las líneas son válidas
                        repaired.append(line)
                    except json.JSONDecodeError:
                        pass
            
            if repaired:
                try:
                    return json.loads(f'[{",".join(repaired)}]')
                except json.JSONDecodeError:
                    pass
        
        raise  # Re-raise si todas las estrategias fallan


# Load PDF
data = PyPDF2.PdfReader("PDF/Mensual/diciembre2021.pdf")
pagina = data.pages[2]
texto = pagina.extract_text()

# Imprime un fragmento del texto extraído para debuguear
print("Extracted text sample:")
print(texto[:500])  # Imprime los primeros 500 valores para verificar la calidad

url_llm = "https://api.fireworks.ai/inference/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('token')}",
    "Content-Type": "application/json",
}
model = "accounts/fireworks/models/llama-v3p3-70b-instruct"
payload = {
    "model": model,
    "messages": [
        {
            "role": "system",
            "content": """Eres un asistente que solo responde con JSON valido. Sigue estas reglas estrictamente:
1. El formato debe ser JSON valido y parseable
2. Todos los nombres de propiedades entre comillas dobles
3. Todos los valores string entre comillas dobles
4. Valores numericos sin comillas
5. No incluyas ningun comentario o explicacion
6. Si hay errores en los datos de entrada, usa null para valores faltantes
7. Separe estrictamente cada objeto con una coma""",
        },
        {
            "role": "user", 
            "content": f"""Extrae los datos de la primera tabla con columnas zonas, Cantidad, Magnitud,Magnitud equivalente, Sismicidad magnitud_equivalente como un array de objetos JSON.
Formato requerido:
{{
"data": [
    {{
    "columna1": valor1,
    "columna2": "valor2"
    }},
    ...
]
}}

Tabla:
{texto}""",
        },
    ],
    "temperature": 0.1,
    "top_p": 0.9,
    "response_format": {"type": "json_object"},  # Importante para el modo JSON
}

try:
    response = requests.post(url_llm, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()
    
    content = result['choices'][0]['message']['content']
    print("Raw LLM response:")
    print(content[:2000])
    
    json_content = clean_json_string(content)
    
    # Usa la versión de validación mejorada
    parsed_data = validate_and_repair_json(json_content)
    
    with open("diciembre2021.json", "w", encoding='utf-8') as file:
        json.dump(parsed_data, file, indent=4, ensure_ascii=False)
    
    print("Datos guardados correctamente en 2021_perceptible.json")
    
except json.JSONDecodeError as e:
    print(f"Final JSON parsing failed: {e}")
    print(f"Problematic content (last 200 chars): {json_content[-200:]}")
    with open("diciembre2021.txt", "w", encoding='utf-8') as f:
        f.write(content)
    # Genera un mensaje de error más poderoso
    if 'Expecting \',\' delimiter' in str(e):
        print("\nERROR: Missing comma between JSON objects in array")
        print("Solution: The AI likely forgot commas between objects in the array")
        print("Try adding 'Strictly separate each object with a comma' to your prompt")
except Exception as e:
    print(f"Unexpected error: {e}")
    print("Full response:")
    pprint(result)