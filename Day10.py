# Day 10 focuses on functions with outputs and our project will be to make a calculator app in python

# Fucntions with outputs

def my_function():
    
    return 3 * 2 
   
output = my_function()

print(output)

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"
formated_string = format_name("NiCK", "nick")
print(formated_string)