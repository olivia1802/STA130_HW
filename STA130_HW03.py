#!/usr/bin/env python
# coding: utf-8

# #1

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the penguins dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
penguins = pd.read_csv(url)

# Calculate relevant statistics for flipper_length_mm by species
species_stats = penguins.groupby('species')['flipper_length_mm'].agg(
    mean_flipper_length='mean',
    median_flipper_length='median',
    min_flipper_length='min',
    max_flipper_length='max',
    q1_flipper_length=lambda x: x.quantile(0.25),
    q3_flipper_length=lambda x: x.quantile(0.75),
    std_flipper_length='std'
).reset_index()

# Create histograms for each species
fig = px.histogram(penguins, x='flipper_length_mm', color='species', facet_col='species', opacity=0.7)

# Add lines and rectangles for each species
for i, species in enumerate(species_stats['species']):
    # Get species-specific statistics
    mean = species_stats.loc[i, 'mean_flipper_length']
    median = species_stats.loc[i, 'median_flipper_length']
    min_val = species_stats.loc[i, 'min_flipper_length']
    max_val = species_stats.loc[i, 'max_flipper_length']
    q1 = species_stats.loc[i, 'q1_flipper_length']
    q3 = species_stats.loc[i, 'q3_flipper_length']
    std = species_stats.loc[i, 'std_flipper_length']
    
    # Calculate the range defined by two standard deviations away from the mean
    lower_std = mean - 2 * std
    upper_std = mean + 2 * std
    
    # Add mean line
    fig.add_vline(x=mean, line_width=2, line_dash="dash", line_color="green", row=1, col=i+1)
    
    # Add median line
    fig.add_vline(x=median, line_width=2, line_dash="dot", line_color="blue", row=1, col=i+1)
    
    # Add range rectangle (min to max)
    fig.add_vrect(x0=min_val, x1=max_val, fillcolor="lightblue", opacity=0.3, line_width=0, row=1, col=i+1)
    
    # Add interquartile range rectangle (Q1 to Q3)
    fig.add_vrect(x0=q1, x1=q3, fillcolor="orange", opacity=0.3, line_width=0, row=1, col=i+1)
    
    # Add 2 standard deviations rectangle
    fig.add_vrect(x0=lower_std, x1=upper_std, fillcolor="lightgreen", opacity=0.3, line_width=0, row=1, col=i+1)

# Update layout and show the plot
fig.update_layout(title_text="Flipper Length Distribution for Penguin Species with Mean, Median, Range, IQR, and 2 Std Dev Ranges")
fig.show()


# #2

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the penguins dataset
penguins = pd.read_csv(url)

# Remove rows with missing values in flipper_length_mm
penguins = penguins.dropna(subset=['flipper_length_mm'])

# Set up the seaborn style
sns.set(style="whitegrid")

# Create subplots for the three species
species = penguins['species'].unique()
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Add KDE plots and lines/rectangles for each species
for i, sp in enumerate(species):
    ax = axes[i]
    subset = penguins[penguins['species'] == sp]
    
    # KDE plot for flipper_length_mm
    sns.kdeplot(subset['flipper_length_mm'], ax=ax, fill=True, color='skyblue')
    
    # Get relevant statistics
    mean = subset['flipper_length_mm'].mean()
    median = subset['flipper_length_mm'].median()
    min_val = subset['flipper_length_mm'].min()
    max_val = subset['flipper_length_mm'].max()
    q1 = subset['flipper_length_mm'].quantile(0.25)
    q3 = subset['flipper_length_mm'].quantile(0.75)
    std = subset['flipper_length_mm'].std()
    lower_std = mean - 2 * std
    upper_std = mean + 2 * std
    
    # Add vertical lines for mean and median
    ax.axvline(mean, color='green', linestyle='--', label='Mean')
    ax.axvline(median, color='blue', linestyle=':', label='Median')
    
    # Add shaded areas for range, IQR, and 2 std deviations
    ax.axvspan(min_val, max_val, color='lightblue', alpha=0.3, label='Range')
    ax.axvspan(q1, q3, color='orange', alpha=0.3, label='IQR')
    ax.axvspan(lower_std, upper_std, color='lightgreen', alpha=0.3, label='2 Std Dev')
    
    # Set titles and labels
    ax.set_title(f'{sp} Flipper Length KDE')
    ax.set_xlabel('Flipper Length (mm)')
    ax.legend()

