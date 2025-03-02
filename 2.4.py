# Create 
set1 = {5, 10, 15}
set2 = {4, 8, 12}

# Add 
set1.add(4)
set2.update([6, 7])

# Remove 
set1.remove(10)
set2.discard(5)

# Combine 
union = set1 | set2

# Common 
intersection = set1 & set2

# Difference
difference = set1 - set2

# Subset
subset = set1 <= set2

# Superset
superset = set2 >= set1

# Remove all 
set1.clear()

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("set1 a subset of set2", subset)
print("set2 a superset of set1", superset)