import sys
import os
#프로그램 순서
# 0. chapter16_QA_1.py <찾을 디렉토리명> <찾을 확장자>
# 1. 스크립트 호출시 입력받은 인자값이 디렉토리명이 맞는지 확인한다.
# 2. 파일을 찾는 함수에서 디렉토리명과 찾을 확장자를 인자값으로 준다
# 3. 함수에서는 각 파일의 크기를 키값으로 하는 딕셔너리를 만들며 파일의 크기가 같은 파일은 딕셔너리 값의 리스트로 추가한다.
# 4. 중복된 크기의 파일을 추출하여 출력한다. len()으로 값이 1 이상이면 출력하기


#디렉토리 안의 파일중 원하는 확장자와 매칭되는 파일의 크기와 이름을 딕셔너리에 저장하고 반환한다
def filefinder(ex,dirname):
    filesinfo = dict()
    for (dirsname, dirs, files) in os.walk(dirname):
        for filename in files:
            if filename.endswith(ex):
                filepath = os.path.join(dirname, filename)  #파일 경로 확인
                filesize = os.path.getsize(filepath)        #파일 사이즈 확인
                filepath = (filepath,)  #딕셔너리 값으로 튜플값을 저장하기 위한 형변환
                # 사이즈를 키값으로 하는 딕셔너리 값으로 현재 경로추가
                filesinfo[filesize] = filesinfo.get(filesize, tuple()) + filepath
    return filesinfo    #폴더내 특정 확장자의 파일 사이즈 및 경로가 담긴 딕셔너리

# 딕셔너리 값이 1개 이상인(중복되는) 키값(파일사이즈)를 확인하고 출력
def check_dupli(dic):
    for key, val in dic.items():
        if len(val) == 1: continue
        print("file size : ",key," file names : ",val)

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



