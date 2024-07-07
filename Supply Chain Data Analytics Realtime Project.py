#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


import warnings
warnings.filterwarnings('ignore')


# In[15]:


data = pd.read_csv("C:\\Users\\mohan\\Downloads\\Supply Chain Project\\SupplyChainData.csv")


# In[16]:


data.head(5)


# In[17]:


data.head()


# In[18]:


data.tail()


# In[ ]:


#Data Preparation and cleansing
#Loading the file using pandas
#Leveraging the  infromation about the data & the columns
#Data Cleansing for any missing or incorrect values


# In[19]:


data.columns


# In[20]:


data.shape


# In[21]:


data.describe()


# In[22]:


data.info()


# In[28]:


#Data Cleansing Missing and Duplicate values

data.isnull().sum()


# In[ ]:





# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Analyzing 'data' is your DataFrame with missing values
plt.figure(figsize=(16, 5))

# Calculating percentage of missing values
missing_values = pd.DataFrame(data.isnull().sum() * 100 / data.shape[0]).reset_index()

# Plot using sns.pointplot
ax = sns.pointplot(x='index', y=0, data=missing_values)

plt.xticks(rotation=90, fontsize=7)
plt.title('Missing Values Percentage')
plt.show()


# In[32]:


#Checking Duplicate Values
len(data[data.duplicated()])


# In[33]:


#Identifying all unique values for each columns in the Dataset
data.nunique()


# In[ ]:


#Data Visualisation
#Sales Analysis
#Analyze number of products sold and revenue generated to understand sales performance over time.
#Identify customer demographics to determine which groups are purchasing the most products.
#Track availability and stock levels to ensure the right products are in stock when customers are ready to buy.


# In[34]:


product_sold = data.groupby(['Product type'])['Number of products sold', 'Revenue generated'].sum().reset_index()
data['Revenue generated'] = data['Revenue generated'].round(2)


# In[35]:


product_sold


# In[36]:


plt.figure(figsize = (12,8))
colors = ['#FFB90F', '#00EEEE', '#EEAD0E']
pie_chart = plt.pie(product_sold['Number of products sold'], labels = product_sold['Product type'], autopct = '%.2f%%',wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
       textprops={'size': 'x-large'}, shadow =True, colors = colors)
plt.title('Percent of product Sold by Product Type', fontsize= 15)
plt.show()


# In[41]:


import matplotlib.pyplot as plt

# Assuming 'product_sold' is a dataframe
plt.figure(figsize=(12, 6))
bars1 = plt.bar(x=product_sold['Product type'], height=product_sold["Number of products sold"], color='r', label='Number of products sold')
bars2 = plt.bar(x=product_sold['Product type'], height=product_sold["Revenue generated"], bottom=product_sold["Number of products sold"], color='y', label='Revenue generated')

plt.title("Revenue generated vs. Number of products sold by product type", fontsize=15)
plt.xlabel("Product type")
plt.ylabel("Count/Revenue")

# Add legend
plt.legend()

# Annotate totals inside the bars
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    plt.text(bar1.get_x() + bar1.get_width() / 2, height1 / 2, f'{round(height1, 2)}', ha='center', va='center', color='white', fontsize=12)
    plt.text(bar2.get_x() + bar2.get_width() / 2, height1 + height2 / 2, f'{round(height2, 2)}', ha='center', va='center', color='black', fontsize=12)

plt.show()


# In[ ]:


#So, the highest number of products sold of the three product categories is Beauty & Personal Care,
#which means 45% of business comes from Beauty & Personal Care, 30% from Automotive, and 26% from Cell Phone Accesories.


# In[42]:


data['Customer demographics'].unique()


# In[44]:


demographics = data.groupby(['Customer demographics', 'Product type'])['Number of products sold'].sum().reset_index()


# In[45]:


demographics


# In[55]:


