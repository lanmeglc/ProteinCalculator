
protein_per_kg = 0.80
protein_per_kg_kid = 0.85
weight = input("Okay, what is your weight in kg?\n")
age = input("Are you an adult?\n")
protein_amount_adult = int(weight) * float(protein_per_kg)
protein_amount_kid = int(weight) * float(protein_per_kg_kid)

if age == "yes" or age == "yeah" or age == "ye":
 print("Okay, if you weight " + weight + "kg" + " you should eat " + str(protein_amount_adult) +" grams of protein per day.\n ")
elif age == "no" or age == "nah" or age == "nope":
 print("Okay if your not an adult and you weight " + weight + "kg" + " you should eat " + str(protein_amount_kid) + " grams of protein per day.\n ")
exit()

