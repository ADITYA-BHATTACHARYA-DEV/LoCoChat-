import streamlit as st

@st.experimental_dialog("Contact Me")
def show_contact_form():
    st.text_input("First Name")
    st.text_input("Last Name")
    st.text_input("Email")
    st.number_input("Phone Number")
    st.text_input("Message")
    bt=st.button("Submit 🚀 ")
    if bt:
        st.success("Message sent Successfully !!")



col1, col2 =st.columns(2, gap='small', vertical_alignment="center")


with col1:
    st.image("./assets/s.png")
with col2:
    st.title("Aditya Bhattacharya", anchor=False)

    st.write(
      
        "Aspiring Software Engineer and Developer"
    )
    if st.button("🖥️ Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("Experience & Qualification", anchor=False)
st.image("./views/Rajiv_Gandhi_Institute_of_Petroleum_Technology-removebg-preview.png",width=100)
st.write(
      
        "Undergraduate student in B.Tech Computer Science, Rajiv Gandhi Institute of Petroleum Technology ",anchor =False
    )
st.write(
    """
- Strong hands-on experience and knowledge in Python, Flutter
- Good understanding of statistical principles and their respective applications
- Excellent team-player and displaying a strong sense of initiative"""
)