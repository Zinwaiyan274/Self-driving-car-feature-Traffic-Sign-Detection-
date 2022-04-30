
import streamlit as st
from streamlit_option_menu import option_menu



import os
import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st


def demo():
    st.markdown("Try")
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.write('Model Input')
        st.image(uploaded_file)
        if st.button('Predict'):
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)


def mm():
    st.title("ကျေးဇူးပြု၍ မြန်မာဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ။")
    st.subheader("https://share.streamlit.io/zinwaiyan274/zac/main/burmese.py")


def main():
    st.title("Traffic sign detection")
    st.subheader("from the mind of Team ZAC.")

    with st.sidebar:
        selected = option_menu("Main Menu", ["Demo", 'Info'],
                               icons=['house', 'info-circle'], menu_icon="cast", default_index=1)

        st.subheader("💬Language")
        if selected == "Demo" or "Info":
            selected0 = option_menu(None, ["English", "မြန်မာ"],
                                    icons=['fgngf', "translate"], orientation="horizontal")
            st.text("©2022_Team_ZAC")
    if selected0 == "မြန်မာ":
        mm()


    if selected == "Info":
        selected1 = option_menu(None, ["Term and con", "Developer contact" ],
                            icons=['clipboard', 'chat-right-dots'],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "Demo":
       selected0 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
                            icons=['activity', 'eye-fill', "check2-circle"],
                            menu_icon="cast", default_index=0, orientation="horizontal")
       if selected0 == "Demonstration":
           demo()




main()
