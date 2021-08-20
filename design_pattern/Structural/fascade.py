class Sensor():

    def __init__(self):
        pass

    def sensor_on(self):
        print("sensor is ON")

    def sensor_off(self):
        print("sensor is OFF")

class Smoke():

    def __init__(self):
        pass

    def smoke_on(self):
        print("smoke  ON")

    def smoke_off(self):
        print("smoke  OFF")

class Light():

    def __init__(self):
        pass

    def light_on(self):
        print("light is ON")

    def light_off(self):
        print("light is OFF")

class Fascade():

    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Light()

    def emergency(self):
        self._sensor.sensor_on()
        self._smoke.smoke_on()
        self._light.light_on()

    def noEmergency(self):
        self._sensor.sensor_off()
        self._smoke.smoke_off()
        self._light.light_off()

if __name__=='__main__':
    fascade = Fascade()
    sensor=22
    if sensor>22:
        fascade.emergency()

    else:
        fascade.noEmergency()

    
        
        

