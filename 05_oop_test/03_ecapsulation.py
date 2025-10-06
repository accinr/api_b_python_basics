class Student:
    def __init__(self, name, email, ph_number):
        self.__student_name = name
        self.email = email
        self.__ph_number = ph_number
        
    def get_number(self):
        return self.__ph_number
    
    def set_number(self, new_number):
        print(f"New number is {new_number}")
        self.__ph_number = new_number

st = Student("Jill", "jill@gmail.com", 123456)
print(st.email) #access the email directly
# print(st.__ph_number)
print(st.get_number())
print(st.set_number(987654))
print(st.get_number())