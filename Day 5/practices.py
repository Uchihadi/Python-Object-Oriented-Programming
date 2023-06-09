class NameLengthException(Exception):
    pass
class EmployeeIdException(Exception):
    pass
class Employee:
    __trials=0
    def __init__(self,emp_id,emp_name):
        self.__emp_name=emp_name
        self.__emp_id=emp_id
        
    def validate_name(self):
        try:
            if(len(self.__emp_name) < 4):
                Employee.__trials=Employee.__trials+1
                raise NameLengthException
            if( not(self.__emp_id.startswith('E'))):
                raise EmployeeIdException
        except NameLengthException:
            Employee.__trials=Employee.__trials+1
            print(Employee.__trials)
        except EmployeeIdException:
            Employee.__trials=Employee.__trials+1
            print(Employee.__trials)
            
emp1=Employee('E1001','Tom')
emp1.validate_name() #Once the method has been invoked, the __trials count continues to the next function
emp2=Employee('1001','Tomy')
emp2.validate_name() #__trials starts at 2, carried on from the previous function

# ---------------------------------------------------------------

class NotEligibleException(Exception):
    pass
class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def check_salary(self):
        if(self.__salary < 2000):
            raise NotEligibleException
            return False
        else:
            return True

emp1=Employee(5000)
emp2=Employee(1000)
try:
    status=emp1.check_salary()
    print(status)
    status=emp2.check_salary()
    print(status)
except NotEligibleException:
    print("Not Eligible") #After raising the NotEligibleException, scripting ends there
    
# ---------------------------------------------------------------

class InvalidEmployeeException(Exception):
    pass
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        flag=False
        for key in self.__employee_list:
            if(key==employee_id):
                flag=True
        if(flag==False):
            raise InvalidEmployeeException
            print("1")
        return True

project1=Project([1001,1002,1003])
try:
    print(project1.validate_employee(1005))
except Exception:
    print("2")
except InvalidEmployeeException:
    print("3")

# ---------------------------------------------------------------

class CustomerBusiness:
    def get_customer(self,cust_id):
        if cust_id == "":
            raise InvalidCustomerException()
        return cust_id

class AccountUI:
    def deposit_money_ui(self):
        try:
            cust_id = CustomerBusiness().get_customer("") # Meets the condition at CustomerBusiness
        except Exception: #Exception raised under CustomerBusiness()
            print("Exception raised")
        except InvalidCustomerException:
            print("Invalid Customer Exception raised")

class InvalidCustomerException(Exception):
    	pass

a=AccountUI()
a.deposit_money_ui()