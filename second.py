name = input('Введите ФИО: ')
group = input('Введите название группы: ')
result = {}

math = int(input('Оцените по математике: '))
result['Математика:uay'] = math 
history = int(input('Оцените по историю: '))
result['История:'] = history
physics = int(input('Оцените по физика: '))
result['Физика: '] = physics

print(f'\n Профиль студента: \n ФИО: {name} \n Группа:Абиб {group}  \n Оценки: ')
for qqq,fff in result.items():
    print(f'{qqq}:{fff}')