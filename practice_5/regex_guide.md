_____________
So regex is overall the library that helps as to find a difficult patterns in strings


```python
import re

# let's create a regex object to find patterns (\d - digit character)
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# or just: ({x} - amount of elements)
phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")

# finding pattern in the text
text = phone_num_regex.search("My number is 422-324-4223")
print(f"The number is: {text.group()}")
```


-----
### Character classes:
* `\d` - only digits 
* `\w` - words, letters, numbers, underscore
* `\s` - space, tab, newline
* ```.``` - anything except newline
* `\D` - not a digit (Anything that is _not_ 0-9 (letters, symbols, spaces))
* `\W` - not a word (Anything that is _not_ a letter, number, or underscore (like `!`, `@`, or spaces))
* `\S` - not whitespace (Anything that is visible (letters, numbers, punctuation))
____ 
### The Absolute Anchors (`\A` and `\Z`)

These are similar to `^` (start) and `$` (end), but they are more "strict."
- **`\A`**: Matches **only** at the very start of the entire string.
- **`\Z`**: Matches **only** at the very end of the entire string.    

**Why use them instead of `^` and `$`?** In Python, if you use "Multiline Mode" (where you treat each line of a big block of text separately), `^` will match the start of _every_ line. However, **`\A` will still only match the very first character of the first line.**

---------

### Quantifiers:
* `*` - zero or more times
* `+` - one or more times
* `?` - zero or one time
* `{n}` - exactly n times
* `{n,}` - at least n times
* `{min, max}` - limit the times by a range
______
### The "Lazy" Quantifiers (The `?` Trick)
If you add a `?` **after** another quantifier, it turns "Lazy." It will now match the **smallest** amount of text possible to satisfy the pattern.
- **Greedy:** `r"<.*>"` on `<div>Hello</div>` matches the **entire string** because it starts at the first `<` and ends at the very last `>`.
- **Lazy:** `r"<.*?>"` on `<div>Hello</div>` matches **only** `<div>`. It stops at the very first `>` it sees.
__________
### Group Quantifiers
You can apply these to more than just one letter. If you wrap characters in parentheses `()`, the quantifier applies to the **whole group**.
- **Pattern:** `r"(Ha){3}"`
- **Matches:** `"HaHaHa"`
- Without the parentheses, `r"Ha{3}"` would match `"Haaa"`.
____________
### Anchors:
* `^` - the start of a string
* `$` - the end of a string
____
### That one guy:

Usually, you don't want the "OR" to apply to the entire sentence. You use parentheses ``()`` to limit the scope of the `|`.

**Example: Finding different image files** If you want to find files ending in `.jpg`, `.png`, or `.gif`, you would write: `r".*\.(jpg|png|gif)"`


```python
import re

text = "I would like an apple, but a pear is also fine."

# Search for apple OR orange OR pear
fruit_pattern = re.compile(r"apple|orange|pear")

matches = fruit_pattern.findall(text)
print(matches) # Output: ['apple', 'pear']
```

__________
### Sets and groups:
Sometimes basic classes like `\d` are not enough, so we can build our own with sets:
`[ ]` - match any character inside brackets:
* `[aeiou]` - match only vowels
* `[a-z]` - all lowercase letters
We search for specific objects in string to capture exactly that part, so our helper is groups:
`( )` - Captures a part of string so you can extract it later:
* `(\d{3}-\d{4}-\d{4})` - you can specifically ask for this part
------
### The Power of Square Brackets `[]`
A set matches **exactly one** character, but you get to decide which ones are allowed.

| **Set**       | **Meaning**              | **Example**                        |
| ------------- | ------------------------ | ---------------------------------- |
| `[aeiou]`     | Any **vowel**            | Matches `a`, `e`, `i`, `o`, or `u` |
| `[a-z]`       | Any **lowercase** letter | Matches `g`, `z`, etc.             |
| `[A-Z]`       | Any **uppercase** letter | Matches `G`, `Z`, etc.             |
| `[0-9]`       | Any **number**           | (Same as `\d`)                     |
| `[a-zA-Z0-9]` | Any **alphanumeric**     | Matches any letter or number       |

