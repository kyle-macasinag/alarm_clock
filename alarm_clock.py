class Clock:
    def __init__(self):
        self.time = '1300'
        self.switch = False
        self.alarm = ""

    def tell_current_time(self):
        print(self.time)
    
    def flip_switch(self):
        if self.switch == True:
            self.switch = False
        elif self.switch == False:
            self.switch == True
        print(self.switch)

    def set_alarm(self):
        self.alarm = input("What time would you like the alarm to go off?")
        print(self.alarm)

    def clock_function(self):
        self.tell_current_time()
        self.flip_switch()
        self.set_alarm()