alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']

sentence = input('Wprowadź zdanie do kodowania:   ')
kod = 2
wynik = ''
for litera in sentence:
    if litera in alphabet:
        alphabet_index = alphabet.index(litera)
        kodowany_index = (alphabet_index + kod) % len(alphabet)
        wynik += alphabet[kodowany_index]
    else:
        wynik += litera
print (wynik)