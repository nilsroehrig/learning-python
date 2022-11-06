def make_sentence(phrase):
    punctuation = "."

    if is_question(phrase):
        punctuation = "?"

    return phrase.capitalize() + punctuation


def is_question(phrase):
    if first_word_of(phrase.lower()) in ["how", "where", "what", "when", "why", "who"]:
        return True

    return False


def first_word_of(phrase):
    return phrase.split(" ")[0]


def main():
    text = ""
    inputs = []

    while text != "/end":
        text = input("Say something: ")

        if text == "/end":
            break

        inputs.append(make_sentence(text))

    print(" ".join(inputs))


main()
