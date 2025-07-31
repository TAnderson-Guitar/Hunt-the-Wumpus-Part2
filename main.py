"""The main program for Setup for CAPA Showcase"""
import os
from character import Enemy
from character import Npc
from classroom import Classroom
from actions import show_action_prompts

game_state = {
    "dead": False, "alec_learn": False, "mixed_audio1": False, "mixed_audio2": False, "picked_up_box": False, "defeated_miss_earl": False

}

#CAPA
top_quad = Classroom("Top Quad")
top_quad.set_description("An open space for people to play and thrive")
h9 = Classroom("H9")
h9.set_description("A place for art people to create and learn")
h10 = Classroom("H10")
h10.set_description("A creative haven splashed with color")
art_storeroom = Classroom("Art Storeroom")
art_storeroom.set_description("A treasure trove of creative supplies")
h11 = Classroom("H11")
h11.set_description("A sunlit studio buzzing with imagination")
staffroom = Classroom("Staffroom")
staffroom.set_description("Where music hums, ideas dance, and creativity brews")
h12 = Classroom("H12")
h12.set_description("Where rhythms echo and melodies bloom")
hallway = Classroom("Hallway")
hallway.set_description("The Hallway connecting H12, The Middle Room and H14")
middle_room = Classroom("Middle Room")
middle_room.set_description("The Middle Room: where practice becomes performance")
h14 = Classroom("H14")
h14.set_description("Where rhythms echo and melodies bloom")
music_store_room = Classroom("Music Store Room")
music_store_room.set_description("A tucked-away trove of timbre and tone")
h15 = Classroom("Cole's Room")
h15.set_description("Cole Room: where sound finds its soul")

#Hall
random_tables = Classroom("Random Tables")
random_tables.set_description("Just some random tables on the side")
top_stage = Classroom("Top Stage")
top_stage.set_description("The top middle of the stage, where most people perform")
audio_rack = Classroom("Audio Rack")
audio_rack.set_description("Where Mr cole and Mr Brooks work their magic")
stage_right = Classroom("Stage Right")
stage_right.set_description("Some performers emerge from here")
stage = Classroom("Stage")
stage.set_description("Where the lecturn lays to rest")
stage_left = Classroom("Stage left")
stage_left.set_description("Otherwise known as On prompt")
floor = Classroom("Hall Floor")
floor.set_description("Where PE plays their reindeer games")
hall_entrance = Classroom("Hall Entrance")
hall_entrance.set_description("The entrance to the hall with a weird door")

#Carpark Area
teacher_car_park = Classroom("Car park")
teacher_car_park.set_description("The start of the search for Cole's car")
floor_1 = Classroom("Floor 1")
floor_1.set_description("Your are standing in the middle of the car park")
floor_2 = Classroom("Floor 2")
floor_2.set_description("Your are standing in the middle of the car park")
floor_3 = Classroom("Floor 3")
floor_3.set_description("Your are standing in the middle of the car park")
floor_4 = Classroom("Floor 4")
floor_4.set_description("Your are standing in the middle of the car park")
floor_5 = Classroom("Floor 5")
floor_5.set_description("Your are standing in the middle of the car park")
cole_car = Classroom("Cole car")
cole_car.set_description("Coles car, always hidden, provides spare tyres")
school_exit = Classroom("School exit")
school_exit.set_description("The thin line between freedom, and torture")
beaty_car = Classroom("Beatrice Car")
beaty_car.set_description("A haunting area, do not proceed")
earl_car = Classroom("Earl Car")
earl_car.set_description("A place where kids are sent but never return")
white_car = Classroom("Mr whites car")
white_car.set_description("Nothing actually happens here.")

#CAPA
top_quad.link_classrooms(h9, "north")
h9.link_classrooms(top_quad, "south")
h9.link_classrooms(h10, "east")
h10.link_classrooms(h9, "west")
h10.link_classrooms(art_storeroom, "east")
art_storeroom.link_classrooms(h10, "west")
art_storeroom.link_classrooms(h11, "east")
h11.link_classrooms(art_storeroom, "west")
h11.link_classrooms(staffroom, "east")
staffroom.link_classrooms(hallway, "east")
staffroom.link_classrooms(h11, "west")
h12.link_classrooms(hallway, "south")
middle_room.link_classrooms(hallway, "west")
hallway.link_classrooms(h12, "north")
hallway.link_classrooms(middle_room, "east")
hallway.link_classrooms(staffroom, "west")
hallway.link_classrooms(h14, "south")
h14.link_classrooms(hallway, "north")
h14.link_classrooms(music_store_room, "south")
music_store_room.link_classrooms(h15, "south")
music_store_room.link_classrooms(h14, "north")
h15.link_classrooms(music_store_room, "north")
h15.link_classrooms(hall_entrance, "south")
hall_entrance.link_classrooms(h15, "north")

