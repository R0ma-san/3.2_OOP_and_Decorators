from datetime import date


class Frontend:
    def __init__(self, FirstName, LastName, salary, dat, experience):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.date = dat
        self.experience = experience
    
    @staticmethod
    def visualize():
        return 'Making visual appearance of project'


class Backend: 
    def __init__(self, FirstName, LastName, salary, dat, experience):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.date = dat
        self.experience = experience
    
    @staticmethod
    def set_up_db():
        return 'Setting up database of project'


class Management:
    def __init__(self, FirstName, LastName, salary, dat, rank):
        self.FirstName = FirstName
        self.LastName = LastName
        self.salary = salary
        self.date = dat
        self.rank = rank

    def fire(self, a):
        del a

class Project:

    def __init__(self, *args):
        self.args = args

    def check_backend(self):
        for i in self.args:
            try:
                print(f'Backend - {i.FirstName} \n {i.set_up_db()}')
            except:
                continue

    def check_frontend(self):
        for i in self.args:
            try:
                print(f'Frontend - {i.FirstName} \n {i.visualize()}')
            except:
                continue
        
manager = Management('Max', 'Maximov', 35000, date(2021, 12, 31), 'Project-manager')
senior_frontend = Frontend('Ivan', 'Ivanov', 50000, date(2021, 12, 30), 'Senior')
senior_backend = Backend('Jane', 'Brown', 50000, date(2021, 10, 30), 'Senior')
junior_backend = Backend('Kate', 'Brown', 30000, date(2021, 11, 1), 'Junior')
middle_backend = Backend('John', 'Brown', 40000, date(2022, 1, 1), 'Middle')
junior_frontend = Frontend('Petr', 'Brown', 30000, date(2021, 5, 30), 'Junior')
middle_frontend = Frontend('Zalhar', 'Karipov', 40000, date(2021, 1, 3), 'Middle')
project = Project(manager, senior_frontend, senior_backend, junior_backend, middle_backend, junior_frontend, middle_frontend)

project.check_backend()
project.check_frontend()


