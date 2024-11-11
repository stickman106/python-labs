while True:
    text = input("Введите текст: ")
    if text != '':
        break
    else:
        print('Строка должна быть написана')
sogl = 'бвгджзйклмнпрстфхцчшщ'
c=0
for i in set(text):
    if i.isalpha() == False:
        text = text.replace(i, ' ')
text = text.lower()
l = text.split()
for word in l:
    for i in range(len(word)-1):
        if word[i] == word[i+1] and word[i] in sogl:
            c+=1
            break
print(f"Текст: {text}")
print('Кол-во слов: ', c)


        
