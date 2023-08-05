import random
import time
print("")
print("------------------------------------- Welcome ---------------------------------------------")
print("----------------------------- Numbers for Answers Only ------------------------------------")
print("")
time.sleep(0.5)
print("You have been born in the future Republic of Yunnan and Shandong during the year 1921 to a rich political family.")
time.sleep(0.5)
print("By the time you were 17, the Japanese had annexed Qingdao")
time.sleep(0.5)
print("When you were 22, Japanese forces occupied most of the current republic, including your hometown of Qingdao")
jscore = 0
pscore = 0
permoney = 5
govbudget = 10
cscore = 2
amescore = 0
UNscore = 0
Kscore = 0
Tscore = 0
govrank = 0
armyscore = 0
popsupport = 0
order = 0
development = 0
time.sleep(0.5)
while True:
    choice1 = int(input("Your college teacher asked you to rebel against the occupation one day after class...you (1: Accept, 2: Reject): "))
    if choice1 == 1:
        print("You took up arms against the Japanese, igniting a revolution...")
        jscore = jscore - 5
        cscore = cscore + 5
        time.sleep(2)
        for chance in range(1):
            chance=random.randint(1,3)
            if chance == 1:
                print("The revolution succeeded under your bravery and leadership. Crowds cheered you on, securing yourself the position of mayor")
                cscore = cscore + 3
                govbudget = govbudget + 3
                govrank = 1
            if chance == 2:
                print("The Japanese battled with fury, killing many of your comrades as they dragged you to jail.")
                cscore = cscore + 5
                armyscore = armyscore + 1
            if chance == 3:
                print("Following a tense stand-off, the Japanese reluctantly agreed to let you and the army lead the town")
                jscore = jscore + 3
                cscore = cscore + 3
                govrank = 1
        break
    if choice1 == 2:
        print("You rejected, reporting your teacher to the soldiers...")
        jscore = jscore + 1
        time.sleep(2)
        for chance in range(1):
            chance=random.randint(1,3)
            if chance == 1:
                print("Chinese patriots came to your house, beating you with sticks and clubs.")
                cscore = cscore - 2
            if chance == 2:
                print("Chinese patriots came to your house, nearly beating you until the Japanese police came, forcing you to become a cop")
                cscore = cscore - 5
                jscore = jscore + 5
            if chance == 3:
                print("You contemplated your choices, asking for a lightened sentence on the teacher. Your efforts resulted in jail.")
                cscore = cscore + 1
                govrank = - 1
        break
    else:
        print("TRY. AGAIN.")
        continue
time.sleep(1)
while True:
    choice2 = int(input("Eventually at the end of the war, the Chinese Armies arrived at the city. You felt... (1: Nervous, 2: Relieved): "))
    if choice2 == 1:
        cscore = cscore - 1
        break
    if choice2 == 2:
        cscore = cscore + 1
        break
    else:
        print("Answer. Again.")
        continue
if govrank > 0:
    print("The Chinese government eventually promoted you to Major in the army, awarding you for your efforts")
    govrank = govrank + 1
    govbudget = govbudget + 1
    armyscore = 3
    cscore = cscore + 4
if govrank < 0:
    print("The Chinese government freed you from jail, promoting you to Lieutenant for your efforts")
    armyscore = 2
    govrank = govrank + 1
    cscore = cscore + 3
if govrank == 0:
    print("You joined the army for redemption, relieving yourself of humiliation")
    armyscore = 1
    cscore = cscore + 2
time.sleep(1)
print("By 1954, you had been upgraded to the position of General. Many opposed this decision, giving a vital position to a 33 year old.")
print("You made dozens of connections, gaining support.")
time.sleep(1)
while True:
    print("The year was 1960, thousands of students called for a major governmental change.")
    print("The military backed up the side of the students, advocating for the removal of the communist dictatorship.")
    choice3 = int(input("Following a clash with the police, you had to make a difficult decision... [1: Peaceful Diplomacy, 2: Armed Revolt]: "))
    if choice3 == 1:
        print("The political tension made you abstain from the violence, calling for the students to have a summit with the government.")
        popsupport = popsupport + 5
        cscore = cscore + 1
        govrank = govrank + 2

        break
    if choice3 == 2:
        print("You took up arms against the Chinese government")
        cscore = cscore - 3
        popsupport = popsupport + 4
        govbudget = govbudget + 1
        armyscore = armyscore + 2
        govrank = govrank + 1
        break
    else:
        print("Answer. Again.")
        continue
social = 0
economic = 0
print("The Chinese government reluctantly agreed to cede the 2 major hotspots of activity, creating the Republic of Yunnan and Shandong ")
print("The move was done in part to stabilize the regime and appease the increasingly hostile United States, which had promised supportfor the students.")
print("Turning to you for leadership and protection, the Republic sweared you in as the first president. During the acceptance speech  you...")
while True:
    choice4 = int(input("1: Discussed Chinese unification, democracy, and peace.                                                                         2: Called for aggression, strength, and international recognition                                                               ANSWER:"))
    if choice4 == 1:
        social = social + 3
        economic = economic + 3
    if choice4 == 2:
        social = social - 3
        economic = economic - 3
    else:
        continue
    choice5 = int(input("You emphasised...[1: Order, 2: Economy, 3: Diplomacy/Military, 4: Health]: "))
    if choice5 == 1:
        print("You discussed the chaotic environment, calling for peace and stability")
        order = order + 3
        popsupport = popsupport + 3
        stability = 1
        break
    if choice5 == 2:
        print("You promised a golden era for the Republic, demanding an end to the dead economy.")
        govbudget = govbudget + 5
        economy = 1
        break
    if choice5 == 3:
        print("You promised international recognition, calling for the aid from democratic allies.")
        Kscore = Kscore + 3
        UNscore = UNscore + 3
        Tscore = Tscore + 3
        pscore = pscore + 3
        cscore = cscore + 3
        jscore = jscore + 3
        popsupport = popsupport + 3
        dipmil = 1
        break
    if choice5 == 4:
        print("You promised increased hospitals, a better rural treatment, and increased living standards.")
        popsupport = popsupport + 5
        development = development + 5
        health = 1
        break
    else:
        print("TRY AGAIN")
        continue
