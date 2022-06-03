# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

"""
Assignment: Arguments 

You need to master the following to complete this assignment:
- Creating and indexing dictionaries;
- Writing functions and function arguments;
- Using various operators.

"""

# Part 1 - Greet Template
# define a function that takes two arguments in order: 
    # name, 
    # greeting_template --> set to default: "Hello, <name>!"

def greet(name="name", greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>", name)

print(greet("Bob"))
print(greet("Bob", "What's up, <name>!"))



# Part 2 - Force
# write a function that takes two arguments: 
    # mass (float), 
    # body(str) --> set to default: "earth"

# Note for myself: The Formula is: force = mass x gravity

def force(mass, body="earth"):

    # dict: Surface Gravity of the planets and the sun. (meter pr. square second)
    planet_gravity = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6
    }

    force = (mass * planet_gravity[body])
    return force

print(force(6, "venus"))
print(force(3, "sun"))
print(force(3))



# Part 3 -- Gravity
# Write a function that takes three arguments:
    # m1 An object's mass in kg (float), 
    # m2 Another object's mass in kg (float), 
    # d Their distance in meters (float).

# Note for myself: The formula is: pull = G × ((m1×m2)/d2)

def pull(m1, m2, d):

    G = 6.674*(10**-11)
    pull = (G * ((m1 * m2)/d ** 2))
    return pull


print(pull(800, 1500, 3))
print(pull(10, 20, 30))
