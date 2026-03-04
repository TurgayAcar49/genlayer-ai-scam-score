class ScamScore:

    def __init__(self):
        self.scores = {}

    def analyze_project(self, project_name: str):

        prompt = f"""
        Analyze this crypto project and give a scam risk score from 0 to 100.
        Only return a number.
        Project: {project_name}
        """

        ai_response = call_ai_oracle(prompt)

        self.scores[project_name] = ai_response
        return ai_response
