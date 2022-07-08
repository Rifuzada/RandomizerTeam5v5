import random

#Chose the players
p1 = str(input("Player 1: "))
p2 = str(input("Player 2: "))
p3 = str(input("Player 3: "))
p4 = str(input("Player 4: "))
p5 = str(input("Player 5: "))
p6 = str(input("Player 6: "))
p7 = str(input("Player 7: "))
p8 = str(input("Player 8: "))
p9 = str(input("Player 9: "))
p10 = str(input("Player 10: "))

#The players you has chosen ill be randomized in two teams, Top = Top laner, Jg = Jungler, Mid = Mid Laner, Adc = Ad Carry, Sup = Support.
#The roles in a MOBA game.
#1-2 is the first and second team.
#Time = Team
times = [p1 ,p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8, p9, p10]   
random.shuffle(times)
time1, time2 = times[:5], times[5:]
#Print the two teams.
print(f"O primeiro time é {time1}")  #The first team is {}
print(f"O Segundo time é {time2}")   #The second team is {}
#👊🏿
