from typing import List, Tuple

from cli.prints import print_hl, print_new_line

HELP = ("-h", "--help", "Lists all available commands with details.")
HELP_MINI = ("-H", "Just lists all available commands.")

TRANSFORM = ("-t", "--transform", "Transforms given text to filename accepted format.")
ENCLOSE_TRANSFORM = ("-te", "Transform encloses with given char, default is '[' ']' .")

PARSE = ("-p", "--parse", "Pareses transformed text to its otiginal format")
PARSE_ENCLOSED = ("-pe", "Parse included enclosings, if custom char used, it must be passed.")

GET = ("-g", "--get", "Downloads the file from given url. Used together with '-t' option.")

# TODO - More commands
# ["append name, replace name"]

COMMANDS_HELP_LIST:List[Tuple] = [HELP, HELP_MINI]
COMMANDS_TEXT_TRANSFORM_LIST:List[Tuple] = [TRANSFORM, PARSE]
COMMANDS_NETOWORK_OP_LIST: List[Tuple] = [GET]

COMMANDS_AVAILABLE = [*COMMANDS_HELP_LIST, *COMMANDS_TEXT_TRANSFORM_LIST, *COMMANDS_NETOWORK_OP_LIST]

class InvalidArgException(Exception):
    pass



# Print outs elements of tuple of list of commans. Tuple must have either 2 or 3 elements. 
def list_commands(list:List[Tuple]):
    for cmd in list:
        if len(cmd) == 3:
            print(f"\t{cmd[0]}, {cmd[1]}\t - {cmd[2]}")

        else:
            print(f"\t{cmd[0]}\t\t - {cmd[1]}")

    print_new_line()

# 
def print_detaild_commands():
    """
    Prints all the available commands with category and with/without example
    """
    print("Help")
    print_hl()
    list_commands(COMMANDS_HELP_LIST)

    print("Text transform and Parse")
    print_hl()
    list_commands(COMMANDS_TEXT_TRANSFORM_LIST)

    print("Network operations")
    print_hl()
    list_commands(COMMANDS_NETOWORK_OP_LIST)


