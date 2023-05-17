from other_functions import get_employee_info
from pickle_operations import save_to_picle_file
from  pickle_operations import read_pickle_file

employees_data_file = "employees_data.pkl"
employees = []

employees.append(get_employee_info())
employees.append(get_employee_info())
employees.append(get_employee_info())

save_to_picle_file(employees,employees_data_file)

print(read_pickle_file(employees_data_file))

