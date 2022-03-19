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

english_alphabet = ['A']


def encrypt():
    message = input('Type the message you wish to have encrypted below...')
    shift_num = input('Now enter the number of shifts you want the encryption '
                      'of your message to be based on...')
    message = message.rstrip()

    for letter in message:
        pass
