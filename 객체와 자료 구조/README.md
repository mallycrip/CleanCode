# 객체와 자료 구조
__객체 : 새로운 자료 타입 추가 시 유용, 새로운 동작 추가 힘듬__<br/>
__자료 구조(절차지향적) : 새로운 동작 추가시 유용, 새로운 자료 타입 추가 힘듬__

## 왜 변수는 `Private`로 정의하는가?
남들이 변수에 의존하지 않게 만들고 싶기 때문
### 그러면서 왜 `getter`, `setter`함수를 당연하게 공개할까?
변수를 `private`로 선언하더라도 각 값마다 `getter`와 `setter`이 있으면 구현을 외부로 노출하는 셈이다.<br/>
변수 사이에 함수라는 계층을 추가해도 구현이 감추어 지는 것은 아니다. 구현을 감추기 위해서는 `추상화`가 필요하다

### 추상화?
다음은 어떠한 사각형에 대한 클래스이다.
```python
class Square:
    def __init__(self):
        self._width = 10
        self._height = 10
```
이 클래스에서 정보를 가져오는 방법하면 보통 `getter`을 사용하여 가져오는 방법을 생각한다.
```python
class Square:
    ...
    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height
```
하지만 위와 같은 방법은 제대로 된 클래스라고 하기 어렵다. 클래스는 `추상 인터페이스`를 제공해 사용자가 구현을 모른 채로 자료의 핵심을 조작할 수 있어야 한다.<br/>
다음은 사각형에 대한 상태를 구체적으로 알려준다.
```python
class Square:
    ...
    def get_area(self):
        return self._width * self._height
```
위와 같이 자료를 세세하게 공개하기 보다는 `추상적인 개념`으로 표현하는 방법이 좋다. <br/>
절대 `인터페이스`나 `getter`, `setter`만으로는 `추상화`가 이루어 지지는 않는다.<br/>
특히 아무 생각 없이 `getter`, `setter`을 추가하는 방법이 가장 나쁘다.
<br/>
<br/>
Page 118 ~ 119
