#### IMPORTS ####
import event_manager as EM

def idCorrect(id):
    id=id.replace(" ","")
    return (id.isdigit() and 10000000<=int(id)<=99999999)

def ageAndYearOfBirthCorrect(age,year):
    year=year.replace(" ","")
    age=age.replace(" ","")
    return age.isdigit()and year.isdigit()and (16<=int(age)<=120)and (2020-int(year)==int(age))

def makingNameValid(name):
    list_of_names=name.split(" ")
    list_of_valid_names=[name1 for name1 in list_of_names if name1.isalpha()]
    name=" ".join(list_of_valid_names)
    return name 

def makingStringValid(str1):
    id,name,age,year,semester=str1.split(',')
    id=id.replace(" ","")
    age=age.replace(" ","")
    year=year.replace(" ","")
    semester=semester.replace(" ","")
    name=makingNameValid(name)
    list1=[id,name,age,year,semester]
    return list1 

def semesterIsValid(semester):
    semester=semester.replace(" ","")
    semester=semester.replace("\n","")
    return semester.isdigit() and  int(semester)>=1
    

def nameIsValid(name):
    return name.replace(" ","").isalpha()

def stringIsValid(string_to_check):
    list_to_check=string_to_check.split(",")
    return bool(idCorrect(list_to_check[0])*nameIsValid(list_to_check[1])*ageAndYearOfBirthCorrect(list_to_check[2],list_to_check[3])*semesterIsValid(list_to_check[4]))

def sortingFunc(list):
    return int(list[0])

#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    input_file=open(orig_file_path,'r')
    list_of_lines=[makingStringValid(line) for line in input_file if stringIsValid(line)]
    list_of_lines.sort(key=sortingFunc)
    list_of_strings=[(', ').join(list1) for list1 in list_of_lines] 
    output_file=open(filtered_file_path,'w')
    for string in set(list_of_strings):
        output_file.write(string)
    input_file.close
    output_file.close
    
# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if(k<=0):
        return -1
    fileCorrect(in_file_path,"temp_file_Youngest")
    corrected_file = open("temp_file_Youngest", "r")
    user_list = corrected_file.readlines()
    if(k>len(user_list)):
        corrected_file.close
        printYoungestStudentsHelper(user_list,out_file_path,len(user_list))
    else:
        corrected_file.close
        printYoungestStudentsHelper(user_list,out_file_path,k)
    #TODO
    
def printYoungestStudentsHelper(user_list, out_file_path: str, k: int) -> int:
    for i in user_list:
        user_list[i]=user_list[i].split(', ')
    write_to_file = open("out_file_path", "w")
    hist = len(user_list)*[0]
    for i in range(k):
        iterator = 0
        minimum = [user_list[i][2] for i in hist if hist[i]==0]
        for j,current_user in enumerate(user_list):
            if(current_user[2]<minimum[0] and hist[j]==0):
                iterator = j
                minimum = current_user[2]
        hist[iterator]=1
        write_to_file.write(user_list[iterator][0])
    write_to_file.close
    #TODO
    
# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if(semester<=0):
        return -1
    fileCorrect(in_file_path,"temp_file_Youngest")
    corrected_file = open("temp_file_Youngest", "r")
    user_list = corrected_file.readlines()
    for i in user_list:
        user_list[i]=user_list[i].split(', ')
    students_in_semester=0
    age_in_semester=0
    for student in user_list[i]:
        if (student[4]==semester):
            age_in_semester+=student[2]
            students_in_semester+=1
    return age_in_semester/students_in_semester
    #TODO
    

#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    #TODO   
    
    
def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])
