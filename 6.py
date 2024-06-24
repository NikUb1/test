MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def encode_to_morse(text):
    text = text.upper()
    morse_code = ""
    for char in text:
        if char in MORSE_CODE:
            morse_code += MORSE_CODE[char] + " "
    return morse_code


def decode_from_morse(morse_code):
    morse_code = morse_code.strip()
    words = morse_code.split(" ")
    text = ""
    for word in words:
        for letter, code in MORSE_CODE.items():
            if word == code:
                text += letter
                break
    return text


def main():
    while True:
        action = input("Выберите действие (кодировать/декодировать/выход): ").lower()

        if action == "кодировать":
            text = input("Введите текст латиницей: ")
            encoded_text = encode_to_morse(text)
            print(f"Закодированный текст: {encoded_text}")
        elif action == "декодировать":
            morse_code = input("Введите текст в азбуке Морзе: ")
            decoded_text = decode_from_morse(morse_code)
            print(f"Декодированный текст: {decoded_text}")
        elif action == "выход":
            break
        else:
            print("Неверная команда.")


main()
