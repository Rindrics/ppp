from datetime import datetime

class Greeter:
    def __init__(self, name):
        self.name = name
        
    def _day(self):
        return datetime.now().strftime('%A')
    
    def _part_of_day(self):
        current_hour = datetime.now().hour
        if current_hour < 12:
            part_of_day "morning"
        elif 12 <= current_hour < 17:
            part_of_day "afternoon"
        else:
            part_of_day "evening"
        
    def greet(self, store):
        day         = self._day()
        part_of_day = self._part_of_day()
        print(f"Hi, welcome to {store}!")
        print(f"How’s your {day} {part_of_day} going?")
        print(f"Here’s a coupon for 20% off!")
