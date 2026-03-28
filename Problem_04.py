def calculate_fine():
    book_title=input()
    days_overdue=int(input())
    extra_day=float(input())
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    fine=float(days_overdue*extra_day)
    print("Fine: Rs.",fine)
c=calculate_fine()    
