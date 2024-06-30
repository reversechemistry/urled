
"""
RULES APPLICABLE TO WINDOWS
-x--> In Windows utilities, the space and the period are not allowed as the final character of a filename   
    \\> if STR starts with " " or "." then TRUE

RULES APPLICABLE TO UNIX/LINUX
-x--> In Unix, the period is used to describe hidden files
    \\> if STR starts with "." then TRUE

RULES APPLICABLE TO BOTH
"""

from .chars import LIST, TUPLE_BRACKETS, TUPLE_ANGLE_BRACKETS, TUPLE_CURLY_BRACKETS, TUPLE_PARANTAHSES

def get_char_if_equal(char: str, to_match: str, replace_with: str, enclose:bool = False, enclose_sym:str | tuple[str,str] = TUPLE_BRACKETS) -> str:
    """
    If given char equal to to_match, then return replace_with else return char.

    char:str - the base character/text to match against.

    to_match:str - the character/text to be match with the char.

    replace_with:str - char to be replace the character/text.

    enclose:bool - whether to enclose the character/text or not, default is False.
    
    enclose_sym:str|tuple[str, str] - string or two string element tuple to enclose the character/text.
    """
    if char == to_match:
        # if enclose and enclose_sym provided
        if enclose and enclose_sym is not None:
            # if tuple char set
            if type(enclose_sym) == tuple:
                return enclose_sym[0]+replace_with+enclose_sym[1]
            
            elif type(enclose_sym) == str:
                return enclose_sym+replace_with+enclose_sym
        return replace_with
    else:
        return char


def replace_if_exist(text:str, to_find:str, replace_with:str):
    if text.find(to_find) != -1:
        return text.replace(to_find, replace_with)
    else:
        return text


def text_to_fn(url: str, enclose:bool = False, enclose_sym:str | tuple[str,str] = TUPLE_BRACKETS) -> str:
    copied = url
    for sym in LIST:
        char = get_char_if_equal(sym[1], sym[1], sym[0], enclose, enclose_sym)
        copied = copied.replace(sym[1], char, -1)

    return copied


def parse_text(text: str, enclose_sym:str | tuple[str, str]| None = None):
    """
    Parses given text to it's original form

    if text is enclosed with chars like (,),[,],{,},<,>
        will automatically parses.
        
        but in case other characters/string used, it must be passed or text will not parse correctly.

    
    text:str - text to parsed back

    enclose_sym:str|tuple[str, str] - string or two string element tuple used to enclose the character/text.
        
    """
    copied = text
    for sym in LIST:
        copied = copied.replace(sym[0], get_char_if_equal(sym[0], sym[0], sym[1]), -1)

        if enclose_sym:
            if type(enclose_sym) == tuple:
                copied = replace_if_exist(copied, enclose_sym[0], "")
                copied = replace_if_exist(copied, enclose_sym[1], "")

            elif type(enclose_sym) == str:
                copied = replace_if_exist(copied, enclose_sym, "")    


        copied = replace_if_exist(copied, "[", "")
        copied = replace_if_exist(copied, "]", "")

        copied = replace_if_exist(copied, "(", "")
        copied = replace_if_exist(copied, ")", "")

        copied = replace_if_exist(copied, "{", "")
        copied = replace_if_exist(copied, "}", "")

        copied = replace_if_exist(copied, "<", "")
        copied = replace_if_exist(copied, ">", "")


    return copied
