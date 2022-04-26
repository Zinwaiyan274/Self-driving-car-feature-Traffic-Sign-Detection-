import streamlit as st
from PIL import Image
#
#
# st.title("title")
# st.code("sgf")
# st.header("dg")
# st.subheader("Meme photo")
# st.text("hsghs")
#
# st.markdown("waii")
# st.success("done")
# st.warning("dgf")
# st.info("sdf")
# st.error("dgf")
# st.exception("Name error ('Not defined')")
# st.sidebar.header("About")
#
#
# with st.echo():
#     import numpy as np
#     import pandas as pd
#     # sdfgrsf
#
# img  = Image.open("Meme.jpg")
# st.image(img,width=300, caption= "meme photo")
# st.checkbox("Sfsd")


import streamlit as st
#
# def main():
#     st.title("Welcome to Simbolo")
#     menu = ["BMI calculator","Zen", "Human proof testing"]
#     choice = st.sidebar.selectbox("Menu",menu)
#     if choice =="BMI calculator":
#         st.subheader("BMI calculator")
#     elif choice == "Zen":
#         st.subheader("Zen")
#         Zen()
#     elif choice == "Human proof testing":
#         st.subheader("Human proof testing")
#
#
# def Zen():
#
#     form1 = st.radio("Are you stressed about something or do you have any problem?",("Yes","No"))
#     # form = st.form(key=form1)
#     sumbit = form1.form_submit_button("Sumbit")
#     if sumbit == "Yes":
#         st.subheader("Yes")
#     elif sumbit == "No":
#         st.subheader("No")
#
#     buttom = st.button("sumbuit")
#
#
#
#
#
#
#
# if  __name__ == "__main__":
#     main()


import streamlit as st

# python -m streamlit.cli run app.py
#
#     weight = st.number_input("Enter your weight(in Kgs)")
#
#     status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
#
#     if status == 'cms':
#         height = st.number_input('Centimeters')
#         try:
#             bmi = weight / ((height / 100) ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     elif status == 'meters':
#         height = st.number_input('Meters')
#         try:
#             bmi = weight / (height ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     else:
#         height = st.number_input('Feet')
#         try:
#             bmi = weight / (((height / 3.28)) ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     if st.button('calculate BMI'):
#         st.text("Your BMI Index is {}.".format(bmi))
#
#         if (bmi < 16):
#             st.error("You are Extremely Underweight")
#         elif (bmi >= 16 and bmi < 18.5):
#             st.warning("You are Underweight")
#         elif (bmi >= 18.5 and bmi < 25):
#             st.success("Healthy")
#         elif (bmi >= 25 and bmi < 30):
#             st.warning("Overweight")
#         elif (bmi >= 30):
#             st.error("Extremely Overweight")
#

import streamlit as st
from streamlit_option_menu import option_menu


def mm():
    st.title("ကျေးဇူးပြု၍ အင်္ဂလိပ်ဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ")
    st.subheader("https://share.streamlit.io/zinwaiyan274/streamlit_testing/main/main.py")


def main():
    st.title("Traffic sign detection")
    st.subheader("from the mind of Team ZAC.")

    with st.sidebar:
        selected = option_menu("Main Menu", ["Demo", 'Info'],
                               icons=['house', 'info-circle'], menu_icon="cast", default_index=1)
        # st.subheader(f"Current page {selected}")
        # horizontal Menu
        # selected2 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
        #     icons=['activity', 'eye-fill', "check2-circle"],
        #     menu_icon="cast", default_index=0, orientation="horizontal")
        st.subheader("💬Language")
        if selected == "Demo" or "Info":
            selected0 = option_menu(None, ["မြန်မာ", "English"],
                                    icons=['fgngf', "translate"], orientation="horizontal")
            st.text("©2022_Team_ZAC")
    if selected0 == "English":
        mm()


#  if selected == "Info":
#      selected1 = option_menu(None, ["Term and con", "Developer contact", "blabla", ],
#                             icons=['clipboard', 'chat-right-dots', "flag fill"],
#                             menu_icon="cast", default_index=0, orientation="horizontal")

#  if selected == "Demo":
#        selected0 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
#                             icons=['activity', 'eye-fill', "check2-circle"],
#                             menu_icon="cast", default_index=0, orientation="horizontal")


# #  with st.sidebar:
# #     selected = option_menu("Main Menu", ["Demo", 'Info'],
# #         icons=['house', 'info-circle'], menu_icon="cast", default_index=1)
# #     selected
# # # horizontal Menu
#  selected2 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric"])
#     icons=['activity', 'eye-fill', "check2-circle"]
#     menu_icon="cast", default_index=0, orientation="horizontal")
#     st.subheader("Language")
#      if selected == "Demo" or "Info":
#         selected0 = option_menu(None, ["English", "Myanmar"],
#                                 icons=['translate'],
#                                 menu_icon="cast", default_index=0, orientation="horizontal")
#  if selected0 == "English":
#              main()


if __name__ == "__main__":
    main()

