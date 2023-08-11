# Extract Middle Characters from a input

This is a Python function that extracts the middle character(s) from a given input.

## Usage

You can use the `extract_middle_characters` function to extract the middle character(s) from a input.

### Example

```python
def extractmiddlecharacters(input_string):
    if (len(input_string)%2 == 0):
        print(f"The given string {input_string} is even .\nExtracting the middle two characters : {input_string[(len(input_string)-1)//2:(len(input_string)+2)//2]}")

    else:
        print(f"The given string {input_string} is odd .\nExtracting the middle character : {input_string[(len(input_string)-1)//2:(len(input_string)+2)//2]}")

extractmiddlecharacters(input())

