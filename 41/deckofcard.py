class Deck:
    def __init__(self):
        self.cards = ['♠︎ A', '♣︎ A', '♥︎ A', '♦︎ A']

    def __len__(self):
        return len(self.cards)

    def __add__(self, card):
        self.cards.append(card)

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return 'The deck is ' + str(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]
