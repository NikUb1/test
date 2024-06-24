def lucky(ticket):
    global lastTicket
    smt = sum(list(map(int, list(ticket[:4])))) == sum(list(map(int, list(ticket[-3:]))))
    smlt = sum(list(map(int, list(lastTicket[:4])))) == sum(list(map(int, list(lastTicket[-3:]))))
    if smt and smlt:
        print("Счастливый")
    else:
        print("Несчастливый")
