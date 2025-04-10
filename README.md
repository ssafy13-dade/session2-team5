# 변경 이력
- 2025-04-09
    - develop 브랜치 생성
    - 원본 데이터셋 파일 저장 완료
    - 원본 데이터셋 정의서 저장 완료

<br/><br/>

# 1. 프로젝트 개요
## 주제
- 제조 데이터 수집 파이프라인 구축과 분석

<br/>

## 목적
- 본 프로젝트는 SSAFY-13 DADE 스터디 활동의 일부입니다.
프로젝트의 **실제 목적**은 다음의 역량을 강화하기 위함입니다.
    - 데이터 엔지니어링 관련 경험
    - 데이터 분석 관련 경험
    - 프로젝트 매니지먼트 경험
    - 협업 활동 경험
- 경험하고 연습하고자 진행하는 프로젝트인 점 참고하여 프로젝트의 규모, 완성도, 실제 활용도 등을 조절하면 좋겠습니다.

<br/>

## 팀 구성
- DE 팀
    - 김영우
    - 유건우
- DA 팀
    - 김대현 (프로젝트 팀장)
    - 노규백

<br/>

## 주요 기능
- 생산 도메인 데이터를 스트리밍 처리하여 수집 및 저장 파이프라인을 구축
- 여러 분석 목표에 따라 분석 수행하여 인사이트 도출

<br/>

## 협업 환경
- 버전 관리 도구: [Github](https://github.com/ssafy13-dade/session2-team5)

- 회의록 & 일정 관리: Notion
- 실시간 회의: Discord

<br/><br/>

# 2. 시스템 아키텍처
시스템 구성도가 들어갑니다.

인프라 및 환경 (프로그래밍 툴, 사용 환경) 설명이 들어갑니다.

데이터 파이프라인. 어떤 데이터가 어떻게 이동하는지 설명이 들어갑니다.

<br/>

## 디렉토리 구조
```/session2-team5
├── .github/
│   └── pull_request_template.md
├── data-engineering/
├── data-analysis/
├── docs/
│   ├── Guidebook_전자부품(배터리팩) 품질보증 AI 데이터셋.pdf
│   └── Dataset_전자부품(배터리팩) 품질보증 AI 데이터셋.zip
├── README.md
├── .gitignore
└── requirements.txt
```

<br/><br/>

# 3. 개발 가이드
개발 환경 세팅법 내용이 들어갑니다. (개발하는 버전의 사용법)

의존성 설치, 환경 변수 설치 방법이 들어갑니다. (requirements.txt, pip, .env 등)

<br/>

## 브랜치 구성
```
main: 배포용 코드
└─ develop: 개발 통합 브랜치
    ├── feature/eng-기능명: DE 라벨링 + 기능 개발
    └── feature/ana-기능명: DA 라벨링 + 기능 개발
```

<br/><br/>

# 4. 데이터 정의서
## 데이터 목록
- Sample-table.csv

## (1) Sample-table.csv
| No | 논리명(Attribute) | 물리명(Field Name) | 데이터 타입 | 기본값 | 값의 범위 | 
|-------|-------|-------|-------|-------|-------|
| 1 | 제조시각 | time | datetime |  |  |
| 2 | 센서 이름 1 | sensor_1 | float |  |  |
| 3 | 합격 여부 | test | char | Y, N |  |

<br/><br/>			

# 5. 모듈별 설명
## data-engineering/streaming/
- 설명: 엔지니어링 관련 작업
- 주요 파일:
    - sample_1.js: 설명 1
    - sample_2.py: 설명 2
