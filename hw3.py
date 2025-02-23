import data

# Part 1

# This function, when given a list of county demographics objects (type list[CountyDemographics]), will return the total
# 2024 population across the set of counties in the input list.

def population_total(county_lst:list[data.CountyDemographics]) -> int:
    total_pop = 0
    for county in county_lst:
        total_pop += county.population["2014 Population"]
    return total_pop


# Part 2

# This function, when given a list of county demographics objects (type list[CountyDemographics]) and a two-letter state
# abbreviation (type str), will return a list of county demographics objects from the input list that are within the
# specified state. If the input state does not exist in the list, it will return an empty list.

def filter_by_state(county_lst:list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:

    new_county_lst = []
    for county in county_lst:
        if state == county.state:
            new_county_lst.append(county)
    return new_county_lst


# Part 3

# This function, when given a list of county demographics objects (type list[CountyDemographics]) and an education key
# of interest (type str), will return the total 2014 population for the specified key of interest. If the input key does
# not exist, it will return 0.

def population_by_education(county_lst:list[data.CountyDemographics], edu_interest:str) -> float:
    edu_population = 0.0

    for county in county_lst:
        if edu_interest in county.education:
            local_edu_pop = (county.education[edu_interest] / 100 ) * county.population["2014 Population"]
            edu_population += local_edu_pop
    return edu_population

# This function, when given a list of county demographics objects (type list[CountyDemographics]) and an ethnicity key
# of interest (type str), will return the total 2014 population for the specified key of interest. If the input key does
# not exist, it will return 0.

def population_by_ethnicity(county_lst:list[data.CountyDemographics], ethn_interest:str) -> float:
    ethn_population = 0.0

    for county in county_lst:
        if ethn_interest in county.ethnicities:
            local_ethn_pop = (county.ethnicities[ethn_interest] / 100 ) * county.population["2014 Population"]
            ethn_population += local_ethn_pop
    return ethn_population

# This function, when given a list of county demographics objects (type list[CountyDemographics]), will return the total
# 2014 population for the income key 'Persons Below Poverty Level'.

def population_below_poverty_level(county_lst:list[data.CountyDemographics]) -> float:
    total_pop = 0
    for county in county_lst:
        local_pop = (county.income['Persons Below Poverty Level'] / 100 ) * county.population["2014 Population"]
        total_pop += local_pop
    return total_pop


# Part 4

# This function, when given a list of county demographics objects (type list[CountyDemographics]) and an education key
# of interest (type str), will return the total 2014 population for the specified key of interest as a percentage of the
# total 2024 population. If the input key does not exist, it will return 0.

def percent_by_education(county_lst:list[data.CountyDemographics], edu_interest:str) -> float:
    for county in county_lst:
        if edu_interest not in county.education:
            return 0
    edu_pop = population_by_education(county_lst, edu_interest)
    return (edu_pop / population_total(county_lst)) * 100

# This function, when given a list of county demographics objects (type list[CountyDemographics]) and an ethnicity key
# of interest (type str), will return the total 2014 population for the specified key of interest as a percentage of the
# total 2024 population. If the input key does not exist, it will return 0.

def percent_by_ethnicity(county_lst:list[data.CountyDemographics], ethn_interest:str) -> float:
    for county in county_lst:
        if ethn_interest not in county.ethnicities:
            return 0
    ethn_pop = population_by_ethnicity(county_lst, ethn_interest)
    return (ethn_pop / population_total(county_lst)) * 100

# This function, when given a list of county demographics objects (type list[CountyDemographics]), will return the total
# 2014 population for the income key 'Persons Below Poverty Level' as a percentage of the total 2024 population.

def percent_below_poverty_level(county_lst:list[data.CountyDemographics]) -> float:
    if len(county_lst) == 0:
        return 0
    poverty_pop = population_below_poverty_level(county_lst)
    return (poverty_pop / population_total(county_lst)) * 100


# Part 5

# This function, when given a list of county demographics objects (type list[CountyDemographics]), an education key of
# interest (type str), and a percent threshold (type float), will return a list of all county demographics objects for
# which the value for the specified key is greater than the specified threshold value.

def education_greater_than(county_lst:list[data.CountyDemographics], edu_interest:str, percent_threshold:float) \
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if edu_interest in county.education:
            if county.education[edu_interest] > percent_threshold:
                new_lst.append(county)
    return new_lst

# This function, when given a list of county demographics objects (type list[CountyDemographics]), an education key of
# interest (type str), and a percent threshold (type float), will return a list of all county demographics objects for
# which the value for the specified key is less than the specified threshold value.

def education_less_than(county_lst:list[data.CountyDemographics], edu_interest:str, percent_threshold:float) \
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if edu_interest in county.education:
            if county.education[edu_interest] < percent_threshold:
                new_lst.append(county)
    return new_lst

# This function, when given a list of county demographics objects (type list[CountyDemographics]), an ethnicity key of
# interest (type str), and a percent threshold (type float), will return a list of all county demographics objects for
# which the value for the specified key is greater than the specified threshold value.

def ethnicity_greater_than(county_lst:list[data.CountyDemographics], ethn_interest:str, percent_threshold:float)\
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if ethn_interest in county.ethnicities:
            if county.ethnicities[ethn_interest] > percent_threshold:
                new_lst.append(county)
    return new_lst

# This function, when given a list of county demographics objects (type list[CountyDemographics]), an ethnicity key of
# interest (type str), and a percent threshold (type float), will return a list of all county demographics objects for
# which the value for the specified key is less than the specified threshold value.

def ethnicity_less_than(county_lst: list[data.CountyDemographics], ethn_interest: str, percent_threshold: float)\
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if ethn_interest in county.ethnicities:
            if county.ethnicities[ethn_interest] < percent_threshold:
                new_lst.append(county)
    return new_lst

# This function, when given a list of county demographics objects (type list[CountyDemographics]), and a percent
# threshold (type float), will return a list of all county demographics objects for which the value for key
# 'Persons Below Poverty Level' is greater than the specified threshold value.

def below_poverty_level_greater_than(county_lst:list[data.CountyDemographics], percent_threshold:float)\
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if county.income['Persons Below Poverty Level'] >  percent_threshold:
                new_lst.append(county)
    return new_lst

# This function, when given a list of county demographics objects (type list[CountyDemographics]), and a percent
# threshold (type float), will return a list of all county demographics objects for which the value for key
# 'Persons Below Poverty Level' is less than the specified threshold value.

def below_poverty_level_less_than(county_lst:list[data.CountyDemographics], percent_threshold:float)\
        -> list[data.CountyDemographics]:

    new_lst = []

    for county in county_lst:
        if county.income['Persons Below Poverty Level'] <  percent_threshold:
                new_lst.append(county)
    return new_lst