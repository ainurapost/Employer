class Employee:
    def __init__(self):
        self.employee_list = [
            {
                "name": "Liam",
                "phone": "+1-202-555-0176",
                "email": "liam006@gmail.com",
                "position": "Team Lead",
                "salary": 8200
            },
            {
                "name": "Oliver",
                "phone": "+1-202-666-3159",
                "email": "mad_oliver@gmail.com",
                "position": "Back-end developer",
                "salary": 6150
            },
            {
                "name": "William",
                "phone": "+1-204-875-4563",
                "email": "william.jackson@gmail.com",
                "position": "Front-end developer",
                "salary": 5550
            },
            {
                "name": "Mason",
                "phone": "+1-224-8547-1232",
                "email": "mason@gmail.com",
                "position": "Tester",
                "salary": 5300
            }
        ]

    def get_employee_by_name(self, name):
        for i in self.employee_list:
            if i["email"] == name:
                return i
        return False


    def get_employee_by_email(self, email):
        for i in self.employee_list:
            if i["name"] == email:
                return i
        return False

    def get_employee_by_salary(self, salary):
        for i in self.employee_list:
            if i["salary"] == salary:
                return i
        return False

    def add_employee(self, name, phone, email, position, salary):
        accepted_chars = [chr(i) for i in  range(97, 123)] + [chr(i).upper() for i in  range(97, 123)] + \
                                [str(i) for i in range(10)] + ['-', '_', '.']

        email = email.split ('@')
        if len(email) != 2:
            return False
        if len(email[0]) < 1:
            return False
        if email[1].count('.') != 1:
            return False
        for i in email[0]:
            if i not in(accepted_chars):
                return False



        print(list(map(chr, range(97, 123))))


        dict1 = {
            "name": name,
            "phone": phone,
            "email": email,
            "position": position,
            "salary": salary
        }

        self.employee_list.append(dict1)



e1 = Employee()
e1.get_employee_by_name("L")
