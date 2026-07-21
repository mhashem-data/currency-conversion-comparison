#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


# Importing requests library to connect with frankfurter API.
import requests
import datetime
import logging


# In[3]:


# Define a new function that helps to bring currencies data as requested.
def get_exchange_rate(base_currency):
    url = f"https://api.frankfurter.dev/v2/rates?base={base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"API request failed: {response.text}")
    data = response.json()
    return data

currency_rate = get_exchange_rate("EGP")


# In[4]:


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Fetching exchange rates from frankfurter API...")


# In[5]:


# Check if all currencies rate is up  to date.
today = str(datetime.date.today())
important_currencies = ['USD', 'SAR', 'EGP']
all_updated = True
for rate in currency_rate:
    if rate['quote'] in important_currencies and rate['date'] != today:
        all_updated = False
        logging.warning(f"{rate['quote']} rate is outdated, last updated: {rate['date']}")
if all_updated:
    logging.info('Needed currencies are up to date')


# In[6]:


for rate in currency_rate:
    if rate['quote'] in ['USD', 'SAR'] and rate['rate'] is None:
        raise ValueError(f"{rate['quote']} rate is missing - cannot proceed with comparison")


# In[7]:


# Base is the main currency, EGP rate to others.
for rate in currency_rate[:5]:
    print(f"1 {rate['base']} = {rate['rate']} {rate['quote']}, -----> Updated in {rate['date']}")


# In[8]:


# other rates to EGP.
for rate in currency_rate[:5]:
        print(f"1 {rate['quote']} = {round(1 / rate['rate'],2)} {rate['base']}, -> Updated in {rate['date']}")


# In[9]:


# How much USD & SAR in EGP.
for rate in currency_rate:
    if rate['quote'] == 'SAR':
        sar_to_egp = 1 / rate['rate']
    elif rate['quote'] == 'USD':
        usd_to_egp = 1 / rate['rate']
print(sar_to_egp)
print(usd_to_egp)

logging.info(f"sar_to_egp: {sar_to_egp}")
logging.info(f"usd_to_egp: {usd_to_egp}")


# In[10]:


sar_to_usd = sar_to_egp / usd_to_egp
sar_to_usd


# In[11]:


result_direct = 1000 * sar_to_egp
result_direct


# In[12]:


result_indirect = (1000 * sar_to_usd) * usd_to_egp
result_indirect


# In[13]:


if result_direct > result_indirect:
    logging.info(f"Direct value as {round(result_direct,4)} is bigger than indirect value, It's {round((result_direct-result_indirect)/result_indirect*100,4)}% bigger than {round(result_indirect,4)}.")
elif result_direct < result_indirect:
    logging.info(f"Indirect value as {round(result_indirect,4)} is bigger than direct value, It's {round((result_indirect-result_direct)/result_direct*100,4)}% bigger than {round(result_direct,4)}.")
else:
    logging.info(f"{round(result_indirect,4)} & {round(result_direct,4)} ARE EQUALS!!!")


# In[ ]:




