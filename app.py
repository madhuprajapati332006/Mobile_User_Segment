import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from streamlit_option_menu import option_menu

# page segmentation

st.set_page_config(page_title="Mobile User Segmentation", page_icon="📱", layout="wide")

#sidebar

with st.sidebar:
    st.markdown("<h1 style = 'text align : center;'>📱</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style = 'text align : center;'>Mobile User</h2>", unsafe_allow_html=True)
    st.caption("Machine Learning Dashbord")
    selected = option_menu(menu_title="Navigation",options=["Dashbord","Dataset","Statistics","visualization",
                                                            "Prediction"],icons = ["house","table"])
