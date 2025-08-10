import random 
# Simple poker game (Five-card draw)

def royal_flush(cards):
    
    cards = changing_card_type(cards.copy())

    if cards == [10, 11, 12, 13, 14]:
        return True
    return False

def straight(cards):
    cards = changing_card_type(cards.copy())

    for index in range(len(cards)-1):
        if (cards[index+1]) != (cards[index]+1):
            return False

    if cards == [10, 11, 12, 13, 14]:
        return False    
    
    return True

def changing_card_type(cards):
    changing_type = {
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14,
    }
    for index, value in enumerate(cards):
        if isinstance(value, str):
            cards[index] = changing_type[value]
    
    cards.sort()
    return cards

def how_many_points(cards):
    card_ranking = {
        'Royal Flush': 10,
        'Straight flush': 9,
        'Four of a kind': 8,
        'Full house': 7,
        'Flush': 6,
        'Straight': 5,
        'Three of a kind': 4,
        'Two pair': 3,
        'One pair': 2,
        'High card': 1,
    }

    only_values = []
    only_color = []
    points = 1

    for i in range(len(cards)):
        color = cards[i][0]
        value = cards[i][1]
        
        only_color.append(color)
        only_values.append(value)

    only_unique_values = list(set(only_values))
    only_unique_colors = list(set(only_color))
 
    pair_count = 0

    if_pair = False
    if_two_pair = False
    if_three_of_a_kind = False
    if_quads = False

    for value in only_unique_values:
        values_count = only_values.count(value)
        if values_count == 2:
            pair_count  += 1
        elif values_count == 3:
            if_three_of_a_kind = True
        elif values_count == 4:
            if_quads = True

    if pair_count == 1:
        if_pair = True
    if pair_count == 2:
        if_two_pair = True
    
    if royal_flush(only_values) and len(only_unique_colors) == 1:
        points = card_ranking['Royal Flush']
    elif straight(only_values) and len(only_unique_colors) == 1:
        points = card_ranking['Straight flush']
    elif if_quads:
        points = card_ranking['Four of a kind']
    elif if_three_of_a_kind and if_pair:
        points = card_ranking['Full house']
    elif len(only_unique_colors) == 1:
        points = card_ranking['Flush']
    elif straight(only_values):
        points = card_ranking['Straight']
    elif if_three_of_a_kind:
        points = card_ranking['Three of a kind']
    elif if_two_pair:
        points = card_ranking['Two pair']
    elif if_pair:
        points = card_ranking['One pair']
    else:
        points = card_ranking['High card']
    
    return points

def checking_high_card(player_hand, opponent_hand):

    values_player = sorted(changing_card_type([value[1] for value in player_hand]), reverse=True)
    values_opponent = sorted(changing_card_type([value[1] for value in opponent_hand]), reverse=True)

    for card1, card2 in zip(values_player, values_opponent):
        if card1 != card2:
            if card1 > card2:
                return 'You win!'
            elif card1 < card2:
                return 'You lost!'
    return 'Tie'

def checking_quads_trees_or_pairs(player_hand, opponent_hand, value):
    values_player = changing_card_type([value[1] for value in player_hand])
    values_opponent = changing_card_type([value[1] for value in opponent_hand])

    values_unique_player = list(set(values_player))
    values_unique_opponent = list(set(values_opponent))

    suit_value_player = 0
    suit_value_opponent = 0
    for value1, value2 in zip(values_unique_player, values_unique_opponent):
        if values_player.count(value1) == value:
            suit_value_player = value1
        if values_opponent.count(value2) == value:
            suit_value_opponent = value2
    
    if suit_value_player > suit_value_opponent:
        return 'You win!'
    elif suit_value_player < suit_value_opponent:
        return 'You lost!'
    else:
        return checking_high_card(player_hand, opponent_hand)

