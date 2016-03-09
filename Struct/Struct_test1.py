n = 10240099
print((n & 0xff000000)>>24)
print((n & 0xff0000)>>16)

import struct
print(struct.pack('>I',n))