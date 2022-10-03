class Items:
    
    stages = ["Stage One"]
    stage_one_levels = ["Level One"]
    stage_two_levels = ["Level One"]

    def __init__(self, name = 'No Name', life = 5, health = 100, money = 100, gold = 5, key = 0, resume = False, bag = True, wallet = True, back = False, stop_game = False, have_key = 0):
        self.name = name
        self.life = life
        self.health = health
        self.money = money
        self.gold = gold
        self.key = key
        self.resume = resume
        self.bag = bag
        self.wallet = wallet
        self.back = back
        self.stop_game = stop_game
        self.have_key = have_key

    def check_money(self, money):
        if self.money >= money:
            self.money -= money
            return self.money
        else:
            return self.check_life(1)

    def check_life(self, life):
        if self.life < life:
            print('Your life is finish')
            self.stop_game = True
            return self.stop_game
        else:
            self.life -= life
            return self.life
            print('Your life has been reduce by 1 (one)')
        
    def check_health(self, damage):
        temp = 0
        if damage > self.health:
            temp = damage - self.health
            self.check_life()
            self.health = 100 - temp
        else:
            self.life -= damage
        return f'Your health has been reduce by {damage}'

class Interaction(Items):

    def Barman(self):
        self.check_money(5)
        interaction = """
        (Conversation With The Barman)
            you: Hey
            Barman: Welcome, Sir
            you: how are you
            Barman: am ok, what can i get for you sir?
            you: i need a coffee
            Barman: coffee is $5
            you: no problem
            Barman: ok
            you: do you know where i can find ZULU
            Barman: go to the pool
            you: thanks man, i appreciate
            Barman: it's my Pleasure
        """
        print(interaction)

    def zulu(self):
        self.money += 100
        self.gold += 10
        try:
            self.stage_one_levels.index("Level Two")
        except ValueError:
            self.stage_one_levels.append("Level Two")
        else:
            pass 

        interaction = """
        (Conversation Zulu In The Pool)
            you: I ready for the mission Sir.
            Zulu: you took much time.
            you: am sorry sir.
            zulu: you are found of saying that! any way no problem.
            you: it will never happen again.
            (You finish level one of Stage One)
        """
        print(interaction)

    def Drug_Lord(self):
        self.money += 300
        self.gold += 10
        self.health -= 70
        try:
            self.stage_one_levels.index("Level Three")
        except ValueError:
            self.stage_one_levels.append("Level Three")
        else:
            pass

        interaction = f"""
        (Conversation With The Drug Lord and His Gang)
            you: i am {self.name}, Zulu sent me to bring his money
            Tony: we are not giving you any shit!
            Drug Lord: calm down Tony
            Drug Lord: {self.name}, is that you name?
            you: yea,
            Drug Lord: tell him that we have an unfinished business and am not giving him any money.
            you: am order not to go without ittttt.
            John: just go tell him what we said,
            Max: yes man, if you don't want to die
            you: then i will take it by force
            (You fought with them and took the money to Zulu)
        """
        print(interaction)

    def Zulu_House_Fight(self):
        self.money += 400
        self.gold += 50
        self.health -= 100
        if self.have_key == 0:
            self.key += 1
            self.have_key += 1

        try:
            self.stages.index("Stage Two")
        except ValueError:
            self.stages.append("Stage Two")
        else:
            pass 
        interaction = """
        (The Fight With Zulu)
            you: Sir, here is the money
            Zulu: ok, you can go
            you: but you have not given me my money as usual
            Zulu: i said go!!!
            you: am afraid sir, am not
            Zulu: then you will die for disobeying me
            (You fought with Zulu and killed him)
        """
        print(interaction)

    def Village_Elder(self):
        interaction = """
        (Conversation With The Village Elder)
            you: is this ......,
            Elder: i have been waiting for you.
            you: am here now, what's the mission?
            Elder: play the GAME in the Dungeon
            you: ok
        """
        print(interaction)

    def Dragon(self):
        print("Game in the Dungeon,")
        print("""
        You are Welcome to the SPIRIT SECTION, in this section you might have to pass an EVIL FOREST full of SpiritS. You will be given 3 things to choose from. Anything you choose is what will aid you through the Forest. (HINT: While making a choose don't choose base on NAME or STRENGTH of the Material you choose) make sure you understand before choosing any material and remember which section is this, good luck
        1. 10 different Guns
        2. A Stick full of Fire at the top
        3. A Sword
        """)

        while True:
            try:
                material = int(input("Which material do you choose? (eg. 1, 2, 3)"))
            except ValueError:
                print('please enter a number... ')
            else:
                if material == 1:
                    print("""You choose materail 1 which is 10 different Guns, but you FAILED. Remember this section is called SPIRIT SECTION, and we all know Guns can't be use to kill a spirit you lost a live""")
                    self.check_life(1)
                    break
                elif material == 2:
                    print("Hurray, finally you succeed by crossing the Forest with a Stick full of Fire, that's a nice one")
            
                    self.money += 500
                    self.gold += 100
                    try:
                        self.stage_two_levels.index("Level Two")
                    except ValueError:
                        self.stage_two_levels.append("Level Two")
                    else:
                        pass 
                    break
                elif material == 3:
                    print("You choose materail 3 which is a Sword, but you FAILED. because a sword can't kill a Spirit")
                    self.check_life(1)
                    break

    def Village_Two_Challenge(self):
        interaction = """
        (This Is The Next Round Of The Elder's Game)
            You are Welcome to the PROGRAMMING SECTION, in this section you have to answer a question correctly in other to WIN. You will be given 3 options to choose from and its about NIGERIA and PROGRAMMING (HINT: While making a choose don't choose base on NAME or STRENGTH of the Programming Course) make sure you understand before choosing any option and remember which Country is this, good luck
            QUESTION: What is the best aspect of programming to learn in Nigeria base on job opportunity? 
            1. Web Development and Data Science
            2. Game Development
            3. AI (Artificial Intelligence)
        """
        print(interaction)
        while True:
            try:
                program = int(input("Which program do you choose? (eg. 1, 2, 3)"))
            except ValueError:
                print('please enter a number... ')
            else:
                if program == 1:
                    print("""You choose program 1 which is Web Development and Data Science, yor won.""")
                    print('Congratulations You Finish the Game.')
                    self.money += 500
                    self.gold += 100
                    if self.have_key == 1:
                        self.key += 4
                        self.have_key += 1
                    try:
                        self.stage_two_levels.index("Level Three")
                    except ValueError:
                        self.stage_two_levels.append("Level Three")
                    else:
                        pass 
                    break
                elif program == 2:
                    print("You choose program 3 which is Game development, that is not the best to study in nigeria")
                    self.check_life(1)
                    break
        
                elif program == 3:
                    print("You choose program 3 which is AI (Artificial Intelligence), that is not the best to study in nigeria")
                    self.check_life(1)
                    break

        

