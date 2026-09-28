import os
import time  
from google import genai
from google.genai import types  
from PIL import Image
from dotenv import load_dotenv


load_dotenv()


client = genai.Client()
MODEL_NAME = "gemini-3.6-flash"


config = types.GenerateContentConfig(tools=[])


print("=== PARTE 1: ANÁLISIS DE SENTIMIENTO Y ENTIDADES ===\n")

textos = [
    # 5 Textos en Español
    "Me encanta la nueva interfaz del sistema, es súper intuitiva y rápida.",
    "El servicio técnico tardó tres días en responder y no solucionó el problema.",
    "La actualización se instalará esta noche a las 02:00 AM.",
    "No estoy seguro de si este cambio en la configuración nos beneficie a todos.",
    "Google lanzó una nueva herramienta de IA esta semana en California.",
    
    # 5 Textos en Inglés
    "The customer support team in London was amazingly helpful and fast!",
    "This laptop gets extremely hot after only twenty minutes of use.",
    "The meeting with Microsoft was rescheduled for next Thursday.",
    "I'm feeling indifferent about the new design updates made by Apple.",
    "The delivery arrived two days late and the box was completely crushed."
]

for texto in textos:
    prompt = f"""
    Analiza este texto:
    "{texto}"

    Devuelve:
    - Sentimiento (positivo/negativo/neutro)
    - Entidades detectadas
    """
    
    try:
        respuesta = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config  
        )
        
        print(f"Texto: {texto}")
        print(respuesta.text)
        print("-" * 50)
        

        time.sleep(3)
        
    except Exception as e:
        print(f"\n[!] Error temporal con la API: {e}")
        print("Esperando 5 segundos antes de continuar...")
        time.sleep(5)


print("\n=== PARTE 2: ANÁLISIS DE IMAGEN ===")

ruta_imagen = "foto.jpg"

if os.path.exists(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    prompt_imagen = "Describe detalladamente lo que ves en esta imagen, incluyendo elementos principales, colores y contexto."
    
    try:
        response_imagen = client.models.generate_content(
            model=MODEL_NAME,
            contents=[imagen, prompt_imagen],
            config=config
        )
        print(response_imagen.text)
    except Exception as e:
        print(f"Error procesando la imagen: {e}")
else:
    print(f"Aviso: Guarda una imagen llamada '{ruta_imagen}' en esta carpeta para ejecutar la prueba multimodal.")