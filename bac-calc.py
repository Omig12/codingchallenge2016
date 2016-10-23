# Israel O. Dilan-Pantojas
# israel.dilan@upr.edu
# Codetrotters 2017

# Source for BAC formula: http://www.ndaa.org/pdf/toxicology_final.pdf

print ("\nThis calculator will help you determine you Blood Alcohol Content over time.\nAfter drinking a few 10oz Medalla Light cans :P, which contain from 4% to 6% \nAlcohol per Volume so we can settle on 5% ApV.\n")

# Get Users Weight
pounds = input("What is your weight in pounds(lbs)? ")

# Convert weight to grams
weight = pounds * 453.592

print "Pounds: ", pounds,"= Grams: ", weight, "\n"

# Get Ammount of Tasty Medallas ingested and converts if oz, assuming 10oz per can
medallas = input("How many Medallas have you enjoyed today? ") * 10.0

# Assuming 10oz medalla light convert oz to mL  
volume = medallas * 29.5735296875

print "Oz: ", medallas, "= mL: ", volume

# Calculate grams of alcohol within volume of alcohol
grams = volume * .5 * 0.789

print "Grams of Alcohol consumed: ", grams, "\n"

# Get time elapsed since the drinking commenced and multiply it by US average elimination rate 0f 0.015 
time = input("How many hours have passed since you started drinking tody? ") * .015

print "Amount of Alcohol content eliminated in {} hours:".format(time/.015), time, "\n"

# Get user's biological sex
sex = raw_input("Are you a male of a female (m/f)? ") 
while sex not in ["m","f"]:
	sex = raw_input("Are you a male of a female (m/f)? ")

# Figure out the body alcohol distribution ratio 
r = 0 
if sex == "m":
	r = 0.68
else: 
	r = 0.55

print "Alcohol distribution ratio: ", r, "\n"

# Return BAC
print "BAC: ", ((grams / (weight * r)) * 100) - (time), "\n"