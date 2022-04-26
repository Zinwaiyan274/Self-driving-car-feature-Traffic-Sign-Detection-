

import streamlit as st
from streamlit_option_menu import option_menu


def eng():
    st.title("ကျေးဇူးပြု၍ အင်္ဂလိပ်ဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ")
def mm():
    st.title("ကျေးဇူးပြု၍ မြန်မာဘာသာစကားအတွက် ဤနေရာကိုနိုပ်ပါ။")
    st.subheader("https://share.streamlit.io/zinwaiyan274/streamlit_testing/main/main.py")
def main():
    st.subheader("from the mind of Team ZAC.")

    with st.sidebar:
        
        selected = option_menu("ပင်မစာမျက်နှာ", ["လုပ်ဆောင်ချက်", "အကြောင်းအရာ" ])
        selected = option_menu("Main Menu", ["Demo", 'Info'],
                               icons=['house', 'info-circle'], menu_icon="cast", default_index=1)

        st.subheader("💬ဘာသာစကား")
        if selected == "လုပ်ဆောင်ချက်" or "အကြောင်းအရာ":
            selected0 = option_menu(None, ["မြန်မာ", "အင်္ဂလိပ်"], orientation="horizontal")

        st.subheader("💬Language")

        if selected == "Demo" or "Info":
            selected0 = option_menu(None, ["English", "မြန်မာ"],
                                    icons=['fgngf', "translate"], orientation="horizontal")
            st.text("©2022_Team_ZAC")
        if selected0 == "အင်္ဂလိပ်":
                 eng()
        if selected0 == "မြန်မာ":
                    mm()

    if selected == "အကြောင်းအရာ":
         selected1 = option_menu(None, ["စာချုပ်", "တီထွင်သူများသို့ ဆက်သွယ်ခြင်း", "blabla", ])

    if selected == "Info":
        selected1 = option_menu(None, ["Term and con", "Developer contact", "blabla", ],
                            icons=['clipboard', 'chat-right-dots', "flag fill"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "လုပ်ဆောင်ချက်":
                selected0 = option_menu(None, ["လုပ်ဆောင်ချက်", "ကင်မရာ", "ရလဒ်" ])

    if selected == "Demo":
       selected0 = option_menu(None, ["Demonstration", "Computer Vision", " Evaluation Metric", ],
                            icons=['activity', 'eye-fill', "check2-circle"],
                            menu_icon="cast", default_index=0, orientation="horizontal")




st.text("©2022_Team_ZAC")

main()
