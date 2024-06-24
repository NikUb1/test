def translate(text):
    global translated_text
    gl = 'уеыаоэяию?.,!-'
    ot = ''
    for x in text:
        if x.lower() not in gl:
            ot += x
    translated_text = ' '.join(ot.split())


translated_text = None
translate(
    "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
print(translated_text)
