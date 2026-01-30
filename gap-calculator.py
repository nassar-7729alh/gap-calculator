#rojct name: Smart GPAcalculator & Motivator
#author: nassar future software engineer

print("the code start working")

def get_feedback(percentage):
    """
    Returns a motivational message basrd on the percentage score.
    """""
    if percentage >= 90:
        return "outstanding you are doing amazing work. keep it up"
    elif percentage >=80:
        return "great job you are very close to the top. a little more push"
    elif percentage >= 70:
        return "good effort. you are consistent, but i know you can do even beeter."
    elif percentage >= 60:
        return "passed. good, but do not settle for this. Aim higher next time"
    
    else:
        return "do not give up failure is just a stepping stone. learn form it and come back stronger"
    


def get_letter_grade(percentage):
    if percentage >=  90: return "A"
    elif percentage >= 80: return "B"
    elif percentage >= 70: return "c"
    elif percentage >= 60: return " D"
    else: return "F"


def main():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("          Welcome to nassar's smart calculator       ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    try:
        num_subjects = int(input("Enter the number of subjects:"))
    except ValueError:
        print("Invalid input please enter a number.")
        return
    total_percentage = 0


    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        try:
            #1. ask for the totale possible mark ( for example , exame out of 20 , 30 , or 100)
            max_score = float(input(" - what was the total mark for this exam? (e.g., 20, 30, 50, 10):"))


            if max_score <= 0:
                print("Error: Total mark must be greather 0.")
                continue

            # 2. ask for the user's obtained score
            user_score = float(input(f" - Hoe much did your score out of {max_score}?"))
            if user_score < 0 or user_score> max_score:
                print(f"Error: Your score must be between 0 and {max_score}.")
                continue


            # 3. calculate percentage 
            percentage = (user_score / max_score) * 100

            # 4. get feedbacka
            grade = get_letter_grade(percentage)
            massage = get_feedback(percentage)

            print(f" -> percentage: {percentage:.2f}%")
            print(f" -> grade: {grade}")
            print(f" -> feedback:{massage}")


            total_percentage += percentage

        except ValueError:
            print("Invalid input , Please enter numbers only. ")


            # 5. final results
            if num_subjects > 0: 
                final_average = total_percentage / num_subjects
                final_grade   = get_letter_grade(final_average)
                final_massage = get_feedback(final_average)




                print("\n++++++++++++++++++++++++++++++++++++++++++++")
                print("                Final Results                 ")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print(F"Overall Average: {final_average:.2f}%")
                print(F"Final Grade: {final_grade}")
                print(F"Nassar's Advice: {final_massage}")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
if __name__ == "__main__":
 main()
      


       
                          