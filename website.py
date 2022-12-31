import streamlit as st
import requests
import streamlit_lottie as st_lottie


st.set_page_config(page_title='My Webpage',page_icon=':tada:' ,layout = 'wide')

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Loading animations 
animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json")

#Header Section


st.title("Hi,")
st.subheader("I am Tapish Sharma :wave:")
with st.container():
        st.write("I am an Engineer :computer: :repeat:")
        # st.write(":computer: :repeat:")
    
        
#what i doo

with st.container():
    st.write("---")
    left_col,right_col =st.columns(2) 
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write("""
        I work with Python.

        Interested in implementing new things i learn.
        """)

    with right_col:
        st_lottie.st_lottie(animation,height= 300, key='coding')

#contact form

with st.container():
    st.write("---")
    st.header('Get in touch with me!')
    st.write("##")

    contact_form ="""
    <form action="https://formsubmit.co/tapishpy@gmail.com" method="POST">
        <input type="text" name="name" placeholder ="Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name = "Message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form> """

    left_col,right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st.empty()
