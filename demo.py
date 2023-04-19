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
            height:130px;
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
            <img src="data:image/png;base64,{logo_base64}" style="margin-top:20px; margin-left:30px; max-height: 100%; object-fit: contain; margin-right:15px;"/>
        </div>  
        <div style="display:flex;align-items:center;margin-left:auto; top: 50%;">
            <a href="/" style="text-decoration:none; padding-top:40px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="100" viewBox="0 0 24 24" fill="none" stroke="#2953B3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
            </a>
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
