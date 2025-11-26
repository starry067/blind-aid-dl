# Deep Learning Vision Assist App (Graduation Project)

시각장애인의 이동 편의성과 안전성을 향상시키기 위해  
**딥러닝 기반 식품 인식(Food Recognition)** 기능과  
**근거리 장애물 거리 감지(Obstacle Distance Measurement)** 기능을 구현한 모바일 보조 애플리케이션입니다.

본 레포지토리는 팀 프로젝트의 **최종 구현 버전(team-version)** 과  
제가 직접 구현을 시도했던 **거리 감지 기능(my-attempt)** 을  
명확하게 구분하여 정리한 포트폴리오용 저장소입니다.

---

## 📌 Project Overview

- **개발 기간:** 2023년 4월 26일 ~ 2023년 11월 9일 (약 7개월)  
- **프로젝트 유형:** 4인 팀 졸업작품  
- **개발 환경:**
  - HW : 스마트폰(어플리케이션 실행 및 카메라 사용), 외장하드(이미지 저장), 컴퓨터(딥러닝 학습)
  - SW : TensorFlow.js(이미지 학습), react-native(IOS와 Android 클라이언트 개발), SQL Lite(데이터 처리 및 저장), Google Cloud Vison API(외부 라이브러리 사용)
  - 프로그래밍 언어 :  Java Script(TensorFlow.js에서 사용) 
- **본인 역할:**
  - 기획 및 요구사항 정의서 작성  
  - 프로젝트 문서 / 보고서 구성  
  - UI/UX 설계(Figma)  
  - 장애물 거리 측정 기능 구현 시도(CameraX + Depth API)  
  - 기술 검증 및 테스트  

---

## 🎯 System Purpose & Goals

### ✔ 시스템 목적 (Purpose)
- 근거리 장애물 충돌 위험 사전 방지  
- 기존 OCR·바코드 기반 보조 앱의 한계 보완  
- 딥러닝 기반 이미지 분류 모델 적용  
- 장애물-지면 기준점 인식 문제 개선

---

### ✔ 시스템 목표 (Goals)

#### 1) 장애물 거리 감지 기능
- 협소한 공간에서 충돌 위험 사전 감지  
- 특정 거리 이하 접근 시 실시간 음성 경고  

#### 2) 딥러닝 기반 식품 인식 기능
- 다양한 각도의 식품 이미지 학습  
- 정면이 아니어도 식품 감지 및 분류  
- 텍스트 및 TTS 음성 안내 제공  

---

## 🔗 Original Repositories (Reference)

본 프로젝트의 원본 레포지토리는 아래에서 확인할 수 있습니다:

- **개인 기능 구현 시도 버전 (my-attempt 원본)**  
  https://github.com/TPJ1106/recognize_supporter

- **팀 프로젝트 최종 완성 버전 (team-version 원본)**  
  https://github.com/TPJ1106/project

---

## 📞 Contact

**김연희 (Yeonhee Kim)**  
GitHub: https://github.com/starry067

---

본 저장소는  
팀 결과물과 개인 구현 시도를 명확하게 분리하여  
프로젝트의 전체 흐름과 성장 과정을 투명하게 보여주기 위해 제작된  
포트폴리오용 저장소입니다.
---

