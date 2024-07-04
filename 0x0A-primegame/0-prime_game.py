#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    # Helper function to determine if a number is prime
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
        return is_prime
    
    # Calculate the prime numbers up to the maximum possible n in nums
    max_n = max(nums) if nums else 0
    prime_sieve = sieve(max_n)
    
    def prime_game(n):
        # Determine the winner of a single game with range 1 to n
        if n < 2:
            return "Ben"
        
        primes = [i for i in range(2, n + 1) if prime_sieve[i]]
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn
        
        while primes:
            prime = primes.pop(0)
            multiples = set(range(prime, n + 1, prime))
            primes = [p for p in primes if p not in multiples]
            turn = 1 - turn  # Switch turns
        
        return "Maria" if turn == 1 else "Ben"
    
    if not nums or x <= 0:
        return None
    
    win_count = {"Maria": 0, "Ben": 0}
    
    for n in nums:
        winner = prime_game(n)
        win_count[winner] += 1
    
    if win_count["Maria"] > win_count["Ben"]:
        return "Maria"
    elif win_count["Ben"] > win_count["Maria"]:
        return "Ben"
    else:
        return None

