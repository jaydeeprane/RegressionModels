'''
Created on 15-Oct-2016

@author: JaydeepRane
'''

from numpy import *
import numpy as np
from matplotlib.pyplot import *
import pandas as pd
from scipy import *
from pandas.io.parsers import read_table
import statsmodels.formula.api as smf
import statsmodels.api as sm
from _struct import unpack
from pickle import TRUE

def CoinFlip():
    #Initializing variables
    
    tails=0
    cumulativeSum=[0]*10000
    cumulativeProbability=[0]*10000
    y = [0.5]*10000
    #Simulating 10000 flips
    for i in range(10000):
        coinFlips=random.randint(2)#1 represents tails
        if(coinFlips==1):
            tails=tails+1
            cumulativeSum[i]=tails
            cumulativeProbability[i]=cumulativeSum[i]/(i+1)
        else:
            cumulativeSum[i]=tails
            cumulativeProbability[i]=cumulativeSum[i]/(i+1)
    
    plot(cumulativeProbability)
    plot(y)
    show()     
    


def CLT(distribution,sampleSize,nSamples):
    xbar = [0]*nSamples
    
    if (distribution == "normal" and nSamples>100 and sampleSize<=32 and sampleSize>=28):
        for i in range(nSamples):
            xbar[i]=mean(random.normal(50,10,sampleSize))
     
        title("Distribution of Sample means: ")
        hist(xbar)

        show()
    if (distribution == "uniform" and nSamples>100 and sampleSize<=32 and sampleSize>=28): 
        for i in range(1,nSamples):
            xbar[i]=mean(random.uniform(0,100,sampleSize))
        title("Distribution of Sample means: ")
        hist(xbar)

        show()
            
    if distribution not in ["normal", "uniform"]:
        print("Only normal and uniform distributions are implemented")
    if(nSamples<=100):
        print("Please enter number of samples greater than 100")
    if sampleSize not in (28,29,30,31,32):
        print("Please enter sample size between 28 and 32")  
        

def SLR():
    salesdata=pd.read_csv('hw23R-Advertising.csv')
    salesdataTV=salesdata.TV
    salesdataRadio=salesdata.Radio
    salesdataNewspaper=salesdata.Newspaper
    salesoverall=salesdata.Sales
    
    modtv = polyfit(salesdataTV,salesoverall,1)
    print ("Slope and Intercept for SLR of TV and Sales",modtv)# slope and intercept [ 0.04753664  7.03259355]
    subplot(3, 1, 1)
    title("TV")
    scatter(salesdataTV,salesoverall)
    plot(salesdataTV,polyval(modtv,salesdataTV),'r-')

   
    modradio = polyfit(salesdataRadio,salesoverall,1)
    print("Slope and Intercept for SLR of Radio and Sales",modradio)# slope and intercept [ 0.20249578  9.3116381 ]
    subplot(3, 1, 2)
    title("Radio")
    scatter(salesdataRadio,salesoverall)
    plot(salesdataRadio,polyval(modradio,salesdataRadio),'g-')
    
    modnews = polyfit(salesdataNewspaper,salesoverall,1)
    print("Slope and Intercept for SLR of Newspaper and Sales",modnews)#slope and intercept [  0.0546931   12.35140707]
    subplot(3, 1, 3)
    title("Newspaper")
    scatter(salesdataNewspaper,salesoverall)

    subplots_adjust(hspace=1)
    show()


def MLR():
    salesdata=pd.read_csv('hw23R-Advertising.csv')
    lm = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=salesdata).fit()
    print(lm.summary())
    #coefficient for TV: 0.0458
    #coefficient for Radio: 0.1885
    #coefficient for Newspaper: -0.0010


def LogisticRegression():
    q4data=pd.read_table('hw23R-q4.txt')
    q4data.columns=["Y","X1","X2","X3"]
    q4data['intercept'] = 1.0 #statsmodel function being used requires intercept to be specified explicitly
    predictorCols = q4data.columns[1:]
    logit = sm.Logit(q4data['Y'], q4data[predictorCols])
    result = logit.fit()
    print (result.summary())
    
def LogisticRegressionImproved():
    q4data=pd.read_table('hw23R-q4.txt')
    #Using boxplot to show outliers in the data for independent variables
    title("Box Plot to identify outliers")
    q4data.boxplot()
    show()
    
    #Using method below of eliminating X3 variable due to least correlation with dependent variable
    Y,X1,X2,X3 = np.loadtxt('hw23R-q4.txt', skiprows=1,unpack=TRUE)
    print(corrcoef([Y,X1,X2,X3]))
    df=pd.DataFrame(q4data)
    model="Y~X1+X2" #Eliminating X3 due to least correlation with dependent variable
    print (sm.formula.logit(model, data=df).fit().summary())
   
    #Taking Log of X3
    q4data.columns=["Y","X1","X2","X3"]
    q4data['intercept'] = 1.0 #statsmodel function being used requires intercept to be specified explicitly
    df=pd.DataFrame(q4data)
    modelLog="Y~X1+X2+log(X3)"
    print (sm.formula.logit(modelLog, data=df).fit().summary())

#Q1
CoinFlip()  

#Q2
CLT("normal",30,400)
#CLT("uniform",30,500)
#CLT("exponential",30,400)
#CLT("normal",25,400)
#CLT("normal",30,50)
#CLT("exponential",24,50)

#Q3
SLR()

MLR()

#Q4
LogisticRegression()

#Q5
LogisticRegressionImproved()
