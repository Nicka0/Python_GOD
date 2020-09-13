###                     if, else and elif                   ####
user = raw_input('Digite o nome do usuario: ')

if user == 'root':
    print 'User logged in as %s' % user

elif user == 'admin':
        print 'User logged in as %s' % user

else:
    print 'User invalid!'
