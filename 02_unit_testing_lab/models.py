import json

class Car:
    def __init__(self, color, top_speed, gear_box, average_speed, hours_driven):
        self.color = color
        self.top_speed = top_speed
        self.gear_box = gear_box
        self.average_speed = average_speed
        self.hours_driven = hours_driven

    # For the more advanced python folks: Yes, the @property decorator would
    # be the better choice here. However introducing another concept might
    # be confusing
    def get_color(self):
        return self.color

    def get_top_speed(self):
        return self.top_speed

    def get_gear_box(self):
        return self.gear_box

    def get_average_speed(self):
        return self.average_speed

    def get_hours_driven(self):
        return self.hours_driven

    def get_json(self):
        ret = {
            'color': self.get_color(),
            'top_speed': self.get_top_speed(),
            'gear_box': self.get_gear_box(),
            'average_speed': self.get_average_speed(),
            'hours_driven': self.get_hours_driven()
        }

        return json.dumps(ret, sort_keys=True)

    def get_distance_driven(self):
        return self.average_speed * self.hours_driven
