import struct

ret = struct.pack("i", 10000)
print(ret, len(ret))

ret2 = struct.unpack("i", ret)
print(ret2[0])
