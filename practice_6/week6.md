_______________
# Useful function:
## 1. `map()`: Applies a function to every element
how-to-use: `map(function, iterable)`
```python
# Works with numbers
arr = [1,2,3,4,5]

arr_5 = list(map(lambda x: x * 5, arr))
print(*arr_5)
  
# As well with words  
arr_words = ['faudja', 'pairy', 'greet']

arr_upper_words = list(map(str.upper(), arr_words))
print(*arr_upper_words)
```

______________
## 2. `filter()`: keeps only elements that match condition
how-to-use: `filter(function, iterable)`
```python
# example 0 
arr = [0,1,2,3,4,5,6,7,8,9]

arr_even = list(filter(lambda x: x%2 == 0, arr))
print(*arr_even)

# example 1
words = ['lol', 'lmao', 'superioty', 'caught']

new_words = list(filter(lambda x: len(x) > 4, words))
print(*new_words)
```

___________
## 3. `enumerate()`: iterates with index
how-to-use:`enumerate(iterable, start = 0) -> yields (index, value) pair`
```python
arr = ['wash dishes', 'wipe floor', 'clean dust']

for i, chore in enumerate(arr, start=1):
	print(f"{i}: {chore}")
```

_______________
## 4. `zip()`: pair elements from multiple iterables
how-to-use: `zip(iterable_1, iterable_2...)`
```python
names = ['Daulet', 'Abay', 'Ali']
scores = [-1, 0, -9]

for name, score in zip(names, scores):
	print(f"{name}: {score}")
	
	
name_and_score = list(zip(nemas, scores))
# [(Daulet, -1), (Abay, 0), (Ali, -9)]

n, s = zip(*name_and_scores)
```

_____________
## 5. `sorted()` and `reversed()`:
how-to-use:`well, just use it, bruh`
```python
# classic sort
arr = [6,7,6,9,7,7,5,3]

print(sorted(arr))
print(sorted(arr, reverse = True))

# sort by key 
words = ['neuro', 'evil', 'turtle', 'daug']
print(sorted(words, key=len))

# reversed() — lazy iterator
for x in reversed([1, 2, 3]):
    print(x, end=' ')
```

_____________________
## 6. `any()` and `all()`:
how-to-use:`any(smth), all(smth)`
```python
arr = [8,7,9,11,3,4,5]
print(any(x % 2 == 0 for x in arr)) # True
print(all(x % 2 == 0 for x in arr)) # False

words = ['swarm', 'bits', 'karaoke']
print(any(len(x) > 5 for x in words)) # True
print(all(len(x) > 5 for x in words)) # False
```

_______
## 7. More useful commands:
```python
# min / max with key
words = ["banana", "kiwi", "apple"]
print(min(words, key=len))   # kiwi
print(max(words, key=len))   # banana

# sum
print(sum([1, 2, 3, 4, 5]))         # 15
print(sum([1, 2, 3], start=10))     # 16  (Python 3.8+: start param)

# abs, round, pow
print(abs(-42))       # 42
print(round(3.14159, 2))  # 3.14
print(pow(2, 10))     # 1024

# len, type, isinstance
print(len("hello"))           # 5
print(type(3.14))             # <class 'float'>
print(isinstance(42, int))    # True
```
____________

# File handling:
opening file - `open(path, mode)`

`'r'` - Read (default). Error if file doesn't exist
`'w'` - Write. Creates file or **overwrites** existing
`'a'` - Append. Creates file or adds to the end
`'x'` - Create. Error if file already exists

___________
```python
# read all at once
file = open("text.txt", 'r')
content = file.read()

print(content)
file.close()
```
_____________
```python
# read lines
file = open("text.txt", 'r')
line1 = file.readline()
line2 = file.readline()

print(line1,line2)
file.close()
```
_________
```python
# read all lines into array
file = open("text.txt", 'r')
lines = file.readlines()

print(lines)
file.close()
```
________
```python
# iterate, memory efficient
file = open("text.txt", 'r')

for line in file:
	print(line.strip())
	
file.close()
```
_________
## Just forget all of this! That's the right way:

```python
with open('text.txt', 'r') as file:
	for line in file:
		print(line.strip())
# file will be closed automatically
```
________
```python
# Write mode — creates or overwrites
with open('output.txt', 'w') as f:
    f.write('Hello World\n')
    f.write('Second line\n')

# Append mode — adds to the end
with open('output.txt', 'a') as f:
    f.write('Appended line\n')

# Create mode — fails if file already exists
with open('new_file.txt', 'x') as f:
    f.write('Brand new file\n')
```
___________

# Working with directories:
```python
import os
```
_________
```python
import os

print(os.getcwd())          # /Users/askar/Documents/KBTU/PP2_2026
os.chdir('week7')           # change into a subdirectory
print(os.getcwd())          # /Users/askar/Documents/KBTU/PP2_2026/week7
```
_______
```python
import os

path = 'input.txt'

os.path.exists(path)    # True/False — path exists at all?
os.path.isfile(path)    # True/False — is it a file?
os.path.isdir(path)     # True/False — is it a directory?
os.path.join('dir1', 'dir2', 'file.txt')  # 'dir1/dir2/file.txt'
```
_______
## Listing contents — `os.listdir`
```python
import os

BASE = os.getcwd()

for name in os.listdir(BASE):
    full_path = os.path.join(BASE, name)
    if os.path.isfile(full_path):
        print(f'FILE: {name}')
    else:
        print(f' DIR: {name}')
```
_______
## Walking the entire tree — `os.walk`
`os.walk` yields `(root, dirs, files)` for each directory recursively.
```python
import os

for root, dirs, files in os.walk(os.getcwd()):
    print(f"In: {root}")
    for d in dirs:
        print(f"  DIR:  {d}")
    for f in files:
        print(f"  FILE: {f}")
```
_______
## Scanning — `os.scandir`
More efficient than `os.listdir` — gives `DirEntry` objects with metadata.
```python
import os

with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            print(f'File: {entry.name}')
        elif entry.is_dir():
            print(f'Dir:  {entry.name}')
```
__________
