from xmlrpc.client import ServerProxy

# Connect to the server
server = ServerProxy("http://localhost:8000/")

# Example usage
try:
    number = 4  # Replace with the number you want to calculate the factorial of
    result = server.factorial(number)
    print(f"The factorial of {number} is {result}.")
except Exception as e:
    print(f"An error occurred: {e}")