#plt.figure(figsize = (12,8))
#p = sns.barplot(x = demographics['Customer demographics'], y = demographics['Number of products sold'], hue = demographics['Product type'], palette = 'Oranges')
#for container in p.containers:
#    p.bar_label(container,padding=-40, color='black', fontsize=10)
#plt.title("Customer Demographics vs No.of product sold by Product Type", fontsize = (14))
#plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'demographics' is a dataframe
plt.figure(figsize=(12, 8))
p = sns.barplot(x=demographics['Customer demographics'], y=demographics['Number of products sold'], hue=demographics['Product type'], palette='Oranges')

# Display total number of products sold above the bars
for container in p.containers:
    p.bar_label(container, padding=3, color='black', fontsize=10)

plt.title("Customer Demographics vs No. of products sold by Product Type", fontsize=14)
plt.show()


# In[ ]:


#According to the graph, the female group purchases higher-quality Beauty & Personal Care and Cell phone Accesories, 
#whereas the male group purchases products of about equal quality in terms of Automotive and Cell Phone Accesories. 
#And an unknown group category purchases a higher quantity of all three products.
#Beauty & Personal Care products are the most popular among all four product categories.


# In[50]:


stock = data.groupby(['Product type'])['Stock levels','Availability'].sum().reset_index()
stock


# In[56]:


#p = sns.barplot(x ='Product type', y =('Stock levels') , data = stock, palette = 'gist_earth')
#for container in p.containers:
#    p.bar_label(container,padding=-40, color='white', fontsize=10)
    
    
    
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'stock' is a dataframe
plt.figure(figsize=(12, 8))
p = sns.barplot(x='Product type', y='Stock levels', data=stock, palette='gist_earth')

# Display total stock above the bars
for container in p.containers:
    p.bar_label(container, padding=3, color='black', fontsize=10)  # Adjust padding to place the label above the bar

plt.title("Total Stock Levels by Product Type", fontsize=14)
plt.show()


# In[59]:


#plt.figure(figsize = (10,6))
#plt.bar(x ='Product type', height = 'Stock levels' , data = stock, color = 'brown')
#plt.bar(x ='Product type', height = 'Availability' , bottom = 'Stock levels' , data = stock, color = 'green')

#plt.title("Availability and Stock levels of Product Type", fontsize = (15))
#plt.show()




import matplotlib.pyplot as plt

# Assuming 'stock' is a dataframe
plt.figure(figsize=(10, 6))

# Plot the stock levels bar
bars1 = plt.bar(x=stock['Product type'], height=stock['Stock levels'], color='orange', label='Stock levels')

# Plot the availability bar stacked on top of stock levels
bars2 = plt.bar(x=stock['Product type'], height=stock['Availability'], bottom=stock['Stock levels'], color='green', label='Availability')

plt.title("Availability and Stock levels of Product Type", fontsize=15)
plt.xlabel("Product type")
plt.ylabel("Count")

# Add legend
plt.legend()

# Annotate totals inside the bars
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    plt.text(bar1.get_x() + bar1.get_width() / 2, height1 / 2, f'{int(height1)}', ha='center', va='center', color='black', fontsize=10)
    plt.text(bar2.get_x() + bar2.get_width() / 2, height1 + height2 / 2, f'{int(height2)}', ha='center', va='center', color='black', fontsize=10)

plt.show()



# In[60]:


data.groupby(['Product type'])['Stock levels','Availability'].sum().reset_index()


# In[ ]:


#In the graph, green represents the availability and orange represents the stock levels.
#So according to the graph, the company holds an high quantity of availability of Beauty Personal Care and
#Automotive products are less and a bit less stock of Cell Phone Accesories.
#So, Automotive products had a lower availability and higher stock level, which means we can quickly
#manufacture and ship products as needed. On the other hand, 
#Beauty and Cell Phone Accesiores have a somehow resonable stock level and  availability, which means the company 
# has to gather raw material for processing and take time to ship product to the customer because,It takes time to manufacture the product.


