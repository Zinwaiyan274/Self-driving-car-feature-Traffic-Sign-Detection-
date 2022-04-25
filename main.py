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

def cal():
    import streamlit as st

#     st.title('Traffic sign')
#     st.subheader("from the mind of Team ZAC.")

#     weight = st.number_input("Enter your weight(in Kgs)")

#     status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

#     if status == 'cms':
#         height = st.number_input('Centimeters')
#         try:
#             bmi = weight / ((height / 100) ** 2)
#         except:
#             st.text("Enter some value of height")

#     elif status == 'meters':
#         height = st.number_input('Meters')
#         try:
#             bmi = weight / (height ** 2)
#         except:
#             st.text("Enter some value of height")

#     else:
#         height = st.number_input('Feet')
#         try:
#             bmi = weight / (((height / 3.28)) ** 2)
#         except:
#             st.text("Enter some value of height")

#     if st.button('calculate BMI'):
#         st.text("Your BMI Index is {}.".format(bmi))

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


import streamlit as st
from streamlit_option_menu import option_menu

st.title('Traffic sign decection')
st.subheader("from the mind of Team ZAC.")

with st.sidebar:
    selected = option_menu("Main Menu", ["Demo", ' More info'],
        icons=['house', 'info-circle'], menu_icon="cast", default_index=1)
    selected
# horizontal Menu
selected2 = option_menu(None, ["Demostratio", "Metric" ],
    icons=['calculator', 'emoji-wink', "flag fill"],
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Metric":
    st.subheader("Comming soon due to Waii's procrastination")
if selected2 == "Demostration":
    cal()
if selected2 == "Revolution":
    st.subheader("Comming soon due to Waii's procrastination")
