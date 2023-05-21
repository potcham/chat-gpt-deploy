import os 
import openai
from credentials import OPENAI_API_KEY, OPENAI_ORG_ID

openai.organization = OPENAI_ORG_ID
openai.api_key = OPENAI_API_KEY

while True:
    prompt = input('\nIntroduce una pregunta: ')

    if prompt == 'salir':
        break
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user',
            'content': prompt}
        ],
        max_tokens = 2048,
    )

    print(completion.choices[0].message.content)