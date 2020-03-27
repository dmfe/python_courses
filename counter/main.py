import struct

import counter

for i in range(0, 10):
    counter.count()

with open(counter.file_name, 'rb') as count_file:
    num = count_file.read(counter.chunk_size)
    while num:
        print(struct.unpack('i', num)[0])
        num = count_file.read(counter.chunk_size)