#HALL
hall_entrance.link_classrooms(floor, "north")
hall_entrance.link_classrooms(h15, "west")
floor.link_classrooms(stage, "north")
stage.link_classrooms(stage_right, "west")
stage.link_classrooms(stage_left, "east")
stage.link_classrooms(top_stage, "north")
stage.link_classrooms(floor, "south")
floor.link_classrooms(hall_entrance, "south")
stage_right.link_classrooms(random_tables, "north")
stage_right.link_classrooms(stage, "east")
top_stage.link_classrooms(random_tables, "west")
top_stage.link_classrooms(audio_rack, "east")
top_stage.link_classrooms(stage, "south")
stage_left.link_classrooms(stage, "west")
stage_left.link_classrooms(audio_rack, "north")
audio_rack.link_classrooms(stage_left, "south")
audio_rack.link_classrooms(top_stage, "west")
random_tables.link_classrooms(stage_right, "south")
random_tables.link_classrooms(top_stage, "east")
hall_entrance.link_classrooms(teacher_car_park, "east")
teacher_car_park.link_classrooms(hall_entrance, "west")

#carpark
h15.link_classrooms(teacher_car_park, "east")
teacher_car_park.link_classrooms(hall_entrance, "north")
teacher_car_park.link_classrooms(h15, "west")
teacher_car_park.link_classrooms(floor_3, "east")
floor_1.link_classrooms(cole_car, "east")
floor_2.link_classrooms(school_exit, "east")
floor_3.link_classrooms(beaty_car, "east")
floor_4.link_classrooms(earl_car, "east")
floor_5.link_classrooms(white_car, "east")
floor_1.link_classrooms(floor_2, "south")
floor_2.link_classrooms(floor_3, "south")
floor_3.link_classrooms(floor_4, "south")
floor_4.link_classrooms(floor_5, "south")
floor_5.link_classrooms(floor_4, "north")
floor_4.link_classrooms(floor_3, "north")
floor_3.link_classrooms(floor_2, "north")
floor_2.link_classrooms(floor_1, "north")
floor_3.link_classrooms(teacher_car_park, "west")
cole_car.link_classrooms(floor_1, "west")
school_exit.link_classrooms(floor_2, "west")
beaty_car.link_classrooms(floor_3, "west")
earl_car.link_classrooms(floor_4, "west")
white_car.link_classrooms(floor_5, "west")
cole_car.link_classrooms(school_exit, "south")
school_exit.link_classrooms(beaty_car, "south")
beaty_car.link_classrooms(earl_car, "south")
earl_car.link_classrooms(white_car, "south")
white_car.link_classrooms(earl_car, "north")
earl_car.link_classrooms(beaty_car, "north")
beaty_car.link_classrooms(school_exit, "north")
school_exit.link_classrooms(cole_car, "north")



miss_earl = Enemy("Miss Earl", "A Scary Intimidating and Strict teacher")
miss_earl.set_conversation("Hello Student what are you trying to do")
miss_earl.set_weakness("tall shelf")
h10.set_character(miss_earl)

alec = Npc("Alec", "A student who is mediocre at best, at playing guitar and a lil stupid")
alec.set_conversation("Should i hold an unmuted mic right infront of the speaker?")
middle_room.set_character(alec)


mr_cole = Npc("Mr cole", "A teacher who guides students through the art of entertainment")
mr_cole.set_conversation("Hello Student are you working hard or hardly working")
h15.set_character(mr_cole)

