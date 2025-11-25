import os
import json

os.system('cls')
print("======================================")
print("===== STUDENT INFORMATION SYSTEM =====")
print("======================================\n")

record = {}
while True:
    print("===== OPTIONS =====")
    print("A = Add student record.")
    print("B = Print all student record.")
    print("C = Search student record.")
    print("D = Delete student record.")
    print("E = Edit student record.")
    print("F = Export student record.")
    print("G = Exit.")
    print("====================\n")

    pick = input("SELECT OPTION FROM ABOVE: ").lower()

    if pick == 'a':
        print("\n=== ADDING STUDENT RECORD ===\n")
        id = input("Student ID: ").upper()
        fn = input("First Name: ").upper()
        ln = input("Last Name: ").upper()
        age = eval(input("Age: "))
        section = input("Section: ").upper()
        course = input("Course: ").upper()

        record[id] = [fn, ln, age, section, course]
        print("\n======== DATA SAVED ========\n")
        continue

    elif pick == 'b':
        print("===== STUDENT RECORD =====")
        for a, d in record.items():
            print(f'STUDENT ID: {a}, INFORMATION - {d}')
        continue

    elif pick == 'c':
        os.system('cls')
        print("=== SEARCH STUDENT RECORD ===")
        search = input("STUDENT ID NO: ")

        for each_id in record:
            if each_id in record.keys():
                print("=====RECORD FOUND=====")
                print(f'RECORD FOR: {search}')
                
                for a in record[search]:
                    print(f"- {a}")
                print("======================")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif pick == 'd':
        os.system('cls')
        print("=== SEARCH STUDENT RECORD ===")
        search = input("STUDENT ID NO: ")

        for each_id in record:
            if each_id in record.keys():
                print("=====RECORD FOUND=====")
                print(f'RECORD FOR: {search}')
                
                for a in record[search]:
                    print(f"- {a}")
                print("======================")
                
                confirm = input("CONFIRM DELETE (Y/N): ").lower()
                if confirm == 'y':
                    record.pop(search)
                    print("RECORD DELETED")
                    break
                elif confirm == 'n':
                    print("NOT DELETED")
                    break
                else:
                    print("Invalid Option")
                    continue
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif pick == 'e':
        os.system('cls')
        print("=== SEARCH STUDENT RECORD ===")
        search = input("STUDENT ID NO: ")

        for each_id in record:
            if each_id in record.keys():
                print("=====RECORD FOUND=====")
                print(f'RECORD FOR: {search}')
                
                for a in record[search]:
                    print(f"- {a}")
                print("======================")

                # NEW SET OF VALUES
                fn = input("First Name: ").upper()
                ln = input("Last Name: ").upper()
                age = eval(input("Age: "))
                section = input("Section: ").upper()
                course = input("Course: ").upper()

                record[search][0] = fn
                record[search][1] = ln
                record[search][2] = age
                record[search][3] = section
                record[search][4] = course

                print("DATA IS NOW UPDATED")
                
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif pick == 'f':
        print("===== EXPORT RECORD =====")
        
        with open('students_record.json', 'w') as new_file:
            json.dump(record, new_file, indent=4)
        continue

    elif pick == 'g':
        print("SYSTEM EXIT")
        break
    else:
        print("Invalid Choice")
