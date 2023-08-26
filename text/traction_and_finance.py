class financial:
    def __init__(self, income, number_clients, churn_rate):
        self.income = income  # имя человека
        self.number_clients = number_clients  # возраст человека
        self.churn_rate = churn_rate  # возраст человека

    def APRU(self):
        return self.income / self.number_clients

    # рекомендуется изучить информацию на листе "Churn Rate"/заполняется самостоятельно
    def LT(self):
        return 1 / self.churn_rate

    def LTV(self):
        return self.APRU() * self.LT()

# Выручка
# *вбивается самостоятельно участниками на основе данных Чекко/Сбис/Спарк и/или
# income = 100000
# Число клиентов
# *вбивается самостоятельно участниками на основе данных Чекко/Сбис/Спарк и/или
# number_clients = 10
# *рекомендуется изучить информацию на листе "Churn Rate"/заполняется самостоятельноУровень оттока
# churn_rate = 10


test = financial(1000, 10, 10)
print(test.APRU())
print(test.LT())
print(test.LTV())
