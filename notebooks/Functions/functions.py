
import pandas as pd
import numpy as np

def top_5(data: pd.DataFrame, variable: str, year: int=2010)-> pd.DataFrame:

    """"
    This function inputs a data frame, a year from 2010 until 20121, and variable = 'Inflows of foreign population by nationality', 'Acquisition of nationality by country of former nationality',
    'Stock of foreign population by nationality', 'Outflows of foreign population by nationality', 'Stock of foreign-born population by country of birth'    
    Depending on Gender and the year selected the function returns a data frame 
    including the columns = 'Country', 'Year', and 'Value' corresponding to
    every single country included in the data frame  and its total number of immigrants per year.

    """

    immi = data.copy().set_index('Variable')
    immi = immi.loc[[variable]]
    immi = immi[immi['Year'] == year]

       

    max_immi1 = immi[[ 'Country', 'Year', 'Value']].pivot_table(index=[ 'Country', 'Year'], aggfunc = {'sum'} )
            

    max_immi2 = max_immi1.sort_values(by = ('Value', 'sum'), ascending=False).iloc[0:5]
    max_immi2

    

    return max_immi2
