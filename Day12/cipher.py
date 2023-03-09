alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



#TODO1:Create a function called 'encrypt' that takes the 'text' and
#'shift' as inputs

# def encryption(plain_text,shift_amount):
#     #TODO-2:Inside the 'encrypt function shift each letter of the text forward
#     #in the alphabet by the shift amount and print the encrypted text

#     #plain_text="Hello"
#     #shift=5
#     #cipher_text="mjqqt"
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"the encoded Text :{cipher_text}")


# #TODO-2: Create a different function called decrypt that takes the text and shift as inputs
# def decrypt(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         plain_text+=alphabet[new_position]
#     print(f"The decoded text is {plain_text}")




# if direction=='encode':
#     encryption(plain_text=text,shift_amount=shift)
# elif direction=='decode':
#     decrypt(cipher_text=text,shift_amount=shift)




#TODO-1 Combine the encrypt() and decrypt() function into single function called caesar()

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=='decode':
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
              position=alphabet.index(letter)
              new_position=position+shift_amount
              end_text+=alphabet[new_position]
        else:
             end_text+=char
    print(f'here the {direction}d result: {end_text}')



should_continue=True
while should_continue:
     direction=input("Type encode to encrypt type 'decode ' to decrypt ")
     text=input("type your message:\n").lower()
     shift=int(input("Type the shift number:\n"))

     shift=shift%26
     caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
     result=input("Type 'yes' if you want to go again otherwise type no \n")
     if result=='no':
          should_continue=False
          print(f"Good Bye")

 