from survey import StarWarsSurvey
question = "What Character(s) from the Star Wars franchise would you want to be?"
my_survey = StarWarsSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit \n")
while True: 
    #ask for response
    response = input("Character: ")
    if response == 'q': 
        break 
    #store response in list
    my_survey.store_results(response)
    #Show results
print("\nThanks for answering the survey!") 
my_survey.show_results()