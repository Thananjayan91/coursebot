import streamlit as st
# import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
# from streamlit_card import card
import openai
import os
openai.api_key = os.getenv("APIKEY")
st.set_page_config(page_title="My App", page_icon=":rocket:",
                   layout="wide", initial_sidebar_state="expanded")


st.markdown(
    f"""
    <style>
    #MainMenu {{visibility: hidden;}}

    .appview-container .main .block-container{{
        padding: 2rem;
        background: radial-gradient(circle at top right, rgba(255, 0, 255, 0.1), transparent 600px ), radial-gradient(at bottom left, rgba(4, 59, 92, 0.1), transparent 600px);
    
            }}

    sidebar .sidebar-content {{
    background-color: #111 !important;
    background:radial-gradient(circle at top right, rgba(255, 0, 255, 0.2), transparent 600px )
    box-shadow: rgba(0, 0, 0, 0.15) 2.4px 2.4px 3.2px;
}}

 [data-baseweb="textarea"] {{
  box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 56px;
    border-radius: 15px;
    padding:6px;
    width:90%;
    margin-left: 10px;
    
}}

[data-testid="stMarkdownContainer"]> p {{
        font-size: 20px;
        font-weight: bold;

    }}


 [data-baseweb="select"] {{
  box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 56px;
    border-radius: 15px;
    
    
}}


[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {{
     box-shadow: rgba(17, 17, 26, 0.1) 0px 4px 16px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 56px;
    border-radius: 15px;
    padding: 27px 15px 28px 32px;
    margin-left: 10px

}}
    


    .stButton>button {{
        background: linear-gradient(to right, #9B59B6, #f63633);
        color: white;

    }}

    div.stButton > button:first-child {{
         
         box-shadow: 0 5px 15px rgba(145, 92, 182, .4);

          }}

  
    </style>
    """,
    unsafe_allow_html=True
)
# st.markdown("<style> .stTextArea > label {font-size:14px; font-weight:bold;} </style> ",unsafe_allow_html=True)

# st.markdown('<div class="circular-container">', unsafe_allow_html=True)


with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['cpu', 'lightbulb fill',
                                'bar-chart fill', 'book', 'person dash'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background": "radial-gradient(at bottom left, rgba(255, 0, 255, 0.1), transparent 500px)", "border-radius": "16px", "box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)", "backdrop-filter": "blur(5px)", "-webkit-backdrop-filter": "blur(5px)", "border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color": "Grey", "font-size": "14px", "border-radius": "50%"},
        "nav-link": {"font-size": "15px", "font-weight": "700", "border-radius": "10px", "font-color": "Grey", "text-align": "left", "margin": "10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )


# def Update_des(val):
#         return st.text_area('Description', value=val, label_visibility='visible')


if choose == "Write For Me":

    with st.container():

        st.header("Write For Me")
        col1, col2, = st.columns(2)

        x = st.empty()
        descript = x.text_area(
            "Description", label_visibility='visible', key="description", placeholder=None)
        # descript = st.text_area("Description",label_visibility='visible',key="description",placeholder=None)

        options = ['Clever', 'Humorous', 'Sarcastic']
        with col1:
            usecase = st.selectbox("Use Case",  [
                                   'Instagram', 'OnlyFans', 'Twitter Post', 'Tiktok Caption', 'NSFW Video'], label_visibility='visible')
            # output = st.text_area("Here's your Text",label_visibility='visible')
        with col2:
            tone = st.selectbox("Select Tone", options,
                                label_visibility='visible')
        y = st.empty()
        output = y.text_area("Here's your Text", label_visibility='visible')
        save = st.button("Save")

    if usecase == 'Instagram':
        variable = 'Generate an Instagram caption for an image that describes ' + \
            str(descript) + ' The caption should  be short and attention grabbing, the goal is make people excited about the post and make them engage with the post.  use sexual innuendo hashtags and emojis as needed to make it attractive as possible. '
    elif usecase == 'OnlyFans':
        variable = 'Generate an OnlyFans Mass message for the following scenario ' + \
            str(descript) + '  use explicit words, and sexual innuendo  if needed. The message should be less than 300 characters. The message should be triggering and seductive in a way to make the user reply or make a purchase. '
    elif usecase == 'Twitter Post':
        variable = 'Generate a Tweet message in less than 250 words , As a reply for the following tweet  ' + \
            str(descript) + ' The tweet should be attention grabbing, use sexual innuendo hashtags and emojis if required.  The ultimate goal is to obtain as many as interactions for the tweet. '
    elif usecase == 'Tiktok Caption':
        variable = 'Generate a caption for a tik tok video about ' + \
            str(descript) + ' The caption should  be less than 150 characters and attention grabbing, use sexual innuendo hashtags and emojis as needed to make it attractive and attention grabbing as possible'
    else:
        variable = 'Generate a video description for a video about ' + \
            str(descript) + '  use explicit words, and sexual innuendo  if needed. The message should be less than 300 characters. The message should be triggering and seductive in a way to make the user interested in watching the video.'

    query = variable + ' where the tone of the caption should sound ' + \
        str(tone) + ' .'

    if save:
        x.empty()
        with x.container():
            descript = x.text_area(
                "Description", placeholder=query, label_visibility='visible')

        outpt = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=3600,
            n=1,
            stop=None,
            temperature=0.5,
        )
        explan = outpt.choices[0].text.strip()
        # st.write(explan)
        y.empty()

        with y.container():
            output = y.text_area("Here's your Text",
                                 value=explan, label_visibility='visible')

        # descript = st.empty()
        # container(Update_des(query))
        # descript.value = query

    # st.markdown('</div>', unsafe_allow_html=True)
