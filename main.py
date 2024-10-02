students={
    "Oleksandr_Shevchenko":{"surname":"Шевченко","name":"Олександр","addres":"вул. Куликівська 7","school_number":1,"class": 10},
    "Olga_Shevchenko":{"surname":"Шевченко","name":"Ольга","addres":"вул. Куликівська 7","school_number":1,"class": 9},
    "Oleksandr_Boiko":{"surname":"Бойко","name":"Олександр","addres":"вул. Хрещатик 121","school_number":2,"class": 11},
    "Denis_Karpenko":{"surname":"Карпенко","name":"Денис","addres":"вул. Новомістенська 28","school_number":3,"class": 10},
    "Anna_Nahimova":{"surname":"Нахімова","name":"Ганна","addres":"вул. Куликівська 35","school_number":1,"class": 11},
    "Andrey_Gorbachov":{"surname":"Горбачов","name":"Андрій","addres":"вул. Ринкова 67","school_number":4,"class": 8},
    "Katerina_Nemova":{"surname":"Немова","name":"Катерина","addres":"вул. Новомістенська 35А","school_number":5,"class": 9},
    "Denis_Franko":{"surname":"Франко","name":"Денис","addres":"вул. Торгова 5","school_number":6,"class": 10},
    "Grigoryi_Karpov":{"surname":"Карпов","name":"Григорій","addres":"вул. Хрещена 21","school_number":7,"class": 11},
    "Mark_Remarkov":{"surname":"Ремарков","name":"Марк","addres":"вул. Бучанська 11","school_number":1,"class": 9}
}

def print_all(students):
    print("Список учнів:")
    for key,info in students.items():
            print(f"{key}: {info}")


def add_student(students):
    key = input("Введіть ключ(напр. Ivan_Komarov): ")
    if key in students:
        print(f"Учень з ключем {key} вже існує.")
        update = input("Бажаєте оновити дані учня? (так/ні): ").strip().lower()

        if update != 'так':
            print("Дані не були оновлені.")
            return
    # Запитуємо нові дані учня
    surname = input("Введіть прізвище: ")
    name = input("Введіть ім'я: ")
    addres = input("Введіть адресу: ")
    school_number = int(input("Введіть номер школи: "))
    class_number = int(input("Введіть номер класу:"))
    # Оновлюємо або додаємо нового учня
    students[key] = {
        "surname": surname,
        "name": name,
        "addres": addres,
        "school_number": school_number,
        "class": class_number
    }
    print(f"Дані учня {key} було {'оновлено' if key in students else 'додано'} до списку.")

def del_student(students):
    key=input("Введіть ключ учня для видалення: ")
    if key in students:
        del students[key]
        print(f"Учня  {key} успішно видалено")
    else:
        print("Помилка: Учня з таким ключом немає в списку")

def get_older_student(students):
    school_number=int(input("Введіть номер школи: "))
    older_student=[]
    for key,info in students.items():
        if info["school_number"]==school_number and info["class"] in [10,11]:
            older_student.append((key,info["surname"],info["name"],info["addres"]))
    return older_student

def menu():
    while True:
        print("\nДоступні функції: ")
        print("1) Вивести данні про всіх учнів")
        print("2) Додати учня до списку")
        print("3) Видалити учня зі списку")
        print("4) Переглянути учнів 10-11 за номером школи")
        print("5) Вихід з программи")
        choice=int(input("Введіть дію, що бажаєте виконати (1-5): "))
        if choice==1:
            print_all(students)
        elif choice==2:
            add_student(students)
        elif choice==3:
            del_student(students)
        elif choice==4:
            older_students=get_older_student(students)
            if older_students:
                print("Учні зі старших класів за введеним номером школи: ")
                for student in older_students:
                    print(f"Ключ:{student[0]}, Дані: {student[1]}, {student[2]},{student[3]}")
            else:
                print("Помилка: в списку немає учнів з старших класів за вказаним номером школи")
        elif choice==5:
            print("Виконується вихід з програми")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__=="__main__":
    menu()