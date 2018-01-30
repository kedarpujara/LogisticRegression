import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import cufflinks as cf


def LogisticReg():

	titTrain = pd.read_csv("titanic_train.csv")

	titTrain.head()

	#Line below is used to show which data we are missing
	#sns.heatmap(titTrain.isnull(), yticklabels=False, cbar=False,cmap='viridis')

	
	sns.set_style('whitegrid')
	#sns.countplot(x='Survived', hue='Sex', data=titTrain) # Categorize by sex
	#sns.countplot(x='Survived', hue='Pclass', data=titTrain) # Categorize by passenger class
	#sns.distplot(titTrain['Age'].dropna(),kde=False,bins=30)

	#titTrain['Age'].hist(bins=30,color='darkred',alpha=0.7)
	#titTrain['Fare'].hist(bins=40,figsize=(8,4))


	cf.go_offline()
	titTrain['Fare'].iplot(kind='hist',bins=30)

	plt.show()



LogisticReg()


