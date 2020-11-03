
class StarWarsSurvey: 

    def __init__(self, question): 
        """show a question, and prepare to store responses"""
        self.question = question 
        self.responses = []

    def show_question(self): 
        print(self.question)

    def store_results(self, new_response):

        self.responses.append(new_response)

    def show_results(self): 
        """Show all of the responses that have been added"""
        
        print("Survey Results")
        for response in self.responses: 
            print(f" - {response}")

