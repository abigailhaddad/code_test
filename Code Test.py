# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:10:45 2018
Code Test
@author: abhaddad
"""
import os, pandas as pd, numpy as np

def setup(Directory, filename, tab1, tab2):
    os.chdir(Directory)
    xls = pd.ExcelFile(filename)
    df1 = pd.read_excel(xls, tab1)
    df2 = pd.read_excel(xls, tab2)
    return(df1, df2);

def task_1(df1, df2, variable):
    df3=df1.merge(df2, left_on=variable, right_on=variable, how="inner")
    return(df3)
    
def task_2(df, variable, subset):
    df2=df.loc[df[variable]==subset]
    return(df2)

def task_3(df, height, weight):
    df['BMI']=(df[weight] / (df[height]/2.54) / (df[height]/2.54) * 703)
    df['BMI']=pd.to_numeric(df['BMI'], errors='coerce')
    return(df)
    
def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_


def task_4(df):
    df=df.dropna()
    df2=pd.DataFrame()
    df2['Count']=df[['BP', 'BMI']].groupby('BP').count()['BMI']
    df2['Mean']=df[['BP', 'BMI']].groupby('BP').mean()['BMI']
    df2['15th']=df[['BP', 'BMI']].groupby('BP').agg([percentile(15)])
    df2['85th']=df[['BP', 'BMI']].groupby('BP').agg([percentile(85)])
    return(df2)
    
def task5a(df):
    plot1=dat3.plot.scatter("Weight", "BMI")
    return(plot1)
    
def task5b(df):
    df['Height']=pd.to_numeric(df['Height'], errors='coerce')
    plot1=dat3.plot.scatter("Height", "BMI")
    return(plot1)
    


print("Part 1")
    
setup_results=setup(r"C:\Users\abhaddad\Documents\NCQA", "NCQA Analysis Test Data.xlsx", "people", "health")
people=setup_results[0]
health=setup_results[1]

dat1=task_1(people, health, ["IDs", "State"])
dat1.to_excel("dat1.xlsx")

dat2=task_2(dat1, "State", "A")
dat2.to_excel("dat2.xlsx")

dat3=task_3(dat2, "Height", "Weight")
dat3.to_excel("dat3.xlsx")

dat4=task_4(dat3)
dat4.to_excel("dat4.xlsx")

fig=(task5a(dat3)).get_figure()
fig.savefig("Task5a.png")


fig=(task5b(dat3)).get_figure()
fig.savefig("Task5b.png")
