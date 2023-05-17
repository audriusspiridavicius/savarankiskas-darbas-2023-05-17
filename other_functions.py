def set_employee_info(fullname, age, job_position):
    employee = {
        "name": fullname,
        "age": age,
        "job_position": job_position
    }

    return employee


def get_employee_info():

    fullname = input("Please enter employee name/full name: ")
    age = int(input(" please enter your age: "))
    job_position = input("please enter you job position: ")

    return set_employee_info(fullname, age, job_position)