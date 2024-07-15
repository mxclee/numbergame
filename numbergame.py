import streamlit as st

import random

st.title('Welcome to Number Guessing Game')

st.write('### where you guess a number ')

 

num = random.randrange(1, 4) 

txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

num1 = random.randrange(5, 8)

txt_guess = int(st.text_input('Enter a number between 5 and 7: ', 5))

btn_start = st.button('Start Again')

btn_guess = st.button('Make Guess')

if btn_guess:

    if txt_guess == num or txt_guess == num1:

        st.write('You Win')

        st.balloons()

    else:
        html_str = f""" <h1 style='text-align: left; color: #FF4433;'> Sorry . Try again. </h1> """

        st.markdown(html_str, unsafe_allow_html=True)

btn_show = st.button('Show Number')

if btn_show:

    st.write('The number is ', num)

with st.expander("Help..."):

    st.write('''

    Press Start and a random number between 1 and 10 will be generated.

    Try to guess the number by entering your guess in the text box and

    clicking "Make Guess"

    ''')
