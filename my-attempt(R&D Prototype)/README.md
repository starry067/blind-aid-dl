# 📂 my-attempt (R&D Prototype)

> **단안 카메라 기반 심도 추정(Monocular Depth Estimation) 기술 검증 프로토타입**

팀 프로젝트의 최종 버전(team-version)에는 탑재되지 못했으나, <b>핵심 기능 구현을 위해 기술적 타당성(Feasibility)을 검증했던 연구용 코드</b>입니다.

---

## 🧪 R&D Objectives (연구 목표)
- **LiDAR 없는 거리 측정:** 고가의 센서 없이 일반 RGB 카메라와 딥러닝 모델(`mono+stereo`)만으로 심도(Depth)를 추출하는 기술 구현.
- **On-device AI:** 서버 통신 없이 모바일 기기 내부에서 추론을 수행하여 네트워크 제약 없는 실시간성 확보 시도.

---

## ⚠️ Technical Challenges & Analysis (기술적 난관 및 분석)
이 기능을 최종 제품에서 제외하게 된 기술적 원인(Root Cause) 분석입니다.

### 1. Inference Latency (추론 지연)
- **현상:** 모바일 CPU 환경에서 TFLite 모델 추론 시 프레임 드랍 발생 (약 3FPS 미만).
- **분석:** 입력 이미지 전처리(Resizing 640x192)와 추론 연산량이 모바일 리소스 한계를 초과함.

### 2. Depth Value Convergence (출력값 '0' 수렴 이슈)
- **현상:** 추론 결과인 Depth Map의 텐서(Tensor) 값이 `0` 또는 유효하지 않은 값으로 반환됨.
- **기술적 가설:**
    - 모델의 Output을 실제 거리(Meter)로 변환하는 **캘리브레이션(Calibration)** 상수의 매칭 실패.
    - 전처리 과정에서의 **이미지 정규화(Normalization)** 파라미터 불일치로 인한 모델 성능 저하.

---

## 🧩 Key Engineering Learnings (배운 점)
- **Edge AI 최적화의 필요성:** 단순히 모델을 가져다 쓰는 것을 넘어, 모바일 환경에 맞는 <b>**양자화(Quantization)**</b>와 경량화가 필수적임을 체감.
- **Trade-off 분석 능력:** '정확도'와 '실시간성' 사이에서 사용자 경험(UX)을 최우선으로 하여 과감히 기능을 제외하는 <b>**기술적 의사결정**</b> 경험.
- **Fail-Fast:** 프로토타이핑을 통해 기술적 리스크를 조기에 발견하고, 전체 프로젝트 일정에 차질이 없도록 관리하는 리스크 매니지먼트 역량 습득.

---

## 🔧 Tech Stack (Research)
- **Core:** React Native
- **AI Model:** TensorFlow Lite (`mono+stereo_640x192`)
- **Vision:** OpenCV (이미지 전처리)

---

## 📚 Documentation (Reference)
본 프로토타입의 **연구 배경(Background)** 및 **기술적 분석(Technical Analysis)** 내용은 통합 보고서에 상세히 기술되어 있습니다.

* 📄 **[졸업작품 최종 보고서 확인하기 (Click)](../docs/)**
    * *거리 감지 기능의 설계 의도와 실패 요인 분석 등 상세 내용은 상위 `docs/` 폴더 내 보고서를 참고해 주세요.*
