import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="IoT CoE Track 'N' Trace",page_icon=":tada:",layout="wide")

with st.container():
 #st.subheader("Track and Trace Application")
 st.title("IoT CoE Track 'N' Trace")

 with  st.sidebar:
  selected =option_menu(
         menu_title="Assembly Line",
         options=("Material Handling Station","Pinning and Press Station","Drilling Station"),
  )

if selected == "Material Handling Station":
     st.title(f"you have selected {selected}")


if selected == "Pinning and Press Station":
  st.title(f"you have selected {selected}")


if selected == "Drilling Station":
 st.title(f"you have selected {selected}")
