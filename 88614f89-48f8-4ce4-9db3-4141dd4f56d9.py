#!/usr/bin/env python
# coding: utf-8

# ## Review (2)
# 
# Now the final conclusion is better so I can accept your work. Please keep in mind my recommendations for your future projects. Good luck.
# 
# ---Thank you, Yes i will have an eye on those recommendation for next projects.

# ## Review
# 
# Hi Sindhu! My name is Soslan. I'm reviewing your work. I've added all my comments to new cells with the title "Review". Sorry for the delay in review.
# 
# ```diff
# + If you did something great I'm using green color for my comment
# - If the topic requires some extra work so I can accept it then the color will be red.
# ```
# 
# Technically you did the project correctly. I leaved you just one comment to finish. Please, take more care of the decoration of your notebooks in the future. It is important to hold all the content except code in `markdown` cells. It improves the overall impression of the project.

# ## Analyzing borrowers’ risk of defaulting
# 
# Your project is to prepare a report for a bank’s loan division. You’ll need to find out if a customer’s marital status and number of children has an impact on whether they will default on a loan. The bank already has some data on customers’ credit worthiness.
# 
# Your report will be considered when building a **credit scoring** of a potential customer. A ** credit scoring ** is used to evaluate the ability of a potential borrower to repay their loan.

# ### Step 1. Open the data file and have a look at the general information. 

# In[2]:


import pandas as pd
read = pd.read_csv('/datasets/credit_scoring_eng.csv')


# In[3]:


print(read.info())


# ### Conclusion

# In[4]:


#Using info() i have gone through general information of file and datatypes of each column, which has float, int and object datatypes and 12 columns with 21525 rows


# I have read the csv file and went through the columns, datatypes and total entries in the table.

# ## Review
# 
# ```diff
# + Data was read correctly
# ```
# You can also use other methods:  `.head()`, `.describe()` to analyze data. Please use `Markdown` cells for your comments

# ### Step 2. Data preprocessing

# ### Processing missing values

# In[5]:


import pandas as pd
read = pd.read_csv('/datasets/credit_scoring_eng.csv')
null_values_count = pd.DataFrame(read, columns = ['children' , 'days_employed', 'dob_years' , 'education', 'education_id', 'family_status', 'family_status_id', 'gender', 'income_type', 'debt', 'total_income', 'purpose'])
print(null_values_count.isnull().sum())


# In[6]:


read['total_income']=read['total_income'].fillna('0')
read['days_employed']=read['days_employed'].fillna('0')
empty_values_check = pd.DataFrame(read, columns = ['days_employed', 'total_income'])
print(empty_values_check.isnull().sum())

I have used isnull() to check the null values in each column. 
I have used fillna() to replace the null values with 0 values.(The days_employed column has negative values, so i have replaced with 0 for empty values.)
I have checked the columns for null values after replacing the value with isnull().
# #used isnull().sum() method to check for null values in all columns.

# ## Review
# 
# ```diff
# + You find and fill NaNs correctly
# ```
# 
# You don't need to import pandas and read data again in this section. It is enough to do it once in the notebook.

# ### Data type replacement

# In[70]:


import pandas as pd
read = pd.read_csv('/datasets/credit_scoring_eng.csv')
read['days_employed']=read['days_employed'].fillna('0')
read['days_employed'] = read['days_employed'].astype('int')
read['debt'] = read['debt'].astype('bool')
print(read.info())


# In[113]:


read['children'] = read['children'].apply(abs)
print(read['children'].value_counts())
read['days_employed'] = read['days_employed'].apply(abs)
print(read['days_employed'].value_counts()) 
negative_values = dict(filter(lambda x: x[1] < 0, read['days_employed'].items()))
print(read['days_employed'].isnull().sum())


# ### Conclusion

# #Days cant be float datatype, so changed to int datatype using astype(int).
# #Debt column has boolean values, so changed to bool datatype using astype(bool).
# #Using abs function i am changing all the negative values to positive. Negative values might be a technical error while loading #data. So i am chaning them to positive for further analysis. 
# #Using filter(lambda x:) i am checking if there are any negative values still.
# #Using isnull().sum() to check the null values count.

# ### Processing duplicates

# In[27]:


lower = read['education'].str.lower()


# In[40]:


print(read.duplicated().sum())
read = read.drop_duplicates()
read = read.dropna().reset_index(drop=True)
print(read.duplicated().sum())


# In[181]:


