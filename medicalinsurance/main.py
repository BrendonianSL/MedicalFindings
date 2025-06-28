# Imports CSV Python Module
import csv

# The Goal Is To Find Out If The Region Someone Is From Affects The Chance Of Them Becoming A Smoker. For This We Need All The Data.

data = []

# Store All Rows Into A File For Use
with open('insurance.csv') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Function That Analyzes Smokers By Region
def smokersByRegion():
    # Initialize Smokers By Region. Count Total Smokers.
    smokers_by_region = {}
    total_by_region = {}

    # For Each Row, Find Out If They Are A Smoker
    for row in data:
        if row['smoker'] == 'yes':
            # Find The Region In The Dictionaries.
            if row['region'] in smokers_by_region:
                smokers_by_region[row['region']] += 1
            else:
                smokers_by_region[row['region']] = 1
        if row['region'] in total_by_region:
            total_by_region[row['region']] += 1
        else:
            total_by_region[row['region']] = 1
    
    # Print Out The Percentage Of Smokers Per Region
    for region in smokers_by_region:
        print(f"In The {region.title()} Region, There Are {smokers_by_region[region] / total_by_region[region] * 100}% Smokers.")

# Function That Analyzes What Gender Has The Most Smoker
def smokersByGender():
    # Initializes Male And Female Dictionaries Of Smokers And Non Smokers
    smokers_by_gender = {'male': 0, 'female': 0}
    total_by_gender = {'male': 0, 'female': 0}

    # For Each Row, Find If They Are A Smoker.
    for row in data:
        if row['smoker'] == 'yes':
            # Add To Smoker Dictionaries
            smokers_by_gender[row['sex']] += 1
        
        # Add To Total Dictionaries
        total_by_gender[row['sex']] += 1

    # After Looping, Print Out The Percentage Of Smokers Per Gender
    for gender in smokers_by_gender:
        print(f"In The {gender.title()} Gender, There Are {smokers_by_gender[gender] / total_by_gender[gender] * 100}% Smokers.")

# Function To Find Average Cost Per Region.
def averageCostPerRegion():

    cost_by_region = {}
    total_by_region = {}

    # For Each Row, Add Their Number To Total And Cost To Region.
    for row in data:
        if row['region'] in cost_by_region:
            cost_by_region[row['region']] += float(row['charges'])
        else:
            cost_by_region[row['region']] = float(row['charges'])
        
        if row['region'] in total_by_region:
            total_by_region[row['region']] += 1
        else:
            total_by_region[row['region']] = 1

    # Print Out The Average Cost Per Region
    for region in cost_by_region:
        print(f"In The {region.title()} Region. The Average Medical Insurance Cost Per Person Is {cost_by_region[region] / total_by_region[region]} Dollars.")

# Function Calls
smokersByRegion()
smokersByGender()
averageCostPerRegion()