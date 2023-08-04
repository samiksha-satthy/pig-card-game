#Samiksha Satthy and Evana Mahmud
#ICS 208
#January 13, 2022
#Description:
#               Input: asking the users for their goal in the beginning of the game 
#               Processing: using that input to determine if the players got all 4 cards
#               Output: displaying which user has won the game 


#FINAL COPY ****


#comments for the code in general:
#the continuation for loops are used to keep each player's cards private from one another 






#Make the main function 
def main(player1score, player2score):

        #Make the variables and constants 
        player1cards = []
        player2cards = []
        transition_cards = []
        startpile = []
        shuffleddeck = []
        inputplayer1 = ''
        inputplayer2 = ''
        counter1 = 0
        counter2 = 0

        #Ask if the players would like to hear the instructions of our modified game
        print("Hello and Welcome to our version of the Card Game: PIG")
        rules_input = input("If you would like to view the rules, please type 'yes' or if you would like to continue, please type 'no': ")
        print()

        #Print an error message if the answer for the above question was neither "yes" or "no"
        while rules_input != 'yes' and rules_input != 'no':
            print('ERROR! yes or no was not typed')
            rules_input = input('Please type again: ')
            print()
   
    

        #if "yes" was typed in, display the instructions of the game
        if rules_input == 'yes':
                print('Here are the rules: ')
                print("The objective of Pig is to get 4 cards of the same number/denomination.")
                print("For example: 5H, 5Q, 5C, 5S")
                print("When an individual does get all 4 of the same cards, the other player gets a letter and the first one to spell out PIG loses")
                print("Players can switch which number/denomination of card they would like to go for between rounds. ")
                print()

        #if not yes just continue
        else:
                print("Alright let's continue!")
                print()

        #Make the parameters 
        making(player1cards, player2cards, shuffleddeck, startpile, player1score, player2score, inputplayer1, inputplayer2)
        

#Make the new function called making with the arguments        
def making(player1cards1, player2cards2, shuffleddeckk, starttpile, player1score1, player2score2, inputtplayer1, inputtplayer2):

       import random 

        #Create the deck of cards
       deck_cards1 = ["AD", "AS", "AC", "AH",
        "2D", "2S", "2C", "2H",
        "3D", "3S", "3C", "3H",
        "4D", "4S", "4C", "4H",
        "5D", "5S", "5C", "5H",
        "6D", "6S", "6C", "6H",
        "7D", "7S", "7C", "7H",
        "8D", "8S", "8C", "8H",
        "9D", "9S", "9C", "9H",
        "10D", "10S", "10C", "10H",
        "JD", "JS", "JC", "JH",
        "QD", "QS", "QC", "QH",
        "KD", "KS", "KC", "KH"]

       
       #shuffle the deck of cards
       shuffleddeckk = random.sample(deck_cards1, len(deck_cards1))


        #Give each player 4 cards
       for card in range(0, 4):
                    player1cards1.append(shuffleddeckk.pop(0))
                    player2cards2.append(shuffleddeckk.pop(0))

        

        #Display/print player 1's cards
       print("Player 1's Cards: ")
       for i in range(0, len(player1cards1)):
                   print(player1cards1[i])





                #Ask player 1 which card they would like to go for
       inputtplayer1 = input('Player 1, What card value would you like to go for (eg. 7, A, J)? ')
       print()

        #If the card written with an "s" is not in the deck, make player1 choose again
       while inputtplayer1 + 'S' not in deck_cards1:

                    inputtplayer1 = input('Player 1, the value you have chosen is not in the deck. Please choose again: ')
                    print()


       press = input("Enter X to see Player 2's Cards: ")

       while press != 'X':
               press = input("X was not entered, please input again: ")


        #To hide each other's cards 
       for x in range(0, 51):
               print()



                #Display player 2's cards
       print("Player 2's Cards: ")
       for i in range(0, len(player2cards2)):
                    print(player2cards2[i])

        #Ask player 2 which card they would like to go for          
       inputtplayer2 = input('Player 2, What card value would you like to go for (eg. 7, A, J)? ')
       print()

     #If the card written with an "C" is not in the deck, make player2 choose again
       while inputtplayer2 + 'C' not in deck_cards1:

                    inputtplayer2 = input('Player 2, the value you have chosen is not in the deck. PLease choose again: ')
                    print()

        #if player 1 & 2 choose the same card to aim for, make them re-enter a card to go for
       while inputtplayer1 == inputtplayer2:
                    print('Sorry, you guys cannot go for the same card. ')
                    inputtplayer1 = input('Player 1, please enter again: ')
                    inputtplayer2 = input('Player 2, please enter again: ')
                    print()



       press = input("Enter X to start the game: ")

       while press != 'X':
               press = input("X was not entered, please input again: ")


        #To hide each other's cards 
       for x in range(0, 51):
               print()

        #Startpile will take a card from the shuffled deck
       for card in shuffleddeckk:
                    starttpile.append(card)


       

        
        #Make the new parameters
       starting_game(deck_cards1, shuffleddeckk, starttpile, inputtplayer1, inputtplayer2, player1cards1, player2cards2, player1score1, player2score2)


