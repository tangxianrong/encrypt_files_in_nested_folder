

'''
加密程式

改自：
https://www.cxyzjd.com/article/Holidayzz/105344245
https://www.gushiciku.cn/pl/pXle/zh-tw
'''
# from IPython import embed

'''
採用AES對稱加密演算法
'''

from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode
from Cryptodome.Util.Padding import pad, unpad


'''
採用AES對稱加密演算法
'''
# str不是16的倍數那就補足為16的倍數


# 加密方法
def encrypt_oracle(message,key_pri, iv = False):
    '''
    加密函式，傳入明文 & 祕鑰，返回密文；
    :param message: 明文
    :param key_pri: 祕鑰
    :return:encrypted  密文
    '''
    
    # 初始化加密器
    if not iv:
        key_pri = b64decode(key_pri)
        cipher = AES.new(key_pri, AES.MODE_CBC)
    else:
        key_pri = b64decode(key_pri)
        iv = b64decode(iv)
        cipher = AES.new(key_pri, AES.MODE_CBC, iv)        

    # 長度調整
    message_16 = pad(message.encode('utf-8'), AES.block_size)
    # print(message_16)
    #先進行aes加密
    encrypt_aes = cipher.encrypt(message_16)
    #用base64轉成字串形式
    encrypt_aes_64 = b64encode(encrypt_aes)
    return encrypt_aes_64


# 解密方法
def decrypt_oracle(message, key_pri, iv = False):
    '''
    解密函式，傳入密文 & 祕鑰，返回明文；
    :param message: 密文
    :param key_pri: 祕鑰
    :return: encrypted 明文
    '''
    # 初始化加密器
    # try:
    
    if not iv:
        key_pri = b64decode(key_pri)
        cipher = AES.new(key_pri, AES.MODE_CBC)
    else:
        key_pri = b64decode(key_pri)
        iv = b64decode(iv)
        cipher = AES.new(key_pri, AES.MODE_CBC, iv)        
    #優先逆向解密base64成bytes
    message_de64 =  b64decode(message)
    # if message_de64==b"":
    #     return ""
    # print(message_de64)
    #先進行aes加密
    # 解密 aes
    message_de64_deaes = cipher.decrypt(message_de64)
    # print(message_de64_deaes)
    pt = unpad(message_de64_deaes, AES.block_size)
    # except:
        # embed()
    # print(message_de64_deaes)
    # message_de64_deaes_de = message_de64_deaes.decode('utf-8')
    return pt.decode('utf-8')




if __name__ == "__main__":
    message = '我Tommor  row is another day！over!'     # 待加密內容
    
    key_pri = 'abc'  # 密碼
    ivb = '123'  # iv key    
    key_pri = b64encode(key_pri)
    key_pri = b64encode(ivb)

    content_en = encrypt_oracle(message, key_pri, ivb)    # 加密
    print('加密後，密文為：', content_en)            
    content = decrypt_oracle(content_en, key_pri, ivb)    # 解密
    print('解密後，明文為：', content)               