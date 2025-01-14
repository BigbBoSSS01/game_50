Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}


del Geeks['bag']


Geeks['address'] = 'New Address, 123'


Geeks['phone'] = '+1234567890'
Geeks['instagram'] = '@geeks_official'


new_courses = ['Data Science', 'AI', 'Machine Learning']
Geeks['courses'] += new_courses  
Geeks['courses'] = set(Geeks['courses'])  


Geeks['foundation_date'] = '2010-09-15'


print("Количество курсов:", len(Geeks['courses']))


for key, value in Geeks.items():
    print(f"{key}: {value}")
