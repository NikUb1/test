name = ""
vacantion_dates = ""


def setup_profile(nm, vd):
    global name
    global vacantion_dates
    name = nm
    vacantion_dates = vd


def print_application_for_leave():
    print(f"Заявление на отпуск в период {vacantion_dates}. {name}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {name}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {vacantion_dates} моим замести{to_whom}")
