# class tutorial


import datetime


class Employee:
    '''
    Employee case.
    '''
    Raise_Amount = 1.04
    Emp_Count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@abc.com'
        Employee.Emp_Count += 1

        self.emp_id = Employee.Emp_Count

    def fullname(self):
        '''
        ConCat first & lastname.
        '''
        return f"{self.first} {self.last}"

    def apply_raise(self):
        '''
        Annual raise.
        '''
        self.pay = int(self.pay * self.Raise_Amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.Raise_Amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(aDate):
        if aDate.weekday() == 5 or aDate.weekday() == 6:
            return False
        return True


class Developer(Employee):
    Raise_Amount = 1.15

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    # def add_lang(self, lang):
    #     self.prog_lang = lang

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, prog_lang = emp_str.split('-')
        return cls(first, last, pay, prog_lang)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = []
        if employees is not None:
            self.add_emp(employees)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


def main():
    emp_1 = Employee('Fred', 'Flintstone', 100)
    emp_2 = Employee('Barney', 'Rubble', 120)
    emp_3 = Employee('Wilma', 'Flintstone', 130)

    print(emp_1.email)
    print(emp_1.fullname())
    print(
        f"Emp 1: Old Pay = {emp_1.pay} New Pay= {emp_1.apply_raise()} Raise % = {emp_1.Raise_Amount}")
    print(
        f"Emp 2: Old Pay = {emp_2.pay} New Pay= {emp_2.apply_raise()} Raise %= {emp_2.Raise_Amount}")
    emp_3.Raise_Amount = Employee.Raise_Amount+.02
    print(
        f"Emp 3: Old Pay = {emp_3.pay} New Pay= {emp_3.apply_raise()} Raise %= {emp_3.Raise_Amount}")

    # print(emp_2.__dict__)
    # print(emp_3.__dict__)
    # print()
    # print(Employee.__dict__)

    Employee.set_raise_amount(1.5)
    print(
        f"Emp 1: Old Pay = {emp_1.pay} New Pay= {emp_1.apply_raise()} Raise % = {emp_1.Raise_Amount}")
    print(
        f"Emp 2: Old Pay = {emp_2.pay} New Pay= {emp_2.apply_raise()} Raise %= {emp_2.Raise_Amount}")
    print(
        f"Emp 3: Old Pay = {emp_3.pay} New Pay= {emp_3.apply_raise()} Raise %= {emp_3.Raise_Amount}")

    emp_4 = Employee.from_string('bambam-Rubble-10')
    print(emp_4.email)
    mydate = datetime.date(2019, 3, 31)
    print(Employee.is_workday(mydate))
    print(mydate)


# main()
dev_1 = Developer('John', 'Brown', 200, 'COBOL')
dev_2 = Developer('Mary', 'Grey', 200, 'Fortan')
dev_3 = Developer.from_string('Don-Bryan-40000-Python')
# dev_3.add_lang('Python')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.prog_lang)
print(dev_3.prog_lang)
# print(help(Developer))
mgr_1 = Manager('Dru', 'Damico', 60000, dev_1)
mgr_2 = Manager.from_string('Richard-Brown-70000')
mgr_2.add_emp(dev_3)
print(mgr_1.fullname())
mgr_1.print_emps()
mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_2.print_emps()
print(isinstance(mgr_2, Employee))
print(isinstance(mgr_2, Developer))
print(issubclass(Manager, (Employee, Developer)))
print(issubclass(Manager, Manager))
