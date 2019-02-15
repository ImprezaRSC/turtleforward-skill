from mycroft import MycroftSkill, intent_file_handler


class Turtleforward(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleforward.intent')
    def handle_turtleforward(self, message):
        self.speak_dialog('turtleforward')


def create_skill():
    return Turtleforward()

