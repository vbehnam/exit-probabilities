import numpy as np
import numpy.matlib

def main():
    p = [1/4, 2/4, 1/4]
    dist = [1, 1]
    exit = [0, 100]
    t = 100
    exit_prob(p, dist, exit, t)

# parameters: p is a vector of three values, each signifying the probability of moving left, right and staying in the same spot respectively
# dist is a vector of two values, signifying the distance that each particle moves left and right respectively. make sure the order matches p!!!
# exit is vector of two values, signifying where the particle stops moving (or exits). The lower value should be exit[1]
# t is the exit you are interested in. It must be equal to one of the two values in exit

# output: a vector of the probabilities of exiting, with each -ith element signifying the probability of hitting t (the fourth argument),
# given that you have started from the ith position
# i.e. U[80] is the probability of hitting t, given that your initial position was 80

def exit_prob(p, dist, exit, t):

    if sum(p) != 1:
        raise ProbabilityError("p does not sum to 1!")

    if len(p) != len(dist) + 1 or len(dist) != len(exit):
        raise LengthMismatch("the lengths of the vectors do not match up!")

    if type(dist[0]) != int or type(dist[1]) != int or type(exit[0]) != int or type(exit[1]) != int:
        raise NotInteger("one or more of dist entries is not an integer")

    if t != exit[0] and t != exit[1]:
        raise ExitMismatch("neither of the exit values are equal to t!")

    # the smaller number should be first. In the event that it is not, they will be switched
    if exit[0] > exit[1]:
        temp = exit[1]
        exit[1] = exit[0]
        exit[0] = temp

    # if exit[1] == exit[2] then we are already trivially at the boundary
    if exit[0] == exit[1]:
        return 0


    # the possible moves the particle can take are only the points between the two exits
    n = exit[1] - exit[0]

    # however, this is not the dimension yet, as it is possible that, if the possible distance moved is greater than 1,
    # that the particle "jumps" over exit[0] into "exit[-1]". hence, we need to account for all the possible moves it can take
    n = n + dist[0] - 1

    # same goes for the other side (i.e. dist[1])
    n = n + dist[1] - 1

    # now that we have the correct dimensions, we initialize the two most important data structures for this code
    b = [0] * n
    c = np.matlib.zeros((n, n))

    # C should contain ones on the possible exit rows
    for i in range(0, dist[0]):
        c[i, i] = 1

    for i in range(n-1, n-dist[1]-1, -1):
        c[i, i] = 1


    # b should contain one on the exits on the side of t! (not both exits on both extremes, hence the if statements!)
    if exit[0] == t:
        for i in range(0, dist[0]):
            b[i] = 1

    elif exit[1] == t:
        for i in range(n-1, n-dist[1]-1, -1):
            b[i] = 1


    for i in range(dist[0], n-dist[1]):
        c[i,i] = 1-p[2]
        c[i, i-1] = -p[0]
        c[i, i+1] = -p[1]

    # C clearly is square (NxN), and has linearly independent columns. Therefore, it is invertible.

    # since C*U = b, then U = (C)^-1 * b

    u = np.dot(c.I, b)

    print(u)

    return u


class LengthMismatch(Exception):
    pass


class NotInteger(Exception):
    pass


class ExitMismatch(Exception):
    pass


class ProbabilityError(Exception):
    pass


if __name__ == '__main__':
    main()
