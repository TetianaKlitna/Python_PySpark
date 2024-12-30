from Caesar_Art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_amount, encode_or_decode):
    result_text = ""
    size_alphabet = len(alphabet)
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            new_ind = (alphabet.index(letter) + shift_amount) % size_alphabet
            result_text += alphabet[new_ind]
        else:
            result_text += letter
    print(f"Here is the {encode_or_decode}d result: {result_text}")


should_continue = "yes"
while should_continue == "yes":
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(original_text=text, shift_amount=shift,
                  encode_or_decode=direction)
    should_continue = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if should_continue == "no":
        print("Goodbye")
