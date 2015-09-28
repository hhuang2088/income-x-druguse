# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:37:32 2015

@author: henryhuang
"""

import pandas 
import numpy

data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

# Convert data responses into numbers 
data['S1Q10B'] = data['S1Q10B'].convert_objects(convert_numeric=True)
data['DGSTATUS'] = data['DGSTATUS'].convert_objects(convert_numeric=True)
data['S3BD1Q2B'] = data['S3BD1Q2B'].convert_objects(convert_numeric=True)
data['S3BD2Q2B'] = data['S3BD2Q2B'].convert_objects(convert_numeric=True)
data['S3BD3Q2B'] = data['S3BD3Q2B'].convert_objects(convert_numeric=True)
data['S3BD4Q2B'] = data['S3BD4Q2B'].convert_objects(convert_numeric=True)
data['S3BD5Q2B'] = data['S3BD5Q2B'].convert_objects(convert_numeric=True)
data['S3BD6Q2B'] = data['S3BD6Q2B'].convert_objects(convert_numeric=True)
data['S3BD7Q2B'] = data['S3BD7Q2B'].convert_objects(convert_numeric=True)
data['S3BD8Q2B'] = data['S3BD8Q2B'].convert_objects(convert_numeric=True)
data['S3BD9Q2B'] = data['S3BD9Q2B'].convert_objects(convert_numeric=True)
data['S3BD10Q2B'] = data['S3BD10Q2B'].convert_objects(convert_numeric=True)

#Subset Current Drug Users 
sub1 = data[(data["DGSTATUS"]==1)]
print("Total Respondents:", len(data))
print("Total Columns:", len(data.columns))
print("Total Current Drug Users:", len(sub1))
print("\n")


income_ranges = """
 0. $0 (No personal income)
 1. $1 to $4,999
 2. $5,000 to $7,999
 3. $8,000 to $9,999
 4. $10,000 to $12,999
 5. $13,000 to $14,999
 6. $15,000 to $19,999
 7. $20,000 to $24,999
 8. $25,000 to $29,999
 9. $30,000 to $34,999
 10. $35,000 to $39,999
 11. $40,000 to $49,999
 12. $50,000 to $59,999
 13. $60,000 to $69,999
 14. $70,000 to $79,999
 15. $80,000 to $89,999
 16. $90,000 to $99,999
 17. $100,000 or more
 """

# Display income_range categories
print("counts for S1Q10B - TOTAL PERSONAL INCOME IN LAST 12 MONTHS: CATEGORY")
print(income_ranges)
print('\n')

# Display income_ranges of drug users 
c1 = sub1.groupby('S1Q10B').size()
print (c1)
print('\n')

print("frequencies for S1Q10B - TOTAL PERSONAL INCOME IN LAST 12 MONTHS: CATEGORY")
p1 = sub1.groupby('S1Q10B').size() / len(sub1)
print (p1)
print('\n')

print("percentages for S1Q10B - TOTAL PERSONAL INCOME IN LAST 12 MONTHS: CATEGORY")
ct1 = sub1.groupby('S1Q10B').size() * 100 / len(sub1)
print(ct1)
print('\n')

# Display Drug use status of respondents 
print("counts for DGSTATUS - Drug Use Status, Current User=1, Ex-User=2")
print("3=Lifetime nondrug user")
c2 = data['DGSTATUS'].value_counts(sort=False)
print (c2)
print('\n')

print("frequencies for DGSTATUS smoked in the past year, Current User=1, Ex-User=2")
print("3=Lifetime nondrug user")
p2 = data['DGSTATUS'].value_counts(sort=False, normalize=True)
print (p2)
print('\n')

# Display drug use by respondents by drug type 
print("counts for S3BD1Q2B - USE OF SEDATIVES 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c3 = sub1['S3BD1Q2B'].value_counts(sort=False)
print (c3)
print('\n')

print("frequencies for S3BD1Q2B - USE OF SEDATIVES 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p3 = sub1['S3BD1Q2B'].value_counts(sort=False, normalize=True)
print (p3)
print('\n')

print("counts for S3BD2Q2B - USE OF TRANQUILIZERS 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c4 = sub1['S3BD2Q2B'].value_counts(sort=False)
print (c4)
print('\n')

print("frequencies for S3BD2Q2B - USE OF TRANQUILIZERS 1=IN THE LAST 12") 
print("MONTHS, 2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p4 = sub1['S3BD2Q2B'].value_counts(sort=False, normalize=True)
print (p4)
print('\n')

print("counts for S3BD3Q2B - USE OF Opioids 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c5 = sub1['S3BD3Q2B'].value_counts(sort=False)
print (c5)
print('\n')

print("frequencies for S3BD3Q2B - USE OF Opioids 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p5 = sub1['S3BD3Q2B'].value_counts(sort=False, normalize=True)
print (p5)
print('\n')

print("counts for S3BD4Q2B - USE OF Amphetimines 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c6 = sub1['S3BD4Q2B'].value_counts(sort=False)
print (c6)
print('\n')

print("frequencies for S3BD4Q2B - USE OF Amphetimines 1=IN THE LAST 12 Months")
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p6 = sub1['S3BD4Q2B'].value_counts(sort=False, normalize=True)
print (p6)
print('\n')

print("counts for S3BD5Q2B - USE OF Cannabis 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c7 = sub1['S3BD5Q2B'].value_counts(sort=False)
print (c7)
print('\n')

print("frequencies for S3BD5Q2B - USE OF Cannabis 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p7 = sub1['S3BD5Q2B'].value_counts(sort=False, normalize=True)
print (p7)
print('\n')

print("counts for S3BD6Q2B - USE OF Cocaine or Crack 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c8 = sub1['S3BD6Q2B'].value_counts(sort=False)
print (c8)
print('\n')

print("frequencies for S3BD6Q2B - USE OF Cocaine or Crack 1=IN THE LAST 12") 
print("MONTHS, 2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p9 = sub1['S3BD6Q2B'].value_counts(sort=False, normalize=True)
print (p9)
print('\n')

print("counts for S3BD7Q2B - USE OF Hallucinogens 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c10 = sub1['S3BD7Q2B'].value_counts(sort=False)
print (c10)
print('\n')

print("frequencies for S3BD7Q2B - USE OF Hallucinogens 1=IN THE LAST 12") 
print("MONTHS, 2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p10 = sub1['S3BD7Q2B'].value_counts(sort=False, normalize=True)
print (p10)
print('\n')

print("counts for S3BD8Q2B - USE OF Inhalents 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c11 = sub1['S3BD8Q2B'].value_counts(sort=False)
print (c11)
print('\n')

print("frequencies for S3BD8Q2B - USE OF Inhalents 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p11 = sub1['S3BD8Q2B'].value_counts(sort=False, normalize=True)
print (p11)
print('\n')

print("counts for S3BD9Q2B - USE OF Heroin 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c12 = sub1['S3BD9Q2B'].value_counts(sort=False)
print (c12)
print('\n')

print("frequencies for S3BD9Q2B - USE OF Heroin 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p12 = sub1['S3BD9Q2B'].value_counts(sort=False, normalize=True)
print (p12)
print('\n')

print("counts for S3BD10Q2B - USE OF OTHER DRUG 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
c13 = sub1['S3BD10Q2B'].value_counts(sort=False)
print (c13)
print('\n')

print("frequencies for S3BD10Q2B - USE OF OTHER DRUG 1=IN THE LAST 12 MONTHS,") 
print("2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS, 9=UNKOWN")
p13 = sub1['S3BD10Q2B'].value_counts(sort=False, normalize=True)
print (p13)




