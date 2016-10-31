##Purpose: This script processes two data sets from the CIA World Factbook. Two
##independent text files, one for population and one for internet users, are
##merged by country, then a fourth field is added for percentage internet users,
##and finally the percentage of the polulation that uses the internet is
##calculated and input into the new field. This data serves as the basis for my
##leaflet map.
##
##Author: Rachel Cavin
##Date: October 30th, 2016

import argparse
import re

#Gets text file arguments, text files are CIA World Book downloads for country population and internet use.
parser = argparse.ArgumentParser(description = 'Calculates percentage of country populations that use the internet.')
parser.add_argument('--I', help = 'Path to Internet Users Text File')
parser.add_argument('--P', help = 'Path to Population Text File')
args = parser.parse_args()

#Sets text file variables.
int_users_filename = args.I
population_filename = args.P

#Create a function getdata that will read multiple file names to increase reusability.
def getdata(filename, dictionary):
    with open(filename, 'r') as textfile:
        for line in textfile:
            split_data = re.split('  +', line.strip())
            country = split_data[1]
            value = split_data[2]
            if country in dictionary:
                dictionary[country].append(value)
            else:
                dictionary[country] = [value]
    return;
