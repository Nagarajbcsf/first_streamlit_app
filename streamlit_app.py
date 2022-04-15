import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket Somoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🧇Avacado Toast')

streamlit.header('🍌🍍Build your own Fruit Smoothie🥝 🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#lets put a pick list here so they can pick the fruit they want to include
streamlist.multipselect("Pick some fruits:", list(my fruit_list.index))

#display the table on the page
streamlit.dataframe(my fruit_list)

