# Дан словарь с датой:
#
# {
# 	'year' : '2025',
# 	'month': '12',
# 	'day'  : '31',
# }
# Из элементов этого словаря соберите дату в следующем формате:
#
# '2025-12-31'

dict_ = {'year': '2025', 'month': '12', 'day': '31'}
print_year = dict_['year']
print_month = dict_['month']
print_day = dict_['day']
print("'", print_year, "-", print_month, "-", print_day, "'", sep="")
