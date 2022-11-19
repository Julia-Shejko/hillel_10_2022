"""
You can to create 2 instances of a `Price` class and to do operations between them:
        - add prices;
        - do a subtraction of prices.
"""

from dataclasses import dataclass
from decimal import Decimal

# list of currencies available for calculation
currencies: list = ["USD", "EUR", "UAH"]


class PriceError(Exception):
    pass


@dataclass()
class Price:
    amount: Decimal
    currency: str  # currencies

    def __post_init__(self):
        if self.currency not in currencies:
            raise PriceError("❌ Price rejected. Currency is not supported.")

    def __str__(self) -> str:
        return f"The prise is {self.amount} {self.currency}"

    def __add__(self, other: "Price") -> "Price":
        print("⏳ Counting the total price...")
        return Price(amount=(self.amount + other.amount).quantize(Decimal("1.00")), currency=self.currency)

    def __sub__(self, other: "Price") -> "Price":
        if self.amount >= other.amount:
            print("⏳ Counting the difference...")
            return Price(amount=(self.amount - other.amount).quantize(Decimal("1.00")), currency=self.currency)
        else:
            raise PriceError("The negative price is not possible 😕")


def create_price():
    """Creates an instances of a `Price` class"""
    user_input = input(f"Available currencies: {currencies}.   Enter the price in format:\nPRICE CURRENCY\n").split(" ")
    return Price(amount=Decimal(user_input[0]), currency=user_input[1].upper())


def convert(self):
    """Performs currency conversion against the dollar"""
    if self.currency == "EUR":
        self.amount *= Decimal("0.97")
        self.currency = "USD"
    elif self.currency == "UAH":
        self.amount *= Decimal("0.027")
        self.currency = "USD"
    return self.amount


def comparison(self: Price, other: Price):
    """Currency comparison."""
    if self.currency != other.currency:
        convert(self)
        convert(other)


def handle_base_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PriceError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"A certain error occurred: {error}")

    return inner


@handle_base_errors
def main():
    # Ask about prices
    price_a = create_price()
    price_b = create_price()

    comparison(price_a, price_b)

    price_c = price_a + price_b
    price_d = price_a - price_b

    print(price_c)
    print(price_d)


if __name__ == "__main__":
    main()
