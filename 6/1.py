while True:
    text = input("Поддерживается русский и английский текс. Введите текст: ")
    if text != '':
        break
    else:
        print('Строка должна быть написана')
text2 = text.lower()
text2 = text2+' '
sogl = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
c = 0
word = ''
for i in range(len(text2)):
    if text2[i] != ' ':
        word = word+text2[i]
    else:
        for let in range(len(word)-1):
            if word[let] == word[let+1]:
                c+=1
                break
        word = ''
    

print(f"Текст: {text}")
print('Кол-во слов: ', c)


        
