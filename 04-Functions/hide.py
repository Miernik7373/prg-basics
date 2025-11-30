def hide(card_number: str):
    star = card_number[0:2]
    end = card_number[len(card_number)-4:len(card_number)]
    middle = '*'*(len(card_number)-6)
    card_number = star+middle+end
    return card_number
