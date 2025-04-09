# 🧠 AI Memory: 세 가지 기억 유형

LLM 기반의 Agent 시스템을 설계할 때, **기억(Memory)** 구조를 인간의 뇌처럼 세 가지 유형으로 나누어 구성할 수 있습니다:

---

## 🧩 1. Semantic Memory (의미 기억)

- **정의**: 세상에 대한 일반적인 사실, 개념, 지식 등을 기억
- **특징**:  
  - 변하지 않음 (stable)
  - 대화와 무관하게 **사실 기반 지식 저장**
- **예시**:
  - “서울은 대한민국의 수도이다.”
  - “Python은 프로그래밍 언어이다.”
- **AI 구현 방식**:
  - 벡터 DB에 저장된 문서, 문서 기반 RAG 시스템
  - 영구적으로 저장되어 계속 참조됨

---

## 💬 2. Episodic Memory (일화 기억)

- **정의**: 시간순 대화나 사건에 대한 기억. 대화 이력 기반의 문맥 유지
- **특징**:
  - 시간 순서로 구성됨
  - 사용자와의 **대화 흐름**, 맥락 기억
- **예시**:
  - “어제 너는 나에게 ‘영화 추천해줘’ 라고 물었어.”
  - “지금 ‘서울 날씨’에 대해 이야기 중이야.”
- **AI 구현 방식**:
  - LangChain의 `ConversationBufferMemory`, `ChatMessageHistory`
  - LangGraph의 state로 저장/전달
  - Redis 또는 파일 기반의 세션별 로그

---

## ⚙️ 3. Procedural Memory (절차 기억)

- **정의**: 반복 학습을 통해 습득된 **절차적 기술** 또는 행동 규칙
- **특징**:
  - 사용자의 명령을 수행하는 방법에 대한 지식
  - 반복 작업에 대한 루틴화
- **예시**:
  - “파일을 업로드하면 자동으로 PDF 요약을 수행한다.”
  - “사용자가 '계산' 요청 시 계산기 툴을 자동 사용한다.”
- **AI 구현 방식**:
  - Agent의 Tool Use 자동화 (`ReAct`, `LangGraph`, `Autogen` 기반)
  - 조건 분기, 규칙 기반 FSM(상태 머신)으로 구성

---

## 📌 요약 비교

| 기억 유형 | 설명 | AI 적용 예시 |
|-----------|------|---------------|
| Semantic Memory | 일반적 사실 | 벡터 DB, 문서 검색 RAG |
| Episodic Memory | 대화 이력 | BufferMemory, Session 기반 저장 |
| Procedural Memory | 행동 규칙 | Tool 자동화, Graph 기반 제어 |

---

## 🔁 함께 쓰는 구조

```mermaid
graph TD
    User --> Agent
    Agent --> EpisodicMemory[일화 기억: 대화 이력]
    Agent --> SemanticMemory[의미 기억: RAG 지식 검색]
    Agent --> ProceduralMemory[절차 기억: Tool 사용 규칙]