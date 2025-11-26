# List of 10 product names
products = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "Pendrive",
    "Charger", "Phone", "Bag", "Speaker", "Tablet"
]

print("Original List:", products)

# Append
products.append("Cable")

# Insert
products.insert(2, "USB Hub")

# Update
products[0] = "Gaming Laptop"

# Remove by value
products.remove("Bag")

# Pop last item
removed = products.pop()

# Pop at index
removed2 = products.pop(3)

print("\nAfter Operations:", products)
print("Popped:", removed, removed2)


print("-------------")


# Tuple of 10 product names
products = (
    "Laptop", "Mouse", "Keyboard", "Monitor", "Pendrive",
    "Charger", "Phone", "Bag", "Speaker", "Tablet"
)

print("Original Tuple:", products)

# Convert to list for operations
temp = list(products)

temp.append("Cable")
temp.insert(1, "USB Hub")
temp.remove("Monitor")

# Update
temp[0] = "Gaming Laptop"

# Pop
removed = temp.pop()

# Convert back to tuple
products = tuple(temp)

print("\nAfter Operations:", products)
print("Popped:", removed)



print("-------------")

# Set of product names
products = {
    "Laptop", "Mouse", "Keyboard", "Monitor", "Pendrive",
    "Charger", "Phone", "Bag", "Speaker", "Tablet"
}

print("Original Set:", products)

# Add single value
products.add("Cable")

# Update multiple values
products.update(["Router", "USB Hub"])

# Remove (error if not present)
products.remove("Monitor")

# Discard (no error)
products.discard("XYZ")

# Pop (removes random item)
removed = products.pop()

print("\nAfter Operations:", products)
print("Popped:", removed)


print("-------------")


# Dictionary of product names
products = {
    1: "Laptop",
    2: "Mouse",
    3: "Keyboard",
    4: "Monitor",
    5: "Pendrive",
    6: "Charger",
    7: "Phone",
    8: "Bag",
    9: "Speaker",
    10: "Tablet"
}

print("Original Dictionary:", products)

# Add new product
products[11] = "Cable"

# Update a product
products[1] = "Gaming Laptop"

# Remove by key
products.pop(4)

# Pop last item (removes last added)
removed = products.popitem()

print("\nAfter Operations:", products)
print("Popitem removed:", removed)

