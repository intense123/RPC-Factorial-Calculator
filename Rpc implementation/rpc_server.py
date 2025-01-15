# from xmlrpc.server import SimpleXMLRPCServer
# import math

# # Define the server-side methods
# def factorial(n):
#     """Calculate the factorial of a number."""
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     return math.factorial(n)

# # Create the RPC server
# server = SimpleXMLRPCServer(("localhost", 8000))
# print("Server is listening on port 8000...")

# # Register methods to be called remotely
# server.register_function(factorial, "factorial")

# # Start the server
# server.serve_forever()

from xmlrpc.server import SimpleXMLRPCServer
import math
import datetime

# Define the server-side methods
def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = math.factorial(n)
    print(f"[{datetime.datetime.now()}] Request received: factorial({n}) -> Result: {result}")
    return result

# Create the RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")

# Register methods to be called remotely
server.register_function(factorial, "factorial")

# Start the server
server.serve_forever()
