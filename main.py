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

# test function by updating damages
def convert_M_and_B(record):
    updated_record = []

    for data in record:
        if "M" in data:
            updated_data = data.replace("M", "")
            converted_num = float(updated_data) * conversion["M"]
            # print(converted_num)
            updated_record.append(converted_num)
        elif "B" in data:
            updated_data = data.replace("B", "")
            converted_num = float(updated_data) * conversion["B"]
            # print(converted_num)
            updated_record.append(converted_num)
        else:
            converted_num = "Damages not recorded"
            updated_record.append(converted_num)

    return updated_record


# print(convert_M_and_B(damages))


# 2 
# Create a Table
name_with_combined_data = {}
combined_data_list_dict = []

for data in range(len(names)):
    combined_data = dict()
    combined_data["Name"] = names[data]
    combined_data["Month"] = months[data]
    combined_data["Year"] = years[data]
    combined_data["Max Sustained Wind"] = max_sustained_winds[data]
    combined_data["Areas Affected"] = areas_affected[data]
    combined_data["Damage"] = convert_M_and_B(damages)[data]
    combined_data["Deaths"] = deaths[data]
    combined_data_list_dict.append(combined_data)

# print(combined_data_list_dict)


for num in range(len(names)):
    name_with_combined_data[names[num]] = combined_data_list_dict[num]

# Create and view the hurricanes dictionary
# print(name_with_combined_data.get("Michael"))


# 3
# Organizing by Year
year_with_combined_data = {}

def year_key_dict_values(combined_data, year):
  year_dictionary_list = []
  for data in combined_data:
    for dictionary in data.values():
      if dictionary == year:
        year_dictionary_list.append(data)
  
  return year_dictionary_list
# create a new dictionary of hurricanes with year and key
for data in years:
  year_with_combined_data[data] = year_key_dict_values(combined_data_list_dict, data)

# print(year_with_combined_data)


# 4
# Counting Damaged Areas
def count_areas_affected(area_affected):
  all_areas_affected = []

  for data in area_affected:
      for areas in data:
          all_areas_affected.append(areas)

  areas_affected_count = {area_count:all_areas_affected.count(area_count) for area_count in all_areas_affected}
  return areas_affected_count


# create dictionary of areas to store the number of hurricanes involved in
# print(count_areas_affected(areas_affected))

# 5 
# Calculating Maximum Hurricane Count
def area_affected_most_hurricanes(area_dict):
    keymax = max(zip(area_dict.values(), area_dict.keys()))[1]
    return "The area with the most frequent hurricanes is {keymax} with {number} of cases.".format(keymax = keymax, number = area_dict[keymax])

# find most frequently affected area and the number of hurricanes involved in
print(area_affected_most_hurricanes(count_areas_affected(areas_affected)))

# 6
# Calculating the Deadliest Hurricane
def find_highest_death(max_death):
    highest_deaths = 0
    for hurricane, hurricane_death in max_death.items():
        if hurricane_death["Deaths"] > highest_deaths:
            highest_deaths = hurricane_death["Deaths"]
            hurricane_name = hurricane
    return "The hurricane with the highest deaths is {hurricane} with {highest_deaths} deaths".format(hurricane = hurricane_name, highest_deaths= highest_deaths)


# find highest mortality hurricane and the number of deaths
print(find_highest_death(name_with_combined_data))


# 7
# Rating Hurricanes by Mortality
def mortality_scale_rating(name_with_combined_data):
    mortality_scale = {0: [],
                       1: [],
                       2: [],
                       3: [],
                       4: [],
                       5: []}

    for hurricane, hurricane_death in name_with_combined_data.items():
        if hurricane_death["Deaths"] > 10000:
            mortality_scale[5].append(hurricane_death)
        elif 1000 < hurricane_death["Deaths"] <= 10000:
            mortality_scale[4].append(hurricane_death)
        elif 500 < hurricane_death["Deaths"] <= 1000:
            mortality_scale[3].append(hurricane_death)
        elif 100 < hurricane_death["Deaths"] <= 500:
            mortality_scale[2].append(hurricane_death)
        elif 0 < hurricane_death["Deaths"] <= 100:
            mortality_scale[1].append(hurricane_death)
        else:
            mortality_scale[0].append(hurricane_death)

    return mortality_scale

# categorize hurricanes in new dictionary with mortality severity as key

print(mortality_scale_rating(name_with_combined_data)[4])

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(damages,names):
  damage_done = 0
  for num in range(len(damages)):
      if damages[num] == "Damages not recorded":
        continue
      elif damages[num] > damage_done:
        damage_done = damages[num]
        hurricane_name = names[num]

  
  return "The hurricane {hurricane} caused the most damage. It costed {hurricane_damage} dollars".format(hurricane = hurricane_name, hurricane_damage = damage_done)


# find highest damage inducing hurricane and its total cost
print(greatest_damage(convert_M_and_B(damages), names))

# 9
# Rating Hurricanes by Damage

  
def damage_scale_rating(combined_data, damages):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    hurricanes_by_damage = {0: [],
                            1: [],
                            2: [],
                            3: [],
                            4: [],
                            5: []}

    for num in range(len(damages)):
        try:
            if damage_scale[1] >= damages[num] > damage_scale[0]:
                hurricanes_by_damage[1].append(combined_data[num])
            elif damage_scale[2] >= damages[num] > damage_scale[1]:
                hurricanes_by_damage[2].append(combined_data[num])
            elif damage_scale[3] >= damages[num] > damage_scale[2]:
                hurricanes_by_damage[3].append(combined_data[num])
            elif damage_scale[4] >= damages[num] > damage_scale[3]:
                hurricanes_by_damage[4].append(combined_data[num])
            elif damages[num] > damage_scale[4]:
                hurricanes_by_damage[5].append(combined_data[num])
        except TypeError:
            hurricanes_by_damage[0].append(combined_data[num])


    return hurricanes_by_damage

# categorize hurricanes in new dictionary with damage severity as key

print(damage_scale_rating(combined_data_list_dict, convert_M_and_B(damages)))
