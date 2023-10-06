
import pandas as pd
import numpy as np 

def emp_rate_edu (data: pd.DataFrame, place_of_birth: object, Educational_attainment : object,  year: int= 2019)-> pd.DataFrame:

    """"
    This function inputs a data frame, a year from 2015 until 2019, and Educational_attainment = 'Low', 'Medium', 'High'. 
    Depending on the place_of_birth('Native-born', 'Foreign-born'), Educational_attainment and the year selected the function returns a data frame 
    including the columns = 'Country', 'Educational_attainment', 'Year', 'Unit' always showing the value Percentage in every row, and 'Value' corresponding to
    every single country included in the data frame called data.

    """

    immi = data.copy().set_index('Place of birth')
    immi = immi.loc[[place_of_birth]]
    immi = immi[(immi['Educational attainment'] == Educational_attainment) & (immi['Year'] == year)]

    max_immi1 = immi.pivot_table(index=['Country', 'Educational attainment', 'Year'], aggfunc = {'sum'} )

            

    max_immi2 = max_immi1.sort_values(by = ('Value', 'sum'), ascending=False).head(20)
    
   
    return max_immi2
