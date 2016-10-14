
# coding: utf-8

# # Fire up GraphLab Create
# 
# We always start with this line before using any part of GraphLab Create. It can take up to 30 seconds to load the GraphLab library - be patient!
# 
# The first time you use GraphLab create, you must enter a product key to license the software for non-commerical academic use. To register for a free one-year academic license and obtain your key, go to [dato.com](https://dato.com/download/academic.html).

# In[2]:

import graphlab
# Set product key on this computer. After running this cell, you will not need to re-enter your product key. 
graphlab.product_key.set_product_key('C7E4-BB1D-0150-A1E6-645C-66D9-D454-CC8D')

# Limit number of worker processes. This preserves system memory, which prevents hosted notebooks from crashing.
graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)

# Output active product key.
graphlab.product_key.get_product_key()


# # Load a tabular data set

# In[3]:

sf = graphlab.SFrame('people-example.csv')


# # SFrame basics

# In[6]:

sf.head() # we can view first few lines of table


# In[7]:

sf.tail() #Last few lines of the table 


# # GraphLab Canvas

# In[9]:

# .show() visualizes any data structure in GraphLab Create
# If you want Canvas visualization to show up on this notebook, 
# add this line:

sf.show()
graphlab.canvas.set_target('ipynb')


# In[10]:

sf['age'].show(view='Categorical')


# # Inspect columns of dataset

# In[11]:

sf['Country']


# In[12]:

sf['age']


# Some simple columnar operations

# In[13]:

sf['age'].mean()


# In[14]:

sf['age'].max()


# # Create new columns in our SFrame

# In[ ]:

sf


# In[15]:

sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name'] #concatenation


# In[16]:

sf


# In[17]:

sf['age'] * sf['age']


# # Use the apply function to do a advance transformation of our data

# In[18]:

sf['Country'] #USA and United States problematic 


# In[19]:

sf['Country'].show()


# In[21]:

def transform_country(country):
    if country == 'USA':
        return 'United States'
    else:
        return country


# In[22]:

transform_country('Brazil')


# In[23]:

transform_country('Brasil')


# In[24]:

transform_country('USA')


# In[25]:

sf['Country'].apply(transform_country)


# In[26]:

sf['Country'] = sf['Country'].apply(transform_country) #Store it back into the data frame


# In[27]:

sf


# In[ ]:



