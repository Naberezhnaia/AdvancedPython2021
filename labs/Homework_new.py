alphabet = ['�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�','�',' ']
number = input()
message = []
while number != 'End':
    message.append(alphabet[int(number)])
    number = input()
for i in message:
    print (i, end='')

