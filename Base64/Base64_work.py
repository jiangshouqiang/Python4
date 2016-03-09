import base64

def safe_base64_decode(s):
    # print(base64.b64decode(s))
    s_len = len(s)
    if s_len%4 != 0:
        strs = str(s).replace('b','').replace('\'','')
        for i in range(4-s_len%4):
            strs += '='
    else:
        return base64.b64decode(s)
        # print(strs)
    # print(s)
    # strs = strs.replace('=','').replace('b','')
    # print(bytes(strs,encoding='utf8'))
    return base64.b64decode(bytes(strs,encoding='utf8'))

object_test = safe_base64_decode(b'YWJjZA==')
print(object_test)