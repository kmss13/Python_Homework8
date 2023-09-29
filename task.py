
def enter_first_name():
    return input("Введите имя абонента: ").title()

def enter_second_name():
    return input("Введите фамилию абонента: ").title()

def enter_family_name():   
    return input("Введите отчество абонента: ").title()

def enter_phone_number():
    return input("Введите номер телефона: ")   

def enter_address_number():
    return input("Введите адрес абонента: ").title() 
  

def enter_data():
    name =enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number =enter_phone_number()
    address =enter_address_number()
    
    

    with open('file.txt', 'a') as file:
        file.write(f'{name} {surname} {family}\n {number}\n {address}\n\n')
        
       
#enter_data()        

def print_data():
    with open('file.txt', 'r') as file:
        print(file.read())   
        

def search_line():
    searched= input('Введите поисковые данные: ').title()
    with open('file.txt','r',) as file: 
        data= file.read().strip().split('\n\n')
        for item in data:
            if searched in item:
                print(item, end ="\n\n")
            else:
                print("Такого контакта не существует")    
 

def update_contact():

    print("Выберете что хотите изменить: \n"
          '1. Имя \n'
          '2.Фамилию \n'
          '3.Отчество \n'
          '4. Телефон \n'
          '5. Адрес \n')
    
    index = int(input("Введите вариант: "))-1
    old_data = input("Введите данные, которые хотите изменить: ").title()
    change_data= input("Введите новые данные: ").title()

    with open("file.txt", "r") as file:
        database = file.read().strip().split('\n\n')

    new_data =[]    
        
    for item in database:
        contact =item.replace('\n', ' ').split()
        
        if contact[index] == old_data:
            contact[index] = change_data
            new_data.append(f'{contact[0]} {contact[1]} {contact[2]}\n {contact[3]}\n {contact[4]} \n\n')
            print()
        else:
            new_data.append(item)
            
             
    if item  not in database:
        print("Вы ввели неккоректные данные")    

    with open("file.txt", "w") as file:
        file.write('\n'.join(new_data)) 
        print("Контакт изменен")       



def delete_contact():

    print("Выберете что хотите удалить: \n"
          '1. Имя \n'
          '2.Фамилию \n'
          '3.Отчество \n'
          '4. Телефон \n'
          '5. Адрес \n'
          '6. Удалить контакт полностью \n')
    index = int(input("Введите вариант: ")) -1
    searched = input("Введите удаляемые данные: ").title()


    with open("file.txt", "r") as file:
        database= file.read().strip().split('\n\n')
        new_data = []

    for item in database:
        if searched in item:
            contact =item.replace('\n', ' ').split()
            if len(contact) >= index +1: 
                delete_item= contact[index]
                if searched == delete_item:
                    new_data.append(f'{contact[0]} {contact[1]} {contact[2]}\n {contact[3]}\n {contact[4]}\n')
                    print()
                    
        else:
            new_data.append(item) 
                  

    with open("file.txt", "w") as file:
        file.write('\n'.join(new_data))
        print("Контакт удален")           
            
           

def interface():
    cmd = 0
    while cmd != "4":
        print("Выберите действие: \n"  
                "1. Добавить контакт \n"      
                "2. Вывести все контакты \n"  
                "3. Поиск контакта \n" 
                "4. Изменить контакт\n"
                "5. Удалить контакт \n"
                "6. Выход \n"  )
        cmd = input("Введите действие: ")
        while cmd  not in ("1", "2","3","4", "5","6"):
            print("Неккоректный ввод")
            cmd = input("Введите действие: ")
        match cmd: 
            case "1" :
                enter_data()    
            case "2" :
                print_data()   
            case "3" :
                search_line()
            case "4" :  
                update_contact() 
            case "5" :  
                delete_contact()       
            case "6" :  
                print("Всего доброго!")  
        
interface()












