#!/usr/bin/env python
# coding: utf-8

# # 1. Demo downloading files from websites 
# 
# There are ```txt``` and ```pdf``` files on:
# 
# ```https://sandeepmj.github.io/scrape-example-page/pages.html```
# 
# Do the following:
# 
# 1. Download all ```pdf``` files.
# 2. Download all files at one time.

# In[ ]:


## create new cells as necessary


# In[1]:


# import libraries
from bs4 import BeautifulSoup  ## scrape info from web pages
import requests ## get web pages from server
import time # time is required. we will use its sleep function
from random import randrange # generate random numbers

# from google.colab import files ## code for downloading in google colab


# In[2]:


# url to scrape
url = "https://sandeepmj.github.io/scrape-example-page/pages.html"
response = requests.get(url)
response.status_code


# In[3]:


## GET SOUP
soup = BeautifulSoup(response.text, "html.parser")
soup


# In[4]:


pip install wget


# In[5]:


import wget # can put down documents, files from websites


# In[7]:


pdf_holder = soup.find("ul", class_="pdfs")
pdf_holder


# In[8]:


type(pdf_holder)


# In[9]:


pdf_a_tags = pdf_holder.find_all("a")
pdf_a_tags


# In[10]:


pdfs = []
for a_tag in pdf_a_tags:
    pdfs.append(a_tag.get("href"))

pdfs


# In[12]:


base_url = "https://sandeepmj.github.io/scrape-example-page"


# In[13]:


## lc
all_pdfs = [base_url + pdf for pdf in pdfs]
all_pdfs


# In[15]:


pip install wget


# In[ ]:





# In[ ]:


links_a_tags = txt_holder.find_all("a") 


# In[29]:


pdfs_total = len(all_pdfs)
pdf_count = 1

for pdf in all_pdfs:
    print(f"Downloading pdf {pdf_count} of {pdfs_total}")
    pdf_count += 1
    wget.download(pdf)
    snoozer = randrange(3, 7)
    print(f"Snoozing for {snoozer} seconds next pdf")
    time.sleep(snoozer)


# In[28]:


for pdf in all_pdfs:
    print(f"Downloading pdf {pdf_count} of {pdfs_total}")
    pdf_count += 1
    wget.download(pdf)
    snoozer = randrange(3, 7)
    print(f"Snoozing for {snoozer} seconds next pdf")
    time.sleep(snoozer)


# # 2. Universal conversion function
# Rewrite your function from last week so it can do both:
# 
# - take individual string values like ```$12.24267```, ```10,201``` and ```$12,501``` and convert them into floating point numbers like 12.24, 10201.0 and 12501.0
# 
# - take string values in lists and convert them to floating point numbers. (reminder: you use a zip function).
# 
# Test it on the numbers above and in this list:

# In[42]:


## list of string numbers
string_numbers = ["$12.24267", "10,201", "$12,501", "42,901", "$902,091"]


# In[48]:


def string2float(a_string):
    ## remove $ sign and comma
    a_string = a_string.replace("$", "").replace(",", "") 
    ## return what is converted to float and rounded
    return round(float(a_string), 2)


# In[49]:


string2float("$12.24267")


# In[50]:


string2float("10,201")


# In[51]:


string2float("$12,501") 


# In[52]:


string2float("42,901")


# In[53]:


string2float("$902,091")


# In[54]:


def floatNumbers(string_numbers):
    for number in string_numbers:
        print(string2float(string_numbers))


# In[55]:


float_list = floatNumbers(string_numbers)


# In[ ]:




