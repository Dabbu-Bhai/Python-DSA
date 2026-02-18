num = 43261596 #binary = 101
bin = 0
while num != 0:
    bin = bin*10 + (num%2)
    num = num//2
rev = list(str(bin))
for i in range(len(rev)):
    rev[i] = int(rev[i])
print(rev)
bin = int(str(bin)[::-1])
n = len(rev)
revnum = 0
for i in range(n):
    revnum = revnum + (rev[i] * 2**i)
print(revnum)
print(bin)