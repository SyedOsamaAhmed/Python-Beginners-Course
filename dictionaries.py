# phone_digits = {

#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",


# }

# number = input("Phone: ")
# output = ""
# for digit in number:
#     output += phone_digits.get(digit, '!') + " "


# Emoji Generator:

message = input("> ")


def emoji_convertor(message):
    word = message.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😢"
    }
    output = ""
    for word in word:
        output += emojis.get(word, word) + " "

    return output


print(emoji_convertor(message))
