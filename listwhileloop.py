names=['John Doe','Jane Doe','Johnny Turk','Molly Morman']
i=0
total_names=len(names)
print('users:')

while i< total_names:
#if i== total_names -2
    #end='and\n'
    #else:
    #end='\n'
    #alternative method

    end='and\n'if i==total_names -2 else '\n'

    print(' -%s' % names[i],end=end )
    i+=1

