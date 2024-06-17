import time
import os
import streamlit as st
import pages
from pydub import AudioSegment
from pydub.playback import play
import io
import session

# main
def stream_data(stream):
    for word in stream.split(" "):
         yield word + " "
         time.sleep(0.02)
         
# THE AI BASED NSMQ PROJECT FOR THE AFRICAIED HACKATHON
st.sidebar.title(":brain: PROJECT :blue[JALI] :green[EXTENDED]")
st.sidebar.subheader(":grey[NSMQ AI PROJECT]")
st.sidebar.write("### :blue[AfricAIEd Hackathon 2024]")
st.sidebar.caption("The goal is to build an open-source, AI powered tool to help students prepare for the Ghana National Maths and Science Quiz competition - This tool is meant to address the equity problem in NSMQ training. Some schools lack more resources, facilities and platforms for studies.")
st.sidebar.write("---")


side_page = st.sidebar.selectbox("Select page", ["Main", "Trainer", "Quiz Session"])

if side_page == "Main":
    pages.home()


if side_page == "Trainer":
    pages.student_profile()

    

if side_page == "Quiz Session":
    st.title("THE MAIN QUIZ SESSION")

    tab1, tab2 = st.tabs(["Session", "Setup"])

    

    with  tab2:
        rounds = st.multiselect("Select the quiz rounds", ["r1", "r2", "r4", "r5"])
        subjects = st.multiselect("Select the quiz subjects", ["Maths", "Biology", "Chemistry", "Physics"])
        number_of_questions = st.slider("Select the number of questions", 1, 40, 2)
        round_interval = st.slider("Select the round interval", 1, 10, 1)
        question_interval = st.slider("Select the question interval", 1, 10, 1) 

        start = st.button("Start the quiz session")

        # start
        if start: 
            st.info("The quiz session has started")

            time.sleep(1)
          

    with tab1:
       st.subheader("THE MAIN QUIZ SESSION")
       st.write(" The quiz can be set up in the next tab! ")
       st.write("The quiz session will start after the setup is done.")
       st.write("The NSMQ tune")
       st.audio("nsmq.mp3")

       if start:
              for round in rounds:
                st.info(f"Round: {round}")
                # time.sleep(round_interval)
                for subject in subjects:
                     st.info(f"Subject: {subject}")
                    #  time.sleep(question_interval)

                with st.spinner("Setting up the quiz session"):
                    time.sleep(5)
                    st.success("READY!")

                with st.spinner("Contest in session"):
                    time.sleep(5)
                    st.success("Contest in session")
                    # pick the first string from the rounds list
                    session.session(rounds[0], subjects, "The first round of the competition", ["A", "B"], number_of_questions, question_interval)  


                # session.session(round[0], subjects, "The first round of the competition", ["A", "B"], number_of_questions, question_interval)  

                st.warning("The quiz session has ended")
    
                    
                    




    
