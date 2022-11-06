def make_sentence(phrase):
    punctuation = "?" if is_question(phrase) else "."
    return phrase.capitalize() + punctuation


def is_question(phrase):
    return phrase.lower().startswith(("how", "where", "what", "when", "why", "who"))


text = ""
inputs = []

while text != "/end":
    text = input("Say something: ")

    if text == "/end":
        break

    inputs.append(make_sentence(text))

print(" ".join(inputs))