class Map(Interaction):

    def Bar(self):
        self.Barman()
    
    def Zulu_Man(self):
        self.zulu()

    def Dungeon(self):
        self.Drug_Lord()

    def Zulu_House(self):
        self.Zulu_House_Fight()
    
    def Village(self):
        self.Village_Elder()

    def Dungeon_Dragon(self):
        self.Dragon()

    def Village_Two(self):
        self.Village_Two_Challenge()

class Level(Map):

    # Stage One Levels
    def Stage_One_Level_One(self):
        self.Bar()
        self.Zulu_Man()

    def Stage_One_Level_Two(self):
        self.Dungeon()

    def Stage_One_Level_Three(self):
        self.Zulu_House()

    # Stage Two Levels
    def Stage_Two_Level_One(self):
        self.Village()
        self.Dungeon_Dragon()

    def Stage_Two_Level_Two(self):
        self.Village_Two()

    def Stage_Two_Level_Three(self):
        self.Zulu_House()


    def Select_Level(self):
        num = 1
        for i in range(0, len(self.stage_one_levels)):
            print(f'{i + 1} {self.stage_one_levels[i]}')
            num += 1
        print(f'{num} Back')
        while True:
            if self.stop_game == True:
                break
            try:
                user_level_select = input('select eg. (Level One)... ').title()
            except ValueError:
                print('Invalid command')
            else:
                try:
                    check_level = self.stage_one_levels.index(user_level_select)
                except ValueError:
                    if user_level_select == 'Back':
                        self.back = True
                        break
                    else:
                        print('this level is currently not available')
                else:
                    if check_level == 0:
                        self.Stage_One_Level_One()
                    elif check_level == 1:
                        self.Stage_One_Level_Two()
                    elif check_level == 2:
                        self.Stage_One_Level_Three()

    def Select_Level_Two(self):
        num = 1
        for i in range(0, len(self.stage_two_levels)):
            print(f'{i + 1} {self.stage_two_levels[i]}')
            num += 1
        print(f'{num} Back')
        while True:
            if self.stop_game == True:
                break
            try:
                user_level_select = input('select eg. (Level One)... ').title()
            except ValueError:
                print('Invalid command')
            else:
                try:
                    check_level = self.stage_one_levels.index(user_level_select)
                except ValueError:
                    if user_level_select == 'Back':
                        self.back = True
                        break
                    else:
                        print('this level is currently not available')
                else:
                    if check_level == 0:
                        self.Stage_Two_Level_One()
                    elif check_level == 1:
                        self.Stage_Two_Level_Two()
                    elif check_level == 2:
                        self.Stage_Two_Level_Three()

