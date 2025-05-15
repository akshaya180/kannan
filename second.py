import streamlit as st 
from streamlit_option_menu import option_menu 
# may 8 
# form format coding
# input statemnet for name

name=st.text_input("enter a name ")
st.write(name)


age=st.number_input("enter a age")
st.write(age)


city=st.selectbox("select your city",("madura","theni"))
st.write(city)

points=st.slider("enter your points",0,100)
st.write(points)
address=st.multiselect("enter your selection", ("madurai","theni","chennai"))
st.write(address)

st.radio("select your gender",("male","female"))
st.write
st.checkbox("et")

st.button("sumbit")

# after submit click show the table format details 


st.table({

    "name" : "AKSHAYA",
    "age": 18 
})

with st.sidebar:
     menu = option_menu(
        menu_title="My project",
        options=["Home","about","contact"],
        icons=["house","file-person","Person-lines-fill"]
        
    )
 
if menu == "Home":
    st.title("Home")
    # columns separate 
    col1,col2 = st.columns(2)
    with col1:
        st.text_input("enter name")
    with col2:
        name=st.text_input("enter")
        st.write(name)
        
        # same name not work for python display the errow msg
        # example of st.text_input("enter")
elif menu =="about" :
    st.title("about")
else:
    st.title("contact")    