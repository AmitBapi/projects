alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p","q","r", "s", "t", "u", "v", "w", "x", "y", "z"]

##for encryption
# def encrypt(orginal_text,shift_amount):
#     cypher_text=""
#     for letter in orginal_text:
#         shifted_position = alphabet.index(letter)+shift_amount
#         shifted_position %= len(alphabet)
#         cypher_text += alphabet[shifted_position]
#     print(f"your encoded result is : {cypher_text}")
# encrypt(orginal_text=text,shift_amount=shift)

###for decryption
# def decrypt(orginal_text, shift_amount):
#     for letter in orginal_text:
#         shifted_position = alphabet.index(letter)-shift_amount
#         shifted_position %= len(alphabet)
#         cypher_text += alphabet[shifted_position]
#     print(f"your decoded result is : {cypher_text}")
# decrypt(orginal_text=cypher_text,shift_amount=shift)


###add the parts in one
def ceaser(orginal_text, shift_amount, encode_or_decode):
    output_text=""
    
    for letter in orginal_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            if encode_or_decode=="decode":
            # shift_amount*= -1
                shifted_position = alphabet.index(letter)-shift_amount
            elif encode_or_decode == "encode":
                shifted_position = alphabet.index(letter)+shift_amount
            else:
                print("you entered a wrong option!!!")
                exit()
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"your {encode_or_decode}d result is : {output_text}")

should_continue= True
while should_continue:
    direction = input("type 'encode' to encrypt OR type 'decode' to decrypt: \n").lower()
    text = input ("type your message : \n")
    shift = int(input("type the shift number : \n"))
    
    ceaser(text, shift, direction)
    
    continue_or_not= input("Type 'yes' to continue, otherwise type 'no'\n").lower()
    if continue_or_not=="no":
        should_continue=False
        print("Goodbye")