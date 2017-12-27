# exit-probabilities
Given two arbitrary “exit probabilities”, this function finds the probability of hitting one of the two exits at every possible starting point, for a one-dimensional random walk.

Make sure for all the arguments you input the values of the vectors correctly. Particularly for p, make sure you specify a probability for staying put, even if it is 0. i.e. just input p = [q, 1-q, 0]. Otherwise the function will return an error message.

For large values of (exit[1]-exit[0]), there may not be enough memory to compute these probabilities.

The output is a Nx1 vector which returns the probability that at starting position Sn, the random walk hits the specified boundary t.

## Example

Say you’re tracking the price of a stock. You can input as p=[1/4, 2/4, 1/4] which signifies the stock has 1/4th chance of depreciating, 2/4th chance of appreciating and 1/4th chance of staying put. Then, you can input the “distance” (or value it can travel at each iteration). For simplicity, let’s set them both as unit moves i.e. [1, 1]. Then we set the two “exit” points. The lower bound is probably naturally set at 0, and set the upper bound at some arbitrary value, say $100. Now, we want to know the probability of hitting $100 before we hit $0.

This algorithm will return an 100x1 vector with the -ith index representing the probability of the stock appreciating to $100 when it starts at S0=i. in this example, U3 is 0.875, which shows that the probability of hitting $100 when the stock starts at $3 is 0.875. You might think that’s a bit too optimistic, but remember the probability of appreciation is 2/4, double that of depreciation.

