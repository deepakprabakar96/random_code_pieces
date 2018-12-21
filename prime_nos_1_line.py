print([prime for prime in range(2,101) if all([prime%i!=0 for i in range(2,prime)])])
