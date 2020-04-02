import os.path
import struct

file_name = 'count.dat'
chunk_size = 4

def count():
    num = 0

    if os.path.isfile(file_name):
        with open(file_name, 'rb') as count_file:
            file_size = os.path.getsize(file_name)
            if file_size >= chunk_size:
                pos = file_size - chunk_size
                count_file.seek(pos)
                num = struct.unpack('i', \
                        count_file.read(chunk_size))[0] + 1

    with open(file_name, 'ab') as count_file:
        count_file.write(struct.pack('i', num))
