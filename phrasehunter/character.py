# Create your Character class logic in here.

```
Create the Character class in the character.py file
The class should include an initializer or def __init__ that receives a char parameter, which should be a single character string.
Hint: You will likely need at least two instance attributes:
An instance attribute to store the single char string character so the Character object will be able to remember the original character. You might call this instance attribute original, but that will be up to you.
An instance attribute to store a boolean value (True or False) of whether or not this letter has had a guess attempted against it. You can initialize this to False inside __init__ as any new Character object will start with a default of False meaning it has not been guessed before. You might name this instance attribute was_guessed, but that will also be up to you.
Any additional instance attributes you feel you need to store are up to you to decide on.
Hint: You will need at least two instance methods:
An instance method that will take a single string character guess as an argument when its called. The job of this instance method is to update the instance attribute storing the boolean value, if the guess character is an exact match to the instance attribute storing the original char passed in when the Character object was created.
An instance method that when called, will show the original character if the instance attribute was_guessed is True. Otherwise, the instance method should show an _ or underscore character to act as a hidden placeholder character.
The instance method names and their implementation are up to you to determine.
The Character instance is responsible for holding the state of a given single character. You should ensure when you create instances of Character() that you only pass a character that is a single character or len(char) == 1. Anything more or less should be invalid and might cause you bugs in your code, especially if you are passing the user's input directly into the creation of the Character object.
```
