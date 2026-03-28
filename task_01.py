def calculate_fine():
    book_title=input()
    days_overdue=input()
    print(f"Book : {book_title}")
    print(f"Days overdue : {days_overdue}")
    fine=float(days_overdue)*5
    print("Fine : Rs.",fine)
c=calculate_fine()    