### The "Negative" Set `[^ ]`
If you put a caret `^` **inside** the square brackets at the very beginning, it means **"Any character EXCEPT these."**
- `[^aeiou]` matches any consonant, symbol, or number (anything that isn't a lowercase vowel).
- `[^0-9]` matches anything that isn't a digit (same as `\D`).
---
### Word Boundaries `\b` (The "Invisible" Class)
This is a "positional" class, similar to `^` and `$`, but it detects the **edge** of a word.
- **Pattern:** `\bcat\b`
- **Text:** "The **cat** sat on the con**cat**enated rug."
- **Result:** It matches the first "cat" but **ignores** the one inside "concatenated" because that one doesn't have a boundary (space or punctuation) around it.
________
### Regex functions:
#### `re.search()`:
Scans the **entire string** and returns the **first** location where the pattern matches:
- **Returns:** A "Match object" if found, or `None` if not.
- **Best for:** Checking if a string contains a specific pattern (like checking if an input is a valid email).
```python
import re

text = "The price is 200$"
match = re.search(r"\$\d+", text)

if match:
	print(match.group())
```
or	
```python
import re

text = "Hello, my birthday is after ^30^ days!"
match = re.search(r"\^\d+\^ days", text)

if match:
    print(match.group())
```
__________
#### `re.findall()`:
Scans the entire string and finds **every** occurrence of the pattern.
- **Returns:** A **list of strings**.
- **Best for:** Extracting multiple items, like all dates or all hashtags from a paragraph.
```python
import re

text = "dauren@harosh.com, ladno@bopti.lol"
match_text = re.findall(r"\w+@\w+\.\w+", text)

print(match_text)
```

_______________
#### `re.sub()`:
Stands for "substitute." it searches for a pattern and **replaces** it with something else.
- **Returns:** A **new string** with the replacements made.
- **Best for:** Cleaning data or censoring sensitive information.
```python
import re

text = "Daulet take 5 of this beans into his mouth at the same time"
new_text = re.sub(r"\d|beans", '[CENSORED]', text)

print(new_text)
```

_________
#### `re.compile()`:
If you are going to use the same regex pattern dozens or hundreds of times (like in a loop), you "pre-build" it first.
- **Why use it:** It’s faster and keeps your code cleaner.
```python
import re

number_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
email_regex = re.compile(r"\w+@\w+\.\w+")

text = "Ali is available by number: 123-343-4345, and email: chort@gmail.loh"  

print(number_regex.search(text).group())
print(email_regex.search(text).group())
```
_______
#### `re.split()`:
Buffed basic split:
```python
import re

text = "apples banana,qiwi;lemon-melon-cookie"
fruits = re.split(r",|;| +", text)  

print(fruits)
```
or
```python
log = "2026-03-06 ERROR: Database connection failed"

# Split only at the first two spaces
parts = re.split(r" ", log, maxsplit=2)

print(parts)
# Output: ['2026-03-06', 'ERROR:', 'Database connection failed']
```
___________
#### `re.match()`:
You use it when the **structure** of the entire line matters. It is perfect for **validation**.
- **Checking a Username:** If a username must start with a letter.
- **Checking a Protocol:** If a URL must start with `https`.
- **CSV Parsing:** If you are looking for a specific code at the start of a data row.
```python
import re

text = "The answer is 42"

# 1. re.match() looks at the START
result_match = re.match(r"\d+", text) 
print(result_match) # Output: None (because it starts with 'T', not a digit)

# 2. re.search() looks EVERYWHERE
result_search = re.search(r"\d+", text)
print(result_search.group()) # Output: 42
```

_____________
### 1. `re.IGNORECASE` (or `re.I`)

This is the most common flag. It makes your pattern case-insensitive, so `[a-z]` will also match `[A-Z]`.
```python
import re

text = "PYTHON is fun, python is easy."
# Without the flag, this only finds the lowercase one
matches = re.findall(r"python", text, re.IGNORECASE)

print(matches) # Output: ['PYTHON', 'python']
```
________
### 2. `re.MULTILINE` (or `re.M`)
By default, the anchors `^` and `$` only match the very start and very end of the **entire string**.
- **With this flag:** `^` and `$` match the start and end of **each line** (after every newline `\n`).
_________
### 3. `re.DOTALL` (or `re.S`)
Normally, the dot `.` matches everything **except** a newline.
- **With this flag:** The dot matches **everything**, including newlines. This is useful when you want to capture a block of text that spans multiple paragraphs.
```python
text = "First Line\nSecond Line"

# Without DOTALL, this fails because of the newline
match = re.search(r"First.*Line", text, re.DOTALL)
```
_______
### 4. `re.VERBOSE` (or `re.X`)
Regex can get ugly and unreadable very fast. This flag allows you to write regex across **multiple lines** and add **comments** inside the pattern. The engine will ignore all whitespace and comments you add.
```python
# Instead of r"(\d{3})-(\d{3}-\d{4})"
pattern = re.compile(r"""
    (\d{3})     # Area code
    -           # Separator
    (\d{3}-\d{4}) # Main number
""", re.VERBOSE)
```
---
### 5. Combining Multiple Flags
What if you want to ignore case **and** use multiline mode? You use the **pipe symbol `|`** to combine them.
```python
re.findall(r"pattern", text, re.IGNORECASE | re.MULTILINE)
```
_________
