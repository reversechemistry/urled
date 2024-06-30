from src.core import text_filname_parse as TFP

SAMPLE_URL = "https://example.com/search?q=starts*/app\\path;"
SAMPLE_URL_ADVANCED = ".https://www.example.com/search?q=python&oq=python;run@asynchronous::argsBuild-%fhjh/*/id:<int>/q\"from * search;\"&select=u~ldap"

url_text = TFP.text_to_fn(SAMPLE_URL,True, ("$", "#"))
print(url_text)
print("----")
print(TFP.parse_text(url_text, ("$", "#")))

import sys

if __name__ == "__main__":
    print("Urled...")

    sys.exit(0)