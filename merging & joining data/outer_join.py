import pandas as pd

df_products = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
    "category_id": [1, 2, 2, 3, 5]
})

df_categories = pd.DataFrame({
    "category_id": [1, 2, 3, 4],
    "category_name": ["Electronics", "Accessories", "Display", "Furniture"],
    "discount": [10, 15, 5, 20]
})

value = pd.merge(df_products,df_categories,on="category_id",how="outer")
print(df_products)
print(df_categories)
print(value)



#Example 
import pandas as pd

df_sales =pd.DataFrame({
    "sale_id": [501, 502, 503, 504, 505, 506],
    "employee_id": [11, 12, 11, 14, 15, 18],
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Printer"],
    "sales": [55000, 1200, 2500, 18000, 3500, 22000]
})

df_employees = pd.DataFrame({
    "employee_id": [11, 12, 13, 14, 16],
    "employee_name": ["Arjun", "Meera", "Kabir", "Sneha", "Ishita"],
    "department": ["IT", "Sales", "HR", "IT", "Sales"]
})
df_final= pd.merge(df_sales,df_employees,on="employee_id", how="outer",indicator=True)
print(df_sales)
print(df_employees)
print(df_final)