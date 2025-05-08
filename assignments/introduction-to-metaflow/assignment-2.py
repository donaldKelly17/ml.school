"""Assignment 2.

Create a simple flow that tracks a sequence of numerical operations. In the first step,
initialize an artifact with a number. In each subsequent step, update the artifact by
applying a different arithmetic operation (e.g., addition, subtraction, multiplication)
and append each new value to a list. In the final step, print the entire history of
values and calculate both the sum and average.
"""
from metaflow import FlowSpec, step


class Introduction(FlowSpec):
    """A flow for assignment 2."""

    @step
    def start(self):
        """Initialize the variablr."""
        self.variable = 1
        print("Initial value:", self.variable)
        self.next(self.addition)

    @step
    def addition(self):
        """Add 2 to the variable."""
        print("Adding 2 to the variable")
        self.variable += 2
        print("Variable value:", self.variable)
        self.next(self.subtract)

    @step
    def subtract(self):
        """Subtract 1 from the variable."""
        print("Subtracting 1 from the variable")
        self.variable -= 1
        print("Variable value:", self.variable)
        self.next(self.multiply)

    @step
    def multiply(self):
        """Multiply the variable by 3."""
        print("Multiplying the variable by 3")
        self.variable *= 3
        print("Variable value:", self.variable)
        self.next(self.end)

    @step
    def end(self):
        """Every flow must end with an 'end' step."""
        print("Ending the flow")


if __name__ == "__main__":
    Introduction()
