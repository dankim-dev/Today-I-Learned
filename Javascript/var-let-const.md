## 📍 const, var, let 의 차이점

### const ✅
- 상수
- 즉 재선언, 재할당 불가능


<br>

### var
- hoisting으로 인한 문제 : 
    - `hoisting` : 함수가 실행되기 전, 코드 내 변수들을 범위의 최상단으로 올리는 것
    - 변수의 선언과 초기화가 같이 실행됨
- 전역변수와 지역변수의 개념이 확싫하지 않음
    - 함수만 지역변수로 호이스팅되고, 나머지 변수들은 전역변수로 선언됨
- 변수 이름 중복 가능 문제
- 즉 변수 재선언, 재할당 모두 가능

<br>

### let ✅
- ES6 버전 JS로 업데이트 시 새로 생긴 기능 (2015)
- 호이스팅되나, Temporal Death Zone(TDZ) 사용
- 즉 변수 재선언 불가능, 재할당 가능


