# using inner join function

import pandas as pd 
df_students = pd.DataFrame({

    "student_id": [1,2,3,4],
    "name" : ["Rahul","Aman","Priya", "Riya"],
    "course_id": [101,102,103,104]
})

df_Courses = pd.DataFrame({
    "course_id" : [101,102,103,105],
    "course_name": ["python","SQL","Pandas","Java"]
})

print(df_Courses)
print(df_students)

value = pd.merge(df_students,df_Courses,on="course_id")
print(value)