# Set the overall title
plt.suptitle("Penguin Flipper Length KDE with Mean, Median, Range, IQR, and 2 Std Dev", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# #3

# I prefer histograms because they are easy to interpret. They provide a clear picture of how data is distributed across different ranges (bins). The shape of the distribution is also evident, allowing readers to see whether the data is skewed, unimodal, or bimodal, etc. From my perspective, I prefer reading data from a clear image, which is why I like histograms over KDEs and box plots

# In[ ]:


ChatGPT Summary: https://chatgpt.com/c/66f2261d-7d7c-800e-9f2c-b55f8071863e


# #4

# In[2]:


from scipy import stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

n = 1500
data1 = stats.uniform.rvs(0, 10, size=n)
data2 = stats.norm.rvs(5, 1.5, size=n)
data3 = np.r_[stats.norm.rvs(2, 0.25, size=int(n/2)), stats.norm.rvs(8, 0.5, size=int(n/2))]
data4 = stats.norm.rvs(6, 0.5, size=n)

fig = make_subplots(rows=1, cols=4)

fig.add_trace(go.Histogram(x=data1, name='A', nbinsx=30, marker=dict(line=dict(color='black', width=1))), row=1, col=1)
fig.add_trace(go.Histogram(x=data2, name='B', nbinsx=15, marker=dict(line=dict(color='black', width=1))), row=1, col=2)
fig.add_trace(go.Histogram(x=data3, name='C', nbinsx=45, marker=dict(line=dict(color='black', width=1))), row=1, col=3)
fig.add_trace(go.Histogram(x=data4, name='D', nbinsx=15, marker=dict(line=dict(color='black', width=1))), row=1, col=4)

fig.update_layout(height=300, width=750, title_text="Row of Histograms")
fig.update_xaxes(title_text="A", row=1, col=1)
fig.update_xaxes(title_text="B", row=1, col=2)
fig.update_xaxes(title_text="C", row=1, col=3)
fig.update_xaxes(title_text="D", row=1, col=4)
fig.update_xaxes(range=[-0.5, 10.5])

for trace in fig.data:
    trace.xbins = dict(start=0, end=10)
    
# This code was produced by just making requests to Microsoft Copilot
# https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk3/COP/SLS/0001_concise_makeAplotV1.md

fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# 1) 
# - A and B have similar means, which is around 5. 
# - B and C's second part have similar variances. 
# 
# 2) 
# - A and B have similar means, but different variances. 
# A: mean 5 and variance much larger than B
# B: mean 5 and variance smaller than A
# 
# 3) 
# - B and C have similar variances, but quite different means.
# B: normal distribution with mean 5 and std 1.5, variance around 2
# C: two normal distributions with means 2 and 8 (bimodal), variance less than 1
# 4) 
# - A and D have quite different means and quite different variances.
# A: mean 5, large variance
# D: mean 6, smaller variance

# #5

# Mean:
# - arithmetic average of a set of values
# - calculated by summing all the values and dividing by the number of values
# 
# Median:
# - middle value when a data set is ordered from least to greatest
# - if the data set has an odd number of values=> the median is the middle value
# - if the data set has an even number of values => the median is the average of the two middle values
# 
# Relationship:
# - Mean == Median: symmetric distributions
# ex) normal distribution
# - Mean > Median: right-skewed distribution, there are few high values
# - Mean < Median: left-skewed distribution, few low values
# 
# Right Skewness(Positive Skewness):
# - when the right tail(higher values) is longer or fatter than the left tail(lower values)
# 
# Left Skewness(Negative Skewness):
# - when the left tail(lower values) is longer or fatter than the right tail(higher values)

# ChatGPT Summary: https://chatgpt.com/c/66f3844f-775c-800e-a98b-ad39205182a5

# #6

# In[1]:


import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/manuelamc14/fast-food-Nutritional-Database/main/Tables/nutrition.csv")
df # df.columns


# In[7]:


# Summary statistics for numerical columns
df.describe()


# Using summary statistics and visualization, I found one interesting fact about the dataset I used. In terms of caloric range, it range from 0 to 1880 calories per serving, implies a significant diffeence across different items. The median is around 260, but the upper 75%(Q3) of iterms have calories reaching 410 and even up to 1880. Therefore, to visualize this data more precisely and clearly, histogram coould be used to show how calories are distributed across the dataset. I asked ChatGPT to provide me a code that generates caloric range histgram: 

# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt

# Create the histogram for the caloric range
plt.figure(figsize=(10,6))
sns.histplot(df['calories'], bins=30, kde=True, color='skyblue')

# Add titles and labels
plt.title('Caloric Range Distribution', fontsize=16)
plt.xlabel('Calories', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Display the plot
plt.show()


# ChatGPT Summary: https://chatgpt.com/c/66f3844f-775c-800e-a98b-ad39205182a5

# #7

# Animated figures with Plotly Express

# In[1]:


import plotly.express as px
df = px.data.gapminder()
px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])


