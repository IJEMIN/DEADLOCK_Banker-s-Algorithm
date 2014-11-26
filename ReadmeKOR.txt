레퍼런스:
https://github.com/MaoAiz/Deadlocks


Banker's Alogorithm을 시뮬레이션 하는 클래스

v1.0

매소드
__init__: 초기화, 총 자원의 양을 가진 리스트를 입력으로 받는다.

SignProcesses: 프로세스들이 필요로 하는 총 자원의 양, 현재 할당된 자원의 양에 대한 행렬을 받아 클래스를 초기화 한다

Difference: 두 행렬의 차이를 구하는 매소드. 

CalcNeed: Difference 매소드를 사용하여 현재 더 필요로 하는 자원에 대한 Need 행렬을 계산하여 반환

CalcAvaliable: 현재 할당하고 남은 자원의 양을 계산하여 반환

ExecuteProcess: 인덱스를 입력으로 받아 해당하는 프로세스가 요구하는 자원을 할당. 만약 자원이 충분하지 않으면 False 반환

ReleasingProcess: ExecuteProcess 수행후 프로세스가 종료되었음을 명시하기 위해 프로세스의 Finish 상태를 True로 한다.
		  해당 프로세스가 가지고 있던 모든 자원을 반환 하고 자원 상태에 대한 행렬들 갱신.

TempSafeCheckAfterRelease: Safe State 체크.
반드시 ExecuteProcess와 ReleasingProcess가 모두 수행된 다음 수행.
직전의 프로세스가 수행되고 종료된 이후 다음에 연속적으로 수행 가능한 프로세스가 단 하나라도 있는지 검사한다.
만약 모든 프로세스가 수행 불가능이라면, 해당 프로세스 조합은 unSafe한 조합으로서 Deadlock을 피할 수 없는 조합이다.

print_matrixes: 행렬들 상태 출력

Execute: 전체 프로세스 수행을 시작한다.
프로세스를 순차적으로 수행하고, 당장 수행 불가능한 프로세스는 HOLD 상태로 둔 다음, 다음 루프때 다시 수행을 시도한다.
만약 TempSafeCheckAfterRelease에 의한 SafeCheck에서 해당 시퀀스가 수행 불가능이라 판별될 경우 강제 종료한다.