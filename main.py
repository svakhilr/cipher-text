letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
         'z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
         'z']

def encrypt(shift,text):
    encrypt_word=""
    for x in text:
        if x==' ':
            encrypt_word+=' '
        else:
            pos=letters.index(x)
            new_pos=pos+shift

            encrypt_word+=letters[new_pos]

    print(f'Encrypted word {encrypt_word}')

def decrypt(shift,text):
    decrypt_word=""
    for x in text:
        if x == ' ':
            decrypt_word+=' '

        else:
            pos=letters.index(x)
            new_pos=pos-shift
            decrypt_word+=letters[new_pos]

    print(f'Decrypted word  {decrypt_word}')

choice=True
while choice:

    direction=input('enter encrypt or decrypt ').lower()
    plain_text=input('enter  the text ').lower()
    shift_amount=int(input('enter shift amount '))
    if direction == 'encrypt':
        encrypt(shift_amount,plain_text)

    else:
        decrypt(shift_amount,plain_text)

    option=input('Do you want to continue yes or no ').lower()
    if option == 'no':
        choice=False