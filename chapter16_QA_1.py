

#프로그램 순서
# 0. chapter16_QA_1.py <찾을 디렉토리명> <찾을 확장자>
# 1. 스크립트 호출시 입력받은 인자값이 디렉토리명이 맞는지 확인한다.
# 2. 파일을 찾는 함수에서 디렉토리명과 찾을 확장자를 인자값으로 준다
# 3. 함수에서는 각 파일의 크기를 키값으로 하는 딕셔너리를 만들며 파일의 크기가 같은 파일은 딕셔너리 값의 리스트로 추가한다.
# 4. 중복된 크기의 파일을 확인하는

#폴더내 파일 검색
def filefinder(ex,dirname)