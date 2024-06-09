def color_convertation(lamda):
    if lamda < 380:
        red, green, blue = 0, 0, 0
    elif lamda < 440:
        red = (440 - lamda) / 60
        green, blue = 0, 1
    elif lamda < 490:
        red = 0
        green = (lamda - 440) / 50
        blue = 1
    elif lamda < 510:
        red, green = 0, 1
        blue = (510 - lamda) / 20
    elif lamda < 580:
        red = (lamda - 510) / 70
        green, blue = 1, 0
    elif lamda < 645:
        red = 1
        green = (645 - lamda) / 65
        blue = 0
    elif lamda <= 780:
        red, green, blue = 1, 0, 0
    else:
        raise ValueError("Эту длину волны не видно")
    return red, green, blue
