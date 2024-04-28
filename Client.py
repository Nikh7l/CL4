import Pyro4

# Prompt user for input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Create a Pyro4 proxy for the remote object
with Pyro4.Proxy("PYRONAME:ConcatService") as stub:
    # Call the remote method
    response = stub.concatenate(s1, s2)
    print("Concatenated string:", response)
