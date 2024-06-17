# the main quiz logic and operations
import time
import os
import integrations.agents as og
import integrations.tts as tts
import integrations.stt as stt
import integrations.ringers as ringers
import time
import threading
import re

# open txt file, read questions, add to list and return the list
def sample_questions(subject, round):
    # data/samples/math/r1.txt
    with open(f"data/samples/{subject}/{round}.txt", "r") as file:
        questions = file.readlines()
        return questions

def write_questions(tag, subject, round, questions):
    with open(f"{tag}-{subject}-{round}.txt", "a+") as file:
        # questions is a single string and needs to be split into a list        
        # organise the questions by using the question numbers as starting points : break in a list eg. ["1. question", "2. question"]
        # delimiter
        delimiter_list = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. ", "11. ", "12. ", "13. ", "14. ", "15. ", "16. ", "17. ", "18. ", "19. ", "20. ", "21. ", "22. ", "23. ", "24. ", "25. ", "26. ", "27. ", "28. ", "29. ", "30. ", "31. ", "32. ", "33. ", "34. ", "35. ", "36. ", "37. ", "38. ", "39. ", "40. ", "41. ", "42. ", "43. ", "44. ", "45. ", "46. ", "47. ", "48. ", "49. ", "50. "]

        # Assuming delimiter_list is a list of strings
        delimiter_pattern = '|'.join(map(re.escape, delimiter_list))
        questions = re.split(delimiter_pattern, questions)
        print(questions)   

        for question in questions:
            # check if question is empty
            if question == "":
                continue
            else:
                file.write(question)


# to compile AI generated questions 
def compiler(subject, number, round, combined_samples):
    set = og.question_generator(subject, number, round, combined_samples)
    return set

# generate and write questiosn to respective file
def set_questions(subject, round, number, combined_samples):
    combined_samples = sample_questions(subject, round)
    questions = compiler(subject, number, round, combined_samples)
    write_questions("ai", subject, round, questions)


# the main quiz session
def session(round, subjects, situation, contestants, number_of_questions, question_interval):
    sample = sample_questions(subjects, round)
    regn = compiler(subjects, number_of_questions, round, sample)
    write_questions("ai", subjects, round, regn)
    # set the questions
    # set_questions(subjects, round, number_of_questions, subjects)

    # kaufmann address
    tts.text_to_speech(og.quiz_mistress(subjects, round, situation, contestants))
    time.sleep(1)

    # address the contestants
    tts.text_to_speech(f"Contestants, welcome to the {round}. It is time to begin the quiz session. We will start with the first question. Are you ready?")
    time.sleep(1)

    # read each question and wait for the answer in this file
    with open(f"ai-{subjects}-{round}.txt", "r") as file:
        questions = file.readlines()
        for question in questions:
            tts.text_to_speech(question)
            time.sleep(2)
            print("Who rang the bell first?")
            # check who rang the bell first
            print(ringers.output())
            if ringers.output() == 'A':
                tts.text_to_speech("Contestant A, what is your answer?")
                answer = stt.record_and_transcribe(44100, 15)
                time.sleep(15)
                feedback = og.analyse_response(question, answer, 3)
                ringer = "Contestant A"

                # return feedback

            elif ringers.output() == 'B':
                tts.text_to_speech("Contestant B, what is your answer?")
                time.sleep(15)
                answer = stt.record_and_transcribe(44100, 15)
                feedback = og.analyse_response(question, answer, 3)
                ringer = "Contestant B"
                # return feedback
            else:
                tts.text_to_speech(og.quiz_mistress(subjects, round, f"give answer to this question: {question}", contestants))
                answer = "No answer was provided"
                feedback = og.analyse_response(question, answer, 3)
                ringer = "None"

                # return "No answer was provided to", f"question: {question}"

            print(f"Question: {question}")
            print(f"Attempted by: {ringer}")
            print(f"Answer: {answer}")
            print(f"Feedback: {feedback}")

            time.sleep(5)
            # print("Next question")
            
            # pass comment based on feedback
            comment = og.quiz_mistress(subjects, round, feedback, contestants)
            tts.text_to_speech(comment)

            # write to log file
            with open("log.txt", "a+") as log:
                log.write(f"{question} - {ringer}: {answer} - {feedback}\n")

            time.sleep(5)

            # next question
            tts.text_to_speech("Next question")
            print("Next question")
            time.sleep(2)

        # end of round
        # end_remarks = og.quiz_mistress(subjects, round, "end of round", contestants)
        end_remarks = og.scorer("log.txt")
        tts.text_to_speech(end_remarks)
        time.sleep(1)
        tts.text_to_speech("End of round")


            # tts.text_to_speech(f"Your answer is {answer}")
            # time.sleep(2)




# write_questions("may", "math", "r1", ["1+1", "2+2", "3+3", "4+4", "5+5"])


if __name__ == "__main__":
    sample_questions()
    set_questions()
    write_questions()
    compiler()
    session()
