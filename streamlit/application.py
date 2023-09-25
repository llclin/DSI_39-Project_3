
import streamlit as st
import numpy as np
import time
from PIL import Image


st.title("Understanding your attachment style :smile:")
st.subheader("The application is developed to help you understand you and your partner's attachment style, and provide necessary resources to help you in your relationship.")

st.divider()

answer_1 = st.selectbox(
    '***How would you like to be contacted?***',
    ('Email', 'Home phone', 'Mobile phone'))

answer_2 = st.radio(
    "***What's your favorite movie genre***",
    ["Comedy", "Drama", "Documentary"])

answer_3 = st.text_area("***Please do share with us your recent experience with your partner.***")


if st.button('Generate my profile!'):
    with st.spinner('Wait for it...'):
        time.sleep(3)
        prediction = 1
    st.success('Done!')
    
    if prediction == 0:
       st.divider() 
       st.write("Your attachment style is ***Anxious***!")
       st.write("Anxious attachment types are often nervous and stressed about their relationships. They need constant reassurance and affection from their partner.")
       st.divider()
       
       st.write("Below are some recommendations suitable for your attachment style :wink:")
       col1, col2, col3 = st.columns(3, gap="medium")
       with col1:
           image1 = Image.open('streamlit_images/anxious_book_1.png')
           st.image(image1, width = 150, use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/6889424", use_container_width=True)

       with col2:
           image2 = Image.open('streamlit_images/anxious_book_2.png')
           st.image(image2, width = 150, use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/5901249", use_container_width=True)

       with col3:
           image3 = Image.open('streamlit_images/anxious_book_3.png')
           st.image(image3, width = 150,use_column_width="always")
           st.link_button("Click to read more","https://nlb.overdrive.com/media/5168313", use_container_width=True)
       

      
       
    else:
        st.divider()
        st.write("Your attachment style is ***Avoidant***!")
        st.write("Avoidant attachment types are extremely independent, self-directed, and often uncomfortable with intimacy. They’re commitment-phobes and experts at rationalizing their way out of any intimate situation.")
        st.divider()
        
        st.write("Below are some recommendations suitable for your attachment style :wink:")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            image1 = Image.open('streamlit_images/avoidant_book_1.jpg')
            st.image(image1, width = 150, use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Healing-Avoidant-Attachment-Style-Workbook/dp/B0C9SFXJPG/ref=sr_1_1?qid=1695651557&refinements=p_27%3AHenry+Gottman&s=books&sr=1-1", use_container_width=True)

        with col2:
            image2 = Image.open('streamlit_images/avoidant_book_2.jpg')
            st.image(image2, width = 150, use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Avoidant-Attachment-More-Effective-Relationships/dp/B0B2HWK7KD/ref=sr_1_3?crid=SD48F1UGEPHR&keywords=avoidant+attachment&qid=1695651614&s=books&sprefix=avoidant+attachment%2Cstripbooks%2C253&sr=1-3", use_container_width=True)

        with col3:
            image3 = Image.open('streamlit_images/avoidant_book_3.jpg')
            st.image(image3, width = 150,use_column_width="always")
            st.link_button("Click to read more","https://www.amazon.sg/Avoidant-Attachment-Recovery-Relationships-Unhealthy/dp/B0CHLH9WWS/ref=sr_1_5?crid=SD48F1UGEPHR&keywords=avoidant+attachment&qid=1695651689&s=books&sprefix=avoidant+attachment%2Cstripbooks%2C253&sr=1-5", use_container_width=True)

       
       
