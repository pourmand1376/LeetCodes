# https://leetcode.com/discuss/interview-experience/2122483/find-max-number-of-days-for-which-a-person-can-go-for-vacation
# this was an interview question for me. 
# I couldn't solve it for the first time in O(n)
# I still can not understand why this works! 

# pto = paid time off
def find_max_vacation_days(calendar, pto):
    print(calendar)
    print(f"Paid time off in days {pto}")

    left, holiday_count = 0,0
    for right in range(len(calendar)):
        print(f"Left: {left}, Right: {right}, Count: {holiday_count}")
        if calendar[right].lower() == 'w':
            holiday_count += 1
        if holiday_count > pto:
            if calendar[left].lower() == 'w':
                holiday_count -= 1
            left += 1

    return right - left + 1

print(find_max_vacation_days(['H','W','W','H','H','W'],1))
print(find_max_vacation_days(['H','H','H','W','W','W','W'],3))
print(find_max_vacation_days(['W','W','H','W','H','W','W','W','W','W','W','W'],2))
