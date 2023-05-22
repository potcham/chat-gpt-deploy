from flask import Flask, render_template, request
import openai
from credentials import OPENAI_API_KEY, OPENAI_ORG_ID

openai.organization = OPENAI_ORG_ID
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

context = {'role':'system', 
                'content':'Eres un asistente de traduccion de idiomas'}
messages = [context]

conversation = []

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    
    if request.form['question']:
        prompt = request.form['question']
        question = 'Yo: ' + prompt

        messages.append({'role':'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            max_tokens = 1024,
        )

        response_content = response.choices[0].message.content

        messages.append({'role':'assistant', 'content': response_content})

        answer = 'AI: ' + response_content

        conversation.append(question)
        conversation.append(answer)

        return render_template('index.html', chat=conversation)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)