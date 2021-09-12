from .core.funtions import *
from .core.subclass import *


class gun:
    def __init__(self, url):
        self.url: str = url
        self.protocol: str = ''
        self.domain: str = ''
        self.subDomain: list = []
        self.rootDomain: str = ''
        self.topDomain: str = ''
        self.path: list = []
        self.query: dict = {}
        self.is_valid_link: bool = isurl(url=self.url)
        self.ip: str = '-1'

        if self.is_valid_link:
            self.url = add_backslash(url=self.url)

            self.protocol: str = protocol(url=self.url)
            self.sub_domain, self.root_domain, self.top_domain, self.port, self.main_domain, self.host = domain(
                url=self.url, url_protocol=self.protocol)
            self.path, self.query = path_query(url=self.url)

            self.ip = find_ip(main_domain=self.main_domain)

    def whois(self):
        return whois(self.ip)

    def tiny(self):
        return tiny(self.url)
