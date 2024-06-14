import unittest
from main import MainApp
from llama_caller import LlamaCaller
from prompt_builder import PromptBuilder

class TestAffirmationsHelper(unittest.TestCase):
    def test_generate_affirmations(self):
        sample_goals = [
            "To get in amazing shape by my wedding day, October 14th 2024, so I look and feel my absolute best in my red wedding dress! I want to wow myself, my family and friends, and my husband with how amazing I look on my big day!",
            "To get an amazing new job that gives me financial freedom and levels me up in the world financially, and that also uses my Machine Learning skills as well as my talents for creative thinking, collaboration with a team, and ingenuity at problem solving when the pressure is on",
            "To find a dream apartment for my future husband and I! One that is affordable, in the neighborhood of Greenpoint, has outdoor space, and plenty of space inside for all of our stuff as well!"
        ]

        prompt_builder = PromptBuilder()
        prompt = prompt_builder.build_prompt(sample_goals)

        llama_caller = LlamaCaller()
        output_file_name = llama_caller.chat_with_llama_3(prompt)

        self.assertTrue(os.path.exists(output_file_name))

if __name__ == '__main__':
    unittest.main()