class List:
    def __init__(self, data):
        if isinstance(data, (list, str)):
            self.data = data
        else:
            raise Exception("Only list and string datatype are allowed")

    def index(self, value):
        return self.data.index(value)

    def append(self, value):
        if isinstance(self.data, list):
            self.data.append(value)
        else:
            raise Exception("Append operation is only allowed for lists")
try:
    list_obj = List([1, 2, 3, 4]) # Create List object with a list and use append and index
    print("Original list:", list_obj.data)
    list_obj.append(5)    # Append new element
    print("List after append:", list_obj.data)
    idx = list_obj.index(4)# Get index of an element
    print("Index of 4 in list:", idx)
    string_obj = List("abcd")    # Create List object with a string and use index
    idx_str = string_obj.index('c')
    print("Index of 'c' in string:", idx_str)
    string_obj.append('e') # Trying to append to string object (should raise error)

except Exception as e:
    print("Error:", e)
finally:
    print("Thank you:")
