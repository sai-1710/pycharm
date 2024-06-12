import streamlit as st

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

st.title("Sum of Digits Calculator")

# Input number from user
number = st.number_input("Enter a number", min_value=0, step=1, value=0)

# Calculate the sum of digits
if st.button("Calculate"):
    result = sum_of_digits(number)
    st.write(f"The sum of the digits of {number} is: {result}")
