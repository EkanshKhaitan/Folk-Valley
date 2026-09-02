start_q = int(input("""


You wake up on your bed and find yourself in a flood, but you're super hungwy 

Would you:

1) Go and grab some food
2) Run to the attic

"""))


if start_q ==1:
    q_2 = int(input(""""
        
Good instincts, You go to the kitchen and grab some food but as you start eating you realize the water level is rising
        
Would you:
        
1) Continue eating
2) Try to find a safe spot where there is a chance for survival"""
        ))


    
if start_q ==2:
    print("""You reach the attic but the water level rises to above your waist, you frantically try to find a way out but before you know it you start drowning since there were no windows, GAME OVER :<""")
    exit()

if q_2 == 2:
    print("You reach the attic but the water level rises to above your waist, you frantically try to find a way out but before you know it you start drowning since there were no windows, GAME OVER :<")
    exit()

q_3 = int(input("""

You got full after eating for a while, the flood had calmed down by alot but you see your neighbour's kid drowning

Would you:

1) Save the neighbours kid
2) Watch Television
    
"""))


if q_3 == 1:
    print("You thought of being the towns hero but died a villan :< \nGAME OVER!")
    exit()
if q_3 == 2:
    q_4 = int(input('''

You decide to watch Television, you turn on the television

Would you:

1) Watch MrBeast
2) Watch ben azfart

'''))

if q_4 == 1:
    q_5 = int(input("""
You peacefully watch MrBeast's 'Last To Leave The Mansion, Keeps It', the flood calms down by now but you have to go take a doo doo
  
Would you:

1) Go do your 'business'
2) Go outside   """))

if q_4 == 2:
    print("you sit down to watch ben azfart then the flood comes and wipes your home away and you drown till your lifeless corpse decomposes and nobody knows you ever existed")
    exit()
    # This is what happens when u watch ben azfart >:(

if q_5 == 1:
    print('''

You go to the nearest washroom to release the chocolate hostages but as the door opens, you get flooded by dirty sewer water and die due to an infection... yuck

''')
exit()

if q_5 == 2:
    q_6 = int(input(''' 
You make your way outside but on the way you trip and fall hurting your knee on the road

Would you:

1) Go back inside to heal off
2) No pain no gain......
  '''))

if q_6 == 1:
    print('You go inside to grab a medkit since the pain was unbearable. Reaching the medkit took so long that the flood calmed enough that there isnt anything to worry about\n YOU WIN!!!!!!!!!!!!!!!!!!')
if q_6 == 2:
    print('You believe that you should stay out and continue searching for a safer area but then suddenly a massive wave of tsunami comes which ends you, unlucky...')