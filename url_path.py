

class UrlPath:
    # Class variables (shared among all instances)

    def __init__(self, base_url):
        UrlPath.base_url = base_url
        self.urls = [base_url]



