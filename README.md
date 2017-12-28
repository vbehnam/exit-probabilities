# exit-probabilities
Given a vector of probabilities, a vector of the length moved at each step, two “exit points”, this function finds the probability of hitting one of the two exits (which the user specifies) at every possible starting point, for a one-dimensional random walk. (This is clearer in the example below)

Make sure for all the arguments you input the values of the vectors correctly. Particularly for p, make sure you specify a probability for staying put, even if it is 0. i.e. if z is a probability, then just input p = [z, 1-z, 0]. Otherwise, if you do not input the other values, the function will return an error message.

The runtime of this algorithm is O(n^3), where nxn is the dimension of the square c matrix, since inverting a matrix takes O(n^3) time. Hence, the program might not be able to compute for large values of (exit[1]-exit[0]).

The output is a Nx1 vector which returns the probability that at starting position Sn, the random walk hits the specified boundary t.

## Example

Say you’re tracking the price of a stock. You can input as p=[1/4, 2/4, 1/4] which signifies the stock has 1/4th chance of depreciating, 2/4th chance of appreciating and 1/4th chance of staying put. Then, you can input the “distance” (or value it can travel at each iteration). For simplicity, let’s set them both as unit moves i.e. [1, 1] or that the particle moves left one unit or moves right one unit. Then we set the two “exit” points. The lower bound is probably naturally set at 0, and set the upper bound at some arbitrary value, say $100. Now, we want to know the probability of hitting $100 before we hit $0.

This algorithm will return an 100x1 vector with the -ith index representing the probability of the stock appreciating to $100 when it starts at S0=i. in this example, U3 is 0.875, which shows that the probability of hitting $100 when the stock starts at $3 is 0.875. You might think that’s a bit too optimistic, but remember the probability of appreciation is 2/4, double that of depreciation.

