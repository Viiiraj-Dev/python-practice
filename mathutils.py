def is_prime(n):
    # 1. Handle numbers less than 2
    if n <= 1:
        return False
    
    # 2. Handle 2 (the only even prime)
    if n == 2:
        return True
    
    # 3. Exclude all other even numbers immediately
    if n % 2 == 0:
        return False
    
    # 4. Check odd divisors from 3 up to the square root of n
    # We only go to sqrt(n) because if n has a factor, 
    # one must be less than or equal to its square root.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True

def add(a, b):
    return a+b

def factorial(n):
    if n<0:
        raise ValueError("Factorial of -ve does not exist")
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
    print(is_prime(2))
    print(is_prime(9))