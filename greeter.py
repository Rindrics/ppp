from datetime import datetime

class Greeter:
    def __init__(self, name):
        self.name = name
        
    def _day(self):
        return datetime.now().strftime('%A')
    
    def _part_of_day(self):
        time = some_time()
        if time < 12:
            return "morning"
        elif time >= 12 | time < 17:
            return "afternoon"
        else:
            return "evening"
        
    def greet(self, store):
        day         = self._day()
        part_of_day = self._part_of_day()
        print(f"Hi, welcome to {store}!")
        print(f"How’s your {day} {part_of_day} going?")
        print(f"Here’s a coupon for 20% off!")
