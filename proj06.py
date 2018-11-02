#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:50:03 2018

@author: austinmay
 Texas Holdem
This is a simplified version of the popular poker mode
"""

import cards

def less_than(c1,c2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False
    
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index
        
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H

def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    suits=[[],[],[],[]]#creates 4 lists for each suit
    for card in H:
        suits[card.suit()-1].append(card)#appends card to list based on suit
    for suit in suits:
        if len(suit)>=5:#if any list is greater than 5 it is flush and it organizes and returns first 5
            hand=cannonical(suit)
            return hand[0:5]
    return False
def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    low=H[0].rank()#finds low card
    lowcard=H[0]
    strt=[]
    for card in H:
        if card.rank()<low:
            low=card.rank()
            lowcard=card
    strt.append(lowcard)
    for card in H:
        if card.rank()==low+1:#for card in the hand if it has a value 1,2,3,or 4 higher it appends it to the straight list
            if card.rank() in strt:
                continue
            else:
                strt.append(card)#if straight list has a card with the same val it doesnt append it
        if card.rank()==low+2:
            if card.rank() in strt:
                continue
            else:
                strt.append(card)
        if card.rank()==low+3:
            if card.rank() in strt:
                continue
            else:
                strt.append(card)
        if card.rank()==low+4:
            if card.rank() in strt:
                continue
            else:
                strt.append(card)
    if len(strt)==5:
        return strt
    return False
            
    
        
def straight_flush_7(H):
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    suits=[[],[],[],[]]
    low=H[0].rank()
    lowcard=H[0]
    strt=[]
    for card in H:
        if card.rank()<low:
            low=card.rank()
            lowcard=card
    strt.append(lowcard)
    for card in H:#finds the straight first
        if card.rank()==low+1:
            strt.append(card)
        if card.rank()==low+2:
            strt.append(card)
        if card.rank()==low+3:
            strt.append(card)
        if card.rank()==low+4:
            strt.append(card)
    if len(strt)==5:
        for card in strt:
            suits[card.suit()-1].append(card)#then the function determines if the straight contains cards of the same suit
        for suit in suits:
            if len(suit)==5:
                return suit#if it does it returns the straight
    return False

def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    ranks=[[],[],[],[],[],[],[],[],[],[],[],[],[]]#creates list for every rank
    for card in H:
        ranks[card.rank()-1].append(card)#appends cards by rank
    for r in ranks:
        if len(r)==4:
            hand=cannonical(r)#sorts
            return hand#if four cards of same rank in list it returns a 4 of a kind
    return False

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    ranks=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for card in H:
        ranks[card.rank()-1].append(card)
    for r in ranks:
        if len(r)==3:
            return r#if 3 cards of the same rank then 3 of a kind is found
    return False
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    ranks=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    double=[]
    for card in H:
        ranks[card.rank()-1].append(card)#splits cards by rank
    for r in ranks:
        if len(r)==2:#if pair found it appends them to a list
             double.append(r[0])
             double.append(r[1])
    if len(double)>=4:#if 2 pairs or more found it returns them sorted
        hand=cannonical(double)
        return hand
    return False

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    ranks=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for card in H:
        ranks[card.rank()-1].append(card)
    for r in ranks:
        if len(r)==2:
            return r#returns a pair that is found
    return False

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    ranks=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    fully=[]
    for c in H:
        ranks[c.rank()-1].append(c)
    for r in ranks:
        if len(r)==2:
            fully.append(r[0])
            fully.append(r[1])#if pair found it appends the pair to a list
        elif len(r)==3:
            fully.append(r[0])#if 3 of a kind found it also appends them
            fully.append(r[1])
            fully.append(r[2])
        else:
            continue
    hand=cannonical(fully)
    if len(hand)>=5:#takes all matches found
        if len(hand)%2==0:#doesnt except if no 3 of a kind are found
            return False
        else:
            return hand[0:5]#returns the first 5 in hand if full house achieved
    return False

def main():
    D = cards.Deck()
    D.shuffle()
       
    while True:
        community_list=[]
        hand_1_list=[]
        hand_2_list=[]
        for i in range( 5 ):
            community_list.append( D.deal() )#deals comunity 5 cards
        for i in range( 2 ):
            hand_1_list.append( D.deal() )#deals plyr 1 2 cards
        for i in range( 2 ):
            hand_2_list.append( D.deal() )#deals plyr 2 2cards
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        H1=hand_1_list+community_list#creats plyr 1 hand
        H2=hand_2_list+community_list#creates plyr 2 hand
        strflush1=straight_flush_7(H1)
        strflush2=straight_flush_7(H2)
        fourkind1=four_7(H1)
        fourkind2=four_7(H2)
        full1=full_house_7(H1)
        full2=full_house_7(H2)
        flush1=flush_7(H1)                    #initiates all possible hands in the functions above
        flush2=flush_7(H2)
        threekind1=three_7(H1)
        threekind2=three_7(H2)
        twopair1=two_pair_7(H1)
        twopair2=two_pair_7(H2)
        pair1=one_pair_7(H1)
        pair2=one_pair_7(H2)
        if strflush1 != False:
            if strflush2 != False:#if false isnt returned that means it belongs in that class
                print('TIE with a straight flush:',strflush1)#tie is assumed if both are in that class
            else:
                print('Player 1 wins with a straight flush:',strflush1)#player 1 wins if it is the only one in that class
                #uses boolean to determine the outcome of player1 and 2s hand
        elif fourkind1 != False:
            if fourkind2 != False:
                print('TIE with a four of a kind:',fourkind1)
            elif strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)#player 2 wins if its in a class that is higher than player 1
            else:
                 print('Player 1 wins with four of a kind:',fourkind1)
        elif full1 != False:
        
            if strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)
            elif fourkind2 !=False:
                print('Player 2 wins with a four of a kind:',fourkind2)
            elif full2 != False:
                print('TIE with a full house:',full1)
            else:
                 print('Player 1 wins with a full house:',full1)
        elif flush1 != False:
            if flush2 != False:
                print('TIE with a flush:',flush1)
            elif strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)
            elif fourkind2 !=False:
                print('Player 2 wins with a four of a kind:',fourkind2)
            elif full2 != False:
                print('Player 2 wins with a full house:',full2)
            else:
                print('Player 1 wins with a flush:',flush1)
        elif threekind1 != False:
            if fourkind2 != False:
                print('Player 2 wins with a four of a kind:',fourkind2)
            elif full2 !=False:
                print('Player 2 wins with a full house:',full2)
            elif threekind2 != False:
                print('TIE with a three of a kind:',threekind1)
            elif flush2 != False:
                print('Player 2 wins with a flush:',flush2)
            else:
                print('Player 1 wins with a three of a kind:',threekind1)
        elif twopair1 != False:
            if strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)
            elif fourkind2 !=False:
                print('Player 2 wins with a four of a kind:',fourkind2)
            elif full2 !=False:
                print('Player 2 wins with a full house:',full2)
            elif flush2 != False:
                print('Player 2 wins with a flush:',flush2)
            elif threekind2 != False:
                print('Player 2 wins with a three of a kind:',threekind2)
            elif twopair2 != False:
                print('TIE with two pairs:',twopair1)
            else:
                print('Player 1 wins with a two pair:',twopair1)
        elif pair1 != False:
            if strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)
            elif fourkind2 !=False:
                print('Player 2 wins with four of a kind:',fourkind2)
            elif full2 !=False:
                print('Player 2 wins with a full house:',full2)
            elif flush2 != False:
                print('Player 2 wins with a flush:',flush2)
            elif threekind2 != False:
                print('Player 2 wins with a three of a kind:',threekind2)
            elif twopair2 != False:
                print('Player 2 wins with two pair:',twopair1)
            elif pair2 != False:
                print('TIE with a pair:',pair1)
            else:
                print('Player 1 wins with a pair:',pair1)
        else:
            if strflush2 != False:
                print('Player 2 wins with a straight flush:',strflush2)
            elif fourkind2 !=False:
                print('Player 2 wins with four of a kind:',fourkind2)
            elif full2 !=False:
                print('Player 2 wins with a full house:',full2)
            elif flush2 != False:
                print('Player 2 wins with a flush:',flush2)
            elif threekind2 != False:
                print('Player 2 wins with three of a kind:',threekind2)
            elif twopair2 != False:
                print('Player 2 wins with two pair:',twopair1)
            elif pair2 != False:
                print('Player 2 wins with pair:',pair1)
            else:
                print('TIE with a high card:',H1)
        if len(D)<9:
            print('Deck has too few cards so game is done.')#cuts game if not enough cards remain
            break
        
        while True:
            quest=input('Do you wish to play another hand?(Y or N) ')#asks if the game should go on
            if quest.upper()=='N':#if y game continues no matter upper or lower
                break
            elif quest.upper()=='Y':
                break
            else:
                print()
                print('Enter A Valid Command!')
                quest=input('Do you wish to play another hand?(Y or N) ')#asks if the game should go on
                if quest.upper() == 'Y':
                    break
                elif quest.upper() == 'N':
                    break
                else:
                    print()
                    print('Enter A Valid Command!')
        if quest.upper() == 'Y':
            continue
        if quest.upper() == 'N':
            break
                

if __name__ == "__main__":
    main()