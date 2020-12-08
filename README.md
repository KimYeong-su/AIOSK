# 자율 프로젝트 - AIOSK

 ## 🐱‍💻 ㅅㅁㅅ 팀 

| 이름          | 담당                                           |
| ------------- | ---------------------------------------------- |
| 김영수 (팀장) | AI 모델 구현                                   |
| 박희웅        | 추천 알고리즘 구현                             |
| 이경민        | 서버 통신에 필요한 API 및 모델                 |
| 이동옥        | UI/UX(Front-End)                               |
| 최동녘        | Database 구성(학습 데이터 및 추천 데이터 수집) |
| 최수람        | UI/UX(Front-End)                               |

### :100: 프로젝트 진척률 : 40%

## 목차

-  AIOSK 란?
  - 프로젝트의 목표
  - 프로젝트 가상환경
- 시작하며...
  - 기술 스택
  - WBS
  - 와이어 프레임
  - 일정표 & 역할 분배표
  - 그라운드 룰
- 깃 컨벤션
  - Branch
  - commit
- AIOSK 는 개발중...
  - ERD
  - API 명세서
  - 자료조사 & 학습내용

## 프로젝트 이름

**AIOSK** 는 AI기술을 이용한 스마트 키오스크 입니다.

키오스크를 사용하는 '다양한 연령층', '새로운 메뉴를 원하시는 분' 등등 즐겁고 편하게 키오스크를 사용하시길 원하는 분들을 위해 **스마트 키오스크**을 만들었습니다.

**「키오스크의 기술 소외 집단 문제를 해소하고 코로나 상황에 따라 발생하는 니즈를 충족」**을 목표로 합니다.

### 특징

- 이미지 분석을 통해 나이를 예측하고 그 나이때에 인기 있는 상품을 추천합니다.
- 사용자들의 빅데이터를 수집하고 이용하여 추천 알고리즘을 통해 상품을 추천합니다.
- 모션 인식을 통해 언택트 주문이 가능합니다.
- 연령별 키오스크 사용에 편리한 UI/UX를 제공합니다.
- 카카오 페이를 통해 간단한 결제 서비스를 포함하고 있습니다.

<img src="./Docs/mainpage.png">



## :computer: 시작하며...

> 프로젝트를 시작하며 사용하게 되는 기술 스택 및 팀 룰에 관한 내용입니다.

### 기술 스택

-------------------------

![badge](https://img.shields.io/badge/browser-chrome-red)![badge](https://img.shields.io/badge/framework-Django%20Vue.js-yellow)![badge](https://img.shields.io/badge/DB-sqlite3-skyblue)![badge](https://img.shields.io/badge/node-12.18.2-brightgreen)![badge](https://img.shields.io/badge/npm-6.14.5-brightgreen)![badge](https://img.shields.io/badge/Vue.js-2.6.11-green)![badge](https://img.shields.io/badge/@vue/cli-4.4.6-green)![badge](https://img.shields.io/badge/yarn-1.22.4-blue)![badge](https://img.shields.io/badge/Django-2.1.15-orange)![badge](https://img.shields.io/badge/Python-3.7.6-orange)

### 시스템 아키텍쳐

----------------------------------------

<img src="./Docs/systemArchitecture.JPG">

### 와이어 프레임

-----------------------------------

<img src="./Docs/wireframe.PNG">

### 그라운드 룰

> 팀만의 그라운드 룰을 적습니다.

## 깃 컨벤션

### Git-Branch

Git-flow는 다음과 같이 정해져있습니다.

- master : 배포 가능한 상태 브랜치
- develop : 업데이트 할 브랜치 + Docs 업데이트 브랜치
-  feature : 기능을 개발하는 브랜치
  - 기능 별  feature 브랜치의 이름
    - accounts
    - comments

### Git-commit

```bash
$ git commit -m "Jira 이슈 번호 | Header | 설명"
```

- JIRA 이슈 번호 or README
- Header
  - Initial : 가장 처음 만든 코드
  
  - Update : 정상적으로 동작하면서 수정/추가/보완된 코드
  
  - Fix : 비정상 동작 수정 코드
  
    

### Entity-Relationship Diagram(ERD)

-----------------------

![ERD](./Docs/AIOSK_ERD.png)



### 학습 데이터 다운로드

----------------------------------------------

[face_image 다운로드](https://drive.google.com/file/d/1ZKGkdqU5PDaOay3bcXJhKmg9yJUPVNIw/view?usp=sharing)

### Reference

---------------------

- https://www.tensorflow.org/api_docs/python/tf/all_symbols
- https://github.com/Wanguy/Inception_Tensorflow

