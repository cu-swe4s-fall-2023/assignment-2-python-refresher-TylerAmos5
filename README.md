[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# A Report on Global Forest Fires
## How to Install
Download the repository from Github using ssh
```
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-TylerAmos5.git
```
Navigate to the src folder
```
cd <path>/assignment-2-python-refresher-TylerAmos5/src
```
# Create a Report
## 1) Write a Query List
Create a new txt file with your desired query values.
Each value should have its own line.
e.g. queries.txt
```
Japan
Canada
Brazil
```

## 2) Run Plot Generation
From the root of the repository, use the Snakefile to create an output folder that contains boxplots of the requested data
```
snakemake -c 1
```

# Running Scripts Individually
## How to run print_fires.py
Modify run.sh to set the parameters to query the csv appropriate for your interest
The --operation parameter is optional. Specify the statistic you would like to calculate.
If no --operation parameter is given, a list of integers will be returned.
```
python3 print_fires.py --file_name=<file_name>.csv \
                       --query_column=<column_index> \
                       --query_value="Specific value to match in query column" \
                       --result_column=<column_index>
                       --operation=[mean,median,stdv]
```
## Example
```
python3 print_fires.py --file_name=Agrofood_co2_emission.csv \
                       --query_column=0 --query_value="United States of America" \
                       --result_column=3 --operation=stdv
```
## Testing Instructions
Functional and unit tests are run through github via github actions. See .github/workflows/Tests.yml to see setup. 
As of 10/11/23, all continuous integration tests work when any branch is pushed to github. 

## my_utils.py
**Contains the function get_column, which can returns corresponding values from a queried column and value of interest.**
## print_fires.py
**Reads in command line arguments and runs the main function to report data from the csv file provided**
## run.sh
**Contains 3 test cases to show the functionality of print_fires.**
1. Runs correctly, reporting forrest fires for the United States of America.
2. Produces a FileNotFound exception since the csv file is spelled incorrectly
3. Produces an Exception since values that aren't numbers can't by typecasted to floats or ints.




## Notes from development
### HW2 (9/13): 
Completed get_columns function to return specified values that correspond to queried column and value.
Updated print_fires.py to use get_column correctly from my_utils.
Ensured my_utils.py only runs if main and that all python code satisfies pycodestyle. 
Changed results_column param in get_column to be a named parameter that defaults to 1. 
Created run.sh to execute print_fires.py.

### HW3 (9/26):
Added try except blocks to get_columns function to handle file and type casting errors
print_fires now takes named command line arguments using argparse.
Test cases were added to run.sh.

### HW4 (10/4):
Added statistical calculations to my_utils.
Mean, median, and standard deviation can be calculated for the result column
Added unit and functional tests
print_fires now takes an optional operation parameter that can calculate statistics about the result column. 

## HW5 (10/11):
implemented continuous integration with Tests.yml.

## HW5 (10/17)
# A Comparison of Countries' Forest Fires
## Question
Are there more forest fires in developed countries or undeveloped countries? 

## Approach
Compare volume of forest fires between two developed countries: 
- United States
- Canada

Against forest fires in two underdeveloped countries:
- Rwanda
- Somalia

## Results
### Developed Countries
![Canada Fires](/output/Canada.png)
![US Fires](/output/United%20States%20of%20America.png)
### Underdeveloped Countries
![Rwanada Fires](/output/Rwanda.png)
![Somalia Fires](/output/Somalia.png)
### Interpretation
This data suggests that there are more forest fires in developed countries compared to underdeveloped countries. 
However, there are many limitations to this study, such as a lack of consideration of climate and country size.

## Methods
1) Read in data
2) Pull amount of forest fires reported for the queried country
3) Generate a boxplot showing the mean and spread of the forest fires that have occured annually in the queried country from 1990-2020
4) Compare statistics between developed and underdeveloped countries. 


