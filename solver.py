# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    solver.py                                        .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: vico <vico@student.le-101.fr>              +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/11/04 12:45:01 by vico         #+#   ##    ##    #+#        #
#    Updated: 2019/11/07 17:09:07 by vico        ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

#!/usr/bin/env python3

from decimal import Decimal, getcontext

getcontext().prec = 6

def square_root(x):
    a, new_x = float(x), float(x)

    for i in range(500):
        new_x = 0.5 * (new_x + a / new_x)
    return (Decimal(new_x))

def solve_second_degree(eq):
    a, b, c = eq[2], eq[1], eq[0]
    delta = (b * b) - 4 * a * c
    if delta < 0:
        print("Discriminant is strictly negative, the two solutions are:")
        print(-b / (2 * a), '+ √', (-1 * delta), "/", (2 * a), '* i')
        print(-b / (2 * a), '- √', (-1 * delta), "/", (2 * a), '* i')
    elif delta == 0:
        print("The discriminant equals zero, the solution is:")
        print(-b / (2 * a))
    else:
        print("The discriminant is strictly positive, the two solutions are:")
        print((-b - square_root(delta)) / (2 * a))
        print((-b + square_root(delta)) / (2 * a))

def solve_first_degree(eq):
    a, b = eq[1], eq[0]
    print ("The solution is:")
    print (-a / b)

def solve_eq(eq):
    if len(eq) == 1:
        print('The equation is unsolvable')
    elif len(eq) == 2:
        solve_first_degree(eq)
    else:
        solve_second_degree(eq)