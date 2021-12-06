import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position
revolver_chamber = spin_chamber()
#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	if revolver_chamber == bullet_position:
		"You are dead!"
	else:
		"Keep playing!"
	# YOUR CODE HERE




print(fire_gun())