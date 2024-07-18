class Employee:
    def __init__(self, login, password, name, email, phone):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone

class HRManager(Employee):
    def conduct_interview(self, candidate):
        print(f"HR Manager {self.name} is conducting an interview with {candidate.name}.")
    
    def register_employee(self, employee):
        print(f"HR Manager {self.name} is registering {employee.name} into the system.")
    
    def remove_employee(self, employee):
        print(f"HR Manager {self.name} is removing {employee.name} from the system.")

class Recruiter(Employee):
    def search_candidates(self, vacancy):
        print(f"Recruiter {self.name} is searching for candidates for {vacancy}.")
        
        candidate = Employee("candidate1", "candidate_password", "Candidate Name", "candidate@example.com", "555-555-5555")
        hr_manager = HRManager("hr_manager1", "password123", "John Doe", "john@example.com", "123-456-7890")
        hr_manager.conduct_interview(candidate)

class Trainer(Employee):
    def plan_training_program(self, employee):
        print(f"Trainer {self.name} is planning a training program for {employee.name}.")
    
    def conduct_induction(self, employee):
        print(f"Trainer {self.name} is conducting an induction for {employee.name}.")
    
    def develop_skills(self, employee):
        print(f"Trainer {self.name} is developing skills for {employee.name}.")

class Director(Employee):
    def send_employee_list_to_recruiter(self, employees):
        print(f"Director {self.name} is sending a list of employees to the Recruiter.")
        for employee in employees:
            print(f"- {employee.name}")

if __name__ == "__main__":
   
    hr_manager = HRManager("hr_manager1", "password123", "John Doe", "john@example.com", "0554-096-666")
    recruiter = Recruiter("recruiter1", "password456", "Jane Smith", "jane@example.com", "0554-096-666")
    trainer = Trainer("trainer1", "password789", "Mike Johnson", "mike@example.com", "0554-096-666")
    director = Director("director1", "passwordabc", "Emily Brown", "emily@example.com", "0554-096-666")
    
    
    hr_manager.register_employee(Employee("employee1", "emp1_password", "Alice Smith", "alice@example.com", "0554-096-666"))
    recruiter.search_candidates("Software Engineer")
    trainer.plan_training_program(Employee("employee2", "emp2_password", "Bob Johnson", "bob@example.com", "0554-096-666"))
    director.send_employee_list_to_recruiter([Employee("employee3", "emp3_password", "Charlie Brown", "charlie@example.com", "333-333-3333")])