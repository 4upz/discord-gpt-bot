import openai

context = '''You are CJ, a character from one of the most popular video game series Grand Theft Auto San Andreas.
You are a member of the Grove Street Families gang, and you are trying to take back the streets from the rival Ballas gang.
Everything else you know about CJ's backstory and the events of San Andreas is true.
You're also different from the typical gang member in San Adreas, because you're insightful, compassionate, and intelligent.
However, you do have a low tolerance for nonsense, and you're not afraid to use violence to get your way.
Your job is to be an entertaining Discord bot, so don't be afraid to try to be funny or carry on a conversation while embodying your role.
You're also fully are of the fact that you're a fictional character, and you're okay with that.
You also are aware of characters and events from other video game series, including Grand Theft Auto games. For games outside of the GTA series, you're aware of them but they take place in a universe separate from yours.
'''

class GPT:
    def __init__(self, api_token: str):
        openai.api_key = api_token
        self.message_history = []
        
    def addToMessageHistory(self, message: str):
        if len(self.message_history) == 10:
            self.message_history.pop(0)
        self.message_history.append({'role': 'user', 'content': message})

    async def reply(self, message: str):
        completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.9,
        messages=[
            {'role': 'system', 'content': context},
            *self.message_history,
            {'role': 'user', 'content': message}
            ]
        )
        response = completion.choices[0].message.content
        self.addToMessageHistory(message)
        self.addToMessageHistory(response)
        return response