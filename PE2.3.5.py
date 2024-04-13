class Employee:
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_number = employee_number
    
    def get_name(self):
        return self.__name
    
    def get_emp_number(self):
        return self.__employee_number
    
    def set_name(self, name):
        self.__name = name
    
    def set_emp_number(self, employee_number):
        self.__employee_number = employee_number

class EmployeeWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
    
    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

def main():
    member_of_staff = EmployeeWorker("", "", 0, 0.0)
    
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    member_of_staff.set_name(input("Enter employee name: "))
    member_of_staff.set_emp_number(input("Enter employee number: "))
    member_of_staff.set_hourly_pay_rate(float(input("Enter hourly pay rate: ")))
    member_of_staff.set_shift_number(int(input("Enter shift number: ")))

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", member_of_staff.get_name())
    print("Employee Number:", member_of_staff.get_emp_number())
    print("Shift Number:", member_of_staff.get_shift_number())
    print("Pay Rate:", member_of_staff.get_hourly_pay_rate())

main()
