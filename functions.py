def get_scores():
    scores = []
    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(num_subjects):
        while True:
            try:
                score = float(input(f"Enter the score for subject #{i+1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("⚠️ Score must be between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Very Good"
    elif average >= 60:
        return "Good"
    else:
        return "Poor"

def main():
    print("🎓 Student Grades Calculator")
    try:
        scores = get_scores()
        average = calculate_average(scores)
        grade = get_grade(average)

        print("\n📊 Results:")
        print(f"- Average Score: {average:.2f}")
        print(f"- Grade: {grade}")
    except Exception as e:
        print("An unexpected error occurred:", e)

main()
