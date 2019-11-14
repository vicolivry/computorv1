# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    reducer.py                                       .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: vico <vico@student.le-101.fr>              +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/10/31 16:29:43 by vico         #+#   ##    ##    #+#        #
#    Updated: 2019/11/07 17:10:11 by vico        ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

#!/usr/bin/env python3

from decimal import Decimal

def reducer(eq_split):
	if len(eq_split['l_side']) >= len(eq_split['r_side']):
		l_factors = [Decimal(item.split(' ')[0]) for item in eq_split['l_side']]
		r_factors = [Decimal(item.split(' ')[0]) for item in eq_split['r_side']]
	else:
		l_factors = [Decimal(item.split(' ')[0]) for item in eq_split['r_side']]
		r_factors = [Decimal(item.split(' ')[0]) for item in eq_split['l_side']]
	for l in l_factors:
		if len(l_factors) >= len(r_factors):
			r_factors.append(0)
	result = [tup[0] - tup[1] for tup in zip(l_factors, r_factors)]
	while len(result) > 0 and result[-1] == 0:
		result.pop()
	return (result)