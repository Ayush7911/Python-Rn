first_name= input('Your first name: ')
last_name= input('your last name: ')

#old style formatting.
print('Hello %s %s' %(first_name,last_name))

#new style foematting.

print('Hello {} {}!' .format(first_name, last_name))
print('Hello {0} {1}!' .format(first_name, last_name))

#this is where , you will feel the difference.

print(' Hello {1} {0}' .format(first_name,last_name))
print('Hello world {0} {0} {1}!' .format(first_name, last_name))