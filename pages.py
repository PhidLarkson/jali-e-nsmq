import streamlit as st
import json, re, PyPDF2
import os
import time
from data import management
import time
from integrations.agents import *
from integrations.ghana_nlp import *
from integrations.internet_test import *
import random
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np


with open("data/configurations/student.json", "r") as file:
    data =  json.load(file)

# stream effect
def stream_data(stream):
    for word in stream.split(" "):
         yield word + " "
         time.sleep(0.02)

# saving AI conversations to a json file with AI and USER tags with timestamps
def save_conv(user, ai, timestamp):
    with open("data/conversations/conversations.json", "a") as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        json.dump({"user": user, "ai": ai, "timestamp": timestamp}, file)


# read last section in json file
def read_convo():
    with open("data/conversations/conversations.json", "r") as file:
        data = json.load(file)
        return data


def home():
    # authenticator.login()
    st.title("The JALI PROJECT NSMQ")

    tab1, tab2, tab3 = st.tabs(["Home", "About", "Credits"])

    with tab1:
        st.title("This is the homepage")

        # Information section about the tool
        st.header("What is NSMQ JALI?")
        st.markdown(
            """NSMQ JALI is an open-source, AI-powered platform designed to empower students of all backgrounds to excel in the Ghana National Maths & Science Quiz competition. 

            We address the existing inequities in access to quality NSMQ training by providing a free, comprehensive suite of resources:

                * Practice drills and quizzes: Sharpen your skills with a vast database of questions categorized by topic and difficulty level.
                * AI-powered learning: Get personalized study recommendations based on your strengths and weaknesses.
                * Explanatory videos and tutorials: Gain a deeper understanding of complex concepts with interactive learning materials.
                * Community forum: Connect with fellow students and educators, share tips, and ask questions."""
        )

        # Equity and impact section
        st.header("Bridging the Gap in NSMQ Training")
        st.write(
            """Many schools lack the resources, facilities, and specialized platforms needed for optimal NSMQ preparation. NSMQ Ace aims to bridge this gap by offering:

                * Accessibility: Free and open-source, accessible from any device with internet access.
                * Equity: Levels the playing field by providing quality training regardless of location or school resources.
                * Empowerment: Provides students with the tools and knowledge to compete at the highest level."""
        )

    with tab2:
        st.title("About")
        st.write("The JALI Project is an initiative to improve access to quality education in Ghana. Our team of developers and educators are committed to creating innovative solutions to address the challenges faced by students and educators in the country.")
        st.write("---")
        st.write("Our Vision:")
        st.write("To create a world where every student has access to quality education and the opportunity to reach their full potential.")
        st.write("---")
        st.write("Our Mission:")
        st.write("To empower students and educators with the tools and resources they need to succeed in the classroom and beyond.")
        st.write("---")
        
    with tab3:
        st.write("Credits")
        st.balloons()
        st.write("This project was developed by the JALI team, a group of passionate developers and educators committed to improving access to quality education in Ghana. We are grateful to our partners and sponsors for their support in making this project a reality.")
        st.write("---")
        st.write("Team:")
        st.write("Prince Larbi")
        st.write("Samuel Nadutey")
        st.write("Noeline Mensah")
        st.write("Thompson Emmanuel")

        st.write("---")

        st.write("Partners:")
        st.write("WIKITECH KNUST")

