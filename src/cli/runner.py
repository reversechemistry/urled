from ast import arg
import sys

from cli.handlers import handle_help, handle_invalid_command, handle_parse, handle_transform
from cli.argv import argv_has_cmd

from .commands import InvalidArgException
from .prints import print_header, print_more_info, print_say_invalid_command, print_try_help_footer


def run_cli():
    argv = sys.argv

    argv_length = len(sys.argv)

    # if this criteria true, which means no options or commdand given
    if argv_length == (0 or 1):
            print_header()
            print_more_info()
            exit()    

    #  if it's help, since help does not has any options
    is_help = argv[1] == "-h" or argv[1] == "--help"
    is_help_mini = argv[1] == "-H"

    # Evalutes that given command is either "-t" or "--transform"
    argv_transform = argv_has_cmd(argv, ["-t", "--transform"])

    # Evalutes that given command/s is/has either "-p" or "--parse"    
    argv_parse = argv_has_cmd(argv, ["-p", "--parse"])
    
    target_val = None

    # Ensure a value is given to perform the actions 
    if argv_transform[0] == True and argv_length > argv_transform[1]:
        target_val = argv[argv_transform[1]]

    elif argv_parse[0] == True and argv_length > argv_parse[1]:
        target_val = argv[argv_parse[1]]

    try:
        handle_invalid_command(argv[1])

        # Handles "-h", "--help" and "-H" commands.
        if is_help or is_help_mini:  
            handle_help(detailed = is_help_mini == False)

        # Handles "-t", "--transform" commands
        if argv_transform[0] and target_val:
            handle_transform(target_val, False, "%")
            
        elif argv_transform[0] and not target_val:
            print("A text to transform not provided.")
            print("Try \"urled -t 'atexttotransform'\"")
            exit()


        # Handles "-p", "--parse" commands
        if argv_parse[0]:
            if not target_val:
                print("A text to parse not provided.")
                print("Try \"urled -t 'PERIODatexttoSEMICOLUMNtransform'\"")
                exit()


            else:
                handle_parse(target_val, None)    

    except InvalidArgException:
        print_say_invalid_command()


