class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
        
    def getChannel(self):
        return self.channel
        
    def getVolume(self):
        return self.volume

    def setChannel(self,number):
        if number > 1 and number <= 120:
            self.channel = number
            
    def setVolume(self,volumelevel):
        if volumelevel>=1 and volumelevel<=7:
            self.volume = volumelevel
        
    def turnOn(self):
        self.on = True
        
    def turnOff(self):
        self.on = False