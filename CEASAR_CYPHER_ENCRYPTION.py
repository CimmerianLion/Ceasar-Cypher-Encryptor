# THE CEASAR CYPHER
# BY NICK KONTODIMAS,
# AKA THE CIMMERIAN LION

print('This is the Ceasar Cypher encryption system programmed on Python 3. '
      'The Ceasar Cypher works by shifting every letter of a message from its ' 
      'corresponding place in the alphabet to the letter that corresponds ' 
      'to the number of shifts we use for the encryption plus that of the ' 
      'original letter. ' 
      '' 
      'For example: ' 
      ''
      'With a shift of say 5:  ' 
      'C E A S A R  becomes H J E Y E X.  ' 
      '3 5 1 19 1 18   +5   8 10 6 24 6 23. ')

print('Type the message you wish to have encrypted below...')
message = input('> ')

print('Now enter the number of shifts you want the encryption '
      'of your message to be based on...')
shift_key = int(input('> '))

message = message.rstrip()
#encrypted_message = None
symbols_database = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'\
                   'abcdefghijklmnopqrstuvxyz'\
                   '1234567890'

def encrypt():
    #This variable will hold the encrypted message
    encrypted_message = ''
    
    #We iterate through every letter in our message and encrypt it
    for letter in message:
        
        #Here the ascii alphabet we saved earlier comes in hand
        if letter in symbols_database:
            letterIndex = symbols_database.find(letter)
            
            #The results will vary depeniding on what shift key we use
            encrypted_letterIndex = letterIndex + shift_key
            
            #The if and elif statements prove useful in case the encrypted_letterIndex integer
            #extends outside the length of the ascii alphabet string
            if encrypted_letterIndex >= len(symbols_database):
                encrypted_letterIndex = encrypted_letterIndex - len(symbols_database)

            elif encrypted_letterIndex < 0:
                 encrypted_letterIndex = encrypted_letterIndex + len(symbols_database)
            
            encrypted_message = encrypted_message + symbols_database[encrypted_letterIndex]
        
        #In case there are character we have not included in our symbols_database
        else:
            encrypted_message = encrypted_message + letter

    print(encrypted_message)

if __name__ == '__main__':
    encrypt()



