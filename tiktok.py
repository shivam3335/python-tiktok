# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:07:29 2019

@author: SHIVAM
"""

#board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]
#if game still is going on
game_still_going=True
winner=None;
current_player="x"
#display board
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
    
def play_game():
 #display initial board   
    display_board()
    while game_still_going:
        
        handle_turn(current_player)
        check_if_game_over()
        #flip to other player
        flip_player()
        #game end
    if (winner == "x" or winner =="o"):
        print(winner + 'win..!')
    elif winner== None:
        print("Tie")
    hlt=input("press Y to continue or N to stop the game")
        
    
def handle_turn(player):
    print(player+"'s turn.")
    position=input("choose position from 1 to 9 : ")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("choose position from 1 to 9 : ")
        position=int(position) -1#index of the board
        if board[position]=="-":
            valid=True
        else:
            print("you can't choose that again.")
    board[position]=player
    
    display_board()
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
        
def check_for_winner():
    
    global winner
    #check row
    row_winner=check_rows()
    #check column
    column_winner=check_columns()
    #check diagonal
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
        
    elif column_winner:
        #winner
        winner=column_winner
    elif diagonal_winner:
        winner= diagonal_winner        #winner
    else:
        #no win
        winner=None
    
    return
def check_rows():
    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    if row_1 or row_2 or row_3:
        game_still_going= False
    #return winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1=board[0]==board[3]==board[6]!="-"
    column_2=board[1]==board[4]==board[7]!="-"
    column_3=board[2]==board[5]==board[8]!="-"
    if column_1 or column_2 or column_3:
        game_still_going= False
    #return winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    
    return

def check_diagonals():
    global game_still_going
    diagonal_1=board[0]==board[4]==board[8]!="-"
    diagonal_2=board[2]==board[4]==board[6]!="-"
    if diagonal_1 or diagonal_2:
        game_still_going= False
    #return winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    
    
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    
    return

def flip_player():
    global current_player
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"
    return


play_game()