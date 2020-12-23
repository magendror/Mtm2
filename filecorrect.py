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

def fileCorrect(orig_file_path: str, filtered_file_path: str):
    input_file=open(orig_file_path,'r')
    list_of_lines=[makingStringValid(line) for line in input_file if stringIsValid(line)]
    list_of_lines.sort(key=sortingFunc)
    list_of_strings=[(', ').join(list1) for list1 in list_of_lines] 
    output_file=open(filtered_file_path,'w')
    for string in list_of_strings:
        output_file.write(string)
    input_file.close
    output_file.close

fileCorrect(r'C:\\technion\\matam\\mtm2\\Mtm2\\input_file.txt',r'C:\\technion\\matam\\mtm2\\Mtm2\\output_file.txt')