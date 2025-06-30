"""Cave Class for setup CAPA Showcasee"""
class Classroom:
    """Defines attributes and methods for classroom objects"""
    def __init__(self, classroom_name):
        """Sets the class attributes"""
        self.name = classroom_name
        self.description = None
        self.linked_classroom = {}
        self.character = None

    def set_name(self, classroom_name):
        """Sets the classroom name"""
        self.name = classroom_name

    def get_name(self):
        """Gets the classroom name"""
        return self.name

    def set_description(self, classroom_description):
        """Sets the classrooms description"""
        self.description = classroom_description

    def get_description(self):
        """Gets the classrooms description"""
        return self.description

    def describe(self):
        """Prints the classrooms description"""
        print(self.description)

    def link_classrooms(self, classroom_to_link, direction):
        """Populates dictionary of linked classrooms"""
        self.linked_classroom[direction] = classroom_to_link
        #print(self.name + " linked classrooms:" + repr(self.linked_classroom))

    def get_details(self):
        """Gets the classroom details"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, classroom in self.linked_classroom.items():
            print("The " + classroom.get_name() + " is " + direction)

    def move(self, direction):
        """Allows the player to move throughout the classrooms"""
        if direction in self.linked_classroom:
            return self.linked_classroom[direction]
        else:
            print("You cannot go that way.")
            return self

    def set_character(self, new_character):
        """Sets the character objects in the cave objects"""
        self.character = new_character

    def get_character(self):
        """Returns thename of character object in this cave"""
        return self.character

    def if____statement(self):
        print("""
                def if_statement(self, if__statement):
                    Big brain code that is very useful
                    if if__statement == if___statement:
                        if___statement = if__statement
                        if if__statement == if___statement:
                            if___statement = if__statement
                            if if__statement == if___statement:
                                if___statement = if__statement
                                if if__statement == if___statement:
                                    if___statement = if__statement
                                    if if__statement == if___statement:
                                        if___statement = if__statement
                                        if if__statement == if___statement:
                                            if___statement = if__statement
                                            if if__statement == if___statement:
                                                if if__statement == if___statement:
                                                    if if__statement == if___statement:
                                                        if if__statement == if___statement:
                                                            if if__statement == if___statement:
                                                                if if__statement == if___statement:
                                                                    if if__statement == if___statement:
                                                                        if if__statement == if___statement:
                                                                            if if__statement == if___statement:
                                                                                if if__statement == if___statement:
                                                                                    if if__statement == if___statement:
                                                                                        if if__statement == if___statement:
                                                                                            if if__statement == if___statement:
                                                                                                if if__statement == if___statement:
                                                                                                    if if__statement == if___statement:
                                                                                                        if if__statement == if___statement:
                                                                                                            if if__statement == if___statement:
                                                                                                                if if__statement == if___statement:
                                                                                                                    if if__statement == if___statement:
                                                                                                                        if if__statement == if___statement:
                                                                                                                            if if__statement == if___statement:
                                                                                                                                if if__statement == if___statement:
                                                                                                                                    if if__statement == if___statement:
                                                                                                                                        if if__statement == if___statement:
                                                                                                                                            if if__statement == if___statement:
                                                                                                                                                if if__statement == if___statement:
                                                                                                                                                    if if__statement == if___statement:
                                                                                                                                                        if if__statement == if___statement:
                                                                                                                                                            if if__statement == if___statement:
                                                                                                                                                                if if__statement == if___statement:
                                                                                                                                                                    if if__statement == if___statement:
                                                                                                                                                                        if if__statement == if___statement:
                                                                                                                                                                            if if__statement == if___statement:
                                                                                                                                                                                if if__statement == if___statement:
                                                                                                                                                                                    if if__statement == if___statement:
                                                                                                                                                                                        if if__statement == if___statement:
                                                                                                                                                                                            if if__statement == if___statement:
                                                                                                                                                                                                if if__statement == if___statement:
                                                                                                                                                                                                    if if__statement == if___statement:
                                                                                                                                                                                                        if if__statement == if___statement:
                                                                                                                                                                                                            if if__statement == if___statement:
                                                                                                                                                                                                                if if__statement == if___statement:
                                                                                                                                                                                                                    if if__statement == if___statement:
                                                                                                                                                                                                                        if if__statement == if___statement:
                                                                                                                                                                                                                            if__statement == if___statement

                    
                    else:
                        if___statement = if__statement 
            """)