class Pet:
    def __init__(self, name, pet_type, age_in_months, gender, owner_name, services):
        self.name = name
        self.pet_type = pet_type
        self.age_in_months = age_in_months
        self.gender = gender
        self.owner_name = owner_name
        self.services = services

    def display_details(self):
        print("\n----- Pet Details -----")
        print(f"Pet Name       : {self.name}")
        print(f"Pet Type       : {self.pet_type}")
        print(f"Age            : {self.age_in_months} month(s)")
        print(f"Gender         : {self.gender}")
        print(f"Owner Name     : {self.owner_name}")
        print(f"Services       : {', '.join(self.services)}")

class PetCareSystem:
    
    def __init__(self):
        self.pets = []

    def get_non_empty_input(self, message):
        while True:
            value = input(message).strip()
            if value:
                return value
            print("This field cannot be empty.")

    def get_valid_age_in_months(self):
        while True:
            age = input("Enter pet age in months: ").strip()
            if age.isdigit() and int(age) >= 0:
                return int(age)
            print("Please enter a valid age in months.")

    def get_valid_gender(self, message):
        valid_genders = ["male", "female"]
        while True:
            gender = input(message).strip().lower()
            if gender in valid_genders:
                return gender.capitalize()
            print("Please enter only Male or Female.")

    def get_multiple_services(self):
        services = {
            "1": "Vaccination",
            "2": "Grooming",
            "3": "Health Checkup"
        }

        selected_services = []
        while True:
            print("\nChoose Service:")
            print("1. Vaccination")
            print("2. Grooming")
            print("3. Health Checkup")
            choice = input("Enter your choice: ").strip()

            if choice in services:
                service = services[choice]
                if service not in selected_services:
                    selected_services.append(service)
                    print(f"{service} added successfully.")
                else:
                    print("This service is already selected.")
            else:
                print("Please choose a valid option from 1 to 3.")
                continue
            more = input("Do you want to add another service? (yes/no): ").strip().lower()
            if more != "yes":
                break
        return selected_services
    
    def add_pet(self):
        print("\n===== Add Pet =====")
        name = self.get_non_empty_input("Enter pet name: ")
        pet_type = self.get_non_empty_input("Enter pet type (Dog/Cat/etc): ")
        age_in_months = self.get_valid_age_in_months()
        gender = self.get_valid_gender("Enter pet gender (Male/Female): ")
        owner_name = self.get_non_empty_input("Enter owner name: ")
        services = self.get_multiple_services()
        pet = Pet(name, pet_type, age_in_months, gender, owner_name, services)
        self.pets.append(pet)
        print("\nPet added successfully!")
        pet.display_details()
        print("Thank you for using Pet Care System.")

    def start(self):
        while True:
            self.add_pet()
            again = input("\nDo you want to add another pet? (yes/no): ").strip().lower()
            if again != "yes":
                print("\nExiting Pet Care System.")
                break
            
def main():
    system = PetCareSystem()
    system.start()
if __name__ == "__main__":
    main()