"""Hash table stores key-value pairs."""

"""A Hash table is a data structure that associates keys with values and is
 capable of time-efficient insertions, deletions and lookups.
"""

"""A Hash table inserts elements into different buckets depending on the hash-code of the element. The hash code is an index which can be computed
by a hash function. Unless two or more elements in the hash table have the same hash code, also known as a collision, the time-complexity of looking up the value associated with a certain key
is O(1). When the hash code of two different elements collide, the hash table utilizes linked lists. Then, the worst case time-complexity
of a lookup is linear. Fortunately, with a well designed hash function where different elements is distributed uniformly across all buckets, this is very rare."""

class _Node:
    """A node stores the key-value pair and points at new nodes in case of collision."""
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._next = None

class HashTable:
    """List structure for storing linked-lists of nodes in different buckets.
    Example:
        Bucket  |          Linked-lists
        ------------------------------------
            0   |    _Node --> _Node --> None
                      key       key
                      value     value

            1   |     _Node --> None
                      key
                      value

            2   |     None

        _size = 3
    """
    def __init__(self, bucket_size = 16):
        """Creates new empty hash table."""
        self._bucket = [None]*bucket_size
        self._size = 0


    def _HashFinder(self, key):
        """_hashFinder calculates hash code of a key with Daniel J. Bernsteins method."""
        hash_number = 5381
        if isinstance(key, str):
            #If key is string.
            for chr in key:
                hash_number += (hash_number << 5) + hash_number + ord(chr.lower()) # Same as hash_number += (hash_number*33) + ord(chr) but more efficient
        elif isinstance(key, int):
            #If key is integer.
            hash_number = (hash_number << 5) + hash_number + key
        return hash_number%len(self._bucket)


    def _ReHash(self):
        """_Rehash hashes again when the load factor has been reached. The loadfactor is 75 % of the total amount of buckets.
        _ReHash increases the bucket_size by a factor of two."""
        old_bucket = self._bucket
        self._bucket = [None]*len(self._bucket)*2
        self._size = 0
        for head in old_bucket:
            if head is not None:
                current = head
                while current is not None:
                    self.Add(current._key, current._value)
                    current = current._next



    def Add(self, key, value):
        """Add inserts new key-value pair to hash table."""
        hash_number = self._HashFinder(key)
        current = self._bucket[hash_number]
        prev = current
        if current is None:
            #Bucket is empty:
            self._bucket[hash_number] = _Node(key, value)
            self._size += 1
        else:
            while current:
                #Bucket is not empty. Traverse through bucket to search for duplicate.
                if current._key is key:
                    break
                prev = current
                current = current._next
            if current:
                #Duplicate exists. Update value.
                current._value = value
            else:
                #Duplicate does not exist. Add new element at the end.
                prev._next = _Node(key, value)
            self._size += 1

        if (self._size * 4/3) > len(self._bucket):
            #Load factor has been reached.
            self._ReHash()


    def Delete(self, key):
        """Removes a key-value pair from hash table."""
        hash_number = self._HashFinder(key)
        current = self._bucket[hash_number]
        if current == None:
            #Bucket is empty. Key does not exist in hash table.
            pass
        elif current._key is key:
            self._bucket[hash_number] = current._next
            self._size -= 1
        else:
            next = current._next
            while current:
                #Bucket is not empty. Traverse through list to search for given key.
                if next is not None:
                    if next._key is key:
                        #Key exists. Remove key value-pair.
                        current._next = next._next
                        self._size -= 1
                    else:
                        current = next
                        next = next._next
                #Key does not exist in hash table.
                break


    def Get(self, key):
        """Get returns value associated with given key."""
        hash_number = self._HashFinder(key)
        if self._bucket[hash_number] is None:
            #Key does not exist.
            return None
        else:
            current = self._bucket[hash_number]
            while current:
                if current._key is key:
                    #Key exists. Return value.
                    return current._value
                current = current._next
            return None #Key does not exist.


    def Size(self):
        """Returns the number of key-value pairs in hash table."""
        return self._size
