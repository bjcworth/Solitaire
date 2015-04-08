from random import randint

# 52 deck of cards
# board of 10 spots
# discard pile
# rank: ace=low k=high
# when placing card, every space to left is empty or lower rank
# every space to right is empty or higher rank
# loss = 6th discard
# win = at least one card on every spot on board


lossCount=0;
winCount=0;
for z in range(0,10000):
	deck = list();
	discard = list();
	for i in range(1,5):
		for x in range(1,14):
			deck.append(x);


	for z in range(0,51):
		w = randint(z,51)
		tempCard = deck[z];
		deck[z] = deck[w];
		deck[w] = tempCard;
		
	#print deck;
	#print len(deck);

	board = [None]*10;

	for i in range(0,51):
		#print board;
		card = deck.pop();


		if (None in board) and (len(discard)<6):
			if len(board)>=card:
				board[card-1] = card;
			else: 
				discard.append(card);


	if len(discard)==6:
		lossCount +=1;
		#print ("You lose! :(");

	if ((None in board) == False):
		winCount +=1;
		#print ("You win! :)")

	#print board
	#print discard
print winCount;
print "wins: " + str((100*float(winCount)/float(10000))) +"%";
print "end!"
