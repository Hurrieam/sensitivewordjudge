import sensitivewordjudge

if __name__ == '__main__':
    word: str = input("input tested word: \n>>")
    print(("\"{}\" is " + (
        "not " if sensitivewordjudge.is_sensitive(word) is False else "") + "a sensitive word. ").format(word))
