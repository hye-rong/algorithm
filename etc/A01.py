s = input()
l = [int(n) for n in s]
if sum(l)/2 == sum(l[:len(l)//2]):
    print("LUCKY")
else:
    print("READY")