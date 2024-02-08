
# 0x00. AirBnB clone - The console

## Project Descriptiom

The AirBnB clone project is first step towards building my first full web applicationThis first step is very important because I will use what I build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help me to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## The Command Interpreter
The Command Interpreter is exactly the same as the Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project. The model must be able to Create, Read/Retrieve, Update, and Delete resources as described below:

* Create a new object (ex: a new User or a new Place)
* Read/Retrieve an object from a file, a database etc…
* Update attributes of an object
* Do operations on objects (count, compute stats, etc…)
* Destroy an object

## Execution
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```