# Animated figures in Dash

# In[6]:


get_ipython().system('pip install dash')
get_ipython().system('pip install plotly')


# In[10]:


from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Animated GDP and population over decades'),
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=["GDP - Scatter", "Population - Bar"],
        value='GDP - Scatter',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(
    Output("graph", "figure"), 
    Input("selection", "value"))
def display_animated_graph(selection):
    df = px.data.gapminder() # replace with your own data source
    animations = {
        'GDP - Scatter': px.scatter(
            df, x="gdpPercap", y="lifeExp", animation_frame="year", 
            animation_group="country", size="pop", color="continent", 
            hover_name="country", log_x=True, size_max=55, 
            range_x=[100,100000], range_y=[25,90]),
        'Population - Bar': px.bar(
            df, x="continent", y="pop", color="continent", 
            animation_frame="year", animation_group="country", 
            range_y=[0,4000000000]),
    }
    return animations[selection]


app.run_server(debug=True)
# Download
# commented out the last line since it generated NameError


# Animated Bar Charts with Plotly Express

# In[12]:


import plotly.express as px

df = px.data.gapminder()

fig = px.bar(df, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])
fig.show()


# #8

# In[14]:


import plotly.express as px
import pandas as pd

# Assuming you are working with a baby names dataset
# Load the dataset
bn = pd.read_csv('https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv')

# Make identical boy and girl names distinct by appending sex to the name
bn['name'] = bn['name'] + " " + bn['sex']

# Create 'rank' column based on the 'percent' of each name per year
bn['rank'] = bn.groupby('year')['percent'].rank(ascending=False)

# Sort values to calculate percent change
bn = bn.sort_values(['name', 'year'])

# Create 'percent change' column (the change in name prevalence from the previous year)
bn['percent change'] = bn['percent'].diff()

# Mark new names with their current percentage
new_name = [True] + list(bn.name[:-1].values != bn.name[1:].values)
bn.loc[new_name, 'percent change'] = bn.loc[new_name, 'percent']

# Sort by year for proper animation
bn = bn.sort_values('year')

# Restrict to "common" names by filtering out names with a very small percent
bn = bn[bn.percent > 0.001]

# Create the scatter plot
fig = px.scatter(
    bn, 
    x="percent change", 
    y="rank", 
    animation_frame="year", 
    animation_group="name", 
    size="percent", 
    color="sex", 
    hover_name="name", 
    size_max=50, 
    range_x=[-0.005, 0.005]
)

# Update y-axis to reverse (lower rank is better, so rank 1 should be at the top)
fig.update_yaxes(autorange='reversed')

# Display the plot
fig.show(renderer="png")


# #9

# Yes
