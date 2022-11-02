from main import space_records, Planet, SolarSystem, delete_planet, traverse_orbits

inner = filter(lambda x: x.dist_sun < asteroids.dist_sun, space_records)
outer = filter(lambda x: x.dist_sun > asteroids.dist_sun, space_records)


def partition(p_array, low, high):
    i = -1
    pivot = p_array[high]

    for j in range(low, high):
        if p_array[j].dist_sun <= pivot.dist_sun:
            i += 1
            p_array[i], p_array[j] = p_array[j], p_array[i]
    p_array[i + 1], p_array[high] = p_array[high], p_array[i + 1]
    return i + 1


def quick_sort(p_array, low, high):
    if low < high:
        part = partition(p_array, low, high)
        quick_sort(p_array, low, part - 1)
        quick_sort(p_array, part + 1, high)
    return p_array


def units(p_list):
    for p in p_list:
        if p.dist_sun < 1000:
            print(f"{p.name}, {int(p.dist_sun)} million mi")
        else:
            print(f"{p.name}, {p.dist_sun/1000} billion mi")


# From smallest to largest
def sort_by_size():
    planet_size = {}
    i = 0

    while i in range(len(space_records)):
        name = space_records[i].name
        radius = int(space_records[i].size)
        planet_size[name] = radius
        i += 1

    for k, v in sorted(planet_size.items(), key=lambda x: x[1]):
        print(f"{k}, {v} mi")


def inner_planets():
    planets = [i.name for i in list(inner)]
    print("Inner Planets")
    return planets


def outer_planets():
    planets = [j.name for j in list(outer)]
    print("Outer Planets")
    return planets


if __name__ == "__main__":
    # Root node = Sun
    the_sun = Planet("Sun", 432690, 0)
    solar_btree = SolarSystem(the_sun)
    # Mercury
    mercury = Planet("Mercury", 3031.9, 36.04, 88)
    left_child = SolarSystem(mercury)
    solar_btree.left = left_child
    space_records.append(mercury)
    # Venus
    venus = Planet("Venus", 3760.4, 67.24, 225)
    right_child = SolarSystem(venus)
    solar_btree.right = right_child
    space_records.append(venus)
    # Earth
    earth = Planet("Earth", 3958.8, 92.96, 365)
    solar_btree.insert_planet(earth)
    # Mars
    mars = Planet("Mars", 2106.1, 141.6, 687)
    solar_btree.insert_planet(mars)
    # Asteroid Belt
    asteroids = Planet("Asteroid Belt", 1.40e7, 390)
    solar_btree.insert_planet(asteroids)
    # Jupiter
    jupiter = Planet("Jupiter", 43441, 483.8, 12)
    solar_btree.insert_planet(jupiter)
    # Saturn
    saturn = Planet("Saturn", 36184, 890.8, 29)
    solar_btree.insert_planet(saturn)
    # Uranus
    uranus = Planet("Uranus", 15759, 1784, 84)
    solar_btree.insert_planet(uranus)
    # Neptune
    neptune = Planet("Neptune", 15299, 2793, 165)
    solar_btree.insert_planet(neptune)
    # Pluto
    pluto = Planet("Pluto", 738.38, 3700, 248)
    solar_btree.insert_planet(pluto)
    print("\n")
    space_records.remove(asteroids)
    # Print solar system
    solar_btree.print_names()
    print("\n")
    # Delete planet
    delete_planet(solar_btree, pluto)
    # Search planet
    solar_btree.check_records(mars)
    solar_btree.check_records(pluto)
    print("\n")
    traverse_orbits(solar_btree)
    print("\n")
    # Inner planets
    print(inner_planets())
    print("\n")
    # Outer planets
    print(outer_planets())
    # Sort by distance
    print("\nDistance from the Sun\n")
    planet_dist = quick_sort(space_records, 0, len(space_records) - 1)
    units(planet_dist)
    print("\nSort by Planet Radius\n")
    sort_by_size()

    # Create your own functions here.
