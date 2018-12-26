import random
 
tie= "is a tie"
p1 = "goes to you; the computer loses."
p2 = "goes to the computer; you lose."
 
myDict = {('rock', 'rock') : tie, ('rock', 'paper') : p2,
('rock', 'scissors') : p1, ('paper', 'rock') : p1, ('paper', 'paper') : tie, ('paper', 'scissors') : p2, ('scissors', 'rock') : p2, ('scissors', 'paper') : p1, ('scissors', 'scissors') : tie }
 
def throw(player1, player2):
     verdict = myDict[(player1, player2)]
     print "The game " + verdict
 
def lets_get_started():
  try:
     player1 = raw_input("Throw!  Enter 'rock', 'paper', or 'scissors': " )
     print "You chose: " + player1
     player2 = random.choice(['rock', 'paper', 'scissors'])
     print "The computer chose: " + player2
     throw(player1, player2)
  except KeyError:
     print "Hey!  I said enter 'rock', 'paper' or 'scissors'!  Try again."
     lets_get_started()
 
print "Ya wanna play Rock, Paper, Scissors?"
lets_get_started()
