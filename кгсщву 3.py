from turtle import Turtle, Screen, done


def f(letter):
    global LETTER
    LETTER = letter


def f_write(x, y):
    global LETTER
    if LETTER:
        tut.goto(x, y)
        tut.write(LETTER.upper(), align='center', font=('Timesnewroman', 48, 'bold'))
    LETTER = ''


LETTER = ''
sc = Screen()
sc.setup(startx=0, starty=0)
tut = Turtle()
tut.color('crimson')
tut.pu()
tut.ht()
sc.onclick(f_write)
k = 'qwertyuiopasdfghjklzxcvbnm'
for char in 'qwertyuiopasdfghjklzxcvbnm':
    sc.onkeypress(lambda ch=char: f(ch), char)
sc.listen()
done()
