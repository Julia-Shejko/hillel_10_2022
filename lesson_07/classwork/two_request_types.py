from functools import singledispatchmethod


class HomePageSearchRequest:
    def __init__(self, lang, page) -> None:
        self.lang: str = lang
        self.page_name: str = page


class AboutPageSearchRequest:
    def __init__(self, color, region) -> None:
        self.color: str = color
        self.region: str = region

    @classmethod
    def build(cls, payload: dict) -> "AboutPageSearchRequest":
        mandatory_fields = ("color", "region")
        for field in mandatory_fields:
            if field not in payload:
                raise Exception()

        return cls(**payload)


class WebPageHandler:
    def __init__(self, request: HomePageSearchRequest | AboutPageSearchRequest) -> None:
        self.request = request

    def process(self):
        self._process(self.request)

    @singledispatchmethod
    def _process(self, request: HomePageSearchRequest):
        print("This is the home page")

    @_process.register
    def _(self, request: AboutPageSearchRequest):
        print("This is the about page")


# request = AboutPageSearchRequest.build(payload)

about_request = AboutPageSearchRequest(color="red", region="UA")
home_page_request = HomePageSearchRequest(lang="UA", page="Home")

handler_1 = WebPageHandler(about_request)
handler_1.process()

handler_2 = WebPageHandler(home_page_request)
handler_2.process()
