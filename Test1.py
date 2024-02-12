N = int(input("N = "))
nums = list(range(N + 1))
nums[1] = 0
primes = []

for i in nums:
    if i > 1:
        for j in range(i + i, len(nums), i):
            nums[j] = 0
        primes.append(i)


print(primes)
length = len(primes)
print(f"Всего простых чисел: {length} шт")