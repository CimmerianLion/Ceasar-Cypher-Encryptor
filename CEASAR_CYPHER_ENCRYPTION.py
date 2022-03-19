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
    encrypted_message = ''

    for letter in message:

        if letter in symbols_database:
            letterIndex = symbols_database.find(letter)
            encrypted_letterIndex = letterIndex + shift_key

            if encrypted_letterIndex >= len(symbols_database):
                encrypted_letterIndex = encrypted_letterIndex - len(symbols_database)

            elif encrypted_letterIndex < 0:
                 encrypted_letterIndex = encrypted_letterIndex + len(symbols_database)

            encrypted_message = encrypted_message + symbols_database[encrypted_letterIndex]

        else:
            encrypted_message = encrypted_message + letter

    print(encrypted_message)

if __name__ == '__main__':
    encrypt()