#Make a function for the starting game
def starting_game(deck_cards, shuffled_pile, start_pile, input_player1, input_player2, player_1cards, player_2cards, player1_score, player2_score):


        #constant initialization
        LOSER = 3
        
        #Make a transition card pile
        transition_cards = []

        #making a track pile to track cards once they left start and transition
        track_pile = []


        print('GAME STARTS NOW!')
        
        #When player 1 or 2 score is not equal to 3/LOSER...
        while player1_score != LOSER and player2_score != LOSER:

        
            #Cards in the start pile
                for card1 in start_pile:

                

                         print()
                     
                    #If the card is the one player 1 chose
        
 
                        #Print the card
                         print('Card: ', card1)
                         print()

                        #Display player 1's cards, give the new card to them and ask which card to replace it with
                         print('Current Cards', player_1cards)
                         ask = input('Player 1, Would you like to remove a card from your hands?("yes" or "no") ')
                         print()

                         while ask != 'yes' and ask != 'no':
                            print('ERROR! yes or no was not typed')
                            ask = input('Please type again: ')
                            print()

                         if ask == 'yes':
                                 removal = input('Player 1, which card would you like to remove from your hands? ')

                        #If the card chosen to replace is not in their hand or is misspelled, ask to type again.
                                 while removal not in player_1cards:
                                             removal = input('The card you inserted is either not in your pile or is misspelled. Please enter again: ')
                                             print()

                                              
                                 for item1 in player_1cards:
                                    
                                    #if the ask is equal to item1...
                                     if removal == item1:

                                        #player 1's cards will  take the card1, remove the ask;
                                         # the discard pile will take the ask and
                                         # transition pile will remove the card1
                                        
                                         player_1cards.append(card1)
                                                                         
                                         player_1cards.remove(removal)
                                         transition_cards.append(item1)
                

                                         

                                     else:

                                         #continue until the card they entered is found in their hands 
                                          continue


                                        
                                  #this prints out player 1's new cards after 
                                 print('New Cards: ', player_1cards)
                                 print()

                                         #Reset counter to 0
                                 counter1 = 0
                            
                                          #If player 1 has all 4 of the same cards, increase player 2 score by 1 and display player 1 winning this round
                                 for r in range(0, len(player_1cards)):

                                         #goes through each card in player 1's hands 
                                        if player_1cards[r].startswith(input_player1):
                                                #adds 1 to counter each time
                                                
                                                counter1 += 1
                                                
                                                #only goes to score if counter and all of player's cards starts with their input(what there goal was)
                                                if counter1 == 4:
                                                     print('Congratulations Player 1, you got all 4 of the same cards this round!')
                                                     print()
                                                     player2_score += 1

                                                    #If player 2's score is equal to 1, call/go to the score p player 2 function
                                                     if player2_score == 1:
                                                        counter1 = 0
                                                        score_p_player2(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile)

                                                    #If player 2's score is equal to 2, call/go to the score i player 2 function
                                                     elif player2_score == 2:
                                                        counter1 = 0
                                                        score_i_player2(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile)
                                                        
                                                     #If player 2's score is equal to LOSER / 3, call/go to the score g player 2 function
                                                     elif player2_score == LOSER:
                                                        score_g_player2(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile, deck_cards)
                                                        break

                                                        return
                                                else:

                                                     #Continue on with the loop
                                                     continue

                                 
                                
                                        else:

                                                                       

                                                #ask player 1 if they would like to change what card they are aiming for
                                                ask3 = input('Would you like to change what card value you are going for? (yes or no) ')
                                                print()

                                                while ask3 != 'yes' and ask3 != 'no':
                                                        ask3 = input('You did not input "yes" or "no". please input again: ')
                                                        print()
                                                        
        

                                                #if they say yes, as which card they want instead
                                                if ask3 == 'yes':
                                                    input_player1 = input('What new card value would you like to go for? ')
                                                    print()


                                                    #If player 1 and player want the same card, ask to input again
                                                    while input_player1 == input_player2:
                                                        input_player1 = input('You cannot go for the same card value as Player 2. Please choose again: ')
                                                        print()

                                                    #If the card inputed is either spelled incorrectly or is not in the deck, ask to enter again.
                                                    while input_player1 + 'H' not in deck_cards:
                                                        input_player1 = input('Sorry, you either misspelled the new card value you want to go for or it does not exist. Enter again: ')
                                                        print()

                                                    


                                                    print('New Card: ', input_player1)
                                                    #reset counter1 to 0
                                                    counter1 = 0


                                                    continuation = input("Input a '0' for Player 2's Turn: ")

                                                    while continuation != '0':
                                                           continuation = input("0 was not entered. Please input again: ")
                                                                        

                                                                #To hide each other's cards 
                                                    for x in range(0, 51):
                                                                print()


                                                    input_player2 = player_2transfer(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile, track_pile, deck_cards, LOSER)

                                                    
                                                                
                                                    break
                                            
                                                elif ask3 == 'no':
                                                                counter1 = 0

                                                                continuation = input("Input a '0' for Player 2's Turn: ")

                                                                while continuation != '0':
                                                                        continuation = input("0 was not entered. Please input again: ")
                                                                        

                                                                #To hide each other's cards 
                                                                for x in range(0, 51):
                                                                        print()


                                                                input_player2 = player_2transfer(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile, track_pile, deck_cards, LOSER)
                                                                
                                                                
                                                                break

                                                                
                                        

                                        

                                
                                 
                                            
                         else:


                        
                                #if start pile is on its last card, cards from the track pile will transfer to the start pile so the game continues 
                             if card1 == start_pile[-1]:
                                continuation = input("Input a '0' for Player 2's Turn: ")

                                while continuation != '0':
                                        continuation = input("0 was not entered. Please input again: ")

                                        #To hide each other's cards 
                                for x in range(0, 51):
                                       print()

                
                                #adding card to transition cards
                                transition_cards.append(card1)

                                #calling player 2's function
                                input_player2 = player_2transfer(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile, track_pile, deck_cards, LOSER)
                                


                                #reshuffling deck
                                start_pile = transfer_cards(track_pile, start_pile, player_1cards, player_2cards)


                                #if start pile isn't on last card, game will continue as normal 
                             else:


                               continuation = input("Input a '0' for Player 2's Turn: ")

                               while continuation != '0':
                                        continuation = input("0 was not entered. Please input again: ")

                                        #To hide each other's cards 
                               for x in range(0, 51):
                                       print()

                                #to call out player 2's turn which is in a function       
                                
                                
                        
                               transition_cards.append(card1)

                               #calling player 2's function
                               input_player2 = player_2transfer(player1_score, player2_score, input_player1, input_player2, start_pile, transition_cards, player_1cards, player_2cards, shuffled_pile, track_pile, deck_cards, LOSER)
                               


                         #the transition cards will take the card1


                if player1_score == LOSER or player2_score == LOSER:
                        break
                        
                
