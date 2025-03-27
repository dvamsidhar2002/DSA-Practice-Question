def largest_prime_factors(num):
    factors = []
    factor=2

    while(num>=2):
        if num%factor==0:
            factors.append(factor)
            num=num/factor
        else:
            factor+=1

        factors.sort(reverse=True)

    return factors[0]

if __name__=='__main__':
    n = int(input('Enter any number of your choice : '))
    max = largest_prime_factors(n)

    print(f'Largest prime factor : {max}')