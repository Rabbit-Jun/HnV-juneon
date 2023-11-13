import squre2
from squre2 import base, square  # 변수와 함수를 가져온 뒤 모듈 이름을 붙이지 않고 사용 할 수 있음
import person
import hello
import calc
import calcpkg.operation
import calcpkg.geometry
from calcpkg.geometry import triangle_area
import calcpkg
# calcpkg의 __init__.py에서 하위 모듈을 함께 가져오게 만들었으므로
# import calcpkg로 패키지만 가져와도 calcpkg.operation.add(10, 20)처럼 사용할 수 있습니다.

print(triangle_area(20, 40))
print(calcpkg.operation.add(10, 20))

print(calcpkg.geometry.triangle_area(30, 40))

print('main.py __name__:', __name__)  # 이 코드는 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용.
# 파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행됩니다. 따라서 hello 모듈을 가져오면
# hello.py 안의 코드 실행. 따라서 hello.py의 __name__ 변수에는 'hello'가 들어가고,
#  main.py의 __name__ 변수에는 '__main__'이 들어갑니다.
# 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.
print(squre2.base)   # 모듈.변수 형식으로 모듈의 변수 사용
print(squre2.square(10))  # 모듈.함수() 형식으로 모듈의 함수 사용
print(base)
square(10)

maria = person.Person('maria', 20, 'seoul Korea')
maria.greeting()

# 모듈과 모듈을 사용할 파일이 같은 폴더에 있어야 한다;

calc.add(50, 60)
