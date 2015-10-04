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
sub2 = sub1.copy()

#Replace 'unknown' (coded as 9) responses with NAN responses  
sub2['S3BD1Q2B'] = sub2['S3BD1Q2B'].replace(9, numpy.nan)
sub2['S3BD2Q2B'] = sub2['S3BD2Q2B'].replace(9, numpy.nan)
sub2['S3BD3Q2B'] = sub2['S3BD3Q2B'].replace(9, numpy.nan)
sub2['S3BD4Q2B'] = sub2['S3BD4Q2B'].replace(9, numpy.nan)
sub2['S3BD5Q2B'] = sub2['S3BD5Q2B'].replace(9, numpy.nan)
sub2['S3BD7Q2B'] = sub2['S3BD7Q2B'].replace(9, numpy.nan)

print("Total Respondents:", len(data))
print("Total Columns:", len(data.columns))
print("Total Current Drug Users:", len(sub1))
print("\n")


income_ranges = """
 0.  $0 (No personal income)
 1.  $1 to $4,999
 2.  $5,000 to $7,999
 3.  $8,000 to $9,999
 4.  $10,000 to $12,999
 5.  $13,000 to $14,999
 6.  $15,000 to $19,999
 7.  $20,000 to $24,999
 8.  $25,000 to $29,999
 9.  $30,000 to $34,999
 10. $35,000 to $39,999
 11. $40,000 to $49,999
 12. $50,000 to $59,999
 13. $60,000 to $69,999
 14. $70,000 to $79,999
 15. $80,000 to $89,999
 16. $90,000 to $99,999
 17. $100,000 or more
 """

#

# Display income_range categories
print("counts for S1Q10B - Total Personal Income in Last 12 Months:")
print("Categorical")
print(income_ranges)
print('\n')

# Display income_ranges of drug users 
c1 = sub2.groupby('S1Q10B').size()
print (c1)
print('\n')

print("frequencies for S1Q10B - Total Personal Income in Last 12")
print("Months: Categorical")
p1 = sub2.groupby('S1Q10B').size() / len(sub1)
print (p1)
print('\n')

print("percentages for S1Q10B - Total Personal Income in Last 12")
print("Months: Categorical")
ct1 = sub2.groupby('S1Q10B').size() * 100 / len(sub1)
print(ct1)
print('\n')

# Display Drug use status of respondents 
print("counts for DGSTATUS - Drug Use Status, Current User=1,")
print("Ex-User=2, 3=Lifetime nondrug user")
c2 = data['DGSTATUS'].value_counts(sort=False)
print (c2)
print('\n')

print("frequencies for DGSTATUS - Drug Use Status, Current User=1,")
print("Ex-User=2, 3=Lifetime nondrug user")
p2 = data['DGSTATUS'].value_counts(sort=False, normalize=True)
print (p2)
print('\n')

# Display drug use by respondents by drug type 
print("counts for S3BD1Q2B - Use of Sedatives 1=In the last 12") 
print("months, 2=Prior to last 12 months,, 3=Both time periods")
c3 = sub2['S3BD1Q2B'].value_counts(sort=False)
print (c3)
print('\n')

print("frequencies for S3BD1Q2B - Use of Sedatives 1=In the last 12") 
print("months, 2=Prior to last 12 months,, 3=Both time periods")
p3 = sub2['S3BD1Q2B'].value_counts(sort=False, normalize=True)
print (p3)
print('\n')

print("counts for S3BD2Q2B - Use of tranquilizers 1=In the last 12") 
print("months, 2=Prior to last 12 months,, 3=Both time periods")
c4 = sub2['S3BD2Q2B'].value_counts(sort=False)
print (c4)
print('\n')

print("frequencies for S3BD2Q2B - Use of tranquilizers 1=In the") 
print("last 12 months, 2=Prior to last 12 months, 3=Both time") 
print("periods")
p4 = sub2['S3BD2Q2B'].value_counts(sort=False, normalize=True)
print (p4)
print('\n')

