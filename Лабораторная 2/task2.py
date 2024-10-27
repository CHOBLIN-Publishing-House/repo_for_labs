salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

#Считаем все траты
all_spends = 0
for month in range(months):
    all_spends += spend
    spend *= 1 + increase

#Вся зарплата
all_salary = salary * months

money_capital = all_spends - all_salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
