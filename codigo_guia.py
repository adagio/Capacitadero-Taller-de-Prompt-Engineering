from groq import Groq
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def obtener_completado(prompt, model="llama3-70b-8192"):
    mensajes = [
        {
            "role": "system",
            "content": "Eres un asistente útil."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    modelo = "llama3-70b-8192"
    respuesta = client.chat.completions.create(
        model=modelo,
        messages=mensajes,
        temperature=0
    )
    return respuesta.choices[0].message.content

texto = f"""
Debes expresar lo que quieres que haga un modelo \ 
proporcionando instrucciones lo más claras y \ 
específicas posible. \ 
Esto guiará al modelo hacia la salida deseada \ 
y reducirá las posibilidades de recibir respuestas \ 
irrelevantes o incorrectas. No confundas escribir un \ 
prompt claro con escribir un prompt corto. \ 
En muchos casos, los prompts más largos brindan más claridad \ 
y contexto al modelo, lo que puede llevar a \ 
respuestas más detalladas y relevantes.
"""
prompt = f"""
Resume el texto delimitado por tres guiones \ 
en una sola oración.
---{texto}---
"""
respuesta = obtener_completado(prompt)
print(respuesta)