loan_repayment = read['debt'].value_counts()
print(loan_repayment)    


# # used str.lower() to change the uppercase to lowercase for rows in education column before checking for duplicates.

# #checking for duplicates count using duplicated() and sum()
# # deleting duplicates using drop_duplicates()

# #reset_index(drop=True) to reset the indices. and ensuring again by checking for duplicates if there is any.

# ## Review
# 
# ```diff
# + Mostly done good.
# ```
# 
# You can look one more time to the `days_employed` column to find out what negative number can mean.

# ### Categorizing Data

# In[167]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
read = pd.read_csv('/datasets/credit_scoring_eng.csv')
from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')
purpose_categorization = read['purpose']
for row in purpose_categorization:
    def purpose_new(row):
        stemmed_word = [english_stemmer.stem(word) for word in row.split(' ')]
        if 'hous' in stemmed_word:
            return 'housing'
        if 'car' in stemmed_word:
            return 'cars'
        if 'educ' in stemmed_word:
            return 'education'
        if 'wed' in stemmed_word:
            return 'wedding'
        if 'estat' in stemmed_word:
            return 'realestate'
        if 'properti' in stemmed_word:
            return 'housing'
        return 'other'
    print(purpose_new(row))
    
read['purpose_new'] = read['purpose'].apply(purpose_new)
print(read['purpose_new'].value_counts())


# In[18]:


def age_group(age):
    if age <= 18:
        return 'child'
    if age <= 40:
        return 'adult'
    if age <= 60:
        return 'about to retire'
    return 'retired'
read['age_group'] = read['dob_years'].apply(age_group)
print(read['age_group'].value_counts())
    
        


# In[17]:


def children_cat(number):
    if number >= 1:
        return 'kids'
    return 'no kids'
read['children_cat'] = read['children'].apply(children_cat)
print(read['children_cat'].value_counts())


# In[134]:


def defaulted(loan):
    if loan == 0:
        return 'not_defaulted'
    if loan == 1:
        return 'defaulted'
read['defaulted'] = read['debt'].apply(defaulted)    
print(read['defaulted'].value_counts())


# In[151]:


def income_total(salary):
    if salary >= 2947.572 and salary <= 75144.739:
        return 'basic'
    if salary >= 75144.739 and salary <= 146982.715:
        return 'middle'
    if salary >= 146982.715 and salary <= 218820.692:
        return 'normal'
    if salary >= 218820.692 and salary <= 290658.668:
        return 'high'
    if salary >= 290658.668 and salary <= 362496.645:
        return 'higher'
    return 'other'
read['income_total'] = read['total_income'].apply(income_total)
print(read['income_total'].value_counts())
    


# ### Conclusion

# In[ ]:


# I have used stemming method to find the root word for each row in purpose column.
#Categorized purpose column by writing a function.
#Added a new column in main data table with the categorization.
#Output unique values in purpose column.
#Categorized age into 4 by writing a condition, created a new column, output the unique values using value_counts()
#Categorized children column to kids and no kids by writing a function.
#Categorized debt column to defaulted /not defaulted
#categorized income column.


# 

# ## Review
# 
# Good conclusion but please use markdown cells for non-code content.

# ### Step 3. Answer these questions

# - Is there a relation between having kids and repaying a loan on time?

# In[220]:


def children_cat(number):
    if number >= 1:
        return 'kids'
    return 'no kids'
read['children_cat'] = read['children'].apply(children_cat)
print(read['children_cat'].value_counts())
read.groupby(['children_cat'])['debt'].agg(['count','mean'])


# ### Conclusion

# #I have categorized children column into categories as kids and no-kids. I have used groupby method to find out the mean values based on the categories and debt values.
# 
# People with kids are slightly more likely to pay the loan ontime. 
# 
# People with kids are 9.2%
# People with no kids are 7.4%

# - Is there a relation between marital status and repaying a loan on time?

# In[231]:


print(read['family_status'].value_counts())
def marital_status(status):
    if status == 'married':
        return 'married'
    if status == 'civil partnership':
        return 'civil'
    if status == 'unmarried':
        return 'unmarried'
    if status == 'divorced':
        return 'divorced'
    return 'widow'
read['marital_status'] = read['family_status'].apply(marital_status)
print(read['marital_status'].value_counts())
analyse = read.groupby(['marital_status'])['debt'].agg(['count','mean'])
print(analyse.sort_values(by='mean',ascending=True))



# ### Conclusion

