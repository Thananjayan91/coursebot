import streamlit as st
import base64
from PIL import Image

# Load your logo image and convert it to base64


def get_image_base64(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


logo_image = "your_logo.png"  # Replace with the path to your logo image
logo_base64 = get_image_base64(logo_image)

# Define your header with the logo, tagline, and home button


def custom_header(logo_base64, tagline):
    header = f'''
    <div style="height:100px;background-color:#f0f2f6;display:flex;align-items:center;padding:0px 20px;">
        <div style="display:flex;align-items:center;">
            <img src="data:image/png;base64,{logo_base64}" height="80px" style="margin-right:15px;"/>
            <h2 style="margin:0;">{tagline}</h2>
        </div>
        <div style="margin-left:auto;">
            <a href="/" style="text-decoration:none;font-size:18px;font-weight:bold;color:#4a4a4a;">Home</a>
        </div>
    </div>
    '''
    return header


tagline = "Your Tagline"  # Replace with your tagline

# Display the custom header in the Streamlit app
st.markdown(custom_header(logo_base64, tagline), unsafe_allow_html=True)

# Your Streamlit app content goes here
st.write("Hello, world!")
