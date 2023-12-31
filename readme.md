## Python Personal Assistant

The project is a "Personal Assistant" application developed using Python as the primary programming language. It is a console-based application designed to assist users in managing contacts, storing notes, and keeping track of important dates such as birthdays. The application utilizes MongoDB as the database for storing contact information and notes.

## Authors

- [@czajan83](https://github.com/czajan83)
- [@julotec](https://github.com/julotec)
- [@skovroneq](https://github.com/skovroneq)
- [@Marek511](https://github.com/Marek511)
- [@wiktoriastefania](https://github.com/wiktoriastefania)



## Features

- Contact Management:
Store and manage contacts with names, addresses, phone numbers, email addresses, and birthdays in the contact book

Display a list of contacts with upcoming birthdays within a specified number of days from the current date

Validate entered phone numbers and email addresses during contact creation or editing, and notify the user in case of invalid entries

Search for contacts among the phonebook entries

Edit and delete contact entries.

- Note Taking:
Create and save text-based notes

Search for notes based on their content

Edit and delete notes

- Text Analysis and User Suggestions:
Analyzing user-entered text to identify and suggest contact names when conducting searches

This feature enhances user convenience by suggesting relevant contact names as search results


## Run Locally

Clone the project

```bash
  git clone https://github.com/softest-group4/softest.git
```

Install MongoDB on your machine

```bash
  https://www.mongodb.com/docs/manual/administration/install-community/
```

Install dependencies

```bash
  pip install pymongo~=4.5.0 Levenshtein~=0.23.0 pytest~=7.4.2 setuptools~=65.5.1

```

In setup.py run the following command
```bash
  pip install .

```
Our PA is now installed and ready for use! 

If you encounter any issues during the installation process, make sure you have Python and pip properly configured on your system, and double-check the versions of the specified dependencies in your setup.py and requirements.txt files.


```bash

```
    
