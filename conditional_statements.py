# Project: Movie Ticket Booking System

try:
    age = int(input("Enter your age: "))
    time_of_day = input("Is it morning or evening? ").strip().lower()
    is_student = input("Do you have a student ID? (yes/no): ").strip().lower()

    ticket_price = 0

    if age < 12:
        ticket_price = 40
    elif 12 <= age <= 18:
        if is_student == "yes":
            ticket_price = 50
        else:
            ticket_price = 70
    elif 19 <= age <= 60:
        ticket_price = 100
    else:  # age > 60
        ticket_price = 60

    if time_of_day == "evening":
        ticket_price += 20

    print(f"Your total ticket price is: {ticket_price} EGP")

except ValueError:
    print("Invalid input. Please enter numbers for age and correct text for other fields.")
