

A = "100"
B = "11"
def addBinary(self, A, B):
    x = A
    y = B
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1 
    if carry !=0 : result = '1' + result

    print("result.zfill(max_len)", result.zfill(max_len))
    return result.zfill(max_len)

addBinary('data', A, B)
 