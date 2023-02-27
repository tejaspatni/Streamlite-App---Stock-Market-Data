import streamlit as st

st.title("Stock Market Data App")
st.snow()

btn_click = st.button("Click and start trading")

if btn_click == True:
    st.subheader("Welcome to the world of Stock Market trading")