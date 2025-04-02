import pandas as pd
def demographic_data_analyzer():
    df=pd.read_csv("adults.csv")
    race_count=df['race'].value_counts()
    average_age_men=round(df[df['sex']=='Male']['age'].mean(),1)
    percentage_bachelors=round((df['education']=='Bachelors').mean()*100,1)
    advanced_edu=df['education'].isin(['Bachelors','Masters','Doctorate'])
    higher_edu_rich=round((df[advanced_edu]['salary']=='>50K').mean()*100,1)
    lower_edu_rich=round((df[~advanced_edu]['salary']=='>50K').mean()*100,1)
    min_hours=df['hours-per-week'].min()
    min_hours_workers=df[df['hours-per-week']==min_hours]
    rich_min_workers=round((min_hours_workers['salary']=='>50').mean()*100,1)
    country_salary=df.groupby('native-country')['salary'].value_counts(normalize=true).unstack()
    highest_earning_country=country_salary['>50K'].idxmax()
    highest_earning_percentage=round(country_salary['>50K'].max()*100,1)
    india_rich_jobs=df[(df['native-country']=='India')&(df['salary']=='>50K')]
    top_IN_occupation=india_rich_jobs['occupation'].mode()[0]
     
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_edu_rich': higher_edu_rich,
        'lower_edu_rich': lower_edu_rich,
        'min_hours': min_hours,
        'rich_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_percentage': highest_earning_percentage,
        'top_IN_occupation': top_IN_occupation
    }
if __name__=="__main__":
    results=demographic_data_analyzer()
    for key,value in results.items():
        print(f"{key}:{value}")