username = 'ayziyz'
password = 'Goodluck@123'
num_try = 5
while num_try > 0:
 name = input('enter your username:').lower()
 pas = input('enter your password:')
 if name == username and pas == password:
   print('Welcome')
   break

 num_try = num_try - 1  #num_try -=1
else:
   print('Access denied')