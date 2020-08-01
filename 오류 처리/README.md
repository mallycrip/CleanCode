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
`메서드`에서 `Checked Exception`을 던졌는데 `catch`블록이 세 단계 위에 있다면 그 사이 `메서드`모두가 선언부에 해당 `예외`를 정의해야 한다.
