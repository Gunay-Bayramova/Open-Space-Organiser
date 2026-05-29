import random

from utils.table import Table


class Openspace:
    """
    Class representing the whole open space with several tables.

    :param number_of_tables: An integer representing how many tables are in the room.
    :param table_capacity: An integer representing how many seats each table has.
    """

    def __init__(self, number_of_tables: int = 6, table_capacity: int = 4) -> None:
        """
        Initialize the open space with a default setup of 6 tables and 4 seats per table.

        :param number_of_tables: An integer representing the number of tables.
        :param table_capacity: An integer representing the number of seats per table.
        :return: None
        """
        self.number_of_tables: int = number_of_tables
        self.table_capacity: int = table_capacity
        self.tables: list[Table] = [
            Table(table_capacity) for _ in range(number_of_tables)
        ]
        self.unassigned_people: list[str] = []

    def organize(self, names: list[str]) -> list[str]:
        """
        Randomly assign people to available seats in the open space.

        :param names: A list of strings containing colleague names.
        :return: A list of strings containing people who could not be assigned.
        """
        shuffled_names = names.copy()
        random.shuffle(shuffled_names)

        for name in shuffled_names:
            available_tables = []

            for table in self.tables:
                if table.has_free_spot():
                    available_tables.append(table)

            if available_tables:
                random_table = random.choice(available_tables)
                random_table.assign_seat(name)
            else:
                self.unassigned_people.append(name)

        return self.unassigned_people

    def left_capacity(self) -> int:
        """
        Count how many seats are still free in the whole open space.

        :return: An integer representing the number of free seats.
        """
        free_seats = 0

        for table in self.tables:
            free_seats += table.left_capacity()

        return free_seats

    def total_capacity(self) -> int:
        """
        Count the total number of seats in the whole open space.

        :return: An integer representing the total number of seats.
        """
        return self.number_of_tables * self.table_capacity

    def count_people(self) -> int:
        """
        Count how many people are currently assigned to seats.

        :return: An integer representing the number of assigned people.
        """
        assigned_people = 0

        for table in self.tables:
            assigned_people += len(table.get_occupants())

        return assigned_people

    def generate_seating_plan(self) -> str:
        """
        Generate a readable seating plan.

        :return: A string containing the full seating plan.
        """
        lines = []

        for index, table in enumerate(self.tables, start=1):
            lines.append(f"Table {index}:")

            for occupant in table.get_occupants():
                lines.append(f"- {occupant}")

            empty_seats = table.left_capacity()

            for _ in range(empty_seats):
                lines.append("- Empty")

            lines.append("")

        lines.append(f"Total capacity: {self.total_capacity()} seats")
        lines.append(f"Assigned people: {self.count_people()}")
        lines.append(f"Seats left: {self.left_capacity()}")

        if self.unassigned_people:
            lines.append("")
            lines.append("People without a seat:")

            for person in self.unassigned_people:
                lines.append(f"- {person}")

        return "\n".join(lines)

    def display(self) -> None:
        """
        Display the seating plan in the terminal.

        :return: None
        """
        print(self.generate_seating_plan())

    def __str__(self) -> str:
        """
        Return a readable string representation of the open space.

        :return: A string containing the seating plan.
        """
        return self.generate_seating_plan()