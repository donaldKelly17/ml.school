"""Assignment_4.

Create a flow that takes a list of numbers as a parameter.
Use a foreach loop to square each number in a separate step.
In the join step, collect the squared results
and print both the full list and the total sum.
"""
from metaflow import FlowSpec, step


class Assignment4(FlowSpec):
    """A flow for assignment 3."""

    @step
    def start(self):
        """Initialize a list of numbers."""
        self.numbers = [1, 2, 3, 4, 5]
        print("Starting with numbers:", self.numbers)
        self.next(self.square, foreach="numbers")

    @step
    def square(self):
        """Square each number."""
        number = self.input or 0
        self.squared = number ** 2
        print(f"Squared {number} to get {self.squared}")
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the results of the foreach."""
        self.squared_numbers = [i.squared for i in inputs]
        self.total_sum = sum(self.squared_numbers)
        print("Squared numbers:", self.squared_numbers)
        print("Total sum of squared numbers:", self.total_sum)
        self.next(self.end)

    @step
    def end(self):
        """Every flow must end with an 'end' step."""
        print("Ending the flow")


if __name__ == "__main__":
    Assignment4()
