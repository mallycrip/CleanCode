# 오류 처리
## 오류 코드 보다는 에외를 사용하라
대부분의 언어에서 `예외`를 지원한다.<br/>
`오류 코드`는 코드를 복잡하게 만든다. `함수`를 호출한 즉시 `오류`를 확인 해야하기 때문이다. <br/>
문제는 까먹는다. 그래서 `오류`가 발생하면 `예외`를 던지자. 

## Checked Exception & Unchecked Exception
`Unchecked Exception` : 확인되지 않은 `예외`. `컴파일`이 아닌 `런타임`시에 발생하는 `예외`이다. `예외`발생시 `롤백`한다.<br/>
`Checked Exception` : 확인된 `예외`. `컴파일`시점에서 확인한다. `예외`발생시 `롤백`하지 않는다.<br/>
<br/>
`Checked Exception`은 비용이 발생한다. 바로 `OCP(Open Closed Principle)`를 위반한다.<br/>
`메서드`에서 `Checked Exception`을 던졌는데 `catch`블록이 세 단계 위에 있다면 그 사이 `메서드`모두가 선언부에 해당 `예외`를 정의해야 한다.<br/>
이 말은 하위 단계에서 코드를 변경시 상위 단계 `메서드 선언부`를 고쳐야 한다는 뜻이다. 

## 의미 있는 예외
`오류 메시지`에 정보를 담아서 `예외`하라. 실패한 연산 이름과 실패 유형도 언급한다.<br/>
<br/>
`예외`를 던질 때는 전후 상황을 충분히 덧붙인다. 그래야 `오류`가 발생한 원인과 위치를 찾기 쉬워진다.<br/>
`Java`는 모든 `예외`에 `호출 스택`을 제공하는데 `실패한 코드`의 의도를 파악하려면 `호출 스택`만으로는 부족하다.<br/>

## 호출자를 고려
`오류`를 정의할 때에는 `프로그래머의` 가장 중요한 `관심사`는 `오류를 잡아내는 방법`이어야 한다.<br/>
`Wrapper`을 잘 사용하자. 코드가 깔끔해진다. 다음은 지저분한 `예외`와 `Wrapper`을 사용한 예외이다.
```python
port = ACMEPort()

try:
    port.open()

except DeviceResponseException as e:
    report_port_error(e)
    logger.log("Device Response Exception", e)

except ATM1212UnlockedException as e:
    report_port_error(e)
    logger.log("Unlocked Exception", e)

except GMXError as e:
    report_port_error(e)
    logger.log("GMX Error", e)

finally:
    ...
```
위 코드는 중복이 너무 심하다. 이 코드를 Wrapper로 감싸서 고쳐보겠다.
```python
port = LocalPort()


try:
    port.open()
except PortDeviceFailure as e:
    report_error(e)
    logger.log(e)
finally:
    pass



class LocalPort:
    def __init__(self):
        self.inner_port = ACMEPort()

    def open(self):
        try:
            self.inner_port.open()
        except DeviceResponseException as e:
            raise PortDeviceFailre(e)
        except ATM1212UnlockedException as e:
            raise PortDeviceFailre(e)
        except GMXError as e:
            raise PortDeviceFailre(e)
```

위와 같이 `LocalPort`클래스처럼 `ACMEPort`를 감싸는 `클래스`는 매우 유용하다. 실제로 외부 `API`를 사용할 때는 `Wrapper`이 가장 좋은 방법이다.<br/>
외부 `API`를 `Wrapper`로 감싸면 `의존성`가 크게 줄어든다. 나중에 다른 `라이브러리`로 갈아타도 `비용`이 적다.

## 정상 흐름을 정의
`예외`가 `논리`를 따라가기 어렵게 만들지 말자. `특수 상황`을 `예외`로 처리하려 하지마라.<br/>

### 특수 사례 패턴
`클래스`를 만들거나 `객체`를 조작해 `특수 사례`를 처리하자. 굳이 `클라이언트`코드에서 `예외`적인 상황을 처리할 필요가 없도록 한다.

## Null을 반환하면 안됨
`Null`을 반환하는 코드는 일거리를 늘릴 뿐만 아니라 `호출자`에게 `문제`를 떠넘긴다.<br/>
### Null을 전달하지도 마라
정상적인 `인수`로 `Null`을 기대하는 `API`가 아니라면 메서드로`Null`을 전달하는 코드는 최대한 피한다.

## Conclusion
`깨끗한 코드`는 읽기도 좋아야 하지만 `안정성`도 높아야 한다. 이 둘은 상충하는 목표가 아니다. `오류 처리`를 프로그램 논리와 분리해 독자적인 사안으로 고려하면 튼튼하고 깨끗한 코드를 작성할 수 있다.<br/>
`오류 처리`를 `프로그램 논리`와 분리하면 `독립적인 추론`이 가능해지고 `코드 유지보수성`도 크게 높아진다.
