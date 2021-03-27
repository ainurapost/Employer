from emp import Employee
import unittest

class testget_employee_by_name(unittest.TestCase):
    def test_correct(self):
        employee = Employee()
        res = {
            "name": "Liam",
            "phone": "+1-202-555-0176",
            "email": "liam006@gmail.com",
            "position": "Team Lead",
            "salary": 8200
        }
        self.assertEqual(employee.get_employee_by_name("Liam"), res)
    def test_correct2(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name("Liam"), employee.employee_list[0])

    def test_employee_by_email(self):
        employee = Employee()
        res = {
            "name": "Liam",
            "phone": "+1-202-555-0176",
            "email": "liam006@gmail.com",
            "position": "Team Lead",
            "salary": 8200
        }
        self.assertEqual(employee.get_employee_by_email("liam006@gmail.com"), res)
    def test_employee_by_email2(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email("liam006@gmail.com"), employee.employee_list[0])

    def test_employee_by_salary(self):
        employee = Employee()
        res = {
            "name": "Liam",
            "phone": "+1-202-555-0176",
            "email": "liam006@gmail.com",
            "position": "Team Lead",
            "salary": 8200
        }
        self.assertEqual(employee.get_employee_by_salary(8200), res)
    def test_employee_by_salary2(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_salary(8200), employee.employee_list[0])

    def test_add_correct(self):
        employee = Employee()
        employee.add_employee("Arli", "+1-202-555-9852", "arli@gmail.com", "God", 9999999999)
        res = {
            "name": "Arli",
            "phone": "+1-202-555-9852",
            "email": "arli@gmail.com",
            "position": "God",
            "salary": 9999999999
        }
        self.assertEqual(employee.get_employee_by_name("Arli"), res)