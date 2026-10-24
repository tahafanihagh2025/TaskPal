import sqlite3, os, time, tiktoken
from openai import OpenAI
import view_tasks


def ai_prioritize():
    """
    
    """
    allow_continue = view_tasks.view_task()
        
    if allow_continue:
        pass
    else:
        return
    
    my_conn = sqlite3.connect("taskpal_db.db")
    my_cur = my_conn.cursor()

    my_cur.execute("""SELECT * FROM Tasks;""")
    all_tasks = my_cur.fetchall()

    my_conn.commit()
    my_conn.close()

    class ChatBot():
        def __init__(self):
            self.llm = OpenAI(
                api_key=os.getenv("TP_API_KEY"),
                base_url="https://api.groq.com/openai/v1"
            )
            
            self.prompt = f"""
                Analyze the following tasks's details:
                
                    Tasks -> {all_tasks}
                    All Tasks details are as follows:
                    ID, name, description, priority(1: High, 2: Medium, 3: Low), estimatedTime (in minutes), status (out of 100 completion), createdAt, dueDate
                
                    Provide:
                    Prioritize the given tasks based off of the priority, status, dueDate and status.
                    The prioritization should be in the form of a new table created by yourself.
                    
            """
            self.messages = [
                {"role": "system", "content": self.prompt}
            ]

        def bot(self, message):

            self.messages.append({"role": "user", "content": message})

            response = self.llm.chat.completions.create(
                model="qwen/qwen3.8-27b",
                messages = self.messages,
                temperature=0.7,
                stream=True
            )

            response_text = ""
            for chunk in response:
                if chunk.choices:
                    delta = chunk.choices[0].delta.content
                    if delta:
                        print(delta, end = '', flush=True)
                        response_text += delta
                        time.sleep(0.05)

            print('')
            self.messages.append({"role": "assistant", "content": response_text})

            return response_text


        def chat(self):
            encoding = tiktoken.get_encoding("cl100k_base")

            while True:
                user_input = input("What's on your mind today? (Enter 'q' to exit!): ").strip().lower()

                if user_input == 'q':
                    print("Goodbye!")
                    break
                else:
                    token_count = len(encoding.encode(user_input))
                    print(f"Token count: {token_count}")

                    if token_count > 25:
                        print(f"You've exceeded the input token count limit, Try again! | {token_count}\n")
                        continue

                    self.bot(user_input)
                    print('')

    print("")
    print("Let's see what our adroitly trained AI Model is going to walk you through --->>>")
    print("")

    def main():
        print("=====================================================================")
        print("Hi there, Welcome to your one and only TaskPal Personal Tasks Management!")
        print("=====================================================================")
        bot = ChatBot()
        bot.chat()

    main()
