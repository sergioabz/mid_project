# **ANALYSIS ON IMMIGRATION PROJECT**

## *Motivation*

I am myself a traveler and an immigrant interested in the inflows and outflows of people from one place to the other. I found always fascinating the stories behind people, and how they got to their destination. I expect to clarify some interrogants that I have had for the last few years exploring and cleaning this OECD (Organization for Co-operation and Development) data bases. 

## *Dataset*
The datasets used for this project are  "MIG_NUP_RATES_GENDER_28092023210223162.csv", "MIG_NUP_RATES_GENDER_28092023210223162.csv", "MIG_28092023210139302.csv" , found on https://stats.oecd.org/Index.aspx# theme: Demography and Population.

### **Questions and Answers**

My MidBootcamp Project aims to answer the following questions based on exploration and data cleaning: 

1. Which have been the five OECD countries that received the highest inflow of immigrants during 2010-2020? 

    To understand the overall immigration trends over time, the project explores historical Inflows of foreign population by nationality and visualizes it using appropriate plots 
    in order to identify the five OECD countries.

2. Which are the top 5 OECD countries that have had the highest immigrants outflows rates 2010-2020? 

    To understand the overall immigration trends over time, the project examines historical Outflows of foreign population by nationality and visualizes it using appropriate plots
    in order to identify the five OECD countries.

3. Which are the OECD countries with the highest nationality acquisition rates for the years 2010-2020?

    To understand the overall nationality acquisition rates over time, the project examines historical rates of naturalisation and visualizes it using appropriate plots
    in order to identify the OECD countries.

4. Which are the top five OECD countries that present the best laboral integration rates according to the educational attainment of the immigrant?

    The project examines historical rates of employment and visualizes them using appropriate plots
    in order to identify the five OECD countries.

5. Which are the OECD countires where immigrant women have reached the highest integration rate in the labor market during 2015-2019?

    The project examines historical rates of employment and visualizes them using appropriate plots
    in order to identify the five OECD countries.

## *Challenges*

- The years from 2021 to 2022 are not included. It is considered acceptable as statistic data takes time to be consolidated.

- The first challenge I found was the need to use three data bases in order all the questions. I could not find one containing all the relevant information.

- I could not merge or concatenate the three data bases, therefore I had to work with the three separetely in different notebooks. 

- Modified question: Which is the most common profile of the immigrants into the OECD countries considering gender and studies?
   
- Modified question: Which are the 5 countries with the biggest number of foreign-born and foreign-population to native population in the OECD? How is the ratio to Local population?

### Running the Project
To run this dataset onto my jupyter notebook I used " pd.read_csv ("data/clean/immigration_OECD.csv", "data/clean/immigration_employment_OECD.csv", "data/clean/immigration_education_employment_OECD.csv" encoding="UTF 8 with BOM")".