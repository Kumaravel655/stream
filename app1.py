import streamlit as st

st.header("hey! this is kumaravel website")
st.balloons()
picture = st.camera_input("")
if picture:
    st.image(picture)

 
# import Image from pillow to open images
from PIL import Image
 
 
if st.checkbox("you like the pic"):
 
    # display the text if the checkbox returns True value
    st.text("yeah its likes to you!")

status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")






    