# # People who are unmarried are more likely to pay the loan ontime with 9.7%, whereas the marital status with widow are less likely to the pay the loan ontime with 6.5%, and those who are married are in average to pay the loan ontime with 7.5%.

# - Is there a relation between income level and repaying a loan on time?

# In[234]:


negative_values = dict(filter(lambda x: x[1]<0, read['total_income'].items()))
def income_total(salary):
    if salary >= 2947.572 and salary <= 75144.739:
        return 'basic'
    if salary >= 75144.739 and salary <= 146982.715:
        return 'middle'
    if salary >= 146982.715 and salary <= 218820.692:
        return 'normal'
    if salary >= 218820.692 and salary <= 290658.668:
        return 'high'
    if salary >= 290658.668 and salary <= 362496.645:
        return 'higher'
    return 'other'
read['income_total'] = read['total_income'].apply(income_total)
print(read['income_total'].value_counts())
income = read.groupby(['income_total'])['debt'].agg(['count','mean'])
print(income.sort_values(by='mean',ascending=True))


# ### Conclusion

# # People with higher salary income are more likely to pay the loan ontime with 50%, and people with high salary income are very less likely to pay the loan ontime. 

# - How do different loan purposes affect on-time repayment of the loan?

# In[237]:


import pandas as pd
read = pd.read_csv('/datasets/credit_scoring_eng.csv')
from nltk.stem import SnowballStemmer
english_stemmer = SnowballStemmer('english')
purpose_categorization = read['purpose']
for row in purpose_categorization:
    def purpose_new(row):
        stemmed_word = [english_stemmer.stem(word) for word in row.split(' ')]
        if 'hous' in stemmed_word:
            return 'housing'
        if 'car' in stemmed_word:
            return 'cars'
        if 'educ' in stemmed_word:
            return 'education'
        if 'wed' in stemmed_word:
            return 'wedding'
        if 'estat' in stemmed_word:
            return 'realestate'
        if 'properti' in stemmed_word:
            return 'housing'
        return 'other'
        
read['purpose_new'] = read['purpose'].apply(purpose_new)
print(read['purpose_new'].value_counts())
debt_loan = read.groupby(['purpose_new'])['debt'].agg(['count','mean'])   
print(debt_loan.sort_values(by='mean',ascending=True))


# ### Conclusion

# # People who took loan to purchase cars are more likely to pay the loan ontime, and people who took loan for house are slightly less to pay the loan ontime. 

# ## Review
# 
# ```diff
# + You answer the questions correctly but please take more care about font styles etc... 
# ```

# ### Step 4. General conclusion

# People with higher salary are more likely to pay the loan ontime.
# I have considered 1 as defaulted(paying loan ontime)
# 0 as not-defaulted (not paying loan ontime

# ## Review
# 
# Based on my research with the data i analysed that:
# People with kids are slightly more likely to pay the loan ontime with 1.8% difference with people having no kids.
# People who are unmarried are more likely to pay the loan ontime, people having marital status as widow are less likely to pay the loan ontime.
# People with higher salary income are more likely to pay the loan ontime, people with high salary income are less likely to pay the loan ontime.
# People who took loan to purchase cars are more likely to pay the loan ontime, people who took loan for house are slightly less to pay the loan ontime.
# 
# 

# ### Project Readiness Checklist
# 
# Put 'x' in the completed points. Then press Shift + Enter.

# - [x]  file open;
# - [x]  file examined;
# - [x]  missing values defined;
# - [x]  missing values are filled;
# - [x]  an explanation of which missing value types were detected;
# - [x]  explanation for the possible causes of missing values;
# - [x]  an explanation of how the blanks are filled;
# - [x]  replaced the real data type with an integer;
# - [x]  an explanation of which method is used to change the data type and why;
# - [x]  duplicates deleted;
# - [x]  an explanation of which method is used to find and remove duplicates;
# - [x]  description of the possible reasons for the appearance of duplicates in the data;
# - [x]  data is categorized;
# - [x]  an explanation of the principle of data categorization;
# - [x]  an answer to the question "Is there a relation between having kids and repaying a loan on time?";
# - [x]  an answer to the question " Is there a relation between marital status and repaying a loan on time?";
# - [x]   an answer to the question " Is there a relation between income level and repaying a loan on time?";
# - [x]  an answer to the question " How do different loan purposes affect on-time repayment of the loan?"
# - [x]  conclusions are present on each stage;
# - [x]  a general conclusion is made.

# In[ ]:




