class employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = self.first_name.lower()[0] + self.last_name.lower() + "@thiscompany.com"

    def get_info(self):
        return self.first_name, self.last_name, self.email, self.salary

    def give_raise(self, salary):
        self.salary = salary

class developer(employee):
    def __init__(self, first_name, last_name, salary, programming_languages):
        super().__init__(first_name, last_name, salary)
        self.prog_langs = programming_languages
    
    def get_dev_info(self):
        return self.first_name, self.last_name, self.email, self.salary, self.prog_langs

    def add_lang(self, lang):
        self.prog_langs += [lang]

emp1 = employee("Testy", "McTesterson", 60000)

print(emp1.first_name, emp1.last_name, emp1.email, emp1.salary)
emp1.give_raise(65000)
print(emp1.first_name, emp1.last_name, emp1.email, emp1.salary)

dev1 = developer("Codey", "McCoderson", 55000, ["Javascript", "Python"])

print(dev1.first_name, dev1.last_name, dev1.email, dev1.salary, dev1.prog_langs)
dev1.give_raise(60000)
dev1.add_lang("HTML")
print(dev1.first_name, dev1.last_name, dev1.email, dev1.salary, dev1.prog_langs)
print(dev1.get_info())
# print(dev1.get_dev_info())