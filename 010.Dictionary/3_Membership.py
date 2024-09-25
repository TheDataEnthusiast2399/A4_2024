from typing import Dict

# Membership works for checking keys in dictionaries, it doesn't work for values.
marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 65,
}

print(99 in marks)  # Returns false
print("history" in marks)
print("historyy" in marks)