print("counts for S3BD3Q2B - Use of Opioids 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time") 
print("periods")
c5 = sub2['S3BD3Q2B'].value_counts(sort=False)
print (c5)
print('\n')

print("frequencies for S3BD3Q2B - Use of Opioids 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
p5 = sub2['S3BD3Q2B'].value_counts(sort=False, normalize=True)
print (p5)
print('\n')

print("counts for S3BD4Q2B - Uuse of Amphetimines 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
c6 = sub2['S3BD4Q2B'].value_counts(sort=False)
print (c6)
print('\n')

print("frequencies for S3BD4Q2B - Use of Amphetimines 1=In the last") 
print("12 months, 2=Prior to last 12 months, 3=Both time periods")
p6 = sub2['S3BD4Q2B'].value_counts(sort=False, normalize=True)
print (p6)
print('\n')

print("counts for S3BD5Q2B - Use of Cannabis 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
c7 = sub2['S3BD5Q2B'].value_counts(sort=False)
print (c7)
print('\n')

print("frequencies for S3BD5Q2B - USE OF Cannabis 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
p7 = sub2['S3BD5Q2B'].value_counts(sort=False, normalize=True)
print (p7)
print('\n')

print("counts for S3BD6Q2B - Use of Cocaine or Crack 1=In the last") 
print("12 months, 2=Prior to last 12 months, 3=Both time periods")
c8 = sub2['S3BD6Q2B'].value_counts(sort=False)
print (c8)
print('\n')

print("frequencies for S3BD6Q2B - Use Of Cocaine or Crack 1=In the") 
print("last 12 months, 2=Prior to last 12 months, 3=Both time")
print("periods")
p9 = sub2['S3BD6Q2B'].value_counts(sort=False, normalize=True)
print (p9)
print('\n')

print("counts for S3BD7Q2B - Use of Hallucinogens 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
c10 = sub2['S3BD7Q2B'].value_counts(sort=False)
print (c10)
print('\n')

print("frequencies for S3BD7Q2B - Use of Hallucinogens 1=In the") 
print("last 12 months, 2=Prior to last 12 months, 3=Both time")
print("periods")
p10 = sub2['S3BD7Q2B'].value_counts(sort=False, normalize=True)
print (p10)
print('\n')

print("counts for S3BD8Q2B - Use of Inhalents 1=In the last 12") 
print("months, 2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS")
c11 = sub2['S3BD8Q2B'].value_counts(sort=False)
print (c11)
print('\n')

print("frequencies for S3BD8Q2B - Use of Inhalents 1=In the last 12") 
print("months, 2=PRIOR TO LAST 12 MONTHS, 3=BOTH TIME PERIODS")
p11 = sub2['S3BD8Q2B'].value_counts(sort=False, normalize=True)
print (p11)
print('\n')

print("counts for S3BD9Q2B - Use of Heroin 1=In the last 12 months,") 
print("2=Prior to last 12 months, 3=Both time periods")
c12 = sub2['S3BD9Q2B'].value_counts(sort=False)
print (c12)
print('\n')

print("frequencies for S3BD9Q2B - Use of Heroin 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
p12 = sub2['S3BD9Q2B'].value_counts(sort=False, normalize=True)
print (p12)
print('\n')

print("counts for S3BD10Q2B - Use of Other Drugs 1=In the last 12") 
print("months, 2=Prior to last 12 months, 3=Both time periods")
c13 = sub2['S3BD10Q2B'].value_counts(sort=False)
print (c13)
print('\n')

print("frequencies for S3BD10Q2B - Use of Other Drugs 1=In the last") 
print("12 months, 2=Prior to last 12 months, 3=Both time periods")
p13 = sub2['S3BD10Q2B'].value_counts(sort=False, normalize=True)
print (p13)

