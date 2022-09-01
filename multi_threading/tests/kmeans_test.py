def main():

    ## Initialisation

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import math


    df=pd.read_csv('sampledata.csv')
    #print(df1)

    a=df.iloc[0]
    b=df.iloc[1]
    c=df.iloc[2]
    d=df.iloc[3]
    e=df.iloc[4]
    f=df.iloc[5]
    g=df.iloc[6]
    h=df.iloc[7]
    i=df.iloc[8]

    l1=list(a[2:])
    l2=list(b[2:])
    l3=list(c[2:])
    l4=list(d[2:])
    l5=list(e[2:])
    l6=list(f[2:])
    l7=list(g[2:])
    l8=list(h[2:])
    l=list(i[2:])

    #dict={l1:df.iloc[0][0:1],l2:df.iloc[1][0:1],l3:df.iloc[2][0:1],l4:df.iloc[3][0:1],l5:df.iloc[4][0:1],l6:df.iloc[5][0:1],l7:df.iloc[6][0:1],l8:df.iloc[7][0:1]}


    def diff(x,xp):
        return math.sqrt((x-xp)**2)

    def values(l,test):
        a=[]
        for i in range(0,len(l)):
            a.append(diff(l[i],test[i]))
        return a


    ideal=[250,90,7.7,95,2,1.5]

    t1=values(l1,ideal)
    t2=values(l2,ideal)
    t3=values(l3,ideal)
    t4=values(l4,ideal)
    t5=values(l5,ideal)
    t6=values(l6,ideal)
    t7=values(l7,ideal)
    t8=values(l8,ideal)

    #print(t1,t2,t3,t4,t5,t6,t7,t8)

    '''def result(t,o):
        if (t[0]!=10.0 and t[1]!=10.0 and t[2]!=0.0 and t[3]!=0.0 and t[4]!=11.0 and t[5]!=0.5):
            print("extreme conditions, coordinates are")

            print(o[0:2].to_string())
            print("\n")

        else:
            print("normal conditions\n")'''

    def result(t,o):
        if (t[0]!=10.0 and t[1]!=10.0 and t[2]!=0.0 and t[3]!=0.0 and t[4]!=11.0 and t[5]!=0.5):
            return("extreme conditions, coordinates are",  o[0:2].to_string())
        else:
            return("normal conditions ")

   
    d1=result(t1,a)
    d2=result(t2,b)
    d3=result(t3,c)
    d4=result(t4,d)

    #print(a[0:2].to_string())

    dat=open("data.txt",'w')
    dat.write(str(d1))
    dat.write(str(d2))
    dat.write(str(d3))
    dat.write(str(d4))
    





        


