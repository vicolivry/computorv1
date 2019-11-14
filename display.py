# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    display.py                                       .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: vico <vico@student.le-101.fr>              +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/10/31 18:13:21 by vico         #+#   ##    ##    #+#        #
#    Updated: 2019/11/07 17:11:15 by vico        ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

#!/usr/bin/env python3

def add_operators(factors):
    nf = []
    nf.append(factors[0])
    for f in factors[1:]:
        if f[0] == '-':
            nf.append(' - ' + f[1:])
        else:
            nf.append(' + ' + f[0:])
    return (nf)

def print_reduced(factors):
    if len(factors) == 0:
        print ("Reduced form: 0 = 0 ; all real numbers are a solution")
        return (0)
    factors = [f[:-2] if f.endswith('.0') else f for f in map(str, factors)]
    display_factors = add_operators(factors)
    print("Reduced form: ", end='')
    for idx, f in enumerate(display_factors):
        print(f + ' * x^' + str(idx), end ='')
    print(' = 0')
    print('Polynomial degree:', len(factors) - 1)
    if len(factors) - 1 > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve")
        return (0)
    return (1)
