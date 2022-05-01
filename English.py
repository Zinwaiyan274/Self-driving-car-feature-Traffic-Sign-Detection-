# import matplotlib.pyplot as plt
# import cv2
# import tensorflow as tf
# import os
# from tensorflow.keras import layers
# from tensorflow.keras import Model
# from tensorflow.keras.optimizers import RMSprop
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.layers import Dense,Flatten,Conv2D,MaxPooling2D,Dropout
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# import matplotlib.pyplot as plt
# from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score

import streamlit as st
from streamlit_option_menu import option_menu




# MODEL_DIR = os.path.join(os.path.dirname(__file__), 'Final(1)')
# if not os.path.isdir(MODEL_DIR):
#     os.system('runipy train.ipynb')
#
# model = load_model('model')


def mm():
    st.title("ကျေးဇူးပြု၍ မြန်မာဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ။")
    st.subheader("https://share.streamlit.io/zinwaiyan274/zac/main/burmese.py")


def main():
    st.title("Traffic sign detection")
    st.subheader("from the mind of Team ZAC.")

    with st.sidebar:
        selected = option_menu("Main Menu", ["Demo", 'Info'],
                               icons=['house', 'info-circle'], menu_icon="cast", default_index=1)

        st.subheader("Language")
        # selected0 = option_menu(None, ["Language"],
        #                         icons=["translate"], orientation="horizontal")

        icons=["translate"]
        if selected == "Demo" or "Info":
            selected0 = option_menu(None, ["English", "မြန်မာ"],
                                    icons=['spellcheck', "translate"], orientation="horizontal")
  #english emoji ko ex
            st.text("©2022_Team_ZAC")
    if selected0 == "မြန်မာ":
        mm()


    if selected == "Info":
        selected1 = option_menu(None, ["Term and con", "Developer contact",  ],
                            icons=['clipboard', 'chat-right-dots', "flag fill"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "Demo":
       selected0 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
                            icons=['activity', 'eye-fill', "check2-circle"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

main()
