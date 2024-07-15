import streamlit as st

import random

st.title('Welcome to Number Guessing Game')

st.write('### where you guess a number ')

st.write('Choose either 1-4 or 5-8')

num = random.randrange(1, 4)
txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

num1 = random.randrange(5, 8)
txt_guess1 = int(st.text_input('Enter a number between 5 and 8: ', 5))

btn_one = st.button('1-4')
btn_two = st.button('5-8')
if btn_one:
    num = random.randrange(1, 4)
    txt_guess = int(st.text_input('Enter a number between 1 and 4: ', 1))

else:
    num1 = random.randrange(5, 8)
    txt_guess1 = int(st.text_input('Enter a number between 5 and 8: ', 5))

btn_start = st.button('Start Again')

btn_guess = st.button('Make Guess')

if btn_guess:

    if txt_guess == num or txt_guess1 == num1:

        st.write('You Win')
        st.balloons()
    
    else:
        html_str = f""" <h1 style='text-align: left; color: #FF4433;'> Sorry. Try again. </h1> """

        st.markdown(html_str, unsafe_allow_html=True)

st.write('The number is', num, 'or', num1)

with st.expander("Help..."):

    st.write('''

    Press Start and a random number between 1 and 10 will be generated.

    Try to guess the number by entering your guess in the text box and

    clicking "Make Guess"

    ''')
