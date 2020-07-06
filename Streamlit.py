

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
 
from PIL import Image,ImageFilter,ImageEnhance

#writing App title 
st.title('Eris Data Analysis')

st.subheader("Simple web app with Streamlit")
"""
    	#### Description
    	+ This is a simple Exploratory Data Analysis  of the Iris Dataset depicting the various species built with Streamlit.
    	#### Purpose
    	+ To show a simple EDA of Iris using Streamlit framework. 
    	"""

st.write('Data:')

#function for printing the dataframe
st.write(pd.DataFrame({'column1': [1, 2, 3, 4],
    'column2': [10, 20, 30, 40]}))



#magic commands (no need to write function name)

"""
DATA with magic:
"""

df = pd.DataFrame({
  'column1': [1, 2, 3, 4],
  'column2': [10, 20, 30, 40]
})

df

#adding line chart 

"""
Line chart:
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#ploting a map

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)


#using check box to hide or show something 

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

#USing selectbox to choose from a series.

# option = st.selectbox(
#     'Which number do you like best?',
#      df['column1'])

# 'You selected: ', option

#
df=['Linear','Logistic','SVM']
df2=['Images','Data','DataAnalysis']
option = st.sidebar.selectbox(
    'What do you want to see?',
     df2)

'You selected:', option

dataset="iris.csv"
 # To Improve speed and cache data
# Show Image or Hide Image with Checkbox


@st.cache
def load_image(img):
  im =Image.open(os.path.join(img))
  return im
if st.checkbox("Show Image/Hide Image"):
	my_image = load_image('iris_setosa.jpg')
	enh = ImageEnhance.Contrast(my_image)
	num = st.slider("Set Your Contrast Number",1.0,3.0)
	img_width = st.slider("Set Image Width",300,500)
	st.image(enh.enhance(num),width=img_width)


# Select Image Type using Radio Button
species_type = st.radio('What is the Iris Species do you want to see?',('Setosa','Versicolor','Virginica'))
if species_type == 'Setosa':
      st.text("Showing Setosa Species")
      st.image(load_image('iris_setosa.jpg'))
elif species_type == 'Versicolor':
  st.text("Showing Versicolor Species")
  st.image(load_image('iris_versicolor.jpg'))
elif species_type == 'Virginica':
  st.text("Showing Virginica Species")
  st.image(load_image('iris_virginica.jpg'))

# About
if st.button("About App"):
  st.subheader("Iris Dataset EDA App")
  st.text("Built with Streamlit")
  st.text("Thanks to the Streamlit Team Amazing Work")
  """Thank You    """



if st.checkbox("By"):
  st.text("Madhura KOngutte")
   