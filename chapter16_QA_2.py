import sys
import os
import hashlib

#디렉토리 안의 파일중 원하는 확장자와 매칭되는 파일의 크기와 이름을 딕셔너리에 저장하고 반환한다
def filefinder(ex,dirname):
    filesinfo = dict()
    for (dirsname, dirs, files) in os.walk(dirname):
        for filename in files:
            if filename.endswith(ex):
                #파일 경로
                filepath = os.path.join(dirname, filename)
                #체크썸 계산을 위한 파일 열람
                filedata = open(filepath, 'r',encoding ='utf-8', errors ='ignore').read()
                #체크썸 계산을 위해 utf-8으로 인코딩
                fidata_by = filedata.encode('utf-8')
                #파일의 해쉬값 계산
                filehash = hashlib.md5(fidata_by).hexdigest()
                filepath = (filepath,)
                #딕셔너리 키값에 해쉬값 중복시 파일경로를 튜플로 추가
                filesinfo[filehash] = filesinfo.get(filehash, tuple()) + filepath
    return filesinfo    #폴더내 특정 확장자의 파일 사이즈 및 경로가 담긴 딕셔너리

# 딕셔너리 값이 1개 이상인(중복되는) 키값(파일사이즈)를 확인하고 출력
def check_dupli(dic):
    for key, val in dic.items():
        if len(val) == 1: continue
        print("file md5 : ",key," file names : ",val)


#인자값 선언
tg_dirname = sys.argv[1]    #첫번째 인자값은 디렉토리명
tg_extend = sys.argv[2]     #두번째 인자값은 파일 확장자

#인자값 확인
dir_check1 = os.path.exists(tg_dirname) # 디렉토리명 존재 유부 확인
dir_check2 = os.path.isdir(tg_dirname)  # 디렉토리 여부 확인

if len(sys.argv) != 3:      #인자갯수가 2개 이상이거나 이하일경우
    print("please typing dirname and extend ex) ",sys.argv[0]," dirname extend")
    sys.exit()
elif dir_check1 and dir_check2:
    dir_root = os.path.abspath(tg_dirname)
    result = filefinder(tg_extend, dir_root)
    check_dupli(result)



