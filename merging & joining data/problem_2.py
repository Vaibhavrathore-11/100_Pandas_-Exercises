import pandas as pd

df_employees = pd.DataFrame({
    "employee_id" :[101,102,103,104,105],
    "name": ["rahul","Aman","anshika","radhe","gogi"],
    "department_id": [1,2,1,3,5],
    "salary":[35000,42000,38000,45000,40000]
})

df_departments = pd.DataFrame({
    "department_id": [1,2,3,4],
    "department_name": ["IT","HR","Finance","Marketing"],
    "Location": ["Indore","Bhopal","indore","Ujjain"]
})
print(df_employees)
print(df_departments)

value = pd.merge(df_departments,df_employees,on = "department_id")
print(value)