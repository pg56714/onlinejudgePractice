def evaluate_hand(cards):
    rank_to_number = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    card_counts = {}
    numbers = []

    for card in cards:
        card = card.strip()
        number = rank_to_number[card]
        numbers.append(number)
        # print(numbers)
        if number in card_counts:
            card_counts[number] += 1
        else:
            card_counts[number] = 1

    # Check straight
    if len(numbers) >= 5:
        numbers = sorted(set(numbers))  # remove duplicates
        for i in range(len(numbers) - 4):
            if numbers[i + 4] == numbers[i] + 4:  # five consecutive numbers
                return 1  # straight

    # Check full house and pair
    pairs = 0
    three_of_a_kind = False
    four_of_a_kind = False
    counts = list(card_counts.values())
    for count in counts:
        if count == 4:
            four_of_a_kind = True
        elif count == 3:
            three_of_a_kind = True
        elif count == 2:
            pairs += 1

    if three_of_a_kind and pairs >= 1:
        return 2  # full house
    if four_of_a_kind:
        return 3  # four cards are considered two pairs
    if pairs > 1:
        return 3  # two pairs
    if pairs == 1:
        return 4  # one pair

    return 5  # no any special hand


input_str = input().strip().split(",")
print(evaluate_hand(input_str))