class Stage(Level):

    def Stage_One(self):
        return self.Select_Level()

    def Stage_Two(self):
        return self.Select_Level_Two()

# Main Game Function
class BORING_SPACE_DRAGON_ADVENTURE(Stage):

    def Info(self):
        info = f"""
        KEYS: {self.key}
        GOLD: {self.gold}
        LIFE: {self.life}
        MONEY: ${self.money}
        HEALTH: {self.health}
        """
        return info

    def Game_Help(self):
        game_help = """
        This is a guide on how to play
        """
        return game_help

    def Select_Stage(self):
        num = 1
        for i in range(0, len(self.stages)):
            print(f'{i + 1} {self.stages[i]}')
            num += 1
        print(f'{num} Back')
        while True:
            if self.stop_game == True:
                break

            try:
                user_stage_select = input('select eg. (Stage One)... ').title()
            except ValueError:
                print('Invalid command')
            else:
                try:
                    check_stage = self.stages.index(user_stage_select)
                except ValueError:
                    if user_stage_select == 'Back':
                        self.back = True
                        break
                    else:
                        print('this stage is currently not available')
                else:
                    if check_stage == 0:
                        print(self.Stage_One())
                        break
                    elif check_stage == 1:
                        self.Stage_Two()
                        break
                    elif check_stage == 2:
                        self.Stage_Three()
                        break
                    elif check_stage == 3:
                        self.Stage_Four()
                        break
                    elif check_stage == 4:
                        self.Stage_Five()
                        break
                


    def prompt(self):
        self.back = False
        print()
        print(f'Welcome {self.name}')
        print('What do you want to do?... ')
        if self.resume:
            print('1. Load Game')
        else:
            print('1. Start Game')
        print('2. Status')
        print('3. Help')
        print('4. Open Treasure Box')
        print('5. Pay Dept')
        print('6. Exit')
        self.check()

    def check(self):
        print()
        while True:
            if self.stop_game == True:
                break

            if self.back:
                break

            try:
                user_input = int(input('choose a number from the list listed above... '))
            except ValueError:
                print('please enter a number...')
            else:
                if user_input == 1:
                    print('\nSelect Stage:\n')
                    self.Select_Stage()
                elif user_input == 2:
                    print(self.Info())
                elif user_input == 3:
                    print(self.Game_Help())
                elif user_input == 4:
                    self.Treasure_Box()
                elif user_input == 5:
                    self.Pay_Dept()
                elif user_input == 6:
                    print('Thank you for playing :)')
                    self.stop_game = True
                    break
                else:
                    pass

    def Pay_Dept(self):
        if self.gold >= 10000:
            print('You have paid your dept. Mission accomplished.')
            self.gold -= 10000
        else:
            print('You don\'t have enough Gold to clear your dept.')

    def Treasure_Box(self):
        if self.key >= 5:
            self.gold += 10000
            self.key -= 5
            print('You have successfully open the treasure box.')
        else:
            print('You can\'t open the treasure box, you need to find all the keys that are required.')

intro = """"
##################################################
####                                          ####
#### WELCOME TO BORING SPACE DRAGON ADVENTURE ####
####                                          ####
##################################################
"""

print(intro)
username = input('What is your name?... ')
player = BORING_SPACE_DRAGON_ADVENTURE(username)

while True:
    player.prompt()
    if player.stop_game:
        break

    
