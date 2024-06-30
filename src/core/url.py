from typing import Dict
import key_terms as KT

def get_file(url:str):
    pass

"""
-> The url must be in this following format,
    https://example.com/*/**
"""
def validate_url(url:str):
    copied = url.strip()

    if copied.startswith(KT.PREFIX_URL_HTTP):
        copied.strip()
    if not copied.startswith(KT.PREFIX_URL_HTTPS):
        pass
    pass


class URL:
    """
    URL(url:string, safe:boolean)

    Where,

    -> url is url text.

    -> safe is whether force https or not, if true http will be transformed to https. default is True.

    """
    _protocol:str
    _domain:str
    _subdomain:str
    _tld:str
    _path:str

    def __init__(self, url:str, safe:bool = True) -> None:
        self._url = url

        # Check if url already prefixed with http:// or https://, if not prefix with http:// or https://
        if not self._url.startswith(KT.PREFIX_URL_HTTP):
            if safe:
                self._url = KT.PREFIX_URL_HTTPS+self._url 
            else:
                self._url = KT.PREFIX_URL_HTTP+self._url 

        self._url.split()

    def url(self) -> str:
        return self._url
    
    def to_dict(self) -> Dict[str, str]:
        return dict(protocol=self._protocol, domain=self._domain, subdomain=self._subdomain, tld=self._tld, path=self._path)