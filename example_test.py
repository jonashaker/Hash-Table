import Hash_Table as ht

"""Storing two key-value pairs and using Get() and Size() methods."""
def example():
    hcp = ht.HashTable()
    hcp.Add("Jonas", 3)
    print(hcp.Get("Jonas"))
    # Output: 3
    hcp.Add("Maria", 15)
    print(hcp.Size())
    #Output: 2
