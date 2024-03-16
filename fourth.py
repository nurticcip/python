sum = float(input("Введите сумму для преобразования: "))

begin_sum = input("Введите начальную валюту (USD, EUR, RUB): ")

end_sum = input("Введите целевую валюту (USD, EUR, RUB): ")

coins = {
"USD": 0.014,
"EUR": 0.012,
"RUB": 1.0
}

if begin_sum  == end_sum:
    converted_amount = sum
else:
    converted_amount = sum * coins[begin_sum] / coins[end_sum]

print(f"{sum} {begin_sum} == {converted_amount} {end_sum}.")