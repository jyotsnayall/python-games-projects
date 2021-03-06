
emotes = {
    ":)" : "đī¸",
    "B)" : "đī¸",
    ";)" : "đī¸",
    "XD" : "đī¸",
    ":3" : "đī¸",
    ":O" : "đŽī¸",
    ":(" : "đī¸",
    "X(" : "đŖī¸",
    "TT" : "đ­ī¸",
    "XP" : "đī¸",
    ":P" : "đī¸",
    ":'(" : "đĸī¸",
    ".-." : "đī¸",
    ";3" : "đī¸",
    ":|" : "đī¸",
    ":C" : "âšī¸",
    "^^" : "đī¸",
    ":')" : "đĨ˛",
    "-_-" : "đ",
    "O:)" : "đ",
    ">:O" : "đ˛",
    "<3" : "â¤ī¸",
    "</3" : "đ",
    "oâo" : "đŗ",
    ">.<" : "đ",
    "XO" : "đĩ",
    "_/\_" : "đ",
    "O/" : "đī¸",
    "X_X" : "đŖī¸"
}


def convertor():

    convert = True

    while convert:

        print("Type 'exit' to quit")
        message = input("> ")
        words = message.split(' ')


        if message.lower() == "exit":
            break


        output = ""
        for word in words:
            output += emotes.get(word.upper(),word) + " "

        print(output)


if __name__ == "__main__":
    convertor()


