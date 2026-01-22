#!/usr/bin/env python3
"""
Example usage of the modus function
"""

from modus import modus

print("=== Modus (Mode) Function Examples ===\n")

# Example 1: Single mode
data1 = [1, 2, 2, 3, 4, 5]
print(f"Data: {data1}")
print(f"Modus: {modus(data1)}")
print()

# Example 2: Multiple modes (bimodal)
data2 = [1, 1, 2, 2, 3]
print(f"Data: {data2}")
print(f"Modus: {modus(data2)}")
print()

# Example 3: All unique values
data3 = [1, 2, 3, 4, 5]
print(f"Data: {data3}")
print(f"Modus: {modus(data3)}")
print()

# Example 4: Single element
data4 = [42]
print(f"Data: {data4}")
print(f"Modus: {modus(data4)}")
print()

# Example 5: String values
data5 = ['apel', 'pisang', 'apel', 'jeruk', 'apel']
print(f"Data: {data5}")
print(f"Modus: {modus(data5)}")
print()

# Example 6: Empty dataset
data6 = []
print(f"Data: {data6}")
print(f"Modus: {modus(data6)}")
