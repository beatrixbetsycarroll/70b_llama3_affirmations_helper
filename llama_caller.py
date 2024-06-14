from groq import Groq
import os
import datetime

class LlamaCaller:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY_AFFIRMATIONS_HELPER"))

    # def start_convo_with_llama3(self):
    #     # implementation omitted for brevity

    def chat_with_llama_3(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_file_name = f"affirmations_{timestamp}.md"

        with open(output_file_name, 'w') as output_file:
            for chunk in completion:
                if hasattr(chunk.choices[0], 'delta'):
                    content = chunk.choices[0].delta.content or ""
                    output_file.write(content)

        return output_file_name