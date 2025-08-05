# 📊 N8N Economic Dashboard Automation

**MCP(Model Context Protocol) 기반 n8n 워크플로우 자동 생성 시스템**

## 🚀 주요 기능

- **자동화된 워크플로우 생성**: Python 코드로 n8n 워크플로우를 프로그래매틱하게 생성
- **경제 데이터 수집**: CoinGecko API를 통한 암호화폐 데이터 자동 수집
- **Google Sheets 연동**: 수집된 데이터를 Google Sheets에 자동 기록
- **HTML 이메일 발송**: 예쁜 HTML 형식으로 일일 리포트 이메일 전송
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
`.env` 파일을 생성하고 다음 값들을 입력:
```bash
# .env 파일 생성 및 편집
touch .env
# 다음 환경변수들을 .env 파일에 입력:
# N8N_API_KEY=your_n8n_jwt_token
# GOOGLE_SHEETS_ID=your_google_sheets_id
# GOOGLE_SHEETS_CREDENTIAL_ID=your_credential_id
# SMTP_CREDENTIAL_ID=your_smtp_credential_id
# TARGET_EMAIL=your_email@example.com
```

### 4. n8n Docker 컨테이너 실행
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 5. n8n 웹 인터페이스 접속
브라우저에서 `http://localhost:5678`로 접속하여 n8n 관리 인터페이스에 로그인

## 🐳 Docker 셀프호스팅

### 기본 Docker 실행
```bash
# 기본 실행 (임시 컨테이너)
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 영구 실행 (백그라운드)
```bash
# 백그라운드에서 영구 실행
docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_SECURE_COOKIE=false \
  n8nio/n8n
```

### Docker Compose 사용
`docker-compose.yml` 파일 생성:
```yaml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    volumes:
      - ~/.n8n:/home/node/.n8n
    environment:
      - N8N_SECURE_COOKIE=false
      - N8N_HOST=localhost
      - N8N_PORT=5678
```

실행:
```bash
docker-compose up -d
```

## 🔧 사용법

### 워크플로우 생성 및 등록
```bash
source .venv/bin/activate
python n8n_crypto_automation.py
```

## 📁 파일 구조

```
mcp-bitcoin-automation/
├── .gitignore                    # Git 무시 파일
├── README.md                     # 프로젝트 설명
└── n8n_crypto_automation.py     # MCP 기반 워크플로우 자동 생성 스크립트
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
