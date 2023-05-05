import streamlit as st
import base64
from PIL import Image
from langchain import OpenAI
import streamlit as st
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, QuestionAnswerPrompt, LLMPredictor, ServiceContext
import os
import openai
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path
from llama_index import download_loader
from st_pages import Page, Section, show_pages, add_page_title

# Load your logo image and convert it to base64


hide_menu_style = """
        <style>
        #MainMenu {display:none;}
        [data-testid="stHeader"]>header {{
        display:none !important;
        }}
        .css-hqnn1b{display:none !important;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


def get_image_base64(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


# Replace with the path to your logo image
logo_image = "pages/flipick_coursebot.png"
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
            top:-40px;
            left:0;
            right:0;
            z-index:1000;
        }}
    </style>
    <div class="header">
        <div style="display:flex;align-items:center;">
            <img src="data:image/png;base64,{logo_base64}" style="margin-top:40px; margin-left:50px; max-height: 100%; object-fit: contain; margin-right:15px;"/>
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

# # Your Streamlit app content goes here
# # st.set_page_config(page_title=None, page_icon=None,
# #                    layout="wide", initial_sidebar_state="collapsed")
# # openai.api_key = os.getenv("API_KEY")
# # st.title("CourseBot")
# # st.caption("AI-powered course creation made easy")
# # DATA_DIR = "data"

# # PDFReader = download_loader("PDFReader")

# # loader = PDFReader()


# # def save_uploaded_file(uploaded_file):
# #     with open(os.path.join(DATA_DIR, uploaded_file.name), "wb") as f:
# #         f.write(uploaded_file.getbuffer())


# # # Get a list of available index files in the data directory
# # index_filenames = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]

# # cole, col1, col2, col3 = st.tabs(["⚪ __Upload Chapter__  ", "⚪ __Filter Table of Contents__  ",
# #                                  "⚪ __Extract and Edit Content__  ", " ⚪ __Export Generated XML__  "])


# # uploaded_file = cole.file_uploader(
# #     "Upload a Chapter as a PDF file", type="pdf")

# # # cola, colb = st.columns([6,1],gap="small")
# # if uploaded_file is not None:
# #     # Save the uploaded file to the data directory
# #     save_uploaded_file(uploaded_file)
# #     st.success("It would take a while to index the books, please wait..!")

# #     # Create a button to create the index
# #     # if st.button("Create Index"):
# #     # Get the filename of the uploaded PDF
# #     pdf_filename = uploaded_file.name

# #     # Load the documents from the data directory
# #     documents = loader.load_data(file=Path(f"data/{pdf_filename}"))

# #     # Create the index from the documents
# #     index = GPTSimpleVectorIndex.from_documents(documents)

# #     # Save the index to the data directory with the same name as the PDF
# #     index.save_to_disk(os.path.join(
# #         DATA_DIR, os.path.splitext(pdf_filename)[0] + ".json"))
# #     st.success("Index created successfully!")


# # if index_filenames:
# #     # If there are index files available, create a dropdown to select the index file to load
# #     index_file = cole.selectbox(
# #         "Select an index file to load:", index_filenames, label_visibility="collapsed")
# #     index_path = os.path.join(DATA_DIR, index_file)
# #     llm_predictor = LLMPredictor(llm=OpenAI(
# #         temperature=0, model_name="text-davinci-003", max_tokens=512))
# #     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# #     index = GPTSimpleVectorIndex.load_from_disk(
# #         index_path, service_context=service_context)
# # else:
# #     # If there are no index files available, prompt the user to upload a PDF file
# #     st.warning(
# #         "No index files found. Please upload a PDF file to create an index.")


# # toc = cole.button("Load Chapter")
# # try:
# #     if toc:
# #         toc_res = index.query(
# #             f"Generate a full table of contents for this book in a json format ")
# #         str_toc = str(toc_res)
# #         print(str_toc)
# #         json_output = json.loads(str_toc)
# #         table_of_contents = json_output["Table of Contents"]
# #         if "table_of_contents" not in st.session_state:
# #             st.session_state.table_of_contents = table_of_contents
# #         st.success("Chapter loaded, Go to the next tab")

# #     st.write("")
# #     # st.write()

# #     if "selected_items" not in st.session_state:
# #         st.session_state.selected_items = []
# #     col1.warning("Select the Neccessary topics and go the next page")

# #     quer = col2.button("Extract Selected")
# #     # download = col3.button("Download XML")
# #     # col3.write("")

# #     for item in st.session_state.table_of_contents:
# #         for title, content in item.items():
# #             if col1.checkbox(title):
# #                 if title not in st.session_state.selected_items:
# #                     st.session_state.selected_items.append(title)

# #     if quer:
# #         chapter_contents = {}
# #         for title in st.session_state.selected_items:
# #             chapter_content = index.query(
# #                 f"Extract the contents under the title {title}")
# #             chapter_contents[title] = chapter_content.response

# #         if chapter_contents:
# #             # sav = col2.button("Save Edits")
# #             st.session_state.selected_chapters = chapter_contents

# #             # with col2.expander("Edit PDF Content"):

# #         for title, content in st.session_state.selected_chapters.items():
# #             col2.markdown(f"**Title: {title}**")
# #             content_key = f"{title}_content"
# #             if content_key not in st.session_state:
# #                 st.session_state[content_key] = content
# #             content_value = col2.text_area(
# #                 label="Content", value=st.session_state[content_key], key=content_key)

# #         root = ET.Element("chapter")
# #         for key, value in st.session_state.selected_chapters.items():
# #             if key == "1.1 Objectives":
# #                 topic_name = "objectives"
# #                 topic_content = "objectives_content"
# #             else:
# #                 topic_name = "topic_name"
# #                 topic_content = "topic_content"

# #             topic = ET.SubElement(root, topic_name)
# #             topic.text = key
# #             contents = ET.SubElement(root, topic_content)
# #             contents.text = value

# #         # if col2.button("Save XML"):
# #             xml_string = ET.tostring(root)
# #             # Use minidom to pretty print the XML string
# #             pretty_xml = minidom.parseString(xml_string).toprettyxml()

# #         with st.expander("XML content"):
# #             col3.write(pretty_xml)

# # except AttributeError:
# #     st.warning(
# #         "Click on load chapter first and select the required Topics to extract")