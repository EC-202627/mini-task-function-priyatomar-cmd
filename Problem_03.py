def calculate_fine():
    book_title=input()
    days_overdue=int(input())
    max_fine=3.75
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    fine=float(days_overdue*max_fine)
    print("Fine: Rs.",fine)
    print("You have accumulated the maximum fine of INR:",fine)
c=calculate_fine()
