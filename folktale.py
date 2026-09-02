print("\n\n\n`You wake up and see water everywhere in your home, it takes you a second to realize that it is a flood.")
print("""Would you
1) Rush towards the kitchen to grab a snack
2) You try to reach the attic""")
starting_q = int(input(">>> "))

if starting_q == 1:
    food_q=int(input("\nYou grab a jug of milk and cereal and sit to eat it, with the water from the flood gently flowing near your legs giving you a relaxing experience. You notice the water level rising. Would you\n1)Stay here and eat food\nOR\n2)Rush to the attic\n>>>"))
    if food_q == 1:
        tv_q = int(input("You stay here, enjoying the cold water. Once you finish the cereal, you decide to head to the living room to watch T.V\n1)Would you watch Mr Beast\nOR\n2)Would you watch ben azfart\n>>>"))
        if tv_q == 1:
            print("Great choice, the flood slightly calms down and you continue watching the television")
        if tv_q == 2:
            print("The water starts rising and slowly drowns you untill you cannot breathe and your lifeless corpse just floats there...........\n GAME OVER")
    
if starting_q ==2:
    med_q = int(input("\nOn the way to the ladder of the attic, you accidently hurt your knee by falling on a chair. Would you\n1)Get a medkit to heal\nOR \n2)Push through the pain to reach the attic\n>>>"))
    if med_q == 1:
        tv_q = int(input("Great Choice, you could've gotten an infection if you werent careful!, now you go to the living room to watch T.V, Would you\n!1)Watch Mr.Beast\n2)Watch ben azfart"))
        if tv_q == 1:
            print("Great choice, the flood slightly calms down and you continue watching the television")
        if tv_q == 2:
            print("The water starts rising and slowly drowns you untill you cannot breathe and your lifeless corpse just floats there...........\n GAME OVER")