#Make a score system for player 1 starting with P
def score_p_player1(playerscore1, playerscore2, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck):

     
            #Print the following and clear everything so the next round starts fresh
             print('Player 1 has a P')
             print()
             playerinput1 = ''
             playerinput2 = ''
             cardsplayer1.clear()
             cardsplayer2.clear()
             startpilee.clear()
             transitioncardss.clear()
             shuffledddeck.clear()
             print('NEXT ROUND!!!!!!!!!!!!!')
             print()

             #Bring it back to the making function
             making(cardsplayer1, cardsplayer2, shuffledddeck, startpilee, playerscore1, playerscore2, playerinput1, playerinput2)


#Make a score system for player 1 once they get an i
def score_i_player1(playerscore1, playerscore2, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck):

            #Print the following and clear everything so the next round starts fresh
             print('Player 1 has a P and an I')
             print()
             playerinput1 = ''
             playerinput2 = ''
             cardsplayer1.clear()
             cardsplayer2.clear()
             startpilee.clear()
             transitioncardss.clear()
             shuffledddeck.clear()
             print('NEXT ROUND!!!!!!!!!!!!!')
             print()

            #Bring it back to the making function to start again
             making(cardsplayer1, cardsplayer2, shuffledddeck, startpilee, playerscore1, playerscore2, playerinput1, playerinput2)

#Making a score function for player 2 score once they have reached "g"
def score_g_player1(player1score, player2score, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck, deckkcards):
        print('Player 1 has lost because they spelled out PIG. Congratulations Player 2!')
        print()
                                                                         
        end(player1score, player2score, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck, deckkcards)

