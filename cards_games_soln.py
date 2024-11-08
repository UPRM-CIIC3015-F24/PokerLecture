import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suites = {'hearts', 'spades', 'clubs', 'diamonds'}

winning_hands = ['High Card',
                 'One Pair',
                 'Two Pair',
                 'Three of a Kind',
                 'Straight',
                 'Flush',
                 'Full House',
                 'Four of a Kind',
                 'Straight Flush']


def gen_full_deck():
    full_deck = []
    for rank in ranks:
        for suit in suites:
            full_deck.append([rank, suit])
    return full_deck


All_Deck = gen_full_deck()


def draw_hands(num_players, num_cards):
    hands = []
    for _ in range(0, num_players):
        hands.append([])
    remaining_cards = list(gen_full_deck())  # Copy of entire deck
    random.shuffle(remaining_cards)
    for _ in range(0, num_cards):
        for p in range(0, num_players):
            new_card = remaining_cards[len(remaining_cards)-1]
            hands[p].append(new_card)
            remaining_cards.pop()
    return hands


PlayerHands = draw_hands(4, 5)
print(PlayerHands)


def is_four_of_a_kind(hand):
    cnts = {}
    for rank, suit in hand:
        cnts[rank] = cnts.get(rank, 0) + 1
        if cnts[rank] == 4:
            return True
    return False


print('Four of a Kind',
      is_four_of_a_kind([['A', 'spades'], ['A', 'hearts'], ['A', 'diamonds'],
                         ['A', 'clubs'], ['5', 'spade']]))
print('Four of a Kind',
      is_four_of_a_kind([['A', 'spades'], ['A', 'hearts'], ['A', 'diamonds'],
                         ['5', 'clubs'], ['5', 'spade']]))


def is_full_house(hand):
    cnts = {}
    for rank, suit in hand:
        cnts[rank] = cnts.get(rank, 0) + 1
    cnt2_found = False
    cnt3_found = False
    for rank, cnt in cnts.items():
        if cnt == 2:
            cnt2_found = True
        if cnt == 3:
            cnt3_found = True
        if cnt2_found and cnt3_found:
            return True
    return False


print('Full  House',
      is_full_house([['A', 'spades'], ['A', 'hearts'], ['A', 'diamonds'],
                     ['3', 'clubs'], ['3', 'spade']]))
print('Full House',
      is_full_house([['A', 'spades'], ['A', 'hearts'], ['K', 'diamonds'],
                     ['3', 'clubs'], ['3', 'spade']]))
print('Full  House',
      is_full_house([['A', 'spades'], ['A', 'hearts'], ['3', 'clubs'],
                     ['3', 'spades'],  ['A', 'diamonds']]))


def is_flush(hand):
    cnts = {}
    for rank, suit in hand:
        cnts[suit] = cnts.get(suit, 0) + 1
        if cnts[suit] == 5:
            return True
    return False


print("Flush: ", is_flush([['A', 'spades'], ['J', 'spades'], ['Q', 'spades'],
                          ['3', 'spades'], ['4', 'spades']]))
print("Flush: ", is_flush([['A', 'spades'], ['J', 'clubs'], ['Q', 'spades'],
                          ['3', 'spades'], ['4', 'spades']]))


def rank_index(card):
    return ranks.index(card[0])


def is_straight(hand):
    hand = list(hand)
    hand.sort(key=rank_index)
    for i in range(0, 4):
        if abs(rank_index(hand[i])-rank_index(hand[i+1])) != 1:
            return False
    return True


print('Straight: ',
      is_straight([['10', 'spades'], ['J', 'spades'], ['Q', 'spades'],
                 ['K', 'spades'], ['A', 'spades']]))
print('Straight: ',
      is_straight([['9', 'spades'], ['10', 'spades'], ['J', 'diamonds'],
                   ['Q', 'spades'], ['K', 'spades']]))
print('Straight: ',
      is_straight([['9', 'spades'], ['10', 'spades'], ['2', 'spades'],
                   ['Q', 'spades'], ['K', 'spades']]))


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


print('Straight Flush: ',
      is_straight_flush([['10', 'spades'], ['J', 'spades'], ['Q', 'spades'],
                       ['K', 'spades'], ['A', 'spades']]))
print('Straight Flush: ',
      is_straight_flush([['9', 'spades'], ['10', 'spades'], ['J', 'diamonds'],
                         ['Q', 'spades'], ['K', 'spades']]))
print('Straight Flush: ',
      is_straight_flush([['9', 'spades'], ['10', 'spades'], ['2', 'spades'],
                         ['Q', 'spades'], ['K', 'spades']]))


hands = ['High Card',
         'One Pair',
         'Two Pair',
         'Three of a Kind',
         'Straight',
         'Flush',
         'Full House',
         'Four of a Kind',
         'Straight Flush']


def highest_hand(hand):
    if is_straight_flush(hand):
        return 'Straight Flush'
    elif is_four_of_a_kind(hand):
        return 'Four of a Kind'
    elif is_full_house(hand):
        return 'Full House'
    elif is_flush(hand):
        return 'Flush'
    elif is_straight(hand):
        return 'Straight'
    # elif is_three_of_a_kind(hand):
    #     return 'Three of a Kind'
    # elif is_two_pair(hand):
    #     return 'Two Pair'
    # elif is_one_pair(hand):
    #     return 'One Pair'
    else:
        return 'High Card'


player1 = [['10', 'spades'], ['J', 'spades'], ['Q', 'spades'], ['K', 'spades'], ['A', 'spades']]
player2 = [['A', 'spades'], ['J', 'spades'], ['Q', 'spades'], ['3', 'spades'], ['4', 'spades']]


print('HH Player 1:', highest_hand(player1))
print('HH Player 2:', highest_hand(player2))


def winner(hand1, hand2):
    hh_player1 = highest_hand(hand1)
    hh_player2 = highest_hand(hand2)
    if hands.index(hh_player1) > hands.index(hh_player2):
        print(f'Player 1 wins with a {hh_player1}')
    elif hands.index(hh_player1) < hands.index(hh_player2):
        print(f'Player 2 wins with a {hh_player2}')
    else:
        print(f'It\'s a tie!')


winner(player1, player2)
winner(player2, player1)




