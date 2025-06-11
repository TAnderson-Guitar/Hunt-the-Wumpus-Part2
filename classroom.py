"""Cave Class for setup CAPA Showcasee"""
class classroom:
    """Defines attributes and methods for classroom objects"""
    def __init__(self, classroom_name):
        """Sets the class attributes"""
        self.name = classroom_name
        self.description = None
        self.linked_classroom = {}
        self.character = None

    def set_name(self, classroom_name):
        """Sets the cave name"""
        self.name = classroom_name