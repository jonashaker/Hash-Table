# Hash-Table

## Hash table stores key-value pairs.

A Hash table is a data structure that associates keys with values and is capable of time-efficient insertions, deletions and lookups.

![](buckets.png)


A Hash table inserts elements into different buckets depending on the hash-code of the key associated with a certain element. The hash code is an index which is computed by a hash function. Unless two or more elements in the hash table have the same hash code, also known as a collision, the time-complexity of looking up the value associated with a certain key
is O(1). However, when the hash code of two or more different elements collide, the hash table utilizes linked lists for storing elements. Then, the worst case time-complexity
of a lookup is linear. Fortunately, with a well designed hash function where different elements is distributed uniformly across all buckets, collisions will rarely occur.

## Documentation

Hash Table consists of the following public classes and methods.

### Types

#### Class HashTable

      class HashTable()
          \\ Contains a list of different buckets
          and the number of items added.
Creates new empty hash table.

#### function Add()
      function Add(key, value) --> Void
Add adds key-value pair to hash table where key is either a string or an integer. If key already exists, update value. 
#### function Delete()
      function Delete(key) --> Void
Delete removes key from hash table.
#### function Get():
      function Get(key) --> Value      
Get returns value associated with given key.
#### function Size():
      function Size() --> Int
Size returns number of elements currently in hash table.
