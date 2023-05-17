# https://leetcode.com/discuss/interview-experience/2122483/find-max-number-of-days-for-which-a-person-can-go-for-vacation
# this was an interview question for me. 
# I couldn't solve it for the first time in O(n)

# pto = paid time off
def find_max_vacation_days(calendar, pto):
    left, holiday_count = 0,0
    for right in range(len(calendar)):
        if calendar[right] == 'W':
            holiday_count += 1
        if holiday_count > pto:
            if calendar[left] == 'W':
                holiday_count -= 1
            left += 1

    return right - left + 1

# this is my solution
def find_max_vacation_days2(calendar, pto):
    left,right = 0,0
    used_pto =0
    max_holidays = 0
    while right < len(calendar):
        # if it is holiday right can go ahead
        if calendar[right] == 'H':
            right += 1
        # if it is Working day. Right can only go ahead if there is pto left to be used
        if calendar[right] == 'W' and used_pto < pto:
            used_pto += 1
            right += 1

        # if there is no pto left to be used. Left should go ahead until there opens up a spot 
        if used_pto >= pto:
            if calendar[left] == 'W':
                used_pto -= 1
            left += 1
        
        max_holidays = max(max_holidays, right - left + 1)

    return max_holidays

    
print(find_max_vacation_days(['H','W','W','H','H','W'],1))
print(find_max_vacation_days2(['H','W','W','H','H','W'],1))
print(find_max_vacation_days(['H','H','H','W','W','W','W'],3))
print(find_max_vacation_days2(['H','H','H','W','W','W','W'],3))
print(find_max_vacation_days(['W','W','H','W','H','W','W','W','W','W','W','W'],2))
print(find_max_vacation_days2(['W','W','H','W','H','W','W','W','W','W','W','W'],2))
