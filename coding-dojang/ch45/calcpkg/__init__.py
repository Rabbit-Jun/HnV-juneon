#  폴더(디렉터리) 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식됩니다.
#  그리고 기본적으로 __init__.py 파일의 내용은 비워 둘 수 있습니다
#  (파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식됩니다.
#  하지만 하위 버전에도 호환되도록 __init__.py 파일을 작성하는 것을 권장합니다).

from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

# import로 패키지를 가져오면 __init__.py 파일이 실행되므로 이 파일에서 from . import 모듈 형식으로
# 현재 패키지에서 모듈을 가져오게 만들어야 합니다. 참고로 .(점)은 현재 패키지라는 뜻입니다
from .operation import add, mul
from .geometry import triangle_area, rectangle_area
# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
