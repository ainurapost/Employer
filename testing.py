from emp import Employee
import unittest

class testEmployeClass(unittest.TestCase):
    def test_correct(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name("Liam"), employee.employee_list[0])

    def test_get_by_name_bool(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name(type(bool)), False)

    def test_get_by_name_int(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name(type(int)), False)

    def test_get_by_name_list(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name(type(list)), False)

    def test_get_by_name_dict(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_name(type(dict)), False)

    def test_employee_by_email(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email("liam006@gmail.com"), employee.employee_list[0])

    def test_employee_by_email_int(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email(type(int)), False)

    def test_employee_by_email_bool(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email(type(bool)), False)

    def test_employee_by_email_list(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email(type(list)), False)

    def test_employee_by_email_dict(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_email(type(dict)), False)

    def test_employee_by_salary(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_salary(8200), employee.employee_list[0])

    def test_employee_by_salary_str(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_salary("8200"), False)

    def test_employee_by_salary_bool(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_salary(type(bool)), False)

    def test_employee_by_salary_strall(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_by_salary("asdase"), False)


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
    def test_add_uncorrect(self):
        employee = Employee()
        employee.add_employee("Arli", "+1-202-555-9852", "arli@gmail.com", "God", 9999999999)
        res = {
            "name": "Arliasd",
            "phone": "+1-20asdads2-555-9852",
            "email": "arliasdasd@gasdasdmail.com",
            "position": "Goasdasdd",
            "salary": 9999348999999
        }
        self.assertEqual(employee.get_employee_by_name("Arli"), False)


if __name__ == '__main__':
    unittest.main()