# withA_index
# WithAIndex

# inserted automatically
import os
import marshal

import struct
import shutil

from hashlib import md5

# custom db code start


# custom index code start
# source of classes in index.classes_code
# index code start
class WithAIndex(HashIndex):

    def __init__(self, *args, **kwargs):
        kwargs['entry_line_format'] = '<32s32sIIcI'
        kwargs['hash_lim'] = 4 * 1024
        super(WithAIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("a")
        if a_val:
            if isinstance(a_val, int):
                a_val = str(a_val)
            # unnecessary code?
            # if not isinstance(a_val, bytes):
            #     a_val = bytes(a_val, 'utf-8')
            return md5(a_val.encode()).hexdigest(), {}
        return None

    def make_key(self, key):
        if not isinstance(key, bytes):
            key = bytes(key, 'utf-8')
        return md5(key).hexdigest()
