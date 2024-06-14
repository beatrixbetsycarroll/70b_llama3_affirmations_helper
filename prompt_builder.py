class PromptBuilder:
    def read_long_string_from_file(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            long_string = file.read()
        return long_string

    def build_goal_section(self, goals: list) -> str:
        goal_string = "\n".join(f"Goal {i+1}: {goal}" for i, goal in enumerate(goals))
        return goal_string

    def build_prompt(self, goals: list) -> str:
        long_string = self.read_long_string_from_file('long_prompt_string.txt')
        goal_section = self.build_goal_section(goals)
        return long_string + goal_section