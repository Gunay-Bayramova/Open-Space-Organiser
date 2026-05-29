
Open Space Organiser - Becode Project 1
# Open Space Organiser

## Description

Open Space Organiser is a Python program that randomly assigns colleagues to seats in an open space.

The default room setup is:

* 6 tables
* 4 seats per table
* 24 seats in total

The program reads a list of colleagues from a `.txt` file, randomly places them at the available tables, displays the seating plan in the terminal, and saves the result in a `seating_plan.txt` file.

This project was created as part of the BeCode AI Bootcamp to practice Object-Oriented Programming, project structure, file handling, imports, and GitHub workflow.

## Features

* Read colleague names from a text file
* Randomly assign people to tables
* Display the seating plan in the terminal
* Save the seating plan to a text file
* Show the total room capacity
* Show how many people were assigned
* Show how many seats are left
* Handle the case where there are more people than available seats

## Project Structure

```text
.
├── notebook_guide.ipynb
├── README.md
├── main.py
├── new_colleagues.txt
├── seating_plan.txt
├── .gitignore
└── utils/
    ├── __init__.py
    ├── file_utils.py
    ├── openspace.py
    └── table.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Gunay-Bayramova/Open-Space-Organiser.git
```

Go into the project folder:

```bash
cd Open-Space-Organiser
```

No external Python packages are required. The project only uses built-in Python modules.

## Usage

Run the program from the terminal:

```bash
python3 main.py
```

By default, the program reads names from:

```text
new_colleagues.txt
```

You can also provide another text file as an argument:

```bash
python3 main.py another_file.txt
```

The program displays the seating plan in the terminal and saves the result in:

```text
seating_plan.txt
```

## Example Output

```text
Table 1:
- Anna
- Max
- Ibrahim
- Hiba

Table 2:
- Gunay
- Dan
- Neha
- Victor

Total capacity: 24 seats
Assigned people: 24
Seats left: 0
```

Because the assignment is random, the seating plan changes every time the program is run.

## Technologies Used

* Python
* Object-Oriented Programming
* Git
* GitHub

## Timeline

This project was completed in 2 days.

## Personal Situation

This project was completed as part of the BeCode AI Bootcamp.
