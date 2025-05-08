"""Assignment_3.

Create a flow that starts initializing an artifact with a numerical value. Then split
into two predetermined parallel branches, where the first branch adds a constant to
the artifact and the second branch multiplies the artifact by a constant. In a
subsequent join step, merge the results by printing both branch outcomes and
computing the sum of the two outcomes.
"""
from metaflow import FlowSpec, step


class Assignment3(FlowSpec):
    """A flow for assignment 3."""

    @step
    def start(self):
        """Initialize the variable."""
        self.variable = 1
        print("Initial value:", self.variable)
        self.next(self.addition, self.multiplication)

    @step
    def addition(self):
        """Add 2 to the variable."""
        print("Adding 2 to the variable")
        self.variable += 2
        print("Variable value:", self.variable)
        self.next(self.join)

    @step
    def multiplication(self):
        """Multiply the variable by 3."""
        print("Multiplying the variable by 3")
        self.variable *= 3
        print("Variable value:", self.variable)
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the two branches."""
        print("Step 1's artifact value:", inputs.addition.variable)
        print("Step 2's artifact value:", inputs.multiplication.variable)
        self.final_value = inputs.addition.variable + inputs.multiplication.variable
        print("Final value:", self.final_value)
        self.next(self.end)

    @step
    def end(self):
        """Every flow must end with an 'end' step."""
        print("Ending the flow")


if __name__ == "__main__":
    Assignment3()
