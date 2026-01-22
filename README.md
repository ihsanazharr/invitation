# invitation

## Modus Function

This repository contains a function to calculate the statistical mode (modus) of a dataset.

### What is Modus?

Modus (mode) is the value that appears most frequently in a dataset. It's one of the three measures of central tendency, along with mean and median.

### Usage

```python
from modus import modus

# Single mode
result = modus([1, 2, 2, 3, 4])
print(result)  # Output: 2

# Multiple modes (bimodal)
result = modus([1, 1, 2, 2, 3])
print(result)  # Output: [1, 2]

# Single element
result = modus([5])
print(result)  # Output: 5

# Empty list
result = modus([])
print(result)  # Output: None
```

### Function Signature

```python
def modus(data):
    """
    Calculate the mode (modus) of a dataset.
    
    Args:
        data: A list or iterable of values
        
    Returns:
        The mode value(s). If there are multiple modes, returns a list of all modes.
        Returns None if the dataset is empty.
    """
```

### Running Tests

To run the test suite:

```bash
python3 test_modus.py
```

### Features

- Handles datasets with single mode
- Handles datasets with multiple modes (bimodal/multimodal)
- Works with numbers, strings, and other comparable values
- Returns `None` for empty datasets
- Returns sorted list when multiple modes exist