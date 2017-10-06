# ■모듈이란?
# 모듈이란 함수나 변수 or 클래스 들을 모아 놓은 하나의 파일을 말한다. 즉, 그냥 간단히 .py 파일 하나를 다른 이름으로 거창하게 그냥 모듈이라고 하는것이다.

# ■알아야 할 것들
# 1. 모듈을 가져다 쓰는 명령어가 바로 import이다.
# 2. 모듈을 import하고 싶을 때 해당 모듈이 현재 파일과 같은 디렉토리에 있거나 or ★파이썬 라이브러리가 저장된 디렉토리★에 있어야 한다.



#모듈은 그냥 작성 후 임포트해서 사용하면 된다. 사용법

# 기본적인 import 방식
import module_name


# 함수를 그냥 사용하기위한 통한 import 방식
from module_name import *               # 이런식으로 module을 import하게되면 해당 module의 함수를 그냥 사용 할 수 있게 된다.
                                        # ex) from module_name import *
                                        # ex) sum(a,b)
                                        # 주의해야 할 점은 이렇게 되면 이전에 있던 함수나 다른 모듈의 함수와 이름이 같을 경우
                                        # 마지막에 정의된 함수만을 사용할 수 있게 된다는 것이다.

# 그리고 import를 하게되면 해당 모듈이 실행되는 것이나 마찬가지여서 예를들어 print() 가 있으면 자동으로 실행이 된다.
# 이를 방지하기 위해 사용하는 것이 이는데 그것이 바로
if __name__ == "__main__":

# 위와 같은 코드가 만약 해당 모듈이 직접 실행 되는 것이 맞으면 저 if문이 참이되고 모듈을 improt하는 것이면 거짓이되어서
# if문 안에 있는 코드들을 제어가 가능한 것이다.


# 파이썬 라이브러리가 저장되어 있는 디렉토리 확인 및 디렉토리 추가하는 방법 - sys
import sys
print(sys.path)
# sys.path.append("절대경로")            # 이런식으로 라이브러리 관리 디렉토리로 인정받고 싶은 파일의 절대경로를 추가해서 그
                                        # 목록에 추가 시킬 수 있다.