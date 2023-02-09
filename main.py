# This caesar_cipher program allows the user to encrypt/decrypt
# messages using the ancient caesar cipher method of shifting letters
# of the alphabet. Non-alphabetic chars will not be shifted
# It prompts the user for the following:
#   direction: 'encode' or 'decode'
#   message: the message that will be encoded or decoded
#   shift_amount: the number of spaces to shift the letters
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

# have an external loop to allow the user to perform encode/decode
# more than once
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # if the user enters a shift > the number of letters of the alphabet
    # perform a modulus based on the number of letters in the alphabet
    # to get the remainder to prevent shifting more chars than the
    # number of letters in the alphabet
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
