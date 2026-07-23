alphabets = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message...\n")
    shift = int(input("type the shift number.\n"))
    # encoded_text = ""
    # decoded_text = ""

    def encode(text):
        encoded_text = []
        for item in text:
            if item not in alphabets:
                encoded_text += item
            else:
                ind = alphabets.index(item)
                sf = int(ind) + shift
                # print(sf)
                if sf >= 25:
                    encoded_index = sf - 26
                    encoded_text += alphabets[encoded_index]
                else:
                    encoded_index = sf
                    encoded_text += alphabets[encoded_index]

        a = ""
        for i in encoded_text:
            a += i
        print(f"Your Encoaded Message is: {a}")

    def decode(text):
        encoded_text = []
        for item in text:
            if item not in alphabets:
                encoded_text += item
            else:
                ind = alphabets.index(item)
                sf = int(ind) - shift
                # print(sf)
                if sf < 0:
                    encoded_index = sf + 26
                    encoded_text += alphabets[encoded_index]
                else:
                    encoded_index = sf
                    encoded_text += alphabets[encoded_index]

        a = ""
        for i in encoded_text:
            a += i
        print(f"Your decoaded Message is: {a}")


    if direction == "encode":
        encode(text)
    elif direction == "decode":
        decode(text)
    else:
        print("Please type direction clearly only as encode or decode")

    repeat = input("Do you want to conitinue? [Y/N]\n").lower()
    if repeat == "y":
        should_continue = True
    else:
        should_continue = False