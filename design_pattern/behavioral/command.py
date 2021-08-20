from abc import ABCMeta , abstractstaticmethod
class Icommand(metaclass = ABCMeta):
    "Static Interface"

    @abstractstaticmethod
    def execute():
        pass



class Light():

    def switch_on(self):
        print("The light is ON")

    def switch_off(self):
        print("The light is OFF")

class Switch_on_command(Icommand):
    def __init__(self,light):
        self._light=light

    def execute(self):
        self._light.switch_on()

class Switch_off_command(Icommand):
    def __init__(self,light):
        self._light=light

    def execute(self):
        self._light.switch_off()

class Invoker():

    """ Invoker class"""
    def __init__(self):
        self._commands={}

    def register(self,command_name,command):
        self._commands[command_name]=command

    def execute(self,command_name):
        self._commands[command_name].execute()


if __name__ == '__main__':

    #receiver
    LIGHT = Light()

    #command
    Switch_on = Switch_on_command(LIGHT)
    Switch_off = Switch_off_command(LIGHT)
    #invoker

    Switch = Invoker()
    

    #register command
    Switch.register("ON",Switch_on)
    Switch.register("OFF",Switch_off)

    Switch.execute("ON")
    Switch.execute("OFF")
    Switch.execute("ON")
    
    

    

    

    

        
    

