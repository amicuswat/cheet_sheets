## If you can read this...

### Instruction
#### Task
You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

#### Input:

If, you can read?

#### Output:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

#### Note:

- There are preloaded dictionary you can use, named NATO
- The set of used punctuation is ,.!?.
- Punctuation should be kept in your return string, but spaces should not.
- Xray should not have a dash within.
- Every word and punctuation mark should be seperated by a space ' '.
- There should be no trailing whitespace
### Test
```python
def basic_tests():
    test.assert_equals(to_nato('If you can read'), "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
    test.assert_equals(to_nato('Did not see that coming'), "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
    test.assert_equals(to_nato('.d?d!'),'. Delta ? Delta !')
```

### My variant
```python
letters_dict = {
    'A':'Alfa',
    'B':'Bravo',
    'C':'Charlie',
    'D':'Delta',
    'E':'Echo',
    'F':'Foxtrot',
    'G':'Golf',
    'H':'Hotel',
    'I':'India',
    'J':'Juliett',
    'K':'Kilo',
    'L':'Lima',
    'M':'Mike',
    'N':'November',
    'O':'Oscar',
    'P':'Papa',
    'Q':'Quebec',
    'R':'Romeo',
    'S':'Sierra',
    'T':'Tango',
    'U':'Uniform',
    'V':'Victor',
    'W':'Whiskey',
    'X':'Xray, x-ray',
    'Y':'Yankee',
    'Z':'Zulu',
}

def to_nato(words):
    words = words.replace(' ', '')
    letters = list(words)
    for i in range(len(letters)):
        if letters[i].upper() in letters_dict:
            letters[i] = letters_dict[letters[i].upper()]
    
    return ' '.join(letters)
```

### Other variants
```python
def to_nato(words):
    return " ".join(NATO.get(char, char) for char in words.upper() if not char.isspace())
```
`dict.get(key[, default])` - возвращает значение или значение по умолчанию если ключа нет
В данном случае автор передавал символ, если символ соответствовал, выдавал
значение в словаре, если символ был знак препинания то возвращал символ по дефолту