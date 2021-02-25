# JSON Processing
Json is an data interchange format used widely on the Internet and supported by programming languages

## Encoding python objects in JSON
We can create a python directory 

```
with open('a_few_rocks.json', 'r') as rock_file:
    rocks = json.load(rock_file)
    print(rocks)
for r in rocks:
    print(r, ':', rocks[r])
...
with open('a_few_rocks.json', 'r') as rock_file2:
    #extract the contents of the file manually with file.read()
    rawstring = rock_file2.read()
    print(rawstring)
    # with the string in hand, pass to json.loads
    rocks2 = json.loads(rawstring)
    print(rocks2)
```
