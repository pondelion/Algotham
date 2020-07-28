

class Stock:

    def __init__(
        self,
        code: int = None,
        company_name: str = None,
    ):
        self._code = code
        self._company_name = company_name

    @property
    def code(self) -> int:
        return self._code

    @property
    def company_name(self) -> str:
        return self._company_name
