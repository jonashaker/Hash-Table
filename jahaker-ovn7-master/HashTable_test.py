import Hash_Table as ht
import random

randomkeys = random.sample(range(0, 1000000), 100000)
randomvalues = random.sample(range(0, 1000000), 100000)

def Test_HashFinder():
    """Two different hash_numbers calculated with different bucket sizes by hand and compared to the implemented function."""
    #String keys.
    h1 = ht.HashTable()
    assert h1._HashFinder("Jonas") == 5
    assert h1._HashFinder("Maria") == 3
    h2 = ht.HashTable(2024)
    assert h2._HashFinder("Jonas") == 1157
    assert h2._HashFinder("Maria") == 1723
    #Integer keys
    assert h1._HashFinder(1) == 6
    assert h1._HashFinder(12) == 1


def TestAdd():
    #Inserting key value pair into bucket.
    a1 = ht.HashTable()
    a1.Add("Jonas", 10)
    assert a1._bucket[5]._key == "Jonas"
    assert a1._bucket[5]._value == 10
    assert a1._bucket[5]._next is None
    #Inserting key-value pair in the same bucket as "Jonas". "Jonso" and "Jonas" has the same hash code.
    a1.Add("Jonso", 15)
    assert a1._bucket[5]._key == "Jonas"
    assert a1._bucket[5]._next._key == "Jonso"
    #Inserting key-value pair with the same key but different value as before. Hash table updates the value.
    a1.Add("Jonso", 5)
    assert a1._bucket[5]._next._key == "Jonso"
    assert a1._bucket[5]._next._value == 5
    assert a1._bucket[5]._key == "Jonas"

def TestGet():
    g1 = ht.HashTable()
    g1.Add("Jonas", 5)
    assert g1.Get("Jonas") == 5
    g1.Add("Jonso", 10)
    assert g1.Get("Jonso") == 10
    #Testing with large amounts of random key-value pairs.
    g2 = ht.HashTable(100000)
    for index in range(0, 100000):
        g2.Add(randomkeys[index], randomvalues[index])
    for index in range(0, 100000):
        assert g2.Get(randomkeys[index]) == randomvalues[index]

def TestDelete():
    d1 = ht.HashTable()
    d1.Add("Maria", 5)
    assert d1._bucket[3]._key == "Maria"
    d1.Delete("Maria")
    assert d1._bucket[3] == None
    #Testing Delete if there are more than one key-value pair in the bucket.
    d1.Add("Jonso", 10)
    d1.Add("Jonas", 5)
    assert d1._bucket[5]._key == "Jonso"
    assert d1._bucket[5]._next._key == "Jonas"
    d1.Delete("Jonas")
    assert d1._bucket[5]._key == "Jonso"
    d1.Add("Jonas", 10)
    assert d1._bucket[5]._next._key == "Jonas"
    d1.Delete("Jonso")
    assert d1._bucket[5]._key == "Jonas"

    # Mass test of delete.
    d2 = ht.HashTable(100000)

    for index in range(0,100000):
        d2.Add(randomkeys[index], randomvalues[index])
    for index in range(0, 100000):
        assert d2.Get(randomkeys[index]) == randomvalues[index]
    for index in range(0, 100000):
        d2.Delete(randomkeys[index])
    for i in range(0, len(d2._bucket)):
        assert d2._bucket[i] == None



def Test_ReHash():
    r1 = ht.HashTable()
    for index in range(0,12):
        r1.Add(randomkeys[index], randomvalues[index])

    for index in range(0,12):
        assert r1.Get(randomkeys[index]) == randomvalues[index]

    assert len(r1._bucket) == 16

    r1.Add("Jonas", 10)
    #Load factor has been reached. Hash table should rehash.
    assert len(r1._bucket) == 32
    for index in range(0,12):
        assert r1.Get(randomkeys[index]) == randomvalues[index]


    # Testing _ReHash by adding many different elements.
    r2 = ht.HashTable()
    for index in range(0,1000):
        r2.Add(randomkeys[index], randomvalues[index])

    for index in range(0,1000):
        assert r2.Get(randomkeys[index]) == randomvalues[index]

    assert len(r2._bucket) == 2048



def TestSize():
    s1 = ht.HashTable()
    assert s1.Size() == 0
    s1.Add("Jonas", 10)
    assert s1.Size() == 1
    for index in range(0,1500):
        s1.Add(randomkeys[index], randomvalues[index])
    assert s1.Size() == 1501
    s1.Delete(randomkeys[random.randint(0, 1500)])
    assert s1.Size() == 1500
    s1.Delete("Jopa") #Removing random key not in Hash Table
    assert s1.Size() == 1500


def main():
    TestGet()
    Test_HashFinder()
    TestAdd()
    TestDelete()
    Test_ReHash()
    TestSize()

if __name__ == '__main__':
    main()
