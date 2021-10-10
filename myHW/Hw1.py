#-*-coding:utf-8-*-
ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
            'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
            'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
callnumber = input()
letter = ''

while callnumber != 'End':
    letter += str(ALPHABET[int(callnumber)])
    callnumber = input()

print(''.join(letter))
