# 📊 N8N Economic Dashboard Automation

**MCP(Model Context Protocol) 기반 n8n 워크플로우 자동 생성 시스템**

## 🚀 주요 기능

- **자동화된 워크플로우 생성**: Python 코드로 n8n 워크플로우를 프로그래매틱하게 생성
- **경제 데이터 수집**: CoinGecko API를 통한 암호화폐 데이터 자동 수집
- **Google Sheets 연동**: 수집된 데이터를 Google Sheets에 자동 기록
- **HTML 이메일 발송**: 이쁜 HTML 형식으로 일일 리포트 이메일 전송
- **스케줄링**: 매일 새벽 3시 30분 자동 실행

## 🛠 기술 스택

- **n8n**: 워크플로우 자동화 플랫폼
- **Python**: 워크플로우 생성 스크립트
- **CoinGecko API**: 암호화폐 데이터 소스
- **Google Sheets API**: 데이터 저장
- **SMTP**: 이메일 발송
- **Docker**: n8n 컨테이너 환경

## 📋 설치 및 설정

### 1. 저장소 클론
```bash
git clone [repository-url]
cd n8n
```

### 2. 가상환경 설정
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv
```

### 3. 환경변수 설정
```bash
cp .env.example .env
# .env 파일을 편집하여 실제 값들을 입력
```

### 4. n8n Docker 컨테이너 실행
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

## 🔧 사용법

### 워크플로우 생성 및 등록
```bash
source .venv/bin/activate
python economic_sheets_workflow_template.py
```

## 📁 파일 구조

```
n8n/
├── .env.example                          # 환경변수 템플릿
├── .gitignore                            # Git 무시 파일
├── README.md                             # 프로젝트 설명
├── economic_sheets_workflow_template.py  # 안전한 워크플로우 템플릿
├── economic_email_gpt_v2.py             # 이메일 전용 워크플로우
├── api_test.py                          # CoinGecko API 테스트
└── test_simple.py                       # 정적 HTML 이메일 테스트
```

## 🔐 보안 고려사항

- 모든 민감한 정보는 환경변수로 관리
- `.env` 파일은 Git에서 제외
- API 키, Credential ID 등은 하드코딩하지 않음

## 🎯 핵심 혁신

**MCP(Model Context Protocol) 활용**: GitHub Copilot을 통해 n8n 워크플로우를 코드로 자동 생성하는 Infrastructure as Code 접근 방식

## 🤝 기여

이 프로젝트는 MCP 기반 자동화의 예시입니다. 개선사항이나 버그 리포트는 언제든 환영합니다!

## 📄 라이선스

MIT License
