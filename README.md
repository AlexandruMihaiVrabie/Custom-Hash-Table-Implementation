# Custom-Hash-Table-Implementation

A straightforward, educational Python implementation of a **Hash Table** (or Hash Map) data structure from scratch. This project demonstrates core computer science concepts, including custom hashing algorithms and collision resolution, without relying on Python's built-in dictionary hashing logic.

## 🚀 Features

* **Custom Hashing Algorithm:** Calculates the hash of a string by summing the ASCII values of its characters using Python's native `ord()` function.
* **Intelligent Collision Resolution:** What happens when two different keys generate the same hash (like anagrams "dear" and "read")? This script handles collisions elegantly by utilizing a nested dictionary structure at the hashed index, ensuring no data is overwritten or lost.
* **Standard Data Operations:** Includes the fundamental methods required for a complete hash table: `add(key, value)`, `remove(key)`, and `lookup(key)`.
* **Zero Dependencies:** Written entirely in pure Python, making it perfect for studying data structures.

## 🧠 How This Hash Table Works


1. **Hashing:** When you add a key-value pair, the `hash()` method converts the string key into an integer index. For example, 'golf' becomes `424`.
2. **Storage & Collisions:** The data is stored in the `collection` dictionary. If an index is empty, it creates a new bucket (a nested dictionary) containing the key-value pair. If the index is already occupied by a *different* key (a collision), it simply adds the new key-value pair to that existing bucket.
3. **Retrieval (`lookup`):** To find a value, the script hashes the requested key to find the correct bucket, and then searches inside that specific bucket for the exact original key.

## 🛠️ Requirements & Running

This project requires **Python 3.x**.

1. Clone the repository or download the `hash_table.py` file.
2. Open your terminal or command prompt.
3. Navigate to the folder and run:

```bash
python hash_table.py
```

## 💻 Code Example & Usage

You can easily instantiate the table and manage your key-value pairs. The following example demonstrates how it perfectly handles hash collisions:

```python
ht = HashTable()

# 'dear' and 'read' are anagrams, meaning their ASCII sums are identical (412)
ht.add('dear', 'friend')
ht.add('read', 'book')

# The table successfully stores both at the same hash index without data loss
print(ht.collection[412])
# Output: {'dear': 'friend', 'read': 'book'}

# Retrieve a specific value
print(ht.lookup('dear'))
# Output: friend

# Remove an item
ht.remove('read')
print(ht.collection[412])
# Output: {'dear': 'friend'}
```

## 🤝 Contributing

Contributions are always welcome! This is an educational repository, so if you'd like to implement alternative hashing algorithms (like SHA-256), or different collision handling methods (like linear probing or linked-list separate chaining), feel free to fork the repository and open a Pull Request.
