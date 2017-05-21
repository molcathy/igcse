coach = 550
entry_ticket = 30

students = int(input("How many students?"))

total_tickets_price = students * 30

coach_per_student = coach//students


if students > 9:
    total_tickets_price - 30

elif students > 19:
    total_tickets_price - 60

if students > 29:
        total_tickets_price - 90

elif students > 39:
    total_tickets_price - 120

tickets_price = total_tickets_price // students

students_pay = tickets_price + coach_per_student

if students > 45:
    print ("Students should not be more than 45")

elif students < 46:
    print ("Each student should pay,",students_pay," pounds")
