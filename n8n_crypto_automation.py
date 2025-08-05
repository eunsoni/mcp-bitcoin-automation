# -*- coding: utf-8 -*-
import requests
import os
from dotenv import load_dotenv

load_dotenv()
N8N_API_KEY = os.getenv("N8N_API_KEY")
GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
GOOGLE_SHEETS_CREDENTIAL_ID = os.getenv("GOOGLE_SHEETS_CREDENTIAL_ID")
SMTP_CREDENTIAL_ID = os.getenv("SMTP_CREDENTIAL_ID")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")

economic_sheets_workflow = {
    "name": "📊 Daily Economic Data to Sheets & Email",
    "nodes": [
        {
            "parameters": {
                "rule": {
                    "interval": [{"field": "cronExpression", "cronExpression": "30 3 * * *"}]
                }
            },
            "id": "ff444621-844b-47be-8984-b880cfc58eca",
            "name": "Cron",
            "type": "n8n-nodes-base.cron",
            "typeVersion": 1,
            "position": [-592, 80]
        },
        {
            "parameters": {
                "url": "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin",
                "options": {}
            },
            "id": "66e92981-67a7-4f5f-98d2-c582ca96ae1a",
            "name": "Crypto",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 2,
            "position": [-400, 80]
        },
        {
            "parameters": {
                "functionCode": "const coin = $json[0];\n\nconst utcNow = new Date();\nconst kstNow = new Date(utcNow.getTime() + 9 * 60 * 60 * 1000);\nconst kstTime = new Date(new Date(coin.last_updated).getTime() + 9 * 60 * 60 * 1000);\n\nreturn [\n  {\n    json: {\n      \"날짜\": kstNow.toISOString().slice(0, 10),\n      \"이름\": coin.name,\n      \"현재가\": coin.current_price.toLocaleString(),\n      \"변동률(24h)\": coin.price_change_percentage_24h.toFixed(2),\n      \"시가총액\": coin.market_cap.toLocaleString(),\n      \"시가총액(B)\": Math.round(coin.market_cap / 1e9).toLocaleString(),\n      \"시가총액 순위\": `#${coin.market_cap_rank}`,\n      \"거래량\": coin.total_volume.toLocaleString(),\n      \"고가(24h)\": coin.high_24h.toLocaleString(),\n      \"저가(24h)\": coin.low_24h.toLocaleString(),\n      \"역대최고가\": coin.ath.toLocaleString(),\n      \"역대최고일\": new Date(coin.ath_date).toLocaleDateString(\"ko-KR\"),\n      \"역대최저가\": coin.atl.toLocaleString(),\n      \"역대최저일\": new Date(coin.atl_date).toLocaleDateString(\"ko-KR\"),\n      \"업데이트시각(KST)\": kstTime.toLocaleString(\"ko-KR\")\n    }\n  }\n];\n"
            },
            "id": "c0eba301-59be-4a4f-945b-cc392c500162",
            "name": "정리",
            "type": "n8n-nodes-base.function",
            "typeVersion": 1,
            "position": [-208, 80]
        },
        {
            "parameters": {
                "operation": "append",
                "documentId": {
                    "__rl": True,
                    "value": GOOGLE_SHEETS_ID,
                    "mode": "list",
                    "cachedResultName": "n8n",
                    "cachedResultUrl": f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEETS_ID}/edit?usp=drivesdk"
                },
                "sheetName": {
                    "__rl": True,
                    "value": "gid=0",
                    "mode": "list",
                    "cachedResultName": "시트1",
                    "cachedResultUrl": f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEETS_ID}/edit#gid=0"
                },
                "columns": {
                    "mappingMode": "defineBelow",
                    "value": {
                        "날짜": "={{ $json['날짜'] }}",
                        "이름": "={{ $json['이름'] }}",
                        "현재가": "={{ $json['현재가'] }}",
                        "변동률(24h)": "={{ $json['변동률(24h)'] }}",
                        "시가총액": "={{ $json['시가총액'] }}",
                        "거래량": "={{ $json['거래량'] }}",
                        "고가(24h)": "={{ $json['고가(24h)'] }}",
                        "저가(24h)": "={{ $json['저가(24h)'] }}"
                    },
                    "matchingColumns": [],
                    "schema": [
                        {
                            "id": "날짜",
                            "displayName": "날짜",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "이름",
                            "displayName": "이름",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "현재가",
                            "displayName": "현재가",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "변동률(24h)",
                            "displayName": "변동률(24h)",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "시가총액",
                            "displayName": "시가총액",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "거래량",
                            "displayName": "거래량",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "고가(24h)",
                            "displayName": "고가(24h)",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        },
                        {
                            "id": "저가(24h)",
                            "displayName": "저가(24h)",
                            "required": False,
                            "defaultMatch": False,
                            "display": True,
                            "type": "string",
                            "canBeUsedToMatch": True
                        }
                    ],
                    "attemptToConvertTypes": False,
                    "convertFieldsToString": False
                },
                "options": {}
            },
            "id": "2e0ce87c-95e8-48b6-bdc4-93f091e460e1",
            "name": "Google Sheets - 기록",
            "type": "n8n-nodes-base.googleSheets",
            "typeVersion": 4,
            "position": [0, 160],
            "credentials": {
                "googleSheetsOAuth2Api": {
                    "id": GOOGLE_SHEETS_CREDENTIAL_ID,
                    "name": "Google Sheets account"
                }
            }
        },
        {
            "parameters": {
                "fromEmail": "economic.dashboard@n8n.local",
                "toEmail": TARGET_EMAIL,
                "subject": "📊 Daily Economic Report - V2",
                "emailFormat": "html",
                "html": "=<html>\n  <body style=\"font-family:Arial, sans-serif; margin:20px; background-color:#ffffff; color:#212529;\">\n    <h2 style=\"color:#343a40;\">📈 오늘의 경제 리포트</h2>\n\n    <!-- 비트코인 정보 카드 -->\n    <div style=\"background:#f1f3f5; padding:15px; margin:20px 0; border-radius:8px; border:1px solid #dee2e6;\">\n      <h3 style=\"margin-top:0;\">💰 {{$json[\"이름\"]}}</h3>\n      <p>📍 현재가: <strong>${{$json[\"현재가\"]}}</strong> USD</p>\n      <p>📉 24시간 변동: <strong>{{$json[\"변동률(24h)\"]}}%</strong></p>\n      <p>🔼 고가 (24h): <strong>${{$json[\"고가(24h)\"]}}</strong></p>\n      <p>🔽 저가 (24h): <strong>${{$json[\"저가(24h)\"]}}</strong></p>\n      <p>💵 거래량 (24h): <strong>${{$json[\"거래량\"]}}</strong></p>\n      <p>🏆 시가총액 순위: <strong>{{$json[\"시가총액 순위\"]}}</strong></p>\n    </div>\n\n    <!-- 시가총액 카드 -->\n    <div style=\"background:#f8f9fa; padding:15px; margin:20px 0; border-radius:8px; border:1px solid #dee2e6;\">\n      <h3 style=\"margin-top:0;\">📊 시가총액</h3>\n      <p>💰 총액: <strong>${{$json[\"시가총액(B)\"]}}B USD</strong></p>\n    </div>\n\n    <!-- 역사적 정보 카드 -->\n    <div style=\"background:#e9ecef; padding:15px; margin:20px 0; border-radius:8px; border:1px solid #ced4da;\">\n      <h3 style=\"margin-top:0;\">📅 역사적 데이터</h3>\n      <p>🚀 역대 최고가: <strong>${{$json[\"역대최고가\"]}}</strong> ({{$json[\"역대최고일\"]}})</p>\n      <p>📉 역대 최저가: <strong>${{$json[\"역대최저가\"]}}</strong> ({{$json[\"역대최저일\"]}})</p>\n    </div>\n\n    <!-- 하단 푸터 -->\n    <p style=\"font-size:0.9em; color:#6c757d;\">\n      <em>📅 {{$json[\"날짜\"]}} 기준 / 데이터 업데이트: {{$json[\"업데이트시각(KST)\"]}}</em><br />\n      <em>🛠 n8n 자동화 시스템</em>\n    </p>\n  </body>\n</html>",
                "options": {}
            },
            "id": "8c5acfc8-9bdc-459c-9cff-9b562ee4efab",
            "name": "Send email",
            "type": "n8n-nodes-base.emailSend",
            "typeVersion": 2,
            "position": [-16, -32],
            "credentials": {
                "smtp": {
                    "id": SMTP_CREDENTIAL_ID,
                    "name": "SMTP account"
                }
            }
        }
    ],
    "connections": {
        "Cron": {
            "main": [[{"node": "Crypto", "type": "main", "index": 0}]]
        },
        "Crypto": {
            "main": [[{"node": "정리", "type": "main", "index": 0}]]
        },
        "정리": {
            "main": [
                [
                    {"node": "Google Sheets - 기록", "type": "main", "index": 0},
                    {"node": "Send email", "type": "main", "index": 0}
                ]
            ]
        }
    },
    "settings": {"timezone": "Asia/Seoul"}
}

# 워크플로우 생성 및 등록
response = requests.post(
    "http://localhost:5678/api/v1/workflows",
    json=economic_sheets_workflow,
    headers={
        "Content-Type": "application/json",
        "X-N8N-API-KEY": N8N_API_KEY
    }
)

if response.status_code == 200:
    print("✅ 📊 Google Sheets + Email 워크플로우 생성 완료!")
    print("📝 기능:")
    print("   - 새벽 3시 30분 자동 실행")
    print("   - CoinGecko API에서 비트코인 데이터 수집")
    print("   - Function 노드로 한국어 데이터 정리")
    print("   - Google Sheets에 자동 기록")
    print("   - HTML 형식 이메일 발송")
    print(f"📋 워크플로우 ID: {response.json().get('id')}")
else:
    print(f"❌ 실패: {response.status_code}")
    print(f"오류 내용: {response.text}")
