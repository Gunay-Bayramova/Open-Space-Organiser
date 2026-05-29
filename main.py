import sys

from utils.file_utils import read_colleagues, save_seating_plan
from utils.openspace import Openspace


def main() -> None:
    """
    Run the OpenSpace Organizer program.

    The program reads colleague names from a text file, randomly assigns them
    to seats in the open space, displays the seating plan, and saves the result
    to a text file.

    :return: None
    """
    input_filepath = "new_colleagues.txt"
    output_filepath = "seating_plan.txt"

    if len(sys.argv) > 1:
        input_filepath = sys.argv[1]

    colleagues = read_colleagues(input_filepath)

    open_space = Openspace()
    open_space.organize(colleagues)

    seating_plan = open_space.generate_seating_plan()

    print(seating_plan)

    save_seating_plan(output_filepath, seating_plan)

    print(f"\nSeating plan saved to {output_filepath}")


if __name__ == "__main__":
    main()