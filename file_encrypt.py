from glob import glob
import os
from . import encrypt_cbc


# from IPython import embed

def encrypt_file(file_name, dir_name, key, iv=False):
    '''
    輸入:
        file_name:想要加密的檔案
        dir_name:目標存放的位置與檔名
    輸出:
        無
    
    功能:
    加密檔案
    '''
    with open(dir_name,'w+',encoding="utf-8") as fw:
        with open(file_name,'r',encoding="UTF-8-sig") as fr:
            line=fr.readline()
            while line:

                x = line.strip('\n')
                # print(x)
                x = encrypt_cbc.encrypt_oracle(x, key, iv)
                # print(x)
                fw.write(x.decode("utf-8")+"\n")
                # print(encrypt.decrypt_oracle(x))
                line=fr.readline()

def encrypt_all_file(folder, key, new_folder="", iv=False):
    '''
    輸入:
        folder:想要加密的目標資料夾
        new_folder:存放的新路徑，若無則覆蓋原始檔案
    輸出:
        無
    
    功能:
    加密整個路徑底下的資料，如果沒有給新路徑則會以覆蓋舊檔案形式進行
    '''        
    for file in glob(os.path.join(folder,"**"),recursive=True):
        print(file)
        if os.path.isfile(file):
            encrypt_file(file,'tmp.txt', key, iv=iv)  

            if not new_folder:
                #若沒有提供新路徑則覆蓋原始位置    
                os.remove(file)
                os.rename('tmp.txt', file)
            else:
                #若有提供新路徑則以新路徑加相對位置儲存
                sub_filename = file.split(folder)[-1][1:]
                target_filename = os.path.join(new_folder, sub_filename)
                sub_path = os.path.dirname(os.path.join(new_folder,sub_filename))
                if os.path.exists(target_filename):
                    os.remove(target_filename)
                if not os.path.exists(sub_path):
                    os.makedirs(sub_path)
                os.rename('tmp.txt', target_filename)


def decrypt_file(file_name, key, iv=False):
    '''
    輸入:
        file_name:想要解密的檔案
    輸出:
        list of string
        每一個string為當初未加密前的一行資訊
    
    功能:
    加密檔案
    '''
    data=[]

    with open(file_name, 'r', encoding="UTF-8-sig") as fr:
        line=fr.readline()
        while line:
            x = line.strip('\n').encode("utf-8")
            # print("input", x)
            x = encrypt_cbc.decrypt_oracle(x, key, iv=iv)
            data.append(x)
            line=fr.readline()

    return data




if __name__ == "__main__":
    pass