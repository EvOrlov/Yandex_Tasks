from re import match

arr = ['Мама', 'авТо', 'гриБ', 'ябЛоко', 'агент007', 'стриж', 'ГТО', 'Три богатыря']
pattern = r'^[a-zа-яё]*[A-ZА-ЯЁ][a-zа-яё]*$'
for i in arr:
    print(match(pattern, i))
