import pytest

from bank_account import BankAccount


def test_standard_withdrawal():
    account = BankAccount("Alice", 100)

    account.withdraw(30)

    assert account.getBalance() == 70


def test_withdrawal_over_available_balance_raises():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError, match="Insufficient funds!"):
        account.withdraw(150)

    assert account.getBalance() == 100


def test_negative_withdrawal_raises():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError):
        account.withdraw(-50)

    assert account.getBalance() == 100