#Make a score system for player 2 starting with P
def score_p_player2(playerscore1, playerscore2, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck):

             #Print the following and clear everything so the next round starts fresh
             print('Player 2 has a P')
             print()
             playerinput1 = ''
             playerinput2 = ''
             cardsplayer1.clear()
             cardsplayer2.clear()
             startpilee.clear()
             transitioncardss.clear()
             shuffledddeck.clear()
             print('NEXT ROUND!!!!!!!!!!!!!')
             print()

             #Bring it back to the making function to start again
             making(cardsplayer1, cardsplayer2, shuffledddeck, startpilee, playerscore1, playerscore2, playerinput1, playerinput2)

#Make a score system for player 2 once they get an i
def score_i_player2(playerscore1, playerscore2, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck):

     #Print the following and clear everything so the next round starts fresh
     print('Player 2 has a P and an I')
     print()
     playerinput1 = ''
     playerinput2 = ''
     cardsplayer1.clear()
     cardsplayer2.clear()
     startpilee.clear()
     transitioncardss.clear()
     shuffledddeck.clear()
     print('NEXT ROUND!!!!!!!!!!!!!')
     print()

    #Bring it back to the making function to start again
     making(cardsplayer1, cardsplayer2, shuffledddeck, startpilee, playerscore1, playerscore2, playerinput1, playerinput2)


#Making a score function for player 1 score once they have reached "g"
def score_g_player2(player1score, player2score, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck, deckkcards):
        print('Player 2 has lost because they spelled out PIG. Congratulations Player 1!')
        print()
                                                                          
        end(player1score, player2score, playerinput1, playerinput2, startpilee, transitioncardss, cardsplayer1, cardsplayer2, shuffledddeck, deckkcards)
  

#Make a function for the end of the game
def end(player1scoree, player2scoree, playerinput11, playerinput22, starttpile, transitionpile, cardssplayer1, cardssplayer2, shuffledcardss, deckcardss):
        end_input = input('What a game! If you would like to play a new one, please type yes or if you would like to exit please press the X in the top right: ')

        while end_input != 'yes':
            end_input("yes was not typed or was misspelled. Please enter again: ")

               
        player1scoree = 0
        player2scoree = 0
        playerinput11 = ''
        playerinput22 = ''
        cardssplayer1.clear()
        cardssplayer2.clear()
        starttpile.clear()
        transitionpile.clear()
        shuffledcardss.clear()
        print()
        making(cardssplayer1, cardssplayer2, shuffledcardss, starttpile, player1scoree, player2scoree, playerinput11, playerinput22)

        





