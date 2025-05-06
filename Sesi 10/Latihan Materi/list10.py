my_list = [1,"Nina tidur",False,9.0]
print(my_list[3:])
# del untuk hapus value (del list[2])
# remove untuk hapus index (list.remove("Nina tidur"))
# [1,2,3]+[4,5,6] = [1,2,3,4,5,6]
# numpy [1,2,3]+[4,5,6] = [1,2,3,4,5,6] [4,7,9]


people = {
    'name': 'zacki',
    'age': 20,
    'isMaried': False,
    'address': [
        {
            'city': 'Sukabumi',
            'province': 'Jawa Barat'
        },
        {
            'city': 'Bangalore',
            'province': 'india'
        }
    ]
}

print(people)
print(f'My city is: {people["address"][0]['city']}')
