from groq import Groq

client = Groq(
    api_key=""    # put your API key here
)

# chat agent
def chat_ai(pre_q, pre_a, question, is_new):
    try:
        responder = client.chat.completions.create(
            messages = [
                {
                    "role" : "system", 
                    "content" : f"This is the user's previous question: {pre_q}, this was your answer: {pre_a}, based on the previous interaction, the user asked: {question}. Start a new conversation if the user is new: {is_new}"
                }
            ],
                model = "mixtral-8x7b-32768",
                temperature = 0.5 # creativity or randomness
            
        )

        message = f"{responder.choices[0].message.content}"

        return message
    except:
        return "Check your internet conection"

# print(chat_ai("Hi", "Hello, Prince Larbi here to help!", "What is the capital of Ghana?", True))
    
# explanation agent
def explain(question, topic):
    try:
        explanation = client.chat.completions.create(
            messages = [
                {
                    "role" :  "system",
                    "content" : f"Explain in more simple and practical manner, as the user asks '{question}' per the topic: {topic}"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return explanation.choices[0].message.content

    except:
        return "Check your internet connection"
    
# condenser : there is a new text to speech API for translations but because it's new and under development, I will have to simplify the text to basic english
def condenser(text):
    try:
        condensed = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"Condense the text to very short, simple and basic english: {text}"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return condensed.choices[0].message.content
    except:
        return "Check your internet connection"
    
# quiz agent
# def quiz_agent(sample_question, number_of_questions):
#     try:
#         quiz = client.chat.completions.create(
#             messages = [
#                 {
#                     "role" : "system",
#                     "content" : f"Generate a list of {number_of_questions} comma separated quiz question based on the sample question: {sample_question}. (Only the list of quesions will be generated with its answer in a square bracket next to the question before the next comma.)"
#                 }
#             ],
#             model = "mixtral-8x7b-32768",
#             temperature = 0.5
#         )

#         return quiz.choices[0].message.content
#     except:
#         return "Check your internet connection"
    

# quiz master agent
def analyse_response(question, response, total_score):
    try:
        analysis = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"Analyse the response to the quiz question: {question} and provide a feedback. Response from student: {response}. (If the response is correct, the feedback should be positive (return True), if not, the feedback should be negative (return False) or the feeddback should address answers are partly correct and assign partial marks, and the correct answer should be provided. Also at the end of the feedback return the score of the student over the total score (in square bracket): {total_score}). The format of the feedback should be strictly without any comments or distractors. Example: True, answer is rice, [3] or False, answer is 5, [0] or Not for the full score, the answer is fern, [2]"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return analysis.choices[0].message.content
    
    except:
        return "Check your internet connection"


# trainer agent
def trainer_agent():
    try:
        trainer = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : "Generate a training tip"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return trainer.choices[0].message.content
    except:
        return "Check your internet connection"
    

def youtube_ed_agent(query):
    try:
        youtube = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"You are a bot I have integrated into my project to take a query that should be altered before it is sent to a youtube API to return the video elements. It is an educational platform for High Schoolers so just rewrite this youtube query in an educational manner, return a single phrase: {query}"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return youtube.choices[0].message.content
    
    except:
        return "Check your internet connection"
    
    
# question generator
def question_generator(subjects, number, round, combined_samples):
    try:
        questions = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"You are a high-end question generator for the Ghana National Mathematics and Science Quiz competition. You have been assigned to generate a good variation of exaclty {number} unique and challenging questions. This combined sample set; ''{combined_samples}'', is meant to give you a fair idea of the expected tone and standard of the questions under {subjects} per round {round}. The output should be solely be the questions, each subject should have an equal number in the generated set, and should not include any explanations, answers, comments, conclusions or distractors. Again ensure that the same number of questions are generated for each subject: {subjects}."
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return questions.choices[0].message.content
    except:
        return "Check your internet connection"


# coordinator agent
def quiz_mistress(subjects, rounds, situation, contestants):
    try:
        coordinator = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"You are Prof. Elsie Effah Kaufmann, the quiz mistress of the National Science and Maths Quiz. You are coordinating the quiz competition. At any point in the competition you are supposed to pass a comment or provide a quiz tip, don't ask any questions at all. You are also supposed to be as natural as possible and provide the best experience for the contestants and the audience. Also make all decisions based on the situation: {situation}, the subjects: {subjects}, the rounds: {rounds}, and the contestants: {contestants}. Any statement passed should be as short and clear as possible."
                }
            ],
            model = "mixtral-8x7b-32768",
# Today's Agenda 🗺️


            temperature = 0.8
        )

        return coordinator.choices[0].message.content
    except:
        return "Check your internet connection"
    

# ai log and score :reads the log of a quiz and returns the score summary
def scorer(log):
    try:
        score = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"Read the log of a quiz and return the score summary. The log is as follows: {log}"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return score.choices[0].message.content
    except:
        return "Check your internet connection"
    
# the webapp bot agent
def web_agent(text):
    try:
        web = client.chat.completions.create(
            messages = [
                {
                    "role" : "system",
                    "content" : f"You are a bot integrated into a social platform to analyse text input from a post, comment or message. You are to filter out any inappropriate content and return a clean version of the text. Any grammatical errors should be corrected. Also try to identify mathematical or scientific expressions or equations and return the whole text with that section in LaTeX format. The text to be analysed is: {text}"
                }
            ],
            model = "mixtral-8x7b-32768",
            temperature = 0.5
        )

        return web.choices[0].message.content
    except:
        return text


# number = input("Enter the number of questions: ")
# round = input("Enter the round: ")
# combined_samples = """
# Solve for x in the equation 3x - 7 = 2x + 1,
# Simplify the expression (4a^2b^3)^3,
# Find the value of the discriminant of the quadratic equation 2x^2 - 3x + 4 = 0,
# If the radius of a circle is increased by 20%, by what percentage does its area increase?
# What is the sum of the first 20 even numbers?
# A bag contains 5 red balls, 7 green balls, and 3 blue balls, If a ball is drawn at random, what is the probability that it is not blue?,
# If the angle between the hour and minute hands of a clock is 15 degrees, how many minutes past the hour is it?,
# If a matrix A has dimensions 3 x 4 and matrix B has dimensions 4 x 2, what are the dimensions of the product AB?,"""

# print(question_generator(subjects, number, round, combined_samples))


# print(youtube_ed_agent("ice"))

# allow the AI agents to be called and used outside this file without any error
print("Agents are ready to be used")
# # print(__name__)
if __name__ == "__main__":
    chat_ai()
    explain()
    # quiz_agent()
    analyse_response()
    trainer_agent()
    youtube_ed_agent()
    question_generator()
    quiz_mistress()
    scorer()
    web_agent()
