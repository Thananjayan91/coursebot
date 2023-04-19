import streamlit as st
import base64
from PIL import Image

# Load your logo image and convert it to base64


def get_image_base64(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


logo_image = "flipick_coursebot.png"  # Replace with the path to your logo image
logo_base64 = get_image_base64(logo_image)

# Define your header with the logo and home button


def custom_header(logo_base64):
    header = f'''
    <style>
        .header {{
            height:100px;
            background-color:white;
            display:flex;
            align-items:center;
            padding:0px 20px;
            position:fixed;
            top:0;
            left:0;
            right:0;
            z-index:1000;
        }}
    </style>
    <div class="header">
        <div style="display:flex;align-items:center;">
            <img src="data:image/png;base64,{logo_base64}" height="80px" style="margin-right:15px;"/>
        </div>
        <div style="margin-left:auto;">
            <a href="/" style="text-decoration:none;font-size:18px;font-weight:bold;color:#4a4a4a;">Home</a>
        </div>
    </div>
    '''
    return header


# Display the custom header in the Streamlit app
st.markdown(custom_header(logo_base64), unsafe_allow_html=True)

# Add an empty container to create space for the fixed header
st.empty()

# Your Streamlit app content goes here
st.write("Hello, world!")
