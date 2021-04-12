from random import randint
#check for ladders
def ladders(x):
    if x==1:
    	return 38
    elif x==4:
    	return 14
    elif x==8:
    	return 30
    elif x==21:
    	return 42
    elif x==28:
    	return 76
    elif x==50:
    	return 67
    elif x==71:
    	return 92
    elif x==88:
    	return 99
    else:
    	return x
#check for snakes
def snakes(x): 
    if x==32:
    	return 10
    elif x==36:
    	return 6
    elif x==48:
    	return 26
    elif x==62:
    	return 18
    elif x==88:
    	return 24
    elif x==95:
    	return 56
    elif x==97:
    	return 78
    else:
    	return x
    
def turn(player,score): 
    print()
    print("Its",player,"'s turn.")
    roll=input("Press enter to roll the dice")
    print()
    if roll=="":
        a=randint(1,6)#player dice roll
        print(player,"rolled the dice")
        print(player,"got",a)
        score+=a
        if score<=100:
            ladd=ladders(score) #checking for ladders for player
            if ladd!=score:
                print("There's a ladder!",player,"climbed up.")
                score=ladd
            snake=snakes(score)
            if snake!=score: #checking for snakes for player
                print(player,"got bitten by a snake!",player,"fall down!")
                score=snake
            print(player,"is now on",score)    
        else: #checks if player score is not grater than 100
            score-=a
            print(player,"is blocked.",player,"can't move")
            print(player,"is still on",score)
        if score==100:
            print()
            print(player,"Wins!")
        return score

print()
print("-------------------------SNAKES N LADDERS-------------------------")#game starts
print()
while True:
    play=input("Press Enter to Play and Exit to quit the game: ")
    if play=="":
        print("Choose your mode (Single player/Multiplayer)")#mode selection
        mode=input("Enter \"S\" for sigle player and \"M\" for multiplayer: ")
        if mode=="S" or mode== "s":
            player2="Computer"
            num_players=2
        else:
            num_players=int(input("Enter number of players: "))    
        player1=input("Enter player 1 name: ")
        if (mode=="M" or mode=="m") and 5>num_players>1:
            player2=input("Enter player 2 name: ")
        if 5>num_players>2:
            player3=input("Enter player 3 name: ")
        if 5>num_players>3:
            player4=input("Enter player 4 name: ") 
            print()
        print("Good Luck!")
        print()    
        while True:
            play2=input("Press Enter to start.")
            if play2=="":
                player1_score=player2_score=player3_score=player4_score=0
                while True:
                    if 5>num_players>1:
                        player1_score=turn(player1,player1_score)
                        if player1_score==100:
                            break
                        player2_score=turn(player2,player2_score)
                        if player2_score==100:
                            break
                    if 5>num_players>2:
                        player3_score=turn(player3,player3_score)
                        if player3_score==100:
                            break    
                    if 5>num_players>3:
                        player4_score=turn(player4,player4_score)
                        if player4_score==100:
                            break
                    print("________________________________________________________________")
                    
            break                                                
    elif play=="exit" or play=="Exit":
        break
        quit

       
