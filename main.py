from csv import reader
import unicodedata
import re


def remove_accents(raw_text):
    raw_text = re.sub("[àáâãäå]", "a", raw_text)
    raw_text = re.sub("[èéêë]", "e", raw_text)
    raw_text = re.sub("[ìíîï]", "i", raw_text)
    raw_text = re.sub("[òóôõö]", "o", raw_text)
    raw_text = re.sub("[ùúûü]", "u", raw_text)
    raw_text = re.sub("[ýÿ]", "y", raw_text)
    raw_text = re.sub("[ß]", "ss", raw_text)
    raw_text = re.sub("[ñ]", "n", raw_text)
    raw_text = re.sub("[¿]", "", raw_text)
    raw_text = re.sub("[?]", "", raw_text)
    raw_text = re.sub("[¡]", "", raw_text)
    raw_text = re.sub("[!]", "", raw_text)
    raw_text = re.sub("[.]", "", raw_text)
    return raw_text


answers = []
questions = []
with open("spanishhelper.csv", "r", encoding="UTF-8") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        row[0] = remove_accents(row[0])
        row[1] = remove_accents(row[1])
        answers.append(row[0])
        questions.append(row[1])

while True:
    for index in range(len(questions)):
        user_input = input(questions[index] + ": ")
        if user_input == "stop":
            break
        else:
            if user_input.lower() == answers[index].lower():
                print("You got it!", end="\n\n")
            else:
                print(f"No, it was >> {answers[index]}", end="\n\n")
        print("*********")
