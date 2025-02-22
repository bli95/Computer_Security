#!/usr/bin/env python
import sys, urllib
from pymd5 import md5, padding

def main():
    if len(sys.argv) != 4:
        print 'Wrong usage.'
        sys.exit(1)
    
    with open(sys.argv[1]) as file:
        query = file.read().strip()
    with open(sys.argv[2]) as file:
        cmd3 = file.read().strip()
    
    query = query.split("=", 1)[1]
    [token, msg] = query.split("&", 1)

    bits = (8 + len(msg) + len( padding(8*8+len(msg)*8) ) ) * 8
    h = md5(state=token.decode('hex'), count=bits)
    h.update(cmd3)
    token = h.hexdigest()

    # token = md5(msg + urllib.quote(padding(len(msg)*8)) + cmd3).hexdigest()
    output = 'token='+token+'&'+msg+urllib.quote(padding(8*8 + len(msg)*8))+cmd3

    with open(sys.argv[3], 'w') as file:
        file.write(output)
    
if __name__ == "__main__":
    main()
