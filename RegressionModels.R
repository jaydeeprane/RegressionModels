SLR<-function(path){
  salesdata <- read.csv(path)
  salesdataTV.lm<-lm(Sales~TV,data=salesdata)
  plot(salesdata$TV,salesdata$Sales,xlab = "Sales figures for TV",ylab = "Overall Sales",main = "Simple Linear Regression for TV")
  abline(salesdataTV.lm)
  print(summary(salesdataTV.lm))
  #Residual standard error: 3.259 on 198 degrees of freedom
  
  salesdataRadio.lm<-lm(Sales~Radio,data=salesdata)
  plot(salesdata$Radio,salesdata$Sales,xlab = "Sales figures for Radio",ylab = "Overall Sales",main = "Simple Linear Regression for Radio")
  abline(salesdataRadio.lm)
  print(summary(salesdataRadio.lm))
  #Residual standard error: 4.275 on 198 degrees of freedom
  
  salesdataNewspaper.lm<-lm(Sales~Newspaper,data=salesdata)
  plot(salesdata$Newspaper,salesdata$Sales,xlab = "Sales figures for Newspaper",ylab = "Overall Sales",main = "Simple Linear Regression for Newspaper")
  abline(salesdataNewspaper.lm)
  print(summary(salesdataNewspaper.lm))
  #Residual standard error: 5.092 on 198 degrees of freedom
  
}

MLR<-function(path){
  salesdata <- read.csv(path)
  salesdataoverall.lm<-lm(Sales~TV+Radio+Newspaper,data=salesdata)
  summary(salesdataoverall.lm)#to find difference in B values
  print(salesdataoverall.lm)
}

LogisticRegression<-function(path){
  q4data <- read.table(path,header = TRUE)
  glm(Y~X1+X2+X3,family = binomial,data = q4data)
  
}

LogisticRegressionImproved<-function(path){
  q4data <- read.table(path,header = TRUE)
  #Taking log of only X3 as X1 and X2 have negative values
  original<-glm(Y~X1+X2+X3,family = binomial,data = q4data)
  improved1<-glm(Y~X1+X2+log(X3),family = binomial,data = q4data) 
  print(anova(original,improved1))
  
  
  #This shows least correlation between X3 and Y therefore we remove it from the equation
  print("Corrleation matrix to determine independent variable with least correlation")
  print(cor(q4data))
  improved2<-glm(Y~X1+X2,family = binomial,data = q4data)
  print(improved2)
  
  #For displaying outliers
  boxplot(q4data)
}