#player 2's version of how the game would go
def player_2transfer(player1score, player2score, inputplayer1, inputplayer2, startpile, transitioncards, player1cards, player2cards, shuffledpile, trackpile, deckcards, LOSERR):

                                 #for each card in the transition card
                                 for item2 in transitioncards:
           
        

                                         #display "card:" and the item2
                                         print('Card: ', item2)

                                         #print player 2's cards
                                         # Ask player 2 if they would like to remove a card
                                         print('Curent Cards: ', player2cards)
                                         print()
                                         askk2 = input('Player 2, Would you like to remove a card from your hands?("yes" or "no")? ')

                                        #input validation
                                         while askk2 != 'yes' and askk2 != 'no':
                                            print('ERROR! yes or no was not typed')
                                            askk2 = input('Please type again: ')
                                            print()


                                         #user input is yes 
                                         if askk2 == 'yes':


                                                 #asking which card they would like to remove 
                                                 removall2 = input('Player 2, What card would you like to remove from your hands (eg. 3H, 2S, etc)? ') 

                                                #if ask2 is not in player 2's hand, ask them to reenter due to either mispelling or its not in the hand.
                                                 while removall2 not in player2cards:
                                                     removall2 = input('The card you inserted is either not in your pile or is misspelled. Please enter again: ')
                                                     print()
                                    

                                                 #goes through each of player 2's cards to find the crad they entered to remove
                                                 for item3 in player2cards:

                                                    #If ask2 is equal to item 3...                          
                                                     if removall2 == item3:

                                                        #player 2's cards will  take the item 2, remove the ask 2;
                                                        # the track pile will take the ask 2 and
                                                        # transition pile will remove the item 2
                                                        
                                                         player2cards.append(item2)

                                                         player2cards.remove(removall2)
                                                         trackpile.append(removall2)
                                                         transitioncards.remove(item2)
                 
                                                     else:

                                                         #continuing for loop
                                                         #if ask 2 isn't equal to any of the
                                                         #player 2's cards
                                                         
                                                         continue

                                                    # Display the new cards and player 2's cards
                                                 print('New Cards: ', player2cards)
                                                 print()
                                            
                                                 #Reset counter to 0
                                                 counter2 = 0

                                                 #If player 2 has all 4 of the same cards, increase player 1 score by 1 and display player 2 winning this round
                                                 for r in range(0, len(player2cards)):
                                                         if player2cards[r].startswith(inputplayer2):
                                                             counter2 += 1 
                                                             if counter2 == 4:
                                                                 print('Congratulations Player 2, you got all 4 of the same cards this round!')
                                                                 print()
                                                                 player1score += 1

                                                                 #If player 1's score is equal to 1, call/go to the score p player 1 function
                                                                 if player1score == 1:
                                                                     counter2 = 0
                                                                     score_p_player1(player1score, player2score, inputplayer1, inputplayer2, startpile, transitioncards, player1cards, player2cards, shuffledpile)
                                                                     
                                                                  #If player 1's score is equal to 2, call/go to the score i player 1 function
                                                                 elif player1score == 2:
                                                                   counter2 = 0    
                                                                   score_i_player1(player1score, player2score, inputplayer1, inputplayer2, startpile, transitioncards, player1cards, player2cards, shuffledpile)

                                                                #If player 1's score is equal to LOSER / 3, call/go to the score g player 1 function
                                                                 elif player1score == LOSERR:
                                                                    score_g_player1(player1score, player2score, inputplayer1, inputplayer2, startpile, transitioncards, player1cards, player2cards, shuffledpile, deckcards)

                                                                    break
                                                                    
                                                                 
                                                                    
                                                             else:

                                                                 #Continuing the loop
                                                                 continue

                                                        #Ask player 2 if they would like to change what card they are going for
                                                         else:
                                                            ask3 = input('Would you like to change what card value you are going for? (yes or no) ')

                                                            #input validation
                                                            while ask3 != 'yes' and ask3 != 'no':
                                                                        ask3 = input('You did not input "yes" or "no". please input again: ')

                                                            #If they answer with yes...
                                                            if ask3 == 'yes':

                                                                 #their goal would change
                                                                inputplayer2 = input('What new card value would you like to go for? ')
                                                                print()



                                                                #If player 1 & 2 choose the same card, ask to choose again
                                                                while inputplayer1 == inputplayer2:
                                                                    inputplayer2 = input('You cannot go for the same card value as Player 1. Please choose again: ')
                                                                    print()

                                                                #If the card is not in the deck, print that they either misspelled or the card does not exist and let them try again
                                                                while inputplayer2 +'H' not in deckcards:
                                                                    inputplayer2 = input('Sorry, you either misspelled the new card value you want to go for or it does not exist. Enter again: ')
                                                                    print()

                                                                print('New Goal: ', inputplayer2)
                                                                print()

                                                                #after, it asks for an input to continue and then breaks 
                                                                counter2 = 0

                                                                continuation = input("Input a '0' for Player 1's Turn: ")

                                                                while continuation != '0':
                                                                        continuation = input("0 was not entered. Please input again: ")

                                                                 #To hide each other's cards 
                                                                for x in range(0, 51):
                                                                       print()

                                                                return inputplayer2     
                                                                break


                                                                #if they say no, it asks for an input to continue and then breaks out of the for loop
                                                            elif ask3 == 'no':
                                                                counter2 = 0
                                                                
                                                                continuation = input("Input a '0' for Player 1's Turn: ")

                                                                while continuation != '0':
                                                                        continuation = input("0 was not entered. Please input again: ")

                                                                #To hide each other's cards 
                                                                for x in range(0, 51):
                                                                       print()
                                                                
                                                                return inputplayer2       
                                                                break

                                                

                                                        
                                         else:
                                                #if player 2 dosn't want the card displayed, it gets put in the track pile and removed from transition pile
                                                trackpile.append(item2)
                                                transitioncards.remove(item2)
                                                
                                                continuation = input("Input a '0' for Player 1's Turn: ")

                                                while continuation != '0':
                                                        continuation = input("0 was not entered. Please input again: ")

                                        #To hide each other's cards 
                                                for x in range(0, 51):
                                                       print()

                                        #to call out player 2's turn which is in a function       
                                                return inputplayer2
                                                break


                                 if player1score == LOSERR:
                                                return

#to transfer cards from the track pile to the start pile once cards from the start pile run out 
def transfer_cards(trackpile, startpile, player1cards, player2cards):
        import random
        trackpile_shuffle = []

        #clearing the original start pile 
        startpile.clear()

        #adding cards from the track pile to start pile 
        trackpile_shuffle = random.sample(trackpile, len(trackpile))
        for card in trackpile_shuffle:
                startpile.append(card)

        return startpile

        

#Call the main function
main(0, 0)




