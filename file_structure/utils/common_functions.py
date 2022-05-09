import struct, zlib, decimal

def to_int(b:bytes):
    "convert little endian bytes into unsigned int "
    return int.from_bytes(b, "little", signed=False)

def to_float(b:bytes):
    "convert little endian bytes into float "
    return struct.unpack('<f', b)[0] #little endian

def to_decimal(b:bytes):
    "convert little endian bytes into float with six digits "
    return decimal.Decimal('{0:.6f}'.format(struct.unpack('<f', b)[0])) #little endian

def unzlib_it(data):
    return zlib.decompress(data)

def zlib_it(data,compression):
    return zlib.compress(data,compression)

def file_read(file):
    '''
    Gets a file and return a byte array with his content
    '''
    with open(file, 'rb') as f:
        file_contents  = bytearray(f.read())
    return file_contents