def student_profile():
    # authenticator.login()
    st.title(f"Welcome, :blue[{data['name']}.]")

    tab1, tab2, tab3, tab4 = st.tabs(["Study Space", "Resources and Notes", "Analytics", "Help"])

    with tab1:
        # Research section:pages
        pages = st.sidebar.selectbox("Select", ["Note taking", "AI buddy", "Settings"])
        # st.sidebar.write("Pages")

        if pages == "Note taking":
            st.sidebar.write("---")
            # st.sidebar.write("Upload and study")
            document = st.sidebar.file_uploader("Upload a document", type=["pdf"])

            if document is not None:
                reader = PyPDF2.PdfReader(document)
                pages = len(reader.pages)
                page_number = st.sidebar.number_input("Enter a page number", min_value=1, max_value=pages)

                page = reader.pages[page_number]
                topic = page.extract_text()
                
                st.write(topic)          

            options = st.sidebar.selectbox("Select an option", ["Typed", "Written"])

            if options == "Typed":
                st.write("This is the typed option")

                note_title = st.text_input("Title of the note")
                note = st.text_area("Take a note...", height=100)

                # save record to note record text file
                

                if st.button("Save"):
                    with open(f"data/notes/note_record.txt", "a") as file:
                        file.write(note_title + "\n")

                    with open(f"data/notes/{note_title}.txt", "a") as file:
                        file.write(note + "\n")
                    st.success("Note saved successfully!")

            if options == "Written":
                # Specify canvas parameters in application
                drawing_mode = st.sidebar.selectbox(
                    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
                )

                stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
                if drawing_mode == 'point':
                    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
                stroke_color = st.sidebar.color_picker("Stroke color hex: ")
                bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
                bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

                realtime_update = st.sidebar.checkbox("Update in realtime", True)

                                # Create a canvas component
                canvas_result = st_canvas(
                    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
                    stroke_width=stroke_width,
                    stroke_color=stroke_color,
                    background_color=bg_color,
                    background_image=Image.open(bg_image) if bg_image else None,
                    update_streamlit=realtime_update,
                    height=600,
                    width= 600,
                    drawing_mode=drawing_mode,
                    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
                    key="canvas",
                )

                download = st.button("Show and download")

                if download:
                    if canvas_result.image_data is not None:
                        st.image(canvas_result.image_data)
                    if canvas_result.json_data is not None:
                        objects = pd.json_normalize(canvas_result.json_data["objects"])
                        for col in objects.select_dtypes(include=['object']).columns:
                            objects[col] = objects[col].astype("str")
                        st.dataframe(objects)

                    #loading sign
                    with st.spinner("Downloading..."):
                        time.sleep(1)
                        with open(f"data/notes/{random.randint(100000, 999999)}.png", "wb") as file:
                            file.write(canvas_result.image_data)
                        st.write("Download complete!")
                        st.success("Image saved successfully!")
                   


        if pages == "AI buddy":
            question = st.chat_input("Ask a question...")
            keep_conversation = st.sidebar.checkbox("Keep the conversation going") 

            upload_pdf = st.sidebar.file_uploader("Upload a pdf file", type=["pdf"])
            if upload_pdf is not None:
                reader = PyPDF2.PdfReader(upload_pdf)
                pages = len(reader.pages)
                page_number = st.sidebar.number_input(f"There are {pages} pages. Select a page", min_value=0, max_value=pages)

                st.sidebar.write("---")
                st.sidebar.write("Options")
                languages = {
                    1 : ["en-tw", "Twi"],
                    2 : ["en-fat", "Fante"],
                    3 : ["en-ki", "Kikuyu"],
                    4 : ["en-luo", "Luo"],
                    5 : ["en-mer", "Kimeru"],
                    6 : ["en-ee", "Ewe"],
                    7 : ["en-dag", "Dagbani"],
                    8 : ["en-yo", "Yoruba"],
                    9 : ["en-gaa", "Ga"]

                }
                                
                lang_choice = st.sidebar.selectbox("Select a language to translate to:", list(languages.values()), format_func=lambda x: x[0])
                translate =  st.sidebar.checkbox("Translate")
                audio = st.sidebar.checkbox("Audio")

                try:
                    page = reader.pages[page_number]
                    highligter = st.sidebar.slider("Highlight the text", 0, 5000, 50, 100)
                    topic = page.extract_text()[0:highligter]
                    
                    st.write(topic)

                    if question:
                        with st.chat_message("USER"):
                            st.write_stream(stream_data(question))
                        with st.spinner("Thinking..."):
                            message = explain(question, topic)
                            st.write_stream(stream_data(message))

                            if translate:
                                topic = condenser(topic)
                                print(topic)
                                print(lang_choice[0])
                                t = translation(topic, lang_choice[0])
                                print(t)
                                with st.spinner("Translating..."):
                                    with st.chat_message("AI"):
                                        st.write_stream(stream_data(t))
                            if audio:
                                audio = convert_text_to_speech(t)
                                # if response.status_code == 200:
                                with open('output.mp3', 'wb') as f:
                                    f.write(audio.content)
                                print("Audio file saved as output.mp3")
                                st.success("Audio file saved as output.mp3")                            
                                with st.spinner("Converting to audio..."):
                                    st.audio("output.mp3") 
                except:
                    st.write("...")
                    t = translation("Hello, how are you?", "en-tw")
                    st.write(t)

            else:
                with st.chat_message("AI"):                
                    message = chat_ai("Hi", "Hello, Prince Larbi here to help!", question, keep_conversation)
                    st.write_stream(stream_data(message))            
            

        if pages == "Settings":
            st.write("Settings")
            st.write("https://www.youtube.com/")
            st.audio("hello.mp3")

            # record audio
            audio = st.audio

            sample_rate = 44100  # 44100 samples per second
            seconds = 1  # Note duration of 2 seconds
            frequency_la = 440  # Our played note will be 440 Hz
            # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
            t = np.linspace(0, seconds, seconds * sample_rate, False)
            # Generate a 440 Hz sine wave
            note_la = np.sin(frequency_la * t * 2 * np.pi)
            st.audio(note_la, sample_rate=sample_rate)


    with tab2:
        file = st.file_uploader("Upload the file", accept_multiple_files=False)
        if file is not None:
            file_name = st.text_input("Name the file...")
            if file_name:
                management.uploader(file, file_name)
                st.write(management.uploader(file, file_name))
                # clear the filename input field
                file_name = None
                
            else:
                st.write("Please enter a file name.")
        else:
            st.write("No file uploaded.")
        # with open(f'data/resources/{file_name}', "w") as f:
            
        with open('data/resources/record.txt', 'r') as f:
            books = f.read()
            # print(books)
            books = re.split(r',', books) 
            st.write("---")
            st.caption("Files you saved")     
            st.write(books)

        with open("data/notes/note_record.txt", "r") as f:
            note_titles = f.read()
            note_titles = re.split(r'\n', note_titles)
            st.write("---")
            st.caption("Your notes")
            # st.write(note_titles)

            # if note_titles != [""]:
            # for note_title in note_titles:
            if note_titles is not None:
                # index = note_titles.index(note_title)
                # print(index)
                # return the key as the index of the note title in the list
                for index, note_title in enumerate(note_titles):
                    if note_title != "":
                        if st.button(note_title, key=index):
                            with open(f"data/notes/{note_title}.txt", "r") as file:
                                        notes = file.read()
                                        notes = re.split(r'\n', notes)
                                        st.write("---")
                                        st.caption("Your notes")
                                        for note in notes:
                                            st.write(note)



