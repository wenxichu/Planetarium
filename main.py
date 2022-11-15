import queue as q
from math import floor

space_records = []


class Planet:

    def __init__(self, name, size, dist_sun, len_year=0):
        self.name = str(name)
        self.size = round(size, 0)
        self.dist_sun = round(dist_sun, 0)
        self.len_year = int(len_year)

    def num_digits(self):
        count = 0
        number = self.dist_sun
        while number > 0:
            count += 1
            number = floor(number/10)
        return count


class SolarSystem:
    def __init__(self, p_data):
        self.p_data = p_data
        self.left = None
        self.right = None

    def insert_planet(self, p_node):
        if self.p_data:
            if p_node.name == self.p_data.name:
                print("This planet is already in the solar system!")
                return
            if p_node.dist_sun < self.p_data.dist_sun:
                if self.left:
                    self.left.insert_planet(p_node)
                else:
                    self.left = SolarSystem(p_node)
                    space_records.append(self.left.p_data)
                    print(f"You have added {p_node.name} to the solar system.")
            if p_node.dist_sun > self.p_data.dist_sun:
                if self.right:
                    self.right.insert_planet(p_node)
                else:
                    self.right = SolarSystem(p_node)
                    space_records.append(self.right.p_data)
                    print(f"You have added {p_node.name} to the solar system.")
        else:
            self.p_data = p_node

    def print_names(self):
        if self.p_data.name == "Asteroid Belt":
            print(" |  | / Asteroid Belt", end=" /")
        else:
            digits = self.p_data.num_digits()
            print(" | " * (digits - 1) + self.p_data.name, end="")

        if self.left:
            self.left.print_names()
        if self.right:
            self.right.print_names()

    def search_info(self, p_node):
        if self.p_data:
            if p_node.name == self.p_data.name:
                print(f"\nName: {p_node.name}\n"
                      f"Size: {p_node.size} mi\n"
                      f"Dist: {p_node.dist_sun} million mi")
            if self.left:
                self.left.search_info(p_node)
            if self.right:
                self.right.search_info(p_node)

    def check_records(self, p_node):
        self.search_info(p_node)
        if p_node not in space_records:
            print(f"\nThe planet {p_node.name} was not found.")
            return


def traverse_orbits(r_node):
    print("Orbital Period\n")
    if not r_node:
        print("No planets are in orbit around the sun.")
    else:
        orbit = q.Queue(maxsize=50)
        orbit.put(r_node)

        while not orbit.empty():
            t_node = orbit.get()
            if t_node != r_node:
                name = t_node.p_data.name
                dist = t_node.p_data.dist_sun
                if dist < 360:
                    time = "days"
                else:
                    time = "years"
                period = t_node.p_data.len_year
                if name == "Asteroid Belt":
                    print(f"// {name} //")
                else:
                    print(f"{name} = {period} {time}")
            if t_node.left:
                orbit.put(t_node.left)
            if t_node.right:
                orbit.put(t_node.right)


def delete_planet(r_node, p_node):
    if not r_node:
        print("No planets are in orbit around the sun.")

    if r_node.left is None and r_node.right is None:
        if r_node.p_data == p_node:
            return None
        else:
            return r_node

    if r_node.p_data.name == p_node.name:
        print("Oops, this planet is already in orbit!")
        return

    k_node = None
    t_node = None
    l_node = None

    orbit = q.Queue(maxsize=50)
    orbit.put(r_node)

    while not orbit.empty():
        t_node = orbit.get()

        if t_node.p_data == p_node:
            k_node = t_node

        if t_node.left:
            l_node = t_node
            orbit.put(t_node.left)

        if t_node.right:
            l_node = t_node
            orbit.put(t_node.right)

    if k_node is not None:
        k_node.p_data = t_node.p_data
        if l_node.right == t_node:
            l_node.right = None
        else:
            l_node.left = None
            
    print(f"You have ejected {p_node.name} out of orbit. How rude!")
    space_records.remove(p_node)
    return r_node
