import csv
import openpyxl
def read_bb_file(filepath):
    grades={}
    with open(filepath,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        for rows in reader:
            if(rows[0] == "姓氏"):
                continue
            # print(rows[2],rows[8],rows[9],rows[10])
            tmp_grade = [rows[8],rows[9],rows[10]]
            grades[rows[2].upper()] = tmp_grade
    return(grades)

def write_grade_file(filepath,grades):
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook['Sheet0']
    for row in sheet.rows:
        student_id = row[1].value
        if student_id!= None and student_id in grades.keys():
            row[3].value = grades[student_id][0];
            row[4].value = grades[student_id][1]
            row[5].value = grades[student_id][2]
    workbook.save(filepath)
if __name__ == '__main__':
    bb_file_path = 'gc_011174.02.2020SP_fullgc_2020-04-17-16-46-08.csv'
    grades = read_bb_file(bb_file_path)
    grade_file = '2020春 011174.02成绩考核登记表.xlsx'
    print(write_grade_file(grade_file,grades))
