import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df =  pd.read_csv('adult.data.csv')

    df.head()
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count().sort_values(ascending=False)

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male'].mean().iloc[0], 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,15]
    school = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(school)]
    lower_education = df[df['education-num'].isin(edu_num)]
    # percentage with salary >50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] ) * 100, 1)

    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    #is a number
    min_work = df['hours-per-week']
    min_work_hours = min_work.min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    #is a db that creates a mask of ppl who work min hrs
    num_min_workers = df[min_work == min_work_hours]

    #is a db of min workers with >50k salary
    rich_df = num_min_workers['salary'] == '>50K'
   
    #is a percentage that creates mask of min workers
    rich_percentage = (num_min_workers[rich_df].shape[0] / num_min_workers.shape[0]) * 100
   
    # What country has the highest percentage of people that earn >50K?

    #array of total # ppl per country
    ab = df[['native-country', 'salary']]
    country_pop = ab.groupby(['native-country'], as_index = True).count()
    
    #array of total # rich ppl per country
    rich = ab['salary'] == '>50K'
    highest_earning = ab[rich].groupby(['native-country'], as_index = True).count()


    #find ratios and compare...
    final = (highest_earning / country_pop) * 100
    final.sort_values(by=['salary'], inplace = True, ascending = False)
    #display final result
    highest_earning_country = final.index[0]
    highest_earning_country_percentage = round(final.iloc[0]['salary'], 1)



    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')].groupby('occupation')['occupation'].count().sort_values(ascending=False).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
       print("Number of each race:\n", race_count) 
       print("Average age of men:", average_age_men)
       print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
       print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
       print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
       print(f"Min work time: {min_work_hours} hours/week")
       print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
       print("Country with highest percentage of rich:", highest_earning_country)
       print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
       print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
