loshadi = dict()


def do_bet(num, bet):
    if 0 < num < 11 and num not in loshadi:
        print(f"Ваша ставка в размере {bet} на лошадь {num} принята")
        loshadi[num] = True
    else:
        print("Что-то пошло не так, попробуйте еще раз")
