def main():
    # Get Input Student Names
    try:
        students = []
        f_name = "Meri"
        while f_name != "Done":
            print(
                "Please enter student names. When you are done, enter 'Done' as first name.")
            f_name = input("Please enter First name: ").title()
            if f_name == "Done":
                break
            else:
                l_name = input("Please enter Last name: ").title()
                students.append(f_name + ', ' + l_name + '\n')

        my_file = open('reading_files_class/example.txt', 'w')
        for line in students:
            my_file.write(line)
        print("These students have been added to the file.")
        print(students)

    except Exception as e:
        print(e)


main()
