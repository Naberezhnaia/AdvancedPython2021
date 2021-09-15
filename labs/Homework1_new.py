#-*-coding:utf-8-*-
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ']
number = input()
message = []
while number != 'End':
    message.append(alphabet[int(number)])
    number = input()
for i in message:
    print (i, end='')