"""Manage a collection of calculation objects."""

from calculator.calculation import Calculation


class History:
    """Own session history and expose controlled access to its collection."""

    def __init__(self) -> None:
        # An instance attribute gives each History its own list.
        # A leading underscore means internal use by convention, not security.
        # History HAS MANY calculations; it does not inherit from Calculation.
        self._calculations: list[Calculation] = []

    def add(self, calculation, result) -> None:
        """Append a calculation to history."""
        self._calculations.append((calculation, result))

    def get_history(self) -> list:
        """Return a copy of the history list."""
        return self._calculations.copy()

    def remove(self, index: int):
        """Remove a calculation from history by index."""
        if index < 0 or index >= len(self._calculations):
            raise IndexError("Calculation does not exist")
        return self._calculations.pop(index)
        # isinstance accepts subclasses too, including Add and Subtract.
        