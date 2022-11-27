import numpy as np

def medal_tally(df):
    medals = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally = medals.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    
    medal_tally[['Total','Gold','Silver','Bronze']]=medal_tally[['Total','Gold','Silver','Bronze']].astype('int')
    
    return medal_tally
    
def year_country(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'OverAll')
    
    country=np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'OverAll')
    
    return years,country


def fetch_medal_tally(df,year,country):
    
    flag=0
    
    medals = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport', 'Event','Medal'])
    
    if year == 'OverAll' and country == 'OverAll':
        temp_df = medals
    elif (year !='OverAll') and (country == 'OverAll'):
        temp_df = medals[medals['Year']==int(year)]
    elif (year == 'OverAll') and (country != 'OverAll'):
        flag=1
        temp_df = medals[medals['region']==country]
    elif (year != 'OverAll') and (country != 'OverAll'):
        temp_df = medals[(medals['Year']==int(year)) & (medals['region']==country)]
    
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()    
    else:
        x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']
    
    x[['Total','Gold','Silver','Bronze']]=x[['Total','Gold','Silver','Bronze']].astype('int')
    
    return x