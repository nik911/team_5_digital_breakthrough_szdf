from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import openai

app = Flask(__name__)
openai.api_key = ""

@app.route('/w',methods = ['POST', 'GET'])
def w():

    if request.method == 'POST':
        return ''
    else:
            project_name = request.json['project_name']
            problem = request.json['problem']


            #industry for tam sam som нет на сайте
            APRU = 1  # выручка / число клиентов
            churn_rate = 1
            lt = 1 / churn_rate
            ltv = APRU * lt
            with open(f'json.json', 'w') as f:
                rep = {'project_name': project_name, 'problem': problem}
                js = json.dumps(rep, ensure_ascii=False)
                f.write(js)
            return '1'


@app.route('/project_name',methods = ['POST', 'GET'])
def project_name():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['project_name']


@app.route('/problem',methods = ['POST', 'GET'])
def problem():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            model_engine = "text-davinci-003"
            prompt = "Сфорулируй проблематику более грамотно: "+text['problem']

            max_tokens = 1024

            # генерируем ответ
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # выводим ответ
            return completion.choices[0].tex

@app.route('/za',methods = ['POST', 'GET'])
def problem():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['za']



if __name__=='__main__':
    app.run(debug=True)
