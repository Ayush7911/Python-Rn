names=['John Doe','Jane Doe','Johnny Turk','Molly Morman']
print('Users :')

for name in names:
    end ='and\n' if name==names[-2] else '\n'

    print('- %s'%name, end=end)