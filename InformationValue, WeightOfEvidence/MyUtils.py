import pandas as pd
import numpy as np


def IVandWOE(df):
    """Function that calculates IV value.
    Input - 
    df: dataframe consisting of Number of Good Counts and Number of Bad Counts at column index 2 and 3 respectively
    Output -
    1. Dataframe of values required to calculate IV and WOE.
    2. IV value"""
    df = df.assign(Distribution_Bad =(df.iloc[:,2]/df.iloc[-1][2]))
    df = df.assign(Distribution_Good =(df.iloc[:,3]/df.iloc[-1][3]))
    #Using Lambda Function to form the remaining columns
    df = df.assign(WOE =lambda x:(np.log(x['Distribution_Good']/x['Distribution_Bad'])))
    df = df.assign(IV =lambda x:((x['Distribution_Good'] - x['Distribution_Bad'])*x['WOE']))
    
    #Rounding off till 4 decimals places
    df = df.round(4)   
    #Summing up of individual IV values
    IV = df['IV'].sum(axis=0).round(4)
    print('IV = ')
    return df,IV
    
    

def PSI(df1,df2):
    '''Calculates Population Stability Index (PSI)
    Input -
    df1: Dataframe consisting of account number and score values.
    df2: Dataframe consisting of Expected Percentage values.
    Output -
    1. Dataframe of values required to calculate PSI
    2. PSI value.
    '''
    #Dividing the score into different ranges
    df1['Band']=pd.cut(df1.Score, [0,250, 290, 320, 350,380,410,440,470,520,700], labels=['<250','251–290','291–320','321–350','351–380','381–410','411–440','441–470','471–520','520<']) 
    #Counting the values in each range
    count = df1['Band'].value_counts(dropna=False).sort_index(ascending=True)
    df3 = count.to_frame()
    df3.rename(columns = {'Band':'Band Frequency'}, inplace = True)
    
    #Adding the column of Actual Perrcentage using Lambda Function
    df3 = df3.assign(Actual_Percentage = lambda x:(x/len(df1))*100)
    df2 = df2.set_index(df3.index)
    df3['Expected_Percentage'] = df2

    #Adding the columns using Lambda Function
    df3 = df3.assign(AcExDiff = lambda x:(x['Actual_Percentage'] - x['Expected_Percentage']))
    df3 = df3.assign(lnAcEx = lambda x:(np.log(x['Actual_Percentage']/x['Expected_Percentage'])))
    df3 = df3.assign(Index = lambda x:(x['AcExDiff']*x['lnAcEx'] ))
    
    #Summing up of individual Index values
    PSI = df3['Index'].sum()
    print('PSI = ')
    return df3, PSI
    
    
    

def KS(df):
    '''Calculates Kolmogorov-Smirnov(KS) Statistics
    Input - 
    df: Dataframe consisting of Event and Non Event values at column index 1 and 2 respectively.
    Output - 
    1. Dataframe of values required to calculate KS Stat
    2. KS Stat'''
    
    #Adding the columns using Lambda Function
    df = df.assign(Non_Event_Percent = lambda x: (x['Non-Event']/df.iloc[-1,1])*100)
    df = df.assign(Event_Percent = lambda x: (x['Event']/df.iloc[-1,2])*100)
    df = df.assign(Cum_Per_Event = lambda x: (x['Event_Percent'].cumsum()))
    df = df.assign(Cum_Per_Non_Event = lambda x: (x['Non_Event_Percent'].cumsum()))
    df = df.assign(KS = lambda x: (x['Cum_Per_Event'] - x['Cum_Per_Non_Event']))
    
    #Maximum value of the column KS
    KS = df['KS'].max()
    print('KS = ')
    return df, KS