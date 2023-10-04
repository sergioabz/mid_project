My MidBootcamp Project aims to answer the following questions based on exploration and data cleaning: 

1. Which have been the five OECD countries that received the highest inflow of immigrants every year during the last ten years? 

2. Which is the most common profile of the immigrants into the OECD countries considering gender and studies?

3. Which are the top five OECD countries that present the best laboral integration rates according to the educational attainment of the immigrant ?

4. Which are the top 5 OECD countries that have had the highest immigrants outflows  rates?  How are the nationality acquisition rates behaving?

5. Which are the 5 countries with the highest ratio of immigrant population to native population in the OECD? How are the nationality acquisition rates behaving?

Motivation

I am myself a traveler and an immigrant interested in the inflows and outflows of people from one place to the other. I found always fascinating the stories behind people, and how they got to their destination. I expect to clarify some interrogants that I have had for the last few years exploring and cleaning this data bases from the OECD. 

Data Source 

https://stats.oecd.org/Index.aspx#

Challenges

- The years from 2021 to 2022 are not included. It is considered acceptable as statistic data takes time to be consolidated.

- The first challenge I found was the need to use three data bases in order all the questions. I could not find one containing all the relevant information.

- I could not merge or concatenate the three data bases, therefore I had to work with the three separetely in different notebooks. 

- 

Findings

- Germany has become the first destination for immigrants in the last few 8 years. My first thoughts about this are that many refugees are coming to the country given the constant unstability in the Middle East, for instance, the Syrian War. These numbers are going to be greater in 2022 and 2023 considering the Ukraine War and its consequences.

- There are some countries with no outflows of immigrant population data. I found the following clarification in the metadada:

OECD countries seldom have tools specifically designed to measure the inflows and outflows of the foreign population, and national estimates are generally based either on population registers or residence permit data. This note is aimed at describing more systematically what is measured by each of the sources used.

+Flows derived from population registers

Population registers can usually produce inflow and outflow data for both nationals and foreigners. To register, foreigners may have to indicate possession of an appropriate residence and/or work permit valid for at least as long as the minimum registration period. Emigrants are usually identified by a stated intention to leave the country, although the period of (intended) absence is not always specified.

When population registers are used, departures tend to be less well recorded than arrivals. Indeed, the emigrant who plans to return to the host country in the future may be reluctant to inform about his departure to avoid losing rights related to the presence on the register. Registration criteria vary considerably across countries (as the minimum duration of stay for individuals to be defined as immigrants ranges from three months to one year), which poses major problems of international comparison. For example, in some countries, register data cover a portion of temporary migrants, in some cases including asylum seekers when they live in private households (as opposed to reception centres or hostels for immigrants) and international students.

+Flows derived from residence and/or work permits

Statistics on permits are generally based on the number of permits issued during a given period and depend on the types of permits used. The so-called “settlement countries” (Australia, Canada, New Zealand and the United States) consider as immigrants persons who have been granted the right of permanent residence. Statistics on temporary immigrants are also published in this database for these countries since the legal duration of their residence is often similar to long-term migration (over a year). In the case of France, the permits covered are those valid for at least one year (excluding students). Data for Italy and Portugal include temporary migrants.

Another characteristic of permit data is that flows of nationals are not recorded. Some flows of foreigners may also not be recorded, either because the type of permit they hold is not tabulated in the statistics or because they are not required to have a permit (freedom of movement agreements). In addition, permit data do not necessarily reflect physical flows or actual lengths of stay since: i) permits may be issued overseas but individuals may decide not to use them, or delay their arrival; ii) permits may be issued to persons who have in fact been resident in the country for some time, the permit indicating a change of status, or a renewal of the same permit.

Permit data may be influenced by the processing capacity of government agencies. In some instances a large backlog of applications may build up and therefore the true demand for permits may only emerge once backlogs are cleared.

+Flows estimated from specific surveys

Ireland provides estimates based on the results of Quarterly National Household Surveys and other sources such as permit data and asylum applications. These estimates are revised periodically on the basis of census data. Data for the United Kingdom are based on a survey of passengers entering or exiting the country by plane, train or boat (International Passenger Survey). One of the aims of this survey is to estimate the number and characteristics of migrants. The survey is based on a random sample of approximately one out of every 500 passengers. The figures were revised significantly following the latest census in each of these two countries, which seems to indicate that these estimates do not constitute an “ideal” source either. Australia and New Zealand also conduct passenger surveys which enable them to establish the length of stay on the basis of migrants’ stated intentions when they enter or exit the country.

- When it is wanted to count the stock of foreign-population in a country there are two possible ways to undertake the count: taking into consideration the first offspring generation of immigrants, even if they have the citizenship granted as a right, as foreign-born population; and the most common one and easier to understand, foreign population that takes into account only people born outside the borders of the actual country of resindency.