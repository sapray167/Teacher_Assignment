import gc 
c=gc.collect()
print(c)
def fun(i):
    x = {}
    x[i + 1] = x
    return x
for i in range(5):
    fun(i)

print(gc.collect())