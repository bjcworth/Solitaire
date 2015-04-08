from random import randint

# 52 deck of cards ranked 1-13
# shuffle the deck at game start
# board of 10 spots
# discard pile
# rank: ace=low k=high
# when placing card, every space to left is empty or lower rank
# every space to right is empty or higher rank
# loss = 6th discard
# win = at least one card on every spot on board


lossCount=0;
winCount=0;
# 10,000 play-thrus
for z in range(0,10000):
	# new deck
	deck = list();
	# new discard pile
	discard = list();
	# 4 of each card
	for i in range(1,5):
		for x in range(1,14):
			deck.append(x);

	# shuffling the deck
	for z in range(0,51):
		w = randint(z,51)
		tempCard = deck[z];
		deck[z] = deck[w];
		deck[w] = tempCard;
		
	#print deck;
	#print len(deck);

	# Initializing the board
	board = [None]*10;
	# Automating card draws from the deck
	for i in range(0,51):
		#print board;
		card = deck.pop();

		# Place card in it's corresponding spot if game isn't over yet
		if (None in board) and (len(discard)<6):
			if len(board)>=card:
				board[card-1] = card;
			else: 
				discard.append(card);

	# Loss conditions
	if len(discard)==6:
		lossCount +=1;
		#print ("You lose! :(");
	# Win conditions
	if ((None in board) == False):
		winCount +=1;
		#print ("You win! :)")

	#print board
	#print discard
print winCount;
print "wins: " + str((100*float(winCount)/float(10000))) +"%";
print "end!"
