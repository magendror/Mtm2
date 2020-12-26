#### IMPORTS ####
#import event_manager as EM


def idCorrect(user_id):
    user_id = user_id.replace(" ", "")
    return (user_id.isdigit() and 10000000 <= int(user_id) <= 99999999)


def ageAndYearOfBirthCorrect(age, year):
    year = year.replace(" ", "")
    age = age.replace(" ", "")
    return age.isdigit() and year.isdigit() and (16 <= int(age) <= 120) and (2020-int(year) == int(age))


def makingNameValid(name):
    list_of_names = name.split(" ")
    list_of_valid_names = [name1 for name1 in list_of_names if name1.isalpha()]
    name = " ".join(list_of_valid_names)
    return name


def makingStringValid(str1):
    user_id, name, age, year, semester = str1.split(',')
    user_id = user_id.replace(" ", "")
    age = age.replace(" ", "")
    year = year.replace(" ", "")
    semester = semester.replace(" ", "")
    name = makingNameValid(name)
    list1 = [user_id, name, age, year, semester]
    return ", ".join(list1).replace("\n","")


def semesterIsValid(semester):
    semester = semester.replace(" ", "")
    semester = semester.replace("\n", "")
    return semester.isdigit() and int(semester) >= 1


def nameIsValid(name):
    return name.replace(" ", "").isalpha()


def getID(user_string):
    data_list = user_string.split(",")
    if len(data_list) == 0:
        return None
    user_id = data_list[0]
    if not user_id.isdigit():
        return None
    return int(user_id)

def stringIsValid(string_to_check):
    list_to_check = string_to_check.split(",")
    conditions = [idCorrect(list_to_check[0]), nameIsValid(list_to_check[1]),
                  ageAndYearOfBirthCorrect(list_to_check[2], list_to_check[3]), semesterIsValid(list_to_check[4])]
    return all(conditions)


def sortingFunc(list):
    return int(list[0])

#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file


def fileCorrect(orig_file_path: str, filtered_file_path: str):
    input_file = open(orig_file_path, 'r')
    list_of_lines = [makingStringValid(line)
                     for line in input_file if stringIsValid(line)]
    temp_dictionary = dict()
    for user_string in list_of_lines:
        temp_dictionary[getID(user_string)]=user_string
    list_of_lines = list(temp_dictionary.values())
    list_of_lines.sort(key=getID)
    output_file = open(filtered_file_path, 'w')
    for string in list_of_lines:
        output_file.write(string + "\n")
    input_file.close()
    output_file.close()

# Writes the names of the K youngest students which subscribed
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file


def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if(k <= 0):
        return -1
    youngest_fname = in_file_path + "_youngest.tmp"
    fileCorrect(in_file_path, youngest_fname)
    corrected_file = open(youngest_fname, "r")
    user_list = corrected_file.readlines()
    user_list = [i.split(', ') for i in user_list]
    user_list.sort(key=lambda x: (int(x[2]), int(x[0])))
    write_to_file = open(out_file_path, "w")
    write_list = user_list[:k]
    for i in write_list:
        write_to_file.write(i[1]+"\n")
    write_to_file.close()
    return min(k,len(write_list))

# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.


def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if(semester <= 0):
        return -1
    ageavg_fname = in_file_path + "_youngest.tmp"
    fileCorrect(in_file_path, ageavg_fname)
    corrected_file = open(ageavg_fname, "r")
    user_list = corrected_file.readlines()
    user_list = [e.replace("\n","") for e in user_list]
    user_list = [e.split(', ') for e in user_list]
    students_in_semester = 0
    age_in_semester = 0
    for student in user_list:
        if (int(student[4]) == semester):
            age_in_semester += int(student[2])
            students_in_semester += 1
    if (students_in_semester==0):
        return 0
    else:
        return age_in_semester/students_in_semester
    # TODO


#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
# em, event_names: list, event_id_list: list, day: int, month: int, year: int):
def printEventsList(events: list, file_path: str):
    pass
    # TODO


def testPrintEventsList(file_path: str):
    events_lists = [{"name": "New Year's Eve", "id": 1, "date": EM.dateCreate(30, 12, 2020)},
                    {"name": "annual Rock & Metal party", "id": 2,
                        "date":  EM.dateCreate(21, 4, 2021)},
                    {"name": "Improv", "id": 3,
                        "date": EM.dateCreate(13, 3, 2021)},
                    {"name": "Student Festival", "id": 4, "date": EM.dateCreate(13, 5, 2021)}, ]
    em = printEventsList(events_lists, file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)


#### Main ####
# feel free to add more tests and change that section.
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    """x=printYoungestStudents("./data.txt","./output.txt")
    exit()"""
    import sys
    if len(sys.argv) > 1:
        testPrintEventsList(sys.argv[1])
