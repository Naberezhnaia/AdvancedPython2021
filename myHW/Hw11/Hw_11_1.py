import re
s = ' Молоко стоит $2. Один билет в Сан-Франциско и обратно стоит 30000 ₽, а 2 билета — всего 50000₽! €1 = 90₽ (2021 год, 22 ноября)'
print(re.findall("\d+(?=₽)|(?<=€)\d+|(?<=\$)\d+|\d+(?= ₽)", s))
