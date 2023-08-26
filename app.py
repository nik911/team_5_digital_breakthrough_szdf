from flask import Flask, request
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests
import json
import openai

app = Flask(__name__)
openai.api_key = ""

@app.route('/w',methods = ['POST', 'GET'])
def w():
    if request.method == 'POST':
        return ''
    else:
            title = request.json['title']
            problem = request.json['problem']
            target = request.json['target']
            description = request.json['description']
            advantages = request.json['advantages']
            functionality = request.json['functionality']
            team = request.json['team'][0] # json
            investors = request.json['investors'][0]
            investsAmount = request.json['investsAmount']
            investsTarget =  request.json['investsTarget']
            roadmap = request.json['roadmap'][0]
            email = request.json['email']
            phone = request.json['phone']
            address = request.json['address']
            industry = request.json['industry'] #нет у Арсения
            inn = request.json['inn'] #нет у Арсения


            #industry for tam sam som нет на сайте
            APRU = 1  # выручка / число клиентов
            churn_rate = 1
            lt = 1 / churn_rate
            ltv = APRU * lt
            with open(f'json.json', 'w') as f:
                rep = {'title': title, 'problem': problem, 'target': target, 'description': description,
                       'advantages': advantages, 'functionality': functionality, 'team': team, 'investors': investors,
                       'investsAmount': investsAmount, 'investsTarget': investsTarget, 'roadmap': roadmap,
                       'email': email, 'phone': phone, 'address': address, 'industry': industry,
                       'inn': inn}
                js = json.dumps(rep, ensure_ascii=False)
                f.write(js)
            return '1'


@app.route('/logo',methods = ['POST', 'GET'])
def logo():
    if request.method == 'GET':
        r = requests.post(
            "https://api.deepai.org/api/logo-generator",
            data={
                'text': 'IT company',
            },
            headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
        )
        return r.json()


@app.route('/title',methods = ['POST', 'GET'])
def project_name():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['title']


@app.route('/problem',methods = ['POST', 'GET'])
def problem():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            model_engine = "text-davinci-003"
            prompt = "Сформулируй проблематику более грамотно: "+text['problem']

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

@app.route('/target',methods = ['POST', 'GET'])
def problem():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['target']

@app.route('/description',methods = ['POST', 'GET'])
def problem():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['description']


@app.route('/tam',methods = ['GET'])
def tam():
    with open('json.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        model_engine = "text-davinci-003"
        prompt = "Сфорулируй TAM отрасли " + text['industry']

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


@app.route('/sam',methods = ['GET'])
def sam():
    with open('json.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        model_engine = "text-davinci-003"
        prompt = "Сфорулируй SAM отрасли " + text['industry']

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


@app.route('/som',methods = ['GET'])
def som():
    with open('json.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        model_engine = "text-davinci-003"
        prompt = "Сфорулируй SOM отрасли " + text['industry']

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

@app.route('/competitors',methods = ['POST', 'GET'])
def competitors():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            data = {'key': 'nGjfQjlRSfqBNymo', 'inn': text['inn']}
            r = requests.get('https://api.checko.ru/v2/company', params=data)
            ogrn = r.json()['data']['ОГРН']
            org = ogrn
            url = 'https://checko.ru/company/resurs-' + str(org)
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'lxml')
            table1 = soup.find("section", id="competitors")
            headers = []
            for i in table1.find_all("td"):
                title = i.text
                headers.append(title)
            return headers


if __name__=='__main__':
    app.run(debug=True)
