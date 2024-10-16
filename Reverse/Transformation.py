''' Solution for the reverse engineering question transformation from picoCTF '''
enc=''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print(enc)
enc1='灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽'
msg=""
for i in enc1:
  a=(bin(ord(i)))
  m=a[-8:]
  n=a[2:-8]
  n_real=int(n,2)
  m_real=int(m,2)
  msg+=chr(n_real)+chr(m_real)
print(msg) 
