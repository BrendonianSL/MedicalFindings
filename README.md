# MedicalFindings

Hello! This is a portfolio project tasked by Codecademy as part of their Data Scientist: Analyst certification. The scope of this project is small and is inteded to practice basic Python to ask questions. This was open ended, meaning there were no instructions given. The only task was the ask questions about the dataset and create functions or classes that can be used to answer said questions.

## Basic Project Setup.
Since the project was small, I decided to not store all data by columns but instead by rows. This made it easier to keep all relevant data grouped together for iteration. Then we can start asking the real questions...

### Smokers By Region
The first question I wanted to ask given the dataset is if the region people are from affect the rate at which they smoke. This first analysis didn't require a lot of programming but allowed me to answer an interesting question.

```
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
```

Through this function, we are able to find that the southeast region has the highest percentage of smokers in the dataset with over 25.0% of smokers. Northwest region is tied for 18%~

### Smokers By Gender
Now I wanted to ask given the dataset, which gender has the most amount of smokers. The setup process was the same as the last just with different data.

```
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

```

We found out at 23% of all males in the dataset smoked compared to 17% of all females!

### Average Cost Per Region.
The last function I wanted to create was claculating the average cost of charges by region. This is without genderizing the patients.

```
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
```

The region we found had the highest cost per person was The Southeast region with $14,735 on average! That's a huge number. Set this number up with the smokers by region and it's no wonder their bills are higher! They smoke more often Than other people.

## Digging Deeper.
One way we can take the information we found and take it a step further is if we analyze the people in the set. Was more data collected on people for the southeast which caused bias in the data we are given. Did we interview an equal amount of smokers versus non smokers? What was the average age group of people that we have data on? All these questions could potentially lead us to a biased dataset. While that isn't something that is explored in the scope of this project, as a Data Analyst, it's always something to consider before making matter of fact statemetns!
