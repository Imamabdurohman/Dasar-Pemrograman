nama = "Imam Abdu Rohman Ramdani"
print (nama [3:8])
print (nama [0])
print (nama [-7:])
print (nama [0:4]) # 4 nya nggak kehitung
print (nama [::-1]) # ngebalik nama
print (nama [0:5]*2)
print(len(nama))


sentence = "Maling, Pencuri,Badog"
word = sentence.split(",")
print(word)

def clean(word):
    return word.strip()

cleaned = list(map(clean, word))
print(cleaned)

print(",".join(cleaned))