import os.path
import re

class car:
    def __init__(self, model, year, transmission, regnum, drivelen):
        self.model = model
        self.year = year
        self.transmission = transmission
        self.regnum = regnum
        self.drivelen = drivelen
        
    def __init__(self, info):
        self.model = info[0]
        self.year = int(info[1])
        self.transmission = info[2]
        self.regnum = int(info[3])
        self.drivelen = int(info[4])
    
    def print_car(self):
        print("{0.model:^15}|{0.year:^8d}|{0.transmission:^7}|{0.regnum:^15d}|{0.drivelen:^15d}".format(self))
        
def is_valid_car(info):
    isnum = '^[1-9][0-9]*$'
    isAM = '^[am]$'
    for i in range(len(info)):
        info[i] = info[i].strip()
    if re.match(isnum, info[1]) and re.match(isnum, info[3]) and re.match(isnum, info[4]) and re.match(isAM, info[2]):
        return True
    else:
        return False
        
    
def read_file(mas, err):
    file_name = input("\nIevadiet faila nosaukumu/atrašanās vietu: ").strip()

    if os.path.exists(file_name):
        try:
            with open(file_name) as file:
                cars = file.readlines()
                for single_car in cars:
                    cart = single_car.strip()
                    if len(cart) > 2 and cart[len(cart) - 1] == ";":
                        cart = cart[0:len(cart)-2]
                    info = cart.split(";")
                    if len(info) == 5 and is_valid_car(info):
                        new_car = car(info)
                        mas.append(new_car)
                    else:
                        err.append(single_car)
        except:
            print("\nFailu neizevās veiksmīgi atvērt vai nolasīt - iespējams tas jau ir atvērts kādā citā procesā!\n")
        print("\nIzdevās nolasīt " + str(len(mas)) + " rindas!\n")
        try:
           with open("err.txt", 'w') as out:
                out.writelines(err)
        except:
            print("\nNeizdevās izveidot err.txt - iespējams fails jau ir atvērts kādā citā procesā!\n")
        return True
    else: 
        print("\nFails netika atrasts vai neeksistē!")
        return False

def table_border():
     print("---------------+--------+-------+---------------+---------------")

def print_table():
    print()
    print("{:^15}|{:^8}|{:^7}|{:^15}|{:^15}".format("Marka", "Gads", "Kārba", "Reģ. numurs", "Nobraukums"))
    table_border()

def print_car(cart):
    table_border()
    cart.print_car()
    
def print_all(mas):
    print_table()
    for cart in mas:
        print_car(cart)

def find_model(mas):
    search_for = input("Ievadiet marku: ").lower()
    print_table()
    for cart in mas:
        if cart.model.lower() == search_for:
            print_car(cart)
  
def find_transmission(mas):
    search_for = input("Ievadiet pārnesumkārbas veidu(a/m): ").lower()
    isAM = '^[am]$'
    if re.match(isAM, search_for):
        print_table()
        for cart in mas:
            if cart.transmission == search_for:
                print_car(cart)
    else:
        print("Nepareiza ievade!")

def find_year(mas):
    search_for = input("Ievadiet gadu: ")
    isnum = '^[1-9][0-9]*$'
    if re.match(isnum, search_for):
        print_table()
        for cart in mas:
            if cart.year >= int(search_for):
                print_car(cart)
    else:
        print("Nepareiza ievade")

def main():

    mas = []
    err = []
    
    while(True):
        if read_file(mas,err):
            print_all(mas)
            while(True):
                print("\na.Izdrukāt datus par noteiktās markas mašīnām\n" +
                      "b.Meklēt mašīnas pēc pārnesumkārbas tipa\n" +
                      "c.Meklēt mašīnas, kas tika izlaistas pēc norādītā gada\n" +
                      "(Rakstiet 'all', lai redzētu visus ierakstus!)\n"+
                      "(Rakstiet 'exit', lai izbeigtu programmu!)\n" )
            
                choice = input(">").lower()
                if choice == "a":
                    find_model(mas)
                elif choice == "b":
                    find_transmission(mas)
                elif choice == "c":
                    find_year(mas)
                elif choice == "all":
                    print_all(mas)
                elif choice == "exit":
                    print("\nProgramma izbeigta!\n")
                    return
                else:
                    print("Ievades kļūda!")
        else:
            while(True):
                choice = input("Vai vēlaties mēģināt vērlreiz?(y/n): ").lower();
                if choice == "y":
                    break
                elif choice == "n":
                    print("\nProgramma izbeigta!\n")
                    return
                else:
                    print("Nepareiza ievade!\n")

main()
