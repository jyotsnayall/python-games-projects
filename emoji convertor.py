
emotes = {
    ":)" : "😀️",
    "B)" : "😎️",
    ";)" : "😉️",
    "XD" : "😆️",
    ":3" : "😗️",
    ":O" : "😮️",
    ":(" : "😞️",
    "X(" : "😣️",
    "TT" : "😭️",
    "XP" : "😝️",
    ":P" : "😛️",
    ":'(" : "😢️",
    ".-." : "🙃️",
    ";3" : "😙️",
    ":|" : "😐️",
    ":C" : "☹️",
    "^^" : "😊️",
    ":')" : "🥲",
    "-_-" : "😑",
    "O:)" : "😇",
    ">:O" : "😲",
    "<3" : "❤️",
    "</3" : "💔",
    "o‑o" : "😳",
    ">.<" : "😖",
    "XO" : "😵",
    "_/\_" : "🙏",
    "O/" : "👋️",
    "X_X" : "😣️"
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