st.text("©2022_Team_ZAC")

import streamlit as st
from PIL import Image
#
#
# st.title("title")
# st.code("sgf")
# st.header("dg")
# st.subheader("Meme photo")
# st.text("hsghs")
#
# st.markdown("waii")
# st.success("done")
# st.warning("dgf")
# st.info("sdf")
# st.error("dgf")
# st.exception("Name error ('Not defined')")
# st.sidebar.header("About")
#
#
# with st.echo():
#     import numpy as np
#     import pandas as pd
#     # sdfgrsf
#
# img  = Image.open("Meme.jpg")
# st.image(img,width=300, caption= "meme photo")
# st.checkbox("Sfsd")


import streamlit as st
#
# def main():
#     st.title("Welcome to Simbolo")
#     menu = ["BMI calculator","Zen", "Human proof testing"]
#     choice = st.sidebar.selectbox("Menu",menu)
#     if choice =="BMI calculator":
#         st.subheader("BMI calculator")
#     elif choice == "Zen":
#         st.subheader("Zen")
#         Zen()
#     elif choice == "Human proof testing":
#         st.subheader("Human proof testing")
#
#
# def Zen():
#
#     form1 = st.radio("Are you stressed about something or do you have any problem?",("Yes","No"))
#     # form = st.form(key=form1)
#     sumbit = form1.form_submit_button("Sumbit")
#     if sumbit == "Yes":
#         st.subheader("Yes")
#     elif sumbit == "No":
#         st.subheader("No")
#
#     buttom = st.button("sumbuit")
#
#
#
#
#
#
#
# if  __name__ == "__main__":
#     main()


import streamlit as st

# python -m streamlit.cli run app.py
#
#     weight = st.number_input("Enter your weight(in Kgs)")
#
#     status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
#
#     if status == 'cms':
#         height = st.number_input('Centimeters')
#         try:
#             bmi = weight / ((height / 100) ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     elif status == 'meters':
#         height = st.number_input('Meters')
#         try:
#             bmi = weight / (height ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     else:
#         height = st.number_input('Feet')
#         try:
#             bmi = weight / (((height / 3.28)) ** 2)
#         except:
#             st.text("Enter some value of height")
#
#     if st.button('calculate BMI'):
#         st.text("Your BMI Index is {}.".format(bmi))
#
#         if (bmi < 16):
#             st.error("You are Extremely Underweight")
#         elif (bmi >= 16 and bmi < 18.5):
#             st.warning("You are Underweight")
#         elif (bmi >= 18.5 and bmi < 25):
#             st.success("Healthy")
#         elif (bmi >= 25 and bmi < 30):
#             st.warning("Overweight")
#         elif (bmi >= 30):
#             st.error("Extremely Overweight")
#

import streamlit as st
from streamlit_option_menu import option_menu


def mm():
    st.title("ကျေးဇူးပြု၍ အင်္ဂလိပ်ဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ")
    st.subheader("https://share.streamlit.io/zinwaiyan274/streamlit_testing/main/main.py")


def main():
    st.title("Traffic sign detection")
    st.subheader("from the mind of Team ZAC.")

    with st.sidebar:
        selected = option_menu("အဓိက", ["လုပ်ဆောင်ချက်", "အကြောင်းအရာ" ],
                               icons=['house', 'info-circle'], menu_icon="cast", default_index=1)
        # st.subheader(f"Current page {selected}")
        # horizontal Menu
        # selected2 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
        #     icons=['activity', 'eye-fill', "check2-circle"],
        #     menu_icon="cast", default_index=0, orientation="horizontal")
        st.subheader("💬ဘာသာစကား")
        if selected == "Demo" or "Info":
            selected0 = option_menu(None, ["မြန်မာ", "အင်္ဂလိပ်"])
            st.text("©2022_Team_ZAC")
    if selected0 == "အင်္ဂလိပ်":
        mm()


 if selected == "Info":
     selected1 = option_menu(None, ["Term and con", "Developer contact", "blabla", ],
                            icons=['clipboard', 'chat-right-dots', "flag fill"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

 if selected == "Demo":
       selected0 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
                            icons=['activity', 'eye-fill', "check2-circle"],
                            menu_icon="cast", default_index=0, orientation="horizontal")


# #  with st.sidebar:
# #     selected = option_menu("Main Menu", ["Demo", 'Info'],
# #         icons=['house', 'info-circle'], menu_icon="cast", default_index=1)
# #     selected
# # # horizontal Menu
#  selected2 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric"])
#     icons=['activity', 'eye-fill', "check2-circle"]
#     menu_icon="cast", default_index=0, orientation="horizontal")
#     st.subheader("Language")
#      if selected == "Demo" or "Info":
#         selected0 = option_menu(None, ["English", "Myanmar"],
#                                 icons=['translate'],
#                                 menu_icon="cast", default_index=0, orientation="horizontal")
#  if selected0 == "English":
#              main()


if __name__ == "__main__":
    main()

st.text("©2022_Team_ZAC")