# In[ ]:


#Operations Analysis:
#1.Analyze lead times, order quantities, and production volumes to optimize inventory management and reduce stockouts.
#2.Track manufacturing lead time and costs to identify areas for improvement and cost savings.
#3.Monitor inspection results and defect rates to identify quality issues and improve manufacturing processes.


# In[61]:


data.columns


# In[62]:


product = data.groupby(['Product type'])['Lead time', 'Order quantities', 'Production volumes'].mean().reset_index()
product['Order quantities'] = product['Order quantities'].round(2)
product['Lead time'] = product['Lead time'].round(2)
product['Production volumes'] = product['Production volumes'].round(2)


# In[63]:


product


# In[ ]:


#Beauty & Personal Care products have higher order quantities and a longer lead time. Furthermore,
#it has a higher production volume (production volume means the amount of products that are produced by the company), 
#which means higher production volumes may require longer lead times to ensure that there is enough time to manufacture
#the products and meet customer demand.
#Automotive Parts & Accessories products have a longer lead time and higher production volumes. This may be because Automotive Parts & Accessories products require more specialised ingredients or manufacturing processes.


# In[65]:


avg_costs = data.groupby(['Manufacturing lead time'])['Manufacturing costs'].mean().reset_index().sort_values(by = 'Manufacturing costs')
avg_costs['Manufacturing costs'] = avg_costs['Manufacturing costs'].round(2)

avg_costs


# In[70]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'avg_costs' is a dataframe
plt.figure(figsize=(20, 10))

# Create the barplot with orange color
p = sns.barplot(x=avg_costs['Manufacturing lead time'], y=avg_costs['Manufacturing costs'], palette='Oranges')

# Display the number above each bar
for container in p.containers:
    p.bar_label(container, padding=3, color='black', fontsize=12)  # Adjust padding to place the label above the bar

# Add title and legend with appropriate labels
plt.title('Manufacturing lead time and Cost', fontsize=15)
plt.xlabel('Manufacturing Lead Time')
plt.ylabel('Manufacturing Costs')

# Customize legend labels and title
handles, labels = p.get_legend_handles_labels()
plt.legend(handles, ['Manufacturing Lead Time', 'Manufacturing Costs'], title='Legend')

plt.show()


# In[71]:


rate = data.groupby(['Product type', 'Inspection results'])['Defect rates'].mean().reset_index()
rate['Defect rates'] = rate['Defect rates'].round(2)


# In[72]:


rate


# In[73]:


data['Defect rates'].mean()


# In[74]:


data['Defect rates'].max()


# In[75]:


data['Defect rates'].min()


# In[80]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'rate' is a dataframe
plt.figure(figsize=(12, 8))

# Define custom colors for the legend categories
custom_palette = {'Fail': 'red', 'Pending': 'grey', 'Pass': 'green'}

# Create the barplot with custom colors
p = sns.barplot(x=rate['Product type'], y=rate['Defect rates'], hue=rate['Inspection results'], palette=custom_palette)

# Add labels on top of each bar
for index, row in rate.iterrows():
    for bar, label in zip(p.patches, rate['Defect rates']):
        p.annotate(f'{label:.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom', color='black', fontsize=10)

# Add title and labels
plt.title("Inspection results Vs Defect rates by Product type", fontsize=15)
plt.xlabel("Product type")
plt.ylabel("Defect rates")

# Show the plot with updated legend colors
plt.legend(title='Inspection Results', loc='upper right')

plt.show()


# In[ ]:


All product categories have a resonable higher defect rates.


# In[ ]:


#Shipping Analysis:
#Analyze costs, transportation modes, and routes to optimize logistics and reduce shipping costs.
#Monitor shipping times, shipping carriers, modes of transportation to ensure timely delivery to customers.
#Track shipping costs associated with shipping carriers and revenue generated to identify areas for cost savings


# In[81]:


