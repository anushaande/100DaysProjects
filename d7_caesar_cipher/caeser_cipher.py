UPPER_LIST = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LOWER_LIST = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
go_again = True

def encoded_index(letter_index, num):
    if letter_index+num > 25:
        return letter_index + num-26
    else:
        return letter_index + num

def decoded_index(letter_index, num):
    return(letter_index - num)

def encode(word, shift):
    encoded_list = []
    word_list = list(word)
    for i in word_list:
        encoded_list += '_'
    for i in range(len(word_list)):
        if word_list[i] in UPPER_LIST:
            letter_index = UPPER_LIST.index(word_list[i])
            encoded_list[i] = UPPER_LIST[encoded_index(letter_index, shift)]
        elif word_list[i] in LOWER_LIST:
            letter_index = LOWER_LIST.index(word_list[i])
            encoded_list[i] = LOWER_LIST[encoded_index(letter_index, shift)]
        else:
            encoded_list[i] = word_list[i]
    return(''.join(encoded_list))

def decode(word, shift):
    decoded_list = []
    word_list = list(word)
    for i in word_list:
        decoded_list += '_'
    for i in range(len(word_list)):
        if word_list[i] in UPPER_LIST:
            letter_index = UPPER_LIST.index(word_list[i])
            decoded_list[i] = UPPER_LIST[decoded_index(letter_index, shift)]
        elif word_list[i] in LOWER_LIST:
            letter_index = LOWER_LIST.index(word_list[i])
            decoded_list[i] = LOWER_LIST[decoded_index(letter_index, shift)]
        else:
            decoded_list[i] = word_list[i]
    return(''.join(decoded_list))


while go_again:
    task = input("Type 'e' to encrypt or type 'd' to decrypt: /n").lower()
    if task == 'e':
        word_to_encrypt = input("Type your Message: \n")
        shift_number = int(input("Type the shift number: \n")) 
        print(f"Here is the encoded result: {encode(word_to_encrypt, shift_number)}")
    elif task == 'd':
        word_to_encrypt = input("Type your Message: \n")
        shift_number = int(input("Type the shift number: \n"))
        print(f"Here is the decoded result: {decode(word_to_encrypt, shift_number)}")
    else:
        print("Please enter appropriate text")
    
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if again == 'yes':
        go_again = True
    else:
        go_again = False

