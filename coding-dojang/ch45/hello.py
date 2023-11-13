print('hello 모듈 시작')
print('hello.py__name__', __name__)  # '__name__변수 출력'
print('hello 모듈 끝')

# 즉, 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는 '__main__'이 들어갑니다.
#  이는 프로그램의 시작점(entry point)이라는 뜻입니다.
