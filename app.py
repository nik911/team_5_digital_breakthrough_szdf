from flask import Flask, request
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from datetime import datetime
import requests
import json
import openai
import base64

app = Flask(__name__)
#openai.api_key = "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"

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
            team = request.json['team'] # json
            investors = request.json['investors']
            investsAmount = request.json['investsAmount']
            investsTarget =  request.json['investsTarget']
            roadmap = request.json['roadmap']
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


def create_image(c):
    image = Image.new('RGB', (4000, 2000), 'white')
    draw = ImageDraw.Draw(image)

    draw.line([(400, 1000), (3600, 1000)], width=20, fill='#9999FF')
    c = c
    u = 3200 - 200 * c
    y = u / (c + 1)
    for i in range(c):
        draw.ellipse([(y * (i + 1) + 200 * i + 400, 900), (y * (i + 1) + 200 * i + 600, 1100)], fill='#9999FF')

    image.save('image.png')


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

            # выводим ответ completion.choices[0].tex
            return text['problem']

@app.route('/target',methods = ['POST', 'GET'])
def target():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['target']

@app.route('/description',methods = ['POST', 'GET'])
def description():
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


@app.route('/email',methods = ['POST', 'GET'])
def email():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['email']


@app.route('/phone',methods = ['POST', 'GET'])
def phone():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['phone']


@app.route('/address',methods = ['POST', 'GET'])
def address():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['address']


@app.route('/team',methods = ['POST', 'GET'])
def team():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            return text['team'] #json name+role

@app.route('/roadmap',methods = ['POST', 'GET'])
def roadmap():
    if request.method == 'GET':
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            t = text['roadmap']
            c = len(t)
        image = Image.new('RGB', (4000, 2000), 'white')
        draw = ImageDraw.Draw(image)
        fontL = ImageFont.truetype('Montserrat-Light.ttf', size=40)
        fontM = ImageFont.truetype('Montserrat-Medium.ttf', size=45)
        draw.line([(400, 1000), (3600, 1000)], width=20, fill='#9999FF')
        u = 3200 - 200 * c
        y = u / (c + 1)
        for i in range(c):
            draw.ellipse([(y * (i + 1) + 200 * i + 400, 900), (y * (i + 1) + 200 * i + 600, 1100)], fill='#9999FF')
            p = t[i]
            if i % 2 == 0:
                draw.text(
                    (y * (i + 1) + 200 * i + 400, 650),
                    p['goal'],
                    # Добавляем шрифт к изображению
                    font=fontL,
                    fill='#1C0606')
                draw.text(
                    (y * (i + 1) + 200 * i + 400, 600),
                    p['date'],
                    # Добавляем шрифт к изображению
                    font=fontM,
                    fill='#1C0606')
            else:
                draw.text(
                    (y * (i + 1) + 200 * i + 400, 1350),
                    p['goal'],
                    # Добавляем шрифт к изображению
                    font=fontL,
                    fill='#1C0606')
                draw.text(
                    (y * (i + 1) + 200 * i + 400, 1300),
                    p['date'],
                    # Добавляем шрифт к изображению
                    font=fontM,
                    fill='#1C0606')


        image.save('image.png')
        image = open('image.png', 'rb')  # open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.b64encode(image_read)
        return image_64_encode
if __name__=='__main__':
    app.run(debug=True)
