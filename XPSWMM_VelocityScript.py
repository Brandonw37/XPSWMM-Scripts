import pandas as pd
import numpy as np
import time as Time 

print("This program....")

while True:
    
    filename = input("Input Excel File Path (.xlsx): ")
    Sheet = input("Input Sheet Name: ")

    df = pd.read_excel(filename, sheet_name =Sheet) #import excel .xlsx file located at same location
    df.as_matrix()

    df['values']=(df.Values.diff(1) !=0).astype('int').cumsum() #categorizes +1 everytime a value changes

    df1=df[df.Values !=0] #creates new dataframe that does not include 0 values from column 'Values'

    df2=df1.groupby(['values'])['cfs2'].mean() #finds mean values in grouped columns from df1

    df3=pd.DataFrame({'BeginDate':df1.groupby('values').Date.first(),
                 'EndDate':df1.groupby('values').Date.last(),
                 'Count':df1.groupby('values').size(),})      
    print(df)
    print(df1)
    print(df2)
    print(df3)
    print("\nDouble Check Results\n")

    while True:
        wait = input('Continue? (y/n) if not, restart or Exit (Press e): ')
        if wait in ('y','n','e'):
            break
        print('invalid input.')
    if wait == ('y'):
        Time.sleep(.300)
    elif wait == ('e'):
        break
    else:   
        print ("Start again")
        continue
    
    Output=input('Output File Location: ')
    Sheet_out=input('sheet name: ')
    df3.to_excel(Output, sheet_name=Sheet_out)
    print("\nGoodbye!")
    break
#df.groupby(['0/1'])['cfs2'].mean()
#pd.cut(df[])
##avg = [(a + b) / 2 for a, b in zip(df[::2],df[1::2])]

