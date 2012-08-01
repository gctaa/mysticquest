class Room:
    def __init__(self, id, name, desc, doors):
        self.id = int(id)
        self.name = name
        self.desc = desc
        self.doors = doors

    def __str__(self):
        return "{0}\n{1}\n{2}\n{3}\n".format(self.id, self.name, self.desc, self.doors)


class House:
    def __init__(self):
        self.rooms = []

    def __str__(self):
        rooms_desc = ""
        for room in self.rooms:
            rooms_desc += room.__str__()
        return rooms_desc

    def get_room_by_id(self, id):
        for room in self.rooms:
            if room.id == id:
                return room

    def add_room(self, room):
        self.rooms.append(room)


class Hero:
    def __init__(self, name, house, room):
        self.name = name
        self.house = house
        self.location = house.get_room_by_id(room)

    def __str__(self):
        if self.location:
            return "{0} Room\n{1}".format(self.location.name, self.location.desc)
        return "My name is {0} and I'm lost in the void.".format(self.name)

    def go_north(self):
        if 'N' not in self.location.doors:
            return False
        
        north_room_id = self.location.doors['N']
        self.location = self.house.get_room_by_id(north_room_id)
        return True


    def go_south(self):
        if 'S' not in self.location.doors:
            return False

        south_room_id = self.location.doors['S']
        self.location = self.house.get_room_by_id(south_room_id)
        return True


    def go_west(self):
        if 'W' not in self.location.doors:
            return False
        
        west_room_id = self.location.doors['W']
        self.location = self.house.get_room_by_id(west_room_id)
        return True


    def go_east(self):
        if 'E' not in self.location.doors:
            return False

        east_room_id = self.location.doors['E']
        self.location = self.house.get_room_by_id(east_room_id)
        return True


    

