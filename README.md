# 📱 Deep Learning Vision Assist App (Recognition Supporter)

> **시각장애인을 위한 딥러닝 기반 식품 인식 및 거리 감지 보조 애플리케이션**

본 프로젝트는 시각장애인의 이동 편의성과 안전성을 향상시키기 위해 개발된 모바일 솔루션입니다.
**React Native**를 활용하여 크로스 플랫폼 클라이언트를 구축하였으며, **TensorFlow.js & Lite** 모델을 탑재하여 온디바이스(On-device) 환경에서의 AI 추론 가능성을 연구했습니다.

이 저장소는 **팀 프로젝트의 최종 결과물(team-version)**과, 제가 **기술적 연구(R&D)를 주도했던 거리 감지 기능(my-attempt)** 코드를 분리하여 정리한 포트폴리오용 아카이브입니다.

---

## 📸 Project Architecture & Flow
말뿐인 기획이 아니라, **철저한 요구사항 분석과 시스템 설계**를 바탕으로 개발되었습니다.

| System Flow (Sequence Diagram) | Use Case Diagram |
| :---: | :---: |
| ![Sequence Diagram]([보고서_72페이지_시퀀스다이어그램_캡처이미지]) | ![Use Case]([보고서_62페이지_유스케이스_캡처이미지]) |
> *설계 단계에서 작성한 시퀀스 다이어그램과 유스케이스 (Project Documentation)*

---

## 📌 Project Info

- **프로젝트 명:** 인식 서포터 (Recognition Supporter)
- **개발 기간:** 2023.04.26 ~ 2023.11.09 (약 7개월)
- **팀 구성:** 4인 팀 (역할: **Team Leader**, Tech Lead)
- **개발 환경 (Tech Stack):**
  - **Client:** React Native 0.70 (Android/iOS Cross-Platform)
  - **AI/ML:** TensorFlow.js 3.8.0, Google Cloud Vision API
  - **Database:** SQLite 3.37.2
  - **Design/Collaboration:** Notion, UI/UX Wireframing
- **핵심 기능:**
  - 📷 **식품 인식 (Food Recognition):** 카메라로 인식된 식품(라면, 음료 등)을 분류하고 음성(TTS)으로 안내
  - 📏 **거리 감지 (R&D):** 단안 카메라 및 센서 융합을 통한 장애물 거리 추정 연구

---

## 👨‍💻 My Role (Team Leader & Tech Lead)

팀의 리더로서 **전체 시스템 아키텍처를 설계**하고, **기술적 난이도가 높은 기능의 타당성 검토(Feasibility Check)**를 주도했습니다.

### 1. Project Management & Architecture
- **요구사항 분석:** 기능(FUR), 성능(PER), 인터페이스(IFR) 요구사항 명세서 작성 주도
- **시스템 설계:** UML(Use Case, Sequence Diagram) 작성을 통한 개발 로직 구체화
- **일정 관리:** WBS 기반의 개발 일정 관리 및 리스크 매니지먼트

### 2. R&D: 거리 감지 알고리즘 연구 (my-attempt)
- **목표:** 별도의 LiDAR 센서 없이 일반 카메라만으로 1m 이내 장애물을 감지하는 기능 연구
- **시도:** **TensorFlow Hub의 `mono+stereo_640x192` 모델**을 TFLite로 변환하여 모바일 이식 시도
- **검증:** React Native와 Native Module(Java) 간의 브릿지 통신 및 성능 테스트 수행

---

## 🛠 Technical Trouble Shooting (Retrospective)

프로젝트 요구사항 정의서의 **[PER-004 실시간성(Real-time Performance)]** 요건을 충족하기 위해 치열하게 고민했던 과정입니다.

### 📉 고성능 심도 추정 모델의 모바일 최적화 이슈
**문제 상황 (Issue):**
보고서의 성능 요구사항에 따라 **"모든 인식은 2초 이내, 음성 안내는 1초 이내"**에 수행되어야 했습니다.
하지만 `mono+stereo_640x192` 모델 도입 시, 모바일 CPU/GPU 부하로 인해 추론 시간이 3초 이상 지연되는 **Latency 이슈**가 발생했습니다.

**원인 분석 (Cause):**
1. **리소스 제약:** 640x192 해상도의 이미지를 실시간 프레임으로 처리하기엔 모바일 엣지 환경의 연산 자원이 부족했습니다.
2. **발열 및 배터리:** 반복적인 추론 과정에서 기기 발열이 심해져, 앱의 안정성(Stability) 요구사항을 위협했습니다.

**해결 및 의사결정 (Solution & Learned):**
- **Trade-off 분석:** "느리지만 정확한 딥러닝 거리 측정" vs "빠르고 안정적인 서비스 제공" 사이에서, 사용자 안전을 위해 **실시간성(Speed)**을 우선순위로 두었습니다.
- **결과:** 최종 릴리즈 버전에서는 해당 기능을 제외하는 과감한 의사결정을 내렸습니다.
- **배운 점:** 이 과정을 통해 기획 단계에서의 **PoC(개념 증명) 중요성**과, 모바일 환경에서의 **AI 모델 경량화(Quantization)** 필요성을 절실히 깨달았습니다.

---

## 🔗 Repository Structure

본 프로젝트의 원본 코드는 아래 링크에서 확인할 수 있습니다.

- **`team-version` 폴더:** 팀 프로젝트 최종 완성 코드
  - (원본 리포지토리: [TPJ1106/project](https://github.com/TPJ1106/project))
- **`my-attempt` 폴더:** 거리 감지 기능 연구 및 구현 시도 코드
  - (원본 리포지토리: [TPJ1106/recognize_supporter](https://github.com/TPJ1106/recognize_supporter))

---

## 📞 Contact
- **Name:** 김연희 (Yeonhee Kim)
- **GitHub:** [https://github.com/starry067](https://github.com/starry067)
