#Rock-Paper-
import random
print "Try to beat the computer!"
rock = 1
paper = 2
scissors = 3

answer = raw_input("Pick Rock[1] , Paper[2] , Scissors[3]")

computerpick = random.randint(1,3)

if computerpick > answer :
	print "Computer Wins"
	print computerpick
if computerpick < answer:
	print computerpick
	print "You Win"
if computerpick == answer:
	print "Tie"