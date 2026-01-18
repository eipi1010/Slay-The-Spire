import arrr

def translate_english(english):
    return arrr.translate(english)

if __name__ == "__main__":
    english = input("Type English here: ")
    print(translate_english(english))
