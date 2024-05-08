import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


#set app to wide mode
st.set_page_config(layout='wide')
#create a header
st.title("AIblogcraft: Your AI article companion")

#create a subheader
st.subheader("How can I craft perfect blog with help of AI- Your article creator AIblogcraft")

#creating sidebar for the project
with st.sidebar:
    st.title("Please Input your blog details")
    st.subheader("Enter the details of the blog you want to generate")

    

    #Blog title
    blog_title=st.text_input("Blog title")

    #Blog keywords
    blog_keywords=st.text_area("Keywords")

    #Number of words 
    num_words=st.slider("Number of words",min_value=250,max_value=1000,step=250)

    prompt_part=[
        f"Generate a comprehensive, engaging blog post relevant to the given \"{blog_title}\" and \"{blog_keywords}\" . The blog should be approximately {num_words} in length suitable for an online auidence .Ensure the content is original and maintain consistency tone througout."
        ]

    response=model.generate_content(prompt_part)
    #submit button
    submit_button=st.button("Generate Blog")

if submit_button:
    st.write(response.text)
