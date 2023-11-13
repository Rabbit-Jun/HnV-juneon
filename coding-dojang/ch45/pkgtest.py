# from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴
import calcpkg
# 패키지의 __init__.py에서 from .모듈 import 변수, 함수, 클래스 또는
# from .모듈 import * 형식으로 작성했다면 패키지를 가져오는 스크립트에서는 패키지.함수() 형식으로 사용할 수 있습니다
# (변수, 클래스도 같은 형식). 이때는 import calcpkg와 같이 패키지만 가져오면 됩니다.

print(dir())
print(calcpkg.add(10, 20))
from calcpkg import *
print(triangle_area(30, 40))

# __init__.py에서 모듈만 가져왔을 뿐
# 모듈 안의 함수는 가져오지 않았기 때문에 에러 발생
