import pytest

from price_calculator import PriceCalculator

def test_calculate_raises_value_error_for_negative_age() -> None:
    calculator = PriceCalculator()

    with pytest.raises(ValueError):
        calculator.calculate(-1)


@pytest.mark.parametrize(
    ("age", "expected_price"),
    [
        (0, 50),
        (10, 50),
        (12, 50), ## age 12 was not added as highest boundary for kids price.
        (13, 100), ## age 13 was not added before as lowest boundary with adult price. 
        (20, 100),
        (30, 100),
        (40, 100),
        (50, 100),
        (60, 100),
        (64, 100), ## age 64 was not given as last boundary for adult price
        (65, 80),
        (70, 80),
        (80, 80),
        (90, 80),
    ],
)
def test_calculate_at_price_boundary(age: int, expected_price: int) -> None:
    calculator = PriceCalculator()

    actual_price = calculator.calculate(age)

    assert actual_price == expected_price

