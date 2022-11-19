## <span style="color:olive">Homework</span>

- Create a class `Price`
    ```python
        class Price:
            def __init__(self, amount: int, currency: str) -> None:
                self.amount: int = amount
                self.currency: str = currency
    ```
- Acceptance criterias:
    - If I create 2 instances of a `Price` class I want to do operations between them:
        - add prices with same currency
        - do a subtricttion of prices with same currency

- *Additional: operations between prices with different currencies:
    - If price instances currencies are different I want to do a double convertion
        - USD is a middle currency
        - If right price is USD the regular convertation (not double) is happening
        - If prices currencies is the same convertion is not happening
        - Result currency after the operation is a currency of the price that is on the left or USD (for your decision)
    - Use `@dataclass` decorator instead of a regular class
