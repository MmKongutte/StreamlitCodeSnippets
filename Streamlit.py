

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


#subheader
st.subheader("Simple web app with Streamlit")


"""
    	   
    	#### Oh It's a sub heading
    	+ Ok this too gets printed. 

"""

#using Html inline
html_temp ="""
    <div style="background-color:#025246 ;padding:5px">
    <h2 style="color:white;text-align:center;">Yeah Html successful !</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

#printing
st.write('Data:')

#printing the dataframe
st.write(pd.DataFrame({'column1': [1, 2, 3, 4],
    'column2': [10, 20, 30, 40]}))


#Taking the Text Input

n = st.text_input("name","Type Here")
m = st.text_input("Middle name","Type Here")
s= st.text_input("Surname","Type Here")

m

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

#----------------------------->

#ploting a map

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

#----------------------------->

#using check box to hide or show something 

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

#------------------------------>


#USing selectbox to choose from a series.

option = st.selectbox(
    'Which number do you like best?',
     df['column1'])

'You selected: ', option

#----------------------------->

#Usinf selectbox in a sidebar and displaying result in main  page
df=['Linear','Logistic','SVM']
df2=['Images','Data','DataAnalysis']
option = st.sidebar.selectbox(
    'What do you want to see?',
     df2)

'You selected:', option

dataset="iris.csv"


#---------------------------------------------->

# Show Image or Hide Image with Checkbox and some enhancing properties


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



#----------------------------------------------->


# Select which Image you want to see using Radio Button

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

#------------------------------------------------->

# About
#button
if st.button("About App"):
  st.subheader("Iris Dataset EDA App")
  st.text("Built with Streamlit")
  st.text("Thanks to the Streamlit Team Amazing Work")
  """Thank You    """

#-------------------------------------------------->


#checkbox again

if st.checkbox("By"):
  st.write("Madhura Kongutte")
   