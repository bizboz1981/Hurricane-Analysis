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

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def damage_string_to_int(damages):
  damages_int = []
  for damage in damages:
    if damage == 'Damages not recorded':
      damages_int.append('Unknown')
    else:
      damages_int.append(int((float(damage[:-1]))*conversion[damage[-1]]))
  return damages_int
# test function by updating damages
updated_damages = damage_string_to_int(damages)
#print(updated_damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
  hurricanes = dict()
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i],
                            "Month": months[i],
                            "Year": years[i],
                            "Max Sustained Wind": max_sustained_winds[i],
                            "Areas Affected": areas_affected[i],
                            "Damage": updated_damages[i],
                            "Deaths": deaths[i]}
  return hurricanes


# create hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

#print(hurricanes)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

def create_year_dict(hurricanes):
  hurricanes_by_year = {}
  for cane in hurricanes:
    current_year = hurricanes[cane]['Year']
    current_cane = hurricanes[cane]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_cane]
    elif current_year in hurricanes_by_year:
      hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year
#print(create_year_dict(hurricanes))

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def affected_area_counts(hurricanes):
  from collections import defaultdict
  dd = defaultdict(int)
  for cane in hurricanes:
    current_areas = hurricanes[cane]['Areas Affected']
    for area in current_areas:
      dd[area] += 1
  return dd

affected_area_counts = affected_area_counts(hurricanes)
#print(affected_area_counts[''])

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def affected_areas_count(affected_area_counts):
  max_area = ''
  max_area_count = 0
  for key, value in affected_area_counts.items():
    if value > max_area_count:
      max_area_count = value
      max_area = key
  return max_area, max_area_count
#print(affected_areas_count(affected_area_counts))     

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest_hurricane(hurricanes):
  deadliest_cane = ''
  deadliest_cane_deaths = 0
  for cane in hurricanes:
    current_cane = hurricanes[cane]['Name']
    current_death_toll = hurricanes[cane]['Deaths']
    if current_death_toll > deadliest_cane_deaths:
      deadliest_cane_deaths = current_death_toll
      deadliest_cane = current_cane
  return deadliest_cane, deadliest_cane_deaths

#print(deadliest_hurricane(hurricanes))
#print(hurricanes['Mitch'])
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def rate_by_mortality(hurricanes):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    current_deaths = hurricanes[cane]['Deaths']
    current_cane = hurricanes[cane]
    if current_deaths == 0:
      hurricanes_by_mortality[0].append(current_cane)
    elif 0 < current_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(current_cane)
    elif mortality_scale[1] < current_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(current_cane)
    elif mortality_scale[2] < current_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(current_cane)
    elif mortality_scale[3] < current_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(current_cane)
    else:
      hurricanes_by_mortality[5].append(current_cane)
  return hurricanes_by_mortality
print(rate_by_mortality(hurricanes))

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def costliest_hurricane(hurricanes):
  costliest_cane = ''
  costliest_cane_damage = 0
  for cane in hurricanes:
    current_cane = hurricanes[cane]['Name']
    current_damages = hurricanes[cane]['Damage']
    if isinstance(current_damages, str):
      continue
    elif current_damages > costliest_cane_damage:
      costliest_cane_damage = current_damages
      costliest_cane = current_cane
  return costliest_cane, costliest_cane_damage
#print(costliest_hurricane(hurricanes))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def rate_by_damage(hurricanes):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    current_damage = hurricanes[cane]['Damage']
    current_cane = hurricanes[cane]
    if isinstance(current_damage, str):
      hurricanes_by_damage[0].append(current_cane)
    elif 0 < current_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(current_cane)
    elif damage_scale[1] < current_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(current_cane)
    elif damage_scale[2] < current_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(current_cane)
    elif damage_scale[3] < current_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(current_cane)
    else:
      hurricanes_by_damage[5].append(current_cane)
  return hurricanes_by_damage

#print(rate_by_damage(hurricanes))
# categorize hurricanes in new dictionary with damage severity as key