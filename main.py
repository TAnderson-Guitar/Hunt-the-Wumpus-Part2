"""The main program for Setup for CAPA Showcase"""
from classroom import Classroom


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
stage = Classroom("The Stage")
stage.set_description("Where the lecturn lays to rest")
stage_left = Classroom("Stage left")
stage_left.set_description("Otherwise known as On prompt")
floor = Classroom("The Floor")
floor.set_description("Where PE plays their reindeer games")
hall_entrance = Classroom("Hall Entrance")
hall_entrance.set_description("The entrance to the hall with a weird door")

#Carpark Area
bush_1 = Classroom("Bush 1")
bush_1.set_description("You have found yourself, in the bushes.")
bush_2 = Classroom("Bush 2")
bush_2.set_description("You have found yourself, in the bushes.")
bush_3 = Classroom("Bush 3")
bush_3.set_description("You have found yourself, in the bushes.")
bush_4 = Classroom("Bush 4")
bush_4.set_description("You have found yourself, in the bushes.")
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

top_quad.link_classrooms(Classroom, "North")
h9.link_classrooms(Classroom, "East")
h10.link_classrooms(Classroom, "East")
art_storeroom.link_classrooms(Classroom, "East")
h11.link_classrooms(Classroom, "East")
staffroom.link_classrooms(Classroom, "East")
hallway.link_classrooms(Classroom, "East")
h12.link_classrooms(Classroom, "North")
middle_room.link_classrooms(Classroom, "East")
h14.link_classrooms(Classroom, "South")
music_store_room.link_classrooms(Classroom, "South")
h15.link_classrooms(Classroom, "East")

current_classroom = top_quad
DEAD = False
while DEAD is False:
    print("\n")
    current_classroom.get_details()
    inhabited = current_classroom.get_character()
    if inhabited is not None:
        inhabited.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_classroom = current_classroom.move(command)
    elif command == "Talk":
        if inhabited is not None:
            #inhabited.talk()
    elif command == "Fight":
        if inhabited is not None and isinstance(inhabited, Enemy):
            fight_with = input("What do you want to fight with?")
            if inhabited.fight(fight_with) is True:
                print("Bravo, you win the battle.")
                current_classroom.set_character(None)
            else:
                print("Scurry home. You lost the fight")
                DEAD = True
        else:
            print("There is no one here to fight with.")
