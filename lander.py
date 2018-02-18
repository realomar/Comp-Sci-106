# Omar Ahmad / Ryan Fisher
from cisc106 import *

# Global variables:
altitude = 1000
velocity = 40
fuel = 25
strength = 4
gravity = 1.622
velocity_change_per_thrust = 4

def get_status():
    '''
    Creates a string displaying the ship's current vitals
    No parameter
    Returns: Readout of altitude, velocity, fuel, strength.
    '''
    global altitude
    global velocity
    global fuel
    global strength
    return ("Alt = {:.2f} Vel = {:.2f} Fuel = {:.0f} Str = {}".format(altitude, velocity, fuel, strength))

def thrust(throttle):
    '''
    Consumes fuel to give the ship thrust and decrease its velocity
    Parameter: throttle (int, float), amount of fuel consumed
    Return: none
    '''
    global velocity, fuel
    throttle = int(throttle) # do manually
    if throttle > fuel:
        throttle = fuel
    if throttle > strength:
        throttle = strength
    fuel -= abs(throttle)
    velocity -= throttle * velocity_change_per_thrust

def update_onesecond():
    '''
    Updates velocity and altitude for one second of simulation.
    No parameter
    No return
    '''
    global altitude, velocity, gravity, atmosphere_lower, atmosphere_upper, strength
    velocity = velocity + gravity
    altitude = altitude - velocity
    if altitude < 0:
        altitude = 0
    if atmosphere_lower < altitude < atmosphere_upper:
        strength -= 1

def simulate_landing(player):
    '''
    Landing simulator
    Parameter: player function which returns an amount of thrust
    Returns: a message after landing, depending on if the ship has_crashed or has_safely_landed
    '''
    while has_crashed() == False and has_safely_landed() == False:
        thrust(player())
        update_onesecond()
    if has_crashed() == True:
        print("Oh no the lander has crashed! Better skill next time!")
        return "Oh no the lander has crashed! Better skill next time!"
    elif has_safely_landed() == True:
        print("Great success! You should apply for an internship with NASA!")
        return "Great success! You should apply for an internship with NASA!"
    elif has_disintegrated() == True:
        print("Oh no the lander has disintegrated in the atmosphere!")
        return "Oh no the lander has disintegrated in the atmosphere!"

def player():
    '''
    test function
    '''
    return 1

def has_crashed():
    '''
    tests if the lander has crashed.
    No parameter
    Returns boolean, true if crashed.
    '''
    global altitude, velocity, strength
    if altitude <= 0 and velocity > strength:
        return True
    else:
        return False

def has_safely_landed():
    '''
    tests if the lander has safely landed.
    No parameter
    Returns boolean, true if landed.
    '''
    global altitude, velocity, strength
    if altitude <= 0 and velocity <= strength:
        return True
    else:
        return False

def reset_lander(a,v,f):
    '''
    Resets values for altitude, velocity, and fuel
    Parameter: (floats) altitude, velocity, fuel
    No return
    '''
    global altitude, velocity, fuel
    altitude = float(a)
    velocity = float(v)
    fuel = float(f)

def human_controller():
    '''
    Displays the current status to the user, and asks for input thrust.
    No parameters
    Returns the (int) thrust desired by the user
    '''
    print(get_status())
    return int(input("How much thrust this round? "))

def smart_controller():
    '''
    Function for the lander to control itself.
    No parameter
    Returns suggested thrust
    '''
    global altitude, strength, velocity, velocity_change_per_thrust, atmosphere_lower, atmosphere_upper
    while altitude >= 0:
        if atmosphere_lower < altitude < atmosphere_upper:
            return 0
        elif velocity <= strength:
            return 0
        else:
            calcVelocity = velocity
            increment = 0
            while calcVelocity > strength:
                calcVelocity -= 1
                increment += 1
    return 1 + (increment // velocity_change_per_thrust)
    # id altitude < velocity

atmosphere_lower = -1
atmosphere_upper = -1

# part 4.
# pre-existing functions have been updated
def reset_world(g,s,a_l,a_u):
    '''
    Resets the world according to parameters
    Parameters: gravity, strength, atmosphere_lower, atmosphere_upper
    No returns
    '''
    global gravity, strength, atmosphere_lower, atmosphere_upper
    gravity = g
    strength = s
    atmosphere_lower = a_l
    atmosphere_upper = a_u

def has_disintegrated():
    '''
    docstring for 1 line function lol
    Returns true if the ship's strength is zero or below.
    No parameters
    '''
    return strength <= 0


if __name__ == "__main__":
    simulate_landing(smart_controller)
