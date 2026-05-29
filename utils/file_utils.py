def read_colleagues(filepath: str) -> list[str]:
    """
    Read colleague names from a text file.

    :param filepath: A string representing the path to the text file.
    :return: A list of strings containing colleague names.
    """
    colleagues = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()

            if name:
                colleagues.append(name)

    return colleagues


def save_seating_plan(filepath: str, seating_plan: str) -> None:
    """
    Save the seating plan to a text file.

    :param filepath: A string representing the output file path.
    :param seating_plan: A string containing the seating plan.
    :return: None
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(seating_plan)