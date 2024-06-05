## 게임 목표

본 게임에선 본인의 aircraft로 적의 모든 aircraft를 제거하면 승리하게 됩니다
방향키로 비행기의 위치를 조정 할 수 있고 적의 미사일에 본인의 aircraft가 맞으면 패배하게 됩니다

## Reference
[1] https://github.com/pygame/pygame "pygame"

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|Windows | :x:  |
|MacOS  | :o:  |

## 실행 방법
### Mac

1. python 3.12.2를 설치한다
2. pygame 2.5.2를 설치한다
```
pip3 install pygame==2.5.2
git clone https://github.com/RmKuma/oss_personal_project_phase1.git
cd oss_personal_project_phase1
python3 main.py
```

## 실행 예시
![Screen Recording 2024-06-05 at 1 36 37 PM](https://github.com/KimTaeyoung-219/oss_personal_project/assets/65494946/320e7f3c-1d3a-4486-ad49-8a4f21379a7d)


## 코드 설명
#### class TopGun
- Description: 게임 전체를 관리하는 메인 클래스
- Function: 아군 aircraft와 적군 aircraft를 생성하고 사용자의 input 관리

#### class Fighter, EnemyFighter
- Description: 아군과 적군의 전투기를 담당하는 클래스
- Function: 현재 아군과 적군의 전투기의 위치를 파악하고 전투기 격추 여부를 판단

#### class EnemyFighterMissile, FighterMissile
- Description: 아군과 적군이 쏜 미사일을 관리하는 클래스
- Function: 아군과 적군이 쏜 미사일의 위치와 이동궤적을 판단하고 관리

#### TODO List
 * 게임의 난이도 조절하기
 * 배경화면를 화려하게 꾸미기