import json
import os
import subprocess

import openai
import requests
from bs4 import BeautifulSoup

from text.traction_and_finance import financial


def presa(pattern):
    oldfile = open("./mdFiles/" + pattern + ".md", "r")
    newfile = open("./mdFiles/" + pattern + "_n.md", "w")

    with open('json.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        company_name =  text['title']
        mission_statement = text['statement']

        model_engine = "text-davinci-003"
        prompt = "Сформулируй проблематику более грамотно: "+text['problem']
        max_tokens = 100
        # генерируем ответ
        """completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # выводим ответ
        description_of_the_problem = completion.choices[0].tex"""
        description_of_the_problem = "completion.choices[0].tex"

        model_engine = "text-davinci-003"
        prompt = "Сформулируй проблематику более грамотно: " + text['advantages']
        max_tokens = 100
        # генерируем ответ
        """completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        advantages = completion.choices[0].tex"""
        advantages = "completion.choices[0].tex"

        targen_person = text['target']
        functional_description = text['functionality']

        """model_engine = "text-davinci-003"
        prompt = "Назови значение TAM отрасли " + text['industry']
        max_tokens = 100
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
        tam = completion.choices[0].tex"""
        tam = "100"

        """text = json.load(f)
        model_engine = "text-davinci-003"
        prompt = "Назови значение SAM отрасли " + text['industry']
        max_tokens = 100
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
        sam = completion.choices[0].tex"""
        sam = "10000"

        """text = json.load(f)
        model_engine = "text-davinci-003"
        prompt = "Назови значение SOM отрасли " + text['industry']
        max_tokens = 100
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
        som = completion.choices[0].tex"""
        som = "10000000"


        # Трекшн и финансы
        finan = financial(text['income'], text['number_clients'], text['churn_rate']) ############ Нет данных
        income = str(finan.income)
        number_clients = str(finan.number_clients)
        churn_rate = str(finan.churn_rate)
        APRU = str(finan.APRU())
        LT = str(finan.LT())
        LTV = str(finan.LTV())

        ## Конкуренты
        with open('json.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            #data = {'key': 'nGjfQjlRSfqBNymo', 'inn': text['inn']}
            data = {'key': 'nGjfQjlRSfqBNymo', 'inn': 6321313849}
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

        competitors = str(headers)
        count = text['investsAmount']
        email = text['email']
        phone = text['phone']
        address = text['address']

    for line in oldfile:
        line = line.replace("company_name", company_name)
        line = line.replace("mission_statement", mission_statement)
        line = line.replace("description_of_the_problem", description_of_the_problem)
        line = line.replace("advantages", advantages)
        line = line.replace("targen_person", targen_person)
        line = line.replace("functional_description", functional_description)
        line = line.replace("tam", tam)
        line = line.replace("sam", sam)
        line = line.replace("som", som)
        line = line.replace("income", income)
        line = line.replace("number_clients", number_clients)
        line = line.replace("churn_rate", churn_rate)
        line = line.replace("APRU", APRU)
        line = line.replace("LT", LT)
        line = line.replace("LTV", LTV)
        line = line.replace("competitors", competitors)
        line = line.replace("count", count)
        line = line.replace("email", email)
        line = line.replace("phone", phone)
        line = line.replace("address", address)
        newfile.write(line)



def final_presa():
    # готовим презентации
    presa("pattern1")
    presa("pattern2")
    presa("pattern3")

    command = '/bin/sh ./script_presa.sh'
    os.system(command)
    return "final_presa done!"


final_presa()

