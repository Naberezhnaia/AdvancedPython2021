alphabet = ["à","á","â","ã","ä","å","¸","æ","ç","è","é","ê","ë","ì","í","î","ï","ð","ñ","ò","ó","ô","õ","ö","÷","ø","ù","ú","û","ü","ý","þ","ÿ"," "]
number = input()
message = []
while number != "End":
    message.append(alphabet[int(number)])
    number = input()
for i in message:
    print (i, end='')

