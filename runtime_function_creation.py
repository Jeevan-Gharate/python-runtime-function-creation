def create_dynamic_function(func_name, params, body):
    # func_code = f"def {func_name}({', '.join(params)}):\n" ## if we derefence the params when we get a list of parameters
    func_code = f"def {func_name}({params}):\n" ## if we directly get the params as a string of comma separated parameters
    func_code += f"    {body}"
    exec(func_code, globals())  ## this creates the function dynamically in global context which enables calling it even outside create_dynamic_function()

    choice = input(f"Function '{func_name}' created. Do you want to execute it? (yes/no): ")
    if choice.lower() == 'yes':
        get_params = input(f"Enter the arguments for {func_name}({params}) (comma separated): ")
        result = eval(f"{func_name}({get_params})")  ## example call with dummy args change as needed
        print(f"Function '{func_name}' executed with result: {result}")


# Example: Dynamically create a function
create_dynamic_function("multiply", "a,b", "a=1\n    return a * b") ## function body manipulation for debugging


### now we get the input from the user
func_name = input("Enter the function name: ")
params = input("Enter the parameters (comma separated): ")
print("Enter the function body (use proper indentation):")
body = ""
while True:
    line = input()
    if line == "END":
        break
    body += line + "\n    "  # Append each line of the function body

print("Function body received:\n", body)
create_dynamic_function(func_name, params, body)



#### Call the dynamically created function from the first Example
# result = multiply(5, 3)
# print(f"Result of multiply(5, 3): {result}")
