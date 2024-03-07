n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

max_val = arr[-1]  # 최대값
second_max = arr[-2]  # 두 번째로 큰 값

sum = 0
count = 0

for i in range(m):
    if m < k:
        sum += max_val
    else:
        sum = max_val*(m/k)*k + second_max*(m-(m/k)*k)
print(sum)
