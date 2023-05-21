import openai
from credentials import OPENAI_API_KEY, OPENAI_ORG_ID

openai.organization = OPENAI_ORG_ID
openai.api_key = OPENAI_API_KEY

## 1. Contexto para el asistente
messages = [{'role':'system', 
             'content':'Eres un asistente de traducciones de idiomas'}]

## 2. Inicio de interacción
while True:

    prompt = input('\n¿Cual es tu consulta?: ')

    if prompt == 'salir':
        break

    ## 3. Nueva consulta para el modelo
    messages.append({'role':'user', 'content': prompt})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens = 2048,
    )

    # 4. Guardamos el historial de la conversacion, nuevas consultas tendran una referencia
    response_content = response.choices[0].message.content

    messages.append({'role':'assistant', 'content': response_content})

    print(response_content)