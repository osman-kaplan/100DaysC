
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '(e)ncode' to encrypt, type '(d)ecode' to decrypt:\n> ")
text = input("Type your message:\n> ").lower()
shift = int(input("Type the shift number:\n> "))


def decrypt(text_parameter,shift_parameter):
        decrypted_text=''
        for letter in text_parameter:

          positon = alphabet.index(letter)

          if letter !=0 :
              decrypted_text += alphabet[positon - shift_parameter]
          else:
              decrypted_text += ' '
    
        print(f"The decrypted tex:\n{decrypted_text}")

def encrypt(text_parameter,shift_parameter):
    
        shifted_text=''

        for letter in text_parameter:
          if letter !=' ':
            position= alphabet.index(letter)
            shifted_text += alphabet[position+ shift_parameter]
          else:
            shifted_text += ' '
        print(f"Encrypted text: \n{shifted_text}")

def caesar(text,shift, direction):

    text_to_print = ''

    if shift > len(alphabet):
          shift = (shift % len(alphabet))

    if direction.lower().startswith('d'):
      shift *= -1

    for char in text:
          if char in alphabet:
          
            shifted_positon =alphabet.index(char) + shift         
            text_to_print +=alphabet[shifted_positon]
          else:
            text_to_print +=char
                

    print('working...')      
    print(text_to_print)

       

         

      #       encrypt(text_parameter=text, shift_parameter= shift)
      
      # elif direction.lower().startswith('d'):
      #       decrypt(text_parameter=text, shift_prameter=shift)
      # else:
      #       print('???')


caesar(text,shift,direction)



























  















