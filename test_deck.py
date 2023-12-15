from deck import Deck, Card

# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).


def test_cards():
   card_1 = Card(rank=5, suite='Hearts')
   card_2 = Card(rank= 5, suite= 'Spades')
   assert card_1 == card_2 # checking if the cards with the same rank are equal


def test_deck():
    deck = Deck()

    other_card_index = Card(rank=6, suite='Clubs')
#putind the new card inot the deck
    Deck.insert(deck.cards, other_card_index)

#checking the correct possition
    assert deck.cards[5]== other_card_index

