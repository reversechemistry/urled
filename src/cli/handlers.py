
from typing import Tuple
from core import text_filname_parse as TFP
import copy

from cli.commands import COMMANDS_AVAILABLE, InvalidArgException, list_commands, print_detaild_commands
from cli.prints import print_author, print_header, print_help_header, print_try_help_footer


# Handler for invalid command. On receiving an invalid command, raises InvalidArgException.
def handle_invalid_command(command:str):
    is_includes = False
    for cmd in COMMANDS_AVAILABLE:
        if command == cmd[0] or command == cmd[1]:
            is_includes = True

    if is_includes == False:    
        raise InvalidArgException() 


# Handler for "-h", "--help" and "-H" commands.
def handle_help(detailed:bool = True):
    print_header()
    print_help_header()

    if detailed != True:
        list_commands(COMMANDS_AVAILABLE)
        print_try_help_footer()
        
    else: print_detaild_commands()

    print_author()


# Handler for '-t', '--transform'
def handle_transform(text:str, enclose:bool, enclose_sym:str | tuple[str,str]):
    transformed_text = TFP.text_to_fn(text, enclose, enclose_sym)

    print(f"""
\tOriginal Text
---------------------------
\t\t{text}

\tTransformed Text
---------------------------
\t\t{transformed_text}
                 
""")


# Handler for '-p', '--parse'
def handle_parse(text:str, enclose_sym:str | Tuple[str, str] | None):
    transformed_text = TFP.parse_text(text, enclose_sym)

    print(f"""
\tTransformed Text
---------------------------
\t\t{text}

\tParsed Text
---------------------------
\t\t{transformed_text}
                 
""")