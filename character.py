"""Character class for Hunt the Wumpus"""
class Character:
    """Defines attributes and methods for Character objets"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Displays informaiton about the character"""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Method to set what the character can say"""
        self.conversation = conversation

    def talk(self):
        """Method to make the character talk"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " does not want to talk to you.")

    def fight(self):
        """Method to make the character fight you"""
        print(self.name + " does not want to fight you.")
        return True

class Enemy(Character):
    """Defines attributes and methods for Enemy objets"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """Sets the weakness for the Enemy class"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Gets the weakness for the Enemy class"""
        return self.weakness

    def fight_enemy(self, combat_item):
        "Method to fight the Wumpus"
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you whole! You died.")
            return False



class Npc(Character):
    """Defines attributes and methods for NPC objects"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.quest = None

    def set_quest(self, npc_quest):
        """Sets the quest for the npcs"""
        self.quest = npc_quest

    def get_quest(self):
        """Gets the quest from the npcs"""
        return self.quest