shipping = data.groupby(['Shipping carriers'])['Shipping costs'].sum().reset_index()


# In[82]:


shipping


# In[83]:


plt.figure(figsize = (12,8))
colors = ['#40E0D0', '#9FE2BF','#CCCCFF']
plt.pie( shipping['Shipping costs'], labels = shipping['Shipping carriers'],autopct = '%.2f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
       textprops={'size': 'x-large'}, shadow =True, colors = colors)
plt.title('Cost Distribution by Shipping cost', fontsize = (15))
plt.show()


# In[ ]:


#Shipping of Carrier A is Airways, Carrier B is Roadways and Carrier C is Seaways.


# In[84]:


carrier_revenue = data.groupby(['Shipping carriers'])['Revenue generated'].sum().reset_index()
carrier_revenue['Revenue generated'] = carrier_revenue['Revenue generated'].round(2)


# In[85]:


carrier_revenue


# In[87]:


#plt.figure(figsize = (10,6))
#p = sns.barplot(x = carrier_revenue['Shipping carriers'], y = carrier_revenue['Revenue generated'], palette = 'Wistia_r')
#for container in p.containers:
#    p.bar_label(container,padding=-40, color='black', fontsize=10)

#plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'carrier_revenue' is a dataframe
plt.figure(figsize=(10, 6))

# Define custom colors for each carrier
custom_palette = {'Carrier A': 'blue', 'Carrier B': 'green', 'Carrier C': 'orange'}

# Create the barplot with custom colors
p = sns.barplot(x=carrier_revenue['Shipping carriers'], y=carrier_revenue['Revenue generated'], palette=custom_palette)

# Display the total revenue on top of each bar
for container in p.containers:
    for bar, label in zip(p.patches, carrier_revenue['Revenue generated']):
        p.annotate(f'{label:.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom', color='black', fontsize=10)

# Add title and labels
plt.title("Revenue generated by Shipping Carriers", fontsize=15)
plt.xlabel("Shipping Carriers")
plt.ylabel("Revenue Generated")

# Create custom legend with specified colors
legend_labels = ['Carrier A', 'Carrier B', 'Carrier C']
legend_handles = [plt.Rectangle((0,0),1,1, color=custom_palette[label]) for label in legend_labels]
plt.legend(legend_handles, legend_labels, title='Carriers')

plt.show()


# In[ ]:


#Analyzing the graphs clearly show shipping carrier B is costly as well as generating higher revenue.


# In[88]:


transport = data.groupby(['Transportation modes', 'Routes'])['Costs'].sum().reset_index()


# In[89]:


transport


# In[103]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'transport' is a dataframe
plt.figure(figsize=(12, 8))

# Create the barplot with a bright palette
p = sns.barplot(x=transport['Transportation modes'], y=transport['Costs'], hue=transport['Routes'], palette='bright')

# Add total cost above each bar
for patch in p.patches:
    height = patch.get_height()
    p.annotate(f'{height:.2f}', (patch.get_x() + patch.get_width() / 2, height + 5), ha='center', va='bottom', fontsize=10, color='black')

# Add title and labels
plt.title("Costs by Transportation Modes and Routes", fontsize=15)
plt.xlabel("Transportation Modes")
plt.ylabel("Costs")

# Show the plot
plt.show()


# In[104]:


shipping = data.groupby(['Shipping carriers', 'Transportation modes'])['Shipping times'].mean().reset_index()
shipping['Shipping times'] = shipping['Shipping times'].round(2)
shipping


# In[120]:


plt.figure(figsize = (12,8))
p = sns.barplot(x = shipping['Transportation modes'], y = shipping['Shipping times'], hue = shipping['Shipping carriers'], palette = 'plasma')
for container in p.containers:
    p.bar_label(container,padding=4.1, color='black', fontsize=10)
plt.show()


# In[ ]:


#According to the graph, the fastest and most efficient shipping option is Carrier B in all four transportation modes.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




