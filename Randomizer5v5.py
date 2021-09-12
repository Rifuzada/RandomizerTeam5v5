#Btw sorry for bad english im Brazilian 🇧🇷
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
print("O primeiro time é {}".format(time1))  #The first team is {}
print("O Segundo time é {}".format(time2))   #The second team is {}
#Chose the Roles
#Which role each player will play
lane1 = str(input('Que lane o {} jogará? '.format(p1)))
lane2 = str(input('Que lane o {} jogará? '.format(p2)))
lane3 = str(input('Que lane o {} jogará? '.format(p3)))
lane4 = str(input('Que lane o {} jogará? '.format(p4)))
lane5 = str(input('Que lane o {} jogará? '.format(p5)))
lane6 = str(input('Que lane o {} jogará? '.format(p6)))
lane7 = str(input('Que lane o {} jogará? '.format(p7)))
lane8 = str(input('Que lane o {} jogará? '.format(p8)))
lane9 = str(input('Que lane o {} jogará? '.format(p9)))
lane10 = str(input('Que lane o {} jogará? '.format(p10)))
#Print the lanes of the players.
print("As lanes ficaram separadas como, \n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}\n{} na lane {}".format(p1, lane1, p2 , lane2, p3 , lane3, p4, lane4, p5,lane5,p6,lane6,p7,lane7,p8, lane8,p9,lane9,p10,lane10))
#👊🏿