current_classroom = top_quad
while not game_state["dead"]:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    current_classroom.get_details()
    inhabited = current_classroom.get_character()
    if inhabited is not None:
        inhabited.describe()
    show_action_prompts(current_classroom, game_state, inhabited)
    command = input("> ").lower()
    if command in ["north", "east", "south", "west"]:
        current_classroom = current_classroom.move(command)
    elif command == "quests":
        print("Quests to be completed")
        print(f"- Teach Alec: {'1/1' if game_state['alec_learn'] else '0/1'}")
        print(f"- Mix Lectern: {'1/1' if game_state['mixed_audio1'] else '0/1'}")
        print(f"- Mix ATEM: {'1/1' if game_state['mixed_audio2'] else '0/1'}")
        print(f"- Picked Up Box: {'1/1' if game_state['picked_up_box'] else '0/1'}")
        input("\nPress Enter to continue...")
    elif command == "talk":
        if inhabited is not None:
            inhabited.talk()
            if inhabited == alec and not game_state["alec_learn"]:
                learn = input("Should alec put a mic infront of an unmuted speaker? (y/n) ").lower()
                if learn == "no":
                    print("You have correctly taught alec waterson")
                    input("\nPress Enter to continue...")
                    game_state["alec_learn"] = True
                else:
                    print("Alec then proceeds to go deaf after creating infinite feedback killing everyone in capa")
                    game_state["dead"] = True
        if inhabited == mr_cole:
            if game_state["mixed_audio1"] and game_state["mixed_audio2"] and game_state["picked_up_box"] and game_state["alec_learn"]:
                print("You are finally competent.")
                print("and you have setup for CAPA Showcase")
                game_state["dead"] = True
            elif not game_state["alec_learn"]:
                print("Go teach alec in the middle room about entertainment")
                input("\nPress Enter to continue...")
            elif not game_state["mixed_audio1"]:
                print("Why does the hall sound like theres no lecturn?")
                input("\nPress Enter to continue...")
            elif not game_state["mixed_audio2"]:
                print("Why does the hall sound like theres no atem?")
                input("\nPress Enter to continue...")
            elif not game_state["picked_up_box"]:
                print("Where is the box?")
                input("\nPress Enter to continue...")
    elif command == "mix" and current_classroom == audio_rack:
        print("You have made it to the mixing desk now you must complete this mixing challenge")
        print("Type '1' to unmute Wireless Mic 1")
        print("Type '2' to unmute Lectern")
        print("Type '3' to unmute the ATEM")
        mixing_choice = input("Choose wisely (1/2/3): ")
        if mixing_choice == "1":
            print("Yea so basically that was really loud and now u can't hear anything")
            print("You are so foolish bro what r u doing")
            game_state["dead"] = True
        elif mixing_choice == "2":
            print("The Lectern is now correctly unmuted")
            game_state["mixed_audio1"] = True
            input("\nPress Enter to continue...")
        elif mixing_choice == "3":
            print("The ATEM is now correctly unmuted")
            game_state["mixed_audio2"] = True
            input("\nPress Enter to continue...")
        else:
            print("Everyone in a 100m radius just died because of you")
            game_state["dead"] = True
    elif command == "pickup box" and current_classroom == cole_car:
        print("you have now collected the box, good job bro")
        print("Hint: Can capture evil people when fighting")
        game_state["picked_up_box"] = True
        input("\nPress Enter to continue...")
    elif command == "fight":
        if inhabited is not None and isinstance(inhabited, Enemy):
            if game_state["picked_up_box"]:
                print("You have the box in hand ready to start to battle")
            else:
                print("You are not winning this battle")
            fight_with = input("What do you want to fight with? ").lower()
            if inhabited == miss_earl:
                if fight_with == "box" and game_state["picked_up_box"]:
                    print("LOL, Miss Earl is trapped in the box and she can't escape.")
                    print("\n You have defeated miss earl, the soul of music is finally released")
                    current_classroom.set_character(None)
                    game_state["defeated_miss_earl"] = True

                    print("""
.****************************+++++++-=@@@*#@@%*=+*-:.-*##%%@%*#*+=-=**=+*++++++++++++=+++%%+=-%*+*.
.***********+*++*******+=---===+**-:=@@*@@@@@@@@@@@@%=.....::-::=+#**+==+=+++=+++++++===+@%+=:-#=+.
.*+********+********+==+***+++=--:%@*@%@@##...:.....-#@@@@+=+*%#**=:-++++==++=++=++=++++*%#++=@@*+.
.*****************+++***==--..-:..@+*%##*%@@@%@@@@@@@@#:.:-*@#==+*#**===+++++++++++++==+*@*++--=+=.
.*+++*******+*+*+==**+++-=*%@@@@@@@@%*%@@#=............=@@@%+==%#-=+**=-++=++++++++++==+*%**=====+.
.*******+**+***+=+*+*+=-=-@@#%%@@@@-=%@...@@@@@@@@@@@@@%=...-+%*=*@+=+=-=+++==+++=+=+=++***+===+=+.
.******++++++==-=+=+=-+*%@@@@@@@@%%%%+.@@@@@@@%*-...#@@@@@@#.=..:+-*@#:--++++++=+++++==+***+====++.
.*******+****##*+%%+=+=*@@@@@%%@@@@%+@@@@@@@@@%@@@@@@#....-@@@@-:..=:#@#:=+++++++++=+===+=*+==++=+.
.+****+++++=+**#@#+@*-=%@@%%@@@@@@@@@@@%@#+*@@@@+.=@@@@@@@....@@@#...--%%+===+=+++++++=+++*+===+++.
.***+****+**#@+@@+*..=**@@@@@@@@@@@@@@@@@:@%:..#@@@.:@**@@@@@..+@@@+.:--+@#==++++++++=++++*+==+++=.
.++++++====+=++##%=:+++@*#@@#%@@@@@@%@@@@@@*=@-...:@@.:@*%@@@@=..#@@@..:--%#*+++++++++==++*=====++.
.**++**-+:.-*@#:::-**=+@+*@@@@#*%@@%=....:-*@@@@@*=..#=.+..@@@@@..-+@@.:--+*+*+=++=++++=++*===+=++.
.+****##@@%:+@@.-+++*++%.@@@@*#@@@+-:-+++=+-:=+++**.==-=:@=..*@@@=.-+@@.---=+++++++++=+=+**=====++.
...==-=#@@@@--:=+++#+=**.@*@=%@@%=--=+++=======+++%@-.-#::%@#..=@%-...@@.%.:=+++*++++++=++*=====++.
@@@.+:.*.+@@.=---*+#*+#==@*#*@@@+--===--==+++*+++*+#@@:.#+.:@%@+=#%=..:@%#%.-=+-++=++++=+**=====++.
..@+%*@@@@@.:=-=++**+++:+%%@@@@+*+=-====+====+++==++*#@@.:#..#@@@=++:..@@.@+.-+==++++===+**====+=+.
=@###.@@%@@.=**=+*+*+=+=+==@@@#====+***++***++++++++*+#@@+.%-.:=@@+=-:..@.#@..-*=++++=+=+**-===+++.
*@@@@@@@@@.@@+*:===*+==+-=+@@#-=*+====+**#***#*++++++==+#@*.#*..=@@+=::.+*.@-.-==:*+++==+*+=====++.
+@@@#=-...:*=-*.=-=+=-=%:=%@%*=++---=====*++*+++=+++++*+++@+.+*..:@%+-.#:@.@*=.==.=*+===+#+-=====+.
.....:-=+-##==+.*-++-:-+:*@@%+-=---:......:-=*++++=+--:...-%@.*+..#@---+=%-=#@.:+-:**+=++#=-=====+.
.+****++#+**:=#-+=+*=:-+.#@@*=*@@@@%@@@@@@%====*+++*+==@@@@@@%:%=.:@#-=:@.==+%:.===-++=++#=-====++.
.***+--+****-*#*.-+==:++.@@@@##+==+**++*%@@#*++++=++++###*=--=.=*=..@+=.#-++%-+:=+*+++=++#=======+.
.*++*@@%++++-+%@.:#==-=*.%@@+:............:-======++=-=.....:*@-++-.+#*:@==#%.+.:#*=+==+**-======+.
.***+--=*#*+++%@:-@*=-=#.*@*=....#@@@@@@@..-==---=*++*#:@@@%@%@.@**..**.@*=+@.=:=+*+++=+**-======+.
.**+*++++**==+%@.:*-+--#.+@*:.@@@@@@@#@+@@@@=-=++==+#+@@@@%%@@@@-#@-:=@:**:@@.--=**+++=+#*-=+====+.
.++**********+#@.-#-#*=*-=@#@@@*--=:::+*#%**+=*+=**-#**+**=:.-#@.@*=+.@==+-@*.-*++=++==+#*:======+.
.********++*****++=**++==#@*=-::-:.:+*%@@*=+==*=++*++#*=:-#%%=:-.*@*=.@*=+=@-.-*+++++==+#+-=======.
.*********+++++-+%:+*+*=-*#:-====####+--:-=-**+-+++##*%%##+==*+++*+**++#==+#--+*+++++==+#+-======+.
.****+++#******==@-=*++#**-==+++-+*+++==++*###*+++*###**++=+++***+**=-+@*#**-:++++++===+#=-=======.
.**+===--:--==++%%+++++*%+------+*+===+=-:...-****+==++-*@::-+===++=--+#*=*+=-+++++====+#=-=======.
.++*@@@@@@@@@%@%*+=+#-=@@---=++===-=+==:-@@@*=-=+++*+==.=+#@+--=--==+:+=*+=++=+++=+++==+#--+===+==.
.##%*+=+++*******%+=*-=@%====*+++==--++*@@..-:.::---:......@@*==++++-=+++++++++++++=+==*#-==+=====.
.++*+*+=+++***##%%**=:-@%+++=+====+++=+#@@:=*##*#%***%%@@@**+*+-===+-+=*===++=++++++===#*:=======+.
.###**@@@##*+=+++++%%=*#*=+=+==+==++=++=+**%@@@#**#*+*%#+==-++==++*+===#+++++++++======#+:========.
.*****++=++*+*++++#*-..:.:=+++++===-=++*+=-==+=++==+=.:=**+--+#+-=+=+=+#+++=++=++++====#*=========.
.##***#**#**+**%%##=+@*@.-=++++=++++=++=-=+*#%=###@@@@#@@*#*+-+@+=+++-+*++++++++++++===*+-===+====.
.####*******#@*-....@@@@=.=++++=+++==+=*#==-...............:=+*@+=+=-:++===+++++++++===#+-======+=.
.**=-..........+@@@#@@@@@.-=+++++=++@@==:..-#@@@@@@@@@@@@@@@@#@+:=*=.@+....:+*++==+===+#=-=++=====.
....+@@@@@@@@@@@@@@@#%+%@*.=====+++*++@%#@@@%**%@%#*++-:...-++#+-==.=@.:@@@@.=*+=++===+#==========.
@@@@@@@@@@@@@@@@@@@@@@@@@@-+*=++++=-.#@*=--===-:..:---:--===+*#===..@%.@++*....:-=====+*=-========.
#@@@@@@@@@%%@@@@@@@...-.=@.=*+======+@+=++===-===++==+===**+=:=+=..@@#.@@%@.-@@#:.::==+*-==+======.
#@@@@@@@@@@@@@@@@..@@@-++@.+=+*=+++=+*--=+*+****##%@%%#*#++=+-=:..@@@##:@@@.+@**@@@=::=*=========+.
#@@@@@@%@@@@@@@@@.@*%@@*=@.-+=++==+=+==-=====++=======+++====...@@+@@+#-.%@.+@#@@@::#%:...========.
#@@@@@@@@@@@%....%-...@@+@-.=*==+*+==-=-===++==+++++====+=+-..@@@#.@@-**+*@.#@+%%..@@%-%@#.:-===+=.
#@@@@@@=......:....@%..@@@@..=*==+*#***+=-====-====-==--==-.%@@#@+.@@.***--.#@#%=.%@++*@@.:@*=+++=.
#@@.....=+#%*=-@=-.*@+..@@@@=.:##==+*#%%#+-----++=====+++-.-@#*-@+.@@:-#*+*.@@%%.-@=-+##.@@.....-+.
#@@.=@@*=*@*+:-@=..*#@+..@#@@*:.=@#==+**%@@%#*===--++**#*-=@@+*+@#.-@+:*++%.@@%*.@%.*#%#@@..%#+:...
@@:.=#@@*=+@%##@@=+..#@-.-%=@@@=.:=%%+---==+#%@%@@@@%**=:*@@-=.@@-..@@.###*.%@%=-@.:*@#%..-@%=+-=*.
....+@@-+*++*#@@#-#@=.=*..:@*@@@@+..:+@@*+--==+**=--==:-%@@@==:@@+#+.@-*++*-.@@.*#-%#=#..%@**#@%*-.
.#.=#=@#++*##+=*#+=+@@*#:.:-%:@@%@@#-:::=#@%%#%@##++-:-%@@@+=-*@+*-..-@.-:*#.@@.+.+**#.@*+%@@:::-:.
        """)
                    input("\nPress Enter to continue...")
                else:
                    print("Miss Earl doesnt even recognise your presence, go learn from mr cole.")
                    input("\nPress Enter to continue...")

            elif inhabited.fight(fight_with):
                print("Bravo, you win the battle.")
                current_classroom.set_character(None)
            else:
                print("Scurry home. You lost the fight")
                game_state["dead"] = True
        else:
            print("There is no one here to fight with.")
