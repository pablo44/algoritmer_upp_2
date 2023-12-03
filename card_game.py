def insert(card_list, card):
    if not card_list:
        card_list.append(card)
    else:
        inserted = False
        for i in range(len(card_list)):
            if card < card_list[i]:
                card_list.insert(i, card)
                inserted = True
                break

        if not inserted:
            card_list.append(card)

    return card_list

cards = [2, 5, 7, 10, 15]
new_card = 8
result = insert(cards, new_card)
print(result)