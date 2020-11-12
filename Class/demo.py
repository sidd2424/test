class Employee:

    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.email = F'{first_name.lower()}.{last.lower()}@cybage.com'
        self.pay = pay


    def __str__(self):
        return F"{self.first_name} {self.last_name}"
    
    
emp1= Employee(first="Sidd", last="kamble", pay=25000)
print(emp1.first_name)

# _data_ = {
#     {
#     "first_name" : "Sidd",
#     "last_name" : "Kamble",
#     "pay" : 25000
#     },{
#     "first_name" : "Shubham",
#     "last_name" : "Khindre",
#     "pay" : 25000
#     },{
#     "first_name" : "Shamli",
#     "last_name" : "Ingole",
#     "pay" : 25000
#     },{
#     "first_name" : "Abhishek",
#     "last_name" : "Singh",
#     "pay" : 25000
#     },
# }