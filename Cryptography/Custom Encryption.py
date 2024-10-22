a = 95  # given
p = 97
g = 31
b = 21  # given
cipher=[237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
cipher1=[]

#Inorder to solve this question we first generate the shared key that can be figured out using the given values.
def key_generation(a,b,p,g):
    shared_key=pow(g,a*b,p)
    return shared_key
print(key_generation(a,b,p,g))

# Then we start solving in reverse order by converting the ciphertext into semi-cipher.
d=""
for i in cipher:
    cipher1.append(chr(int(i/(311*key_generation(a,b,p,g)))))
    d+=chr(int(i/(311*key_generation(a,b,p,g))))
print(d)
print(cipher1)

# Finally , by decrypting the semicipher with pre-decided key thats "trudeau" .
def message(d,key_final):
    message=""
    for i, char in enumerate(d):
        key_char = key_final[i % len(key_final)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        message += encrypted_char
    return message
p=message(d,"trudeau")
print(p[::-1])
