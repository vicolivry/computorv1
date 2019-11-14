# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    parser.py                                        .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: vico <vico@student.le-101.fr>              +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/10/31 16:12:29 by vico         #+#   ##    ##    #+#        #
#    Updated: 2019/11/07 17:09:00 by vico        ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

#!/usr/bin/env python3

import argparse

def splitter(arg_str):
	args_splitted = {}
	args_splitted['l_side'] = get_equation_side(arg_str, 'left')
	args_splitted['r_side'] = get_equation_side(arg_str, 'right')
	return (args_splitted)

def	get_equation_side(arg_str, side):
	arg_lst, equation_side = [], []
	elem = ""
	arg_lst = arg_str.split(' ')
	idx = arg_lst.index("=")
	arg_lst = arg_lst[:idx + 1] if side == 'left' else arg_lst[idx + 1:]
	for arg in arg_lst:
		if (arg_lst.index(arg) + 1) % 4 == 1:
			elem += arg
		elif (arg_lst.index(arg) + 1) % 4 == 2 or (arg_lst.index(arg) + 1) % 4 == 3:
			elem += ' ' + arg
			if arg == arg_lst[-1]:
				equation_side.append(elem)
				break
		elif (arg_lst.index(arg) + 1) % 4 == 0:
			equation_side.append(elem)
			elem = ""
			if arg == '-':
				elem = '-' + elem
	return(equation_side)

def parser():
    args_splitted = {}

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "polynomial_equation",
        help="resolves the well formatted polynomial equation you type here (2nd degree max)"
        )
    args = parser.parse_args()
    return splitter(args.polynomial_equation)
	