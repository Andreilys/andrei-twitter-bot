# hash tables map keys with objects
def hash_function(x, buckets):
    return hash(x) % buckets


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def show(self):
        Nodes = []
        current_node = self.head
        while current_node is not None:
            Nodes.append(current_node.data)
            current_node = current_node.next
        return Nodes

    def find(self, key):
        current_node = self.head
        while current_node is not None:
            # if the first data point (the key) is equal to the data
            if current_node.data[0] == key:
                # returns the value
                return current_node
            else:
                current_node = current_node.next
        return None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next


class HashTable(object):
    # initialize the hashtable
    def __init__(self, table=None, bucket=10, size=0):
        # init with a bucket size of 10
        self.bucket = bucket
        self.table = [None] * bucket
        self.size = size

    # set the value of the hash table
    def set(self, key, value):
        # find the correct bucket for key using hash algorithim
        bucket_number = hash_function(key, self.bucket)

        # create a new linked list node with both the key + value to be stored
        if self.table[bucket_number] is None:
            linked_List = LinkedList()
            linked_List.append((key, value))
            self.table[bucket_number] = linked_List
            self.size = self.size + 1
        else:
            # TODO check key if already inside
            self.table[bucket_number].append((key, value))
            self.size = self.size + 1
            # add key value to the linkedList
            # append a new node to the linkedlist in the bucket
        return self.table

    # TODO should this be when above number "x"?
    def check_load_factor(self):
        return (float(self.size)/self.bucket)

    # TODO resize the table/rehash all the current table functions as well
    def resize(self):
        return None

    def get(self, key):
        bucket_number = hash_function(key, self.bucket)
        # if the table w/ bucket number exists, return the value
        if self.table[bucket_number].find(key):
            print("Value is: " + str(self.table[bucket_number].find(key).data[1]))

    # update the value of the hash table
    def update(self, key, value):
        bucket_number = hash_function(key, self.bucket)
        if self.table[bucket_number].find(key):
            Node = self.table[bucket_number].find(key)
            Node.data = (key, value)

    def return_keys(self):
        keys = []
        length = len(self.table)
        for bucket_number in range(length):
            if self.table[bucket_number]:
                Nodes = self.table[bucket_number].show()
                length = len(Nodes)
                for i in range(length):
                    keys.append(Nodes[i][0])
        return keys

    # return the values
    def return_values(self):
        values = []
        length = len(self.table)
        for bucket_number in range(length):
            if self.table[bucket_number]:
                Nodes = self.table[bucket_number].show()
                length = len(Nodes)
                for i in range(length):
                    values.append(Nodes[i][1])
        return values

if __name__ == '__main__':
    roman = HashTable()
    roman.set('I', 1)
    roman.set('B', 2)
    roman.set('C', 3)
    roman.set('D', 4)
    roman.set('R', 2)
    roman.get('R')
    roman.update("I", 5)
    print(roman.check_load_factor())
    print(roman.return_values())
    print(roman.return_keys())
