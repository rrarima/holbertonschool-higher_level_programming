#!/usr/bin/python3
print(''.join('{}'.format(chr(ch))
            for ch in range(97, 123) if chr(ch) not in ['q', 'e']))
