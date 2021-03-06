# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_dmg(damage_cost_list):
    updated_damages = []

    conversion = {
        "M": 1000000,
        "B": 1000000000
    }

    for cost in damage_cost_list:
        if cost == 'Damages not recorded':
            updated_damages.append(None)
        else:
            updated_damages.append(float(cost[:-1]) * conversion[cost[-1]])
    
    return updated_damages

# print(update_dmg(damages)[:10])



# write your construct hurricane dictionary function here:

def construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    '''
    This function will organize all the lists into a dictionary.
    The keys are the names of the hurricanes and the values are all the information related to that hurricane stored into another dictionary.
    '''

    hurricanes_dictionary = {}

    for i, name in enumerate(names):
        hurricanes_dictionary[name] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damages': update_dmg(damages)[i],            #This will call the update_dmg function to return the damages as floats
            'Deaths': deaths[i]
        }
    
    return hurricanes_dictionary

hurriace_dict = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)  # Constructing hurricane dictionary


# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year(hurricane_dictionary):
    """
    return a new dictionary of hurricanes using the years as keys.
    Takes one parameter which is the return value of the construct_hurricane_dict
    """    
    name = list(hurricane_dictionary.keys())
    year = [hurricane_dictionary[hurricane]['Year'] for hurricane in hurricane_dictionary.keys()]
    year_dict = {}

    for i, year in enumerate(year):
        if year in year_dict:
            year_dict[year].append(hurricane_dictionary[name[i]])
        else:
            year_dict[year] = []
            year_dict[year].append(hurricane_dictionary[name[i]])

    return year_dict


# write your count affected areas function here:
def affectation_per_area():
    
    areas_affected_dict = {}

    for region in areas_affected:
        for area in region:
            if area in areas_affected_dict:
                areas_affected_dict[area] += 1
            else:
                areas_affected_dict[area] = 1
            
    return areas_affected_dict


# write your find most affected area function here:
def most_affected(areas_affected_dict):
    most_affected_area = max(areas_affected_dict, key= areas_affected_dict.get)
    return most_affected_area

print(f'The area that has presented most damage is {most_affected(affectation_per_area())}. The total amount of hurricanes that passed through this area is {affectation_per_area()[most_affected(affectation_per_area())]}')    


# write your greatest number of deaths function here:
def greatest_num_deaths():

    death_dict = {name: num_death for name, num_death in zip(names, deaths)}

    cane_name = max(death_dict, key=death_dict.get)
    total_deaths = death_dict[cane_name]

    return cane_name

print(f"the most deadly hurricane is the {greatest_num_deaths()} which caused a total of {hurriace_dict[greatest_num_deaths()]['Deaths']}")


# write your catgeorize by mortality function here:
def mortality_category():

    mortality_scale = {
        0: 0,
        1: 100,
        2: 500,
        3: 1000,
        4: 10000
    }

    hurricanes_by_mortality = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }

    for name, death in zip(names, deaths):
        if death == mortality_scale[0]:
            hurricanes_by_mortality[0].append(name)
        elif death <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(name)
        elif death <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(name)
        elif death <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(name)
        elif death <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(name)
        else:
            hurricanes_by_mortality[5].append(name)
    
    return hurricanes_by_mortality

hurricane_tiers = mortality_category()
print(hurricane_tiers)

# write your greatest damage function here:

def greatest_dmg(hurricanes):
    hurricane_name = ""
    total_damage = 0
    
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Damages'] == None:
            continue
        if hurricanes[hurricane]['Damages'] > total_damage: 
            total_damage = hurricanes[hurricane]['Damages']
            hurricane_name =  hurricanes[hurricane]['Name']

    return hurricane_name, total_damage

most_dmg_name, most_dmg_count = greatest_dmg(hurriace_dict)
print(most_dmg_name, most_dmg_count)

# write your categorize by damage function here:

def dmg_category(hurricanes):

    dmg_scale = {
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }

    dmg_category_dict = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {}
    }

    for hurricane in hurricanes:
        if hurricanes[hurricane]['Damages'] == None:
            continue
        if hurricanes[hurricane]['Damages'] < dmg_scale[1]:
            dmg_category_dict[1][hurricane] = hurricanes[hurricane]
        elif hurricanes[hurricane]['Damages'] < dmg_scale[2]:
            dmg_category_dict[2][hurricane] = hurricanes[hurricane]
        elif hurricanes[hurricane]['Damages'] < dmg_scale[3]:
            dmg_category_dict[3][hurricane] = hurricanes[hurricane]
        elif hurricanes[hurricane]['Damages'] < dmg_scale[4]:
            dmg_category_dict[4][hurricane] = hurricanes[hurricane]
        else:
            dmg_category_dict[5][hurricane] = hurricanes[hurricane]
        
    return dmg_category_dict

tiers = dmg_category(hurriace_dict)

print(tiers)