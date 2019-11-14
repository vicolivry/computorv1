# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    computor.py                                      .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: vico <vico@student.le-101.fr>              +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/10/31 17:39:35 by vico         #+#   ##    ##    #+#        #
#    Updated: 2019/11/07 17:09:12 by vico        ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

#!/usr/bin/env python3

from parser import *
from reducer import *
from display import *
from solver import *

if __name__ == "__main__":
	eq_reduced = reducer(parser())
	if print_reduced(eq_reduced) != 0:
		solve_eq(eq_reduced)