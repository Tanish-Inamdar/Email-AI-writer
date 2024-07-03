import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def create_email():

    sysprompt="""Hello Mathnasium Ocotillo 



    I am resending this email because David asked me to send it again.



    My name is Tanish Inamdar and I am a junior at Basis Chandler. I sending

    this email to apply for a job at the Ocotillo Mathnasium when there is an

    available position. I have taken numerous AP math courses such as Calculus

    AB and Calculus BC and I am currently taking AP statistics. I scored high in

    standardized testing with a 760 perfect score on my PSAT math section.



    I have experience with instructing and tutoring kids. I have taught younger

    kids biology as part of my schools NHS program. I have also taught an

    Intro to Debate online class and helped run my schools Debate program

    teaching Debate to younger kids.



    I have attached my resume below for more information about me. Thank you

    very much for your time and consideration.



    Sincerely,

    Tanish Inamdar"""



    def create():
        messages=[
            {"role": "system", "content": sysprompt}, ]
        
        while True:
            usrprompt = input("\n"+"What do you want your email to look like(Type Done to exit)? ")
            if usrprompt.lower() == "done":
                final = ""
                for message in messages:
                    content = message["content"]
                    final += content + "\n"
                
                return final
            
            messages.append({"role":"user", "content": usrprompt})
        
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages= messages
            )

            reply = chat_completion.choices[0].message.content
            print("\n" + reply)
            messages.append({"role":"assistant", "content": reply})
    
    final_email = create()
    return final_email