def checking_full_house(player_hand, opponent_hand):
    values_player = changing_card_type([value[1] for value in player_hand])
    values_opponent = changing_card_type([value[1] for value in opponent_hand])

    values_unique_player = list(set(values_player))
    values_unique_opponent = list(set(values_opponent))

    pair_value_player = 0
    pair_value_opponent = 0
    three_value_player = 0
    three_value_opponent = 0
    for value1, value2 in zip(values_unique_player, values_unique_opponent):
        if values_player.count(value1) == 3:
            three_value_player = value1
        elif values_player.count(value1) == 2:
            pair_value_player = value1
        if values_opponent.count(value2) == 3:
            three_value_opponent = value2
        elif values_opponent.count(value2) == 2:
            pair_value_opponent = value2

    if three_value_player > three_value_opponent:
        return 'You win!'
    elif three_value_opponent > three_value_player:
        return 'You lost!'
    else:
        if pair_value_player > pair_value_opponent:
            return 'You win!'
        elif pair_value_opponent > pair_value_player:
            return 'You lost!'
        else:
            return 'Tie!'

def checking_two_pair(player_hand, opponent_hand):
    values_player = sorted(changing_card_type([value[1] for value in player_hand]), reverse=True)
    values_opponent = sorted(changing_card_type([value[1] for value in opponent_hand]), reverse=True)

    values_unique_player = list(set(values_player))
    values_unique_opponent = list(set(values_opponent))

    for value1, value2 in zip(values_unique_player, values_unique_opponent):
        if value1 > value2 and values_player.count(value1) == 2 and values_opponent.count(value2) == 2:
            return 'You win'
        elif value1 < value2 and values_player.count(value1) == 2 and values_opponent.count(value2) == 2:
            return 'You lost!'
    else:
        return checking_high_card(player_hand, opponent_hand)

    
def kicker(player_hand, opponent_hand):
    points = how_many_points(player_hand)

    if points == 9:
        return checking_high_card(player_hand, opponent_hand)
    elif points == 8:
        return checking_quads_trees_or_pairs(player_hand, opponent_hand, 4)
    elif points == 7:
        return checking_full_house(player_hand, opponent_hand)
    elif points == 6:
        return checking_high_card(player_hand, opponent_hand)
    elif points == 5:
        return checking_high_card(player_hand, opponent_hand)
    elif points == 4:
        return checking_quads_trees_or_pairs(player_hand, opponent_hand, 3)
    elif points == 3:
        return checking_two_pair(player_hand, opponent_hand)
    elif points == 2:
        return checking_quads_trees_or_pairs(player_hand, opponent_hand, 2)
    elif points == 1:
        return checking_high_card(player_hand, opponent_hand)        

def create_deck():
    colors = ['♣','♦','♥','♠']
    values = list(range(2,11)) + ['king', 'queen', 'jack', 'ace']
    deck = [(color, value) for color in colors for value in values]
    random.shuffle(deck)
    return deck

def draw_cards(deck, count):
    hand = deck[:count]
    del deck[:count]
    return hand

def switch_cards(deck, old_cards, indexes):
    for i in indexes:
        if deck:
            old_cards[i] = deck.pop(0)
    return old_cards
    
def game():
    deck = create_deck()

    # Player draws card from deck
    player_hand = draw_cards(deck, 5)
    print('Here are your cards: ')
    for index, (color, value) in enumerate(player_hand, 1):
        print(f'{index}: {color} {value}')
    
    # Asking the player how many cards does he want to change
    changing_cards = int(input('How many cards would you like to change (0-4): '))
    list_of_indexes = []
    if 4 >= changing_cards >= 0:
       
        for _ in range(changing_cards):
            index = int(input('Choose the number of a card you want to change: '))
            list_of_indexes.append(index-1)

    elif changing_cards == 0:
        print('Ok, so no cards will be changed')

    else:
        print('The number you provided is incorrect')

    # Changing cards for player 
    player_hand = switch_cards(deck, player_hand, list_of_indexes)
    print('Here are your new cards: ')
    for index, (color, value) in enumerate(player_hand, 1):
        print(f'{index}: {color} {value}')

    # Giving the opponent the cards
    opponent_hand = draw_cards(deck, 5)

    # Checking points for each player
    player_points = how_many_points(player_hand)
    opponent_points = how_many_points(opponent_hand)

    print(f'Your points: {player_points}')
    print(f'Opponent points: {opponent_points}')

    print('Here are your opponent cards: ')
    for index, (color, value) in enumerate(opponent_hand, 1):
        print(f'{index}: {color} {value}')
    
    if player_points > opponent_points:
        print('You won!')
    elif opponent_points > player_points:
        print('You lost!')
    else:
        print(kicker(player_hand, opponent_hand))

if __name__ == '__main__':
    game()