sentence = input('Введите предложение: ')

for i, element in enumerate(sentence.split()):
    print(i+1, element[:10])