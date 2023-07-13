import streamlit as st
from streamlit_option_menu import option_menu
import pyodbc
import pymssql
import pandas as pd


st.set_page_config(page_title="IoT CoE Track 'N' Trace",page_icon=":tada:",layout="wide")

with st.container():
 #st.subheader("Track and Trace Application")
 st.title("IoT CoE Track 'N' Trace")

 with  st.sidebar:
  selected =option_menu(
         menu_title="Assembly Line",
         options=("Material Handling Station","Pinning and Press Station","Drilling Station"),
  )


cnxn_str = ("Driver={ODBC Driver 18 for SQL Server};"
            "Server=coepocsqlserver;"
            "Database=coeqrappdb;"
            "UID=coepocadmin;"
            "PWD=Password@123;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

cursor.execute("SELECT  * FROM Block_Details")

data = pd.read_sql("SELECT  * FROM Block_Details", cnxn)


if selected == "Material Handling Station":
     st.title(f"you have selected {selected}")

st.table(data)

if selected == "Pinning and Press Station":
  st.title(f"you have selected {selected}")


if selected == "Drilling Station":
 st.title(f"you have selected {selected}")
