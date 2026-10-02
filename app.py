import streamlit as st

st.title("My HR Calculator")

choice = st.selectbox(
    "What do you want to do?",
    ["Sum", "Difference"]
)

x = st.number_input("Enter first number", value=0)
y = st.number_input("Enter second number", value=0)

if st.button("Calculate"):
    if choice == "Sum":
        st.success("Answer = " + str(x + y))

    elif choice == "Difference":
        st.success("Answer = " + str(x - y))
