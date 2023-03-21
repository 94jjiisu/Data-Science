import hashlib

# 출저 https://sarc.io/index.php/development/803-python-file-md5-hash
def getHash(path, blocksize=65536):
    try:
        afile = open(path, 'rb')
    except:
        return ('queen_track 파일이 없습니다.')
    
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def md5_hash(stu_answer):
    return hashlib.md5(stu_answer.encode()).hexdigest()