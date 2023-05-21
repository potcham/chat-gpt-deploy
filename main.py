import openai
from credentials import OPENAI_API_KEY, OPENAI_ORG_ID
import typer
from rich import print
from rich.table import Table 

def main():

    openai.organization = OPENAI_ORG_ID
    openai.api_key = OPENAI_API_KEY

    print('\n🔥 [bold green]Asistente Virtual con ChatGPT[/bold green] 🔥')

    table = Table('Comando', 'Descripcion')
    table.add_row('exit', 'Finalizar conversación')
    table.add_row('new', 'Iniciar nueva conversación')

    print(table)

    ## 1. Contexto para el asistente
    context = {'role':'system', 
                'content':'Eres un asistente de traducciones de idiomas'}
    messages = [context]

    ## 2. Inicio de interacción
    while True:

        prompt = __prompt()

        if prompt == 'new':
            print('\n🆕Nueva conversación')
            messages = [context]
            prompt = __prompt()

        ## 3. Nueva consulta para el modelo
        messages.append({'role':'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            max_tokens = 1024,
        )

        # 4. Guardamos el historial de la conversacion, nuevas consultas tendran una referencia
        response_content = response.choices[0].message.content

        messages.append({'role':'assistant', 'content': response_content})

        print(f'[bold green]>[/bold green] [green]{response_content}[/green]')

def __prompt()->str:
    prompt = typer.prompt('\n💬¿Cual es tu consulta?: ')
     
    if prompt == 'exit':
        exit = typer.confirm('🔥 ¿Estas seguro?')
        if exit:
            print('👋 ¡Hasta luego!')
            raise typer.Abort
        
        return __prompt()
    
    return prompt

if __name__ == "__main__":
    typer.run(main)