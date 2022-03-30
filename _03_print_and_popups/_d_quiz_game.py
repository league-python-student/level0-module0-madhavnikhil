from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    Score = 0

    ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    Question = simpledialog.askstring(title=window, prompt="How much is 2.3 times 6.8?")
    #      // 3.  Use an if statement to check if their answer is correct
    if Question == "15.64" :
        messagebox.showinfo(title=window, message="You are correct.")
    #      // 4.  if the user's answer was correct, add one to their score
        Score = Score+1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    Questiontwo = simpledialog.askstring(title=window, prompt="How much is 10.8 divided by 2")
    if Questiontwo == "5.4" :
        messagebox.showinfo(title=window, message="You are correct")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
