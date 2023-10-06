
import pandas as pd
import numpy as np 

def emp_rate_gender(data: pd.DataFrame, place_of_birth: object, gender: object, year:int=2020) -> pd.DataFrame :

    """"
    This function inputs a data frame, a year from 2000 until 2021, and Gender = 'Women', 'Men'. 
    Depending on Gender, place_of_birth('Native-born', 'Foreign-born') and the year selected the function returns a data frame 
    including the columns = 'Country', 'Gender', 'Rate' always showing the value Employment rate in every row, 'Year', 'Unit' always showing the value Percentage in every row, and 'Value' corresponding to
    every single country included in the data frame called data and its employment rate by gender.

    """
    
    immi = data.copy().set_index('Place of birth')
    immi = immi.loc[[place_of_birth]]
    immi = immi[(immi['Year'] == year) & (immi['Rate'] == 'Employment rate') & (immi['Gender'] == gender)]

    max_immi1 = immi.pivot_table(index=['Country', 'Gender', 'Rate', 'Year'], aggfunc = {'sum'} )
    max_immi1

    max_immi2 = max_immi1.sort_values(by = ('Value', 'sum'), ascending=False).head(10)

    return max_immi2
