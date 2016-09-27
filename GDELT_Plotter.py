# date:          28/09/2016
# author:        Max James Yendall
# description:   iPython plotter to be run in Jupyter Notebook Environment

import blaze as bz
import pandas as pd
import holoviews as hv

# Load external holoviews module in iPython
# Using Jupyter Virtual Python Environment with in-line graphics
# visualisation
%load_ext holoviews.ipython
%output size=300

# Load MapReduce information into blaze data structure
# Using custom header based on MapReduce implementation results
p = bz.Data('data_files/data.csv')

# Set alpha and overlay aspect ratios
%%opts Points (alpha=0.5) Overlay [aspect=1.7]

# Define negative Goldstein events from sub-negative to very negative
# Generally, Goldstein levels are negative, so positivity is hard to
# come by. Average tone may be a better metric
negative   = p[(p.Goldstein > -5)]
positive   = p[(p.Goldstein < -4)]

# Read negative and positive data into a Pandas DataFrame
negative = bz.into(pd.DataFrame, negative[['Longitude','Latitude']]).values
positive = bz.into(pd.DataFrame, positive[['Longitude','Latitude']]).values

# Display Holoviews labels overlayed on Pandas model map
(hv.Points(positive, label="Positive Goldstein") * \
 hv.Points(negative,   label="Negative Goldstein")).relabel(
 "GDELT Goldstein Levels for Environment and Greenpeace Events (2016)")