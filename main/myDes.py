from pyDes import *
import base64


def encode_des_base64(key, origin_string):
    b_key = bytes(key, 'utf-8')
    b_source = bytes(origin_string, 'utf-8')
    encrypts = des(b_key, ECB, b"\0\0\0\0\0\0\0\0", pad=b"\0", padmode=PAD_NORMAL)
    return base64.b64encode(encrypts.encrypt(b_source)).decode(encoding='utf-8')


def decode_base64_des(key, origin_string):
    b_key = bytes(key, 'utf-8')
    b_source = bytes(origin_string, 'utf-8')
    decrypts = des(b_key, ECB, b"\0\0\0\0\0\0\0\0", pad=b"\0", padmode=PAD_NORMAL)
    temp = base64.b64decode(b_source)
    return decrypts.decrypt(temp, padmode=PAD_NORMAL).decode(encoding='utf-8')
