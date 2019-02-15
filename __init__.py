from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Turtleforward(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleforward.intent')
    def handle_turtleforward(self, message):
        self.speak_dialog('turtleforward')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Turtleforward()

