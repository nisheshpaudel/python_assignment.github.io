week_days = [{'day':'Wednesday', 'day_number':4, 'status':'WORKDAY 3'},{'day':'Friday', 'day_number':6, 'status':'WORKDAY 5'}, {'day':'Monday', 'day_number':2, 'status':'WORKDAY 1'}, {'day':'Saturday', 'day_number':7, 'status':'HOLIDAY 1'}, {'day':'Tuesday', 'day_number':3, 'status':'WORKDAY 2'}, {'day':'Sunday', 'day_number':1, 'status':'HOLIDAY 2'}, {'day':'Thursday', 'day_number':5, 'status':'WORKDAY 4'}]
print("Original list of days in a week :")
print(week_days)
sorted_week_days = sorted(week_days, key = lambda x: x['status'])
print("\nSorting the list of days in a week in the dictionary :")
print(sorted_week_days)