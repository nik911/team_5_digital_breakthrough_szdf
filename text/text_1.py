import openai

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"

# задаем модель и промпт
model_engine = "text-davinci-003"
prompt = "Write poem about how cool readers of uproger website"

# задаем макс кол-во слов
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
print(completion.choices[0].text)
