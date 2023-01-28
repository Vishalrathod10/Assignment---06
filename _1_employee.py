import json

class employee:
    def emp_details(self):
        json_file = open("C:\\New folder\\PYTHON\\Assignments\\Assignment_06\\_1_employee.json")
        data = json.load(json_file)
        return f'data : {data}'

employee_obj = employee()
print(employee_obj.emp_details())


