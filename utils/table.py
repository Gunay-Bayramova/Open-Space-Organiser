from typing import Optional


class Seat:
    """
    Class representing one seat in the open space.

    :param free: A boolean that shows if the seat is free or occupied.
    :param occupant: The name of the person sitting on the seat, or None if empty.
    """

    def __init__(self) -> None:
        """
        Initialize a free seat with no occupant.

        :return: None
        """
        self.free: bool = True
        self.occupant: Optional[str] = None

    def set_occupant(self, name: str) -> bool:
        """
        Assign a person to the seat if the seat is free.

        :param name: A string representing the name of the person.
        :return: A boolean. True if the person was assigned, False if the seat was already occupied.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return True

        return False

    def remove_occupant(self) -> Optional[str]:
        """
        Remove the current occupant from the seat.

        :return: The name of the removed occupant, or None if the seat was already empty.
        """
        removed_occupant = self.occupant
        self.occupant = None
        self.free = True
        return removed_occupant

    def __str__(self) -> str:
        """
        Return a readable string representation of the seat.

        :return: A string showing the occupant name or 'Empty'.
        """
        if self.occupant:
            return self.occupant

        return "Empty"


class Table:
    """
    Class representing one table in the open space.

    :param capacity: An integer representing the number of seats at the table.
    """

    def __init__(self, capacity: int = 4) -> None:
        """
        Initialize a table with a fixed number of seats.

        :param capacity: An integer representing how many seats the table has.
        :return: None
        """
        self.capacity: int = capacity
        self.seats: list[Seat] = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        """
        Check if the table has at least one free seat.

        :return: A boolean. True if there is a free seat, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                return True

        return False

    def assign_seat(self, name: str) -> bool:
        """
        Assign a person to the first available seat at the table.

        :param name: A string representing the name of the person.
        :return: A boolean. True if the person was assigned, False if the table is full.
        """
        for seat in self.seats:
            if seat.set_occupant(name):
                return True

        return False

    def left_capacity(self) -> int:
        """
        Count how many seats are still free at the table.

        :return: An integer representing the number of free seats.
        """
        free_seats = 0

        for seat in self.seats:
            if seat.free:
                free_seats += 1

        return free_seats

    def get_occupants(self) -> list[str]:
        """
        Get the list of people sitting at the table.

        :return: A list of strings containing occupant names.
        """
        occupants = []

        for seat in self.seats:
            if seat.occupant:
                occupants.append(seat.occupant)

        return occupants

    def __str__(self) -> str:
        """
        Return a readable string representation of the table.

        :return: A string containing all seat occupants.
        """
        seat_names = [str(seat) for seat in self.seats]
        return " | ".join(seat_names)