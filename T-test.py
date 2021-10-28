# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:37:56 2021

@author: ikima
"""

import pandas as pd
diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

##import package for t-test
from scipy.stats import ttest_ind

##Generate list of variable names
list(diabetes)

##Q1.Is there a difference between sex (M:F) and the number of days in hospital?

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

##T-test for Q1
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

##Results of t-test
##P-value = 1.4217299655114968e-21
##T-score = 9.542637042242887

"""The p-value is less than 0.05, 
and the high statistic value 
both indicate that there is a significant difference 
between male and female patients for number of days in hospitals."""

##Q2. Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
Caucasian = diabetes[diabetes['race']=='Caucasian']

##T-test for Q2
ttest_ind(AfricanAmerican['time_in_hospital'], Caucasian['time_in_hospital'])

##Results of t-test
##P-value = 4.178330085585203e-07
##T-score = 5.0610017032095325

"""The p-value is less than 0.05, 
and the high statistic value 
both indicate that there is a significant difference 
between Caucasian and African American patients for number of days in hospitals."""

##Q3.Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?

AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
Asian = diabetes[diabetes['race']=='Asian']

##T-test for Q3
ttest_ind(AfricanAmerican['num_lab_procedures'], Asian['num_lab_procedures'])

##Results of t-test
##P-value = 6.948907528800307e-05
##T-score = 3.9788715315360292

"""The p-value is less than 0.05, 
and the high statistic value 
both indicate that there is a significant difference 
between Asian and African American patients for number of lab procedures performed."""