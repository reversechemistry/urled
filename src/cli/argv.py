

def argv_has_cmd(argv:list[str], command:str | list[str]) -> tuple[bool, int]:
    """
    Given the argv and command, checks whether given command/commands is inluced in teh argv
    
    Returns -> (is_icludes:bool, index:int) 

    is_inludes:bool - Whether argv includes given command/commands
    index:int       - Index of given command

    example:
        arg = argv_has_it("-h")\n
        is_help = arg[0]\n
        index_of_help = arg[1]

    Note that if command is a list and any element of the list inlcuded in argv, will return true and the index.
    
    """

    idx = 0
    for arg in argv:
        idx += 1
        if type(command) == list:
            for cmd in command:
                if cmd == arg:
                    return (True, idx)

        else:
            if arg == command:
                return (True, idx)
    return (False, idx)


def argv_parse_commands(argv:list[str], commands:list[str], order:bool = False) -> list[tuple[bool, int, str]]:
    """
    argv_has_commands checks for multiple commands. Unlike argv_has_cmd, which checks for only one command.

    returns empty list if none of the given command matches.

    Further,
    if order passed,
    returns the sorted list according to pass command list
    """

    """
    Implementation might like,
    --------------------------

    lists = []

    for each of elements:
        if cmd in commands:
            tup = (True, index_of_cmd)
            lists.append(tup)

    return lists
            
    """

    commands_exist:list[tuple[bool, int, str]] = []
    idx = 0

    for arg in argv:
        idx += idx
        for cmd in commands:
            if cmd == arg:
                tup = (True, idx, cmd)
                commands_exist.append(tup)

    return commands_exist 

print(argv_parse_commands(["-t", "aaaa", "-e", "#", "$"], ["-t", "-e"]))

"""
Given the arguments,

For the input ["-t", "aaaa", "-e", "#", "$"],
output should be like this,

[
    (True, 1, -t, [aaaa]),
    (True, 3, -e, ["#", "$"])
]

For the input ["-e", "#", "$", "-t", "aaaa"],
again output should be like this,

[
    (True, 1, -t, [aaaa]),
    (True, 3, -e, ["#", "$"])
]

Regardless of the order arguments passed.

But how would the program know in which order they should be ordered?
Well, using main options as base and making decision based on them.
For instance, if the argv has command '-t' or '--transform'

then accepted options ['-e', '--enclose']
again option '-e' may or may not have one/tow value following it.
Example, -e '#' or '-e' '#' '$'

Finally, command '-e' must come after option '-t'

Therefore, above statments are the typicall way.

"""