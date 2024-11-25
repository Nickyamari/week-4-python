# filename = input("Enter the name of the file to read:")
# print("This is a test")
# filename = input("Enter the name of the file to read: ")
# print(f"You entered: {filename}")
filename = input("Enter the name of the file to read:")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content successfully read!")
        print(content)  
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")  

