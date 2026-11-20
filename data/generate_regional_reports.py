# -*- coding: utf-8 -*-
"""
02_지역분석자료 폴더의 5대 핵심 권역(봉담/서수원, 안성, 평택, 천안, 청주) 보고서를 파싱하여
정형화된 JSON 및 TS 데이터셋으로 빌드하는 스크립트.
"""
import os, json

base_reports_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\보고서\02_지역분석자료"
out_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\data"

# 1. 봉담/서수원
bongdam_path = os.path.join(base_reports_dir, "봉담", "오목천_봉담_통합_지역종합분석보고서.md")
with open(bongdam_path, "r", encoding="utf-8") as f:
    bongdam_text = f.read()

# 2. 안성
anseong_path = os.path.join(base_reports_dir, "안성", "안성시_부동산시장분석_PropX데이터솔루션활용보고서.md")
with open(anseong_path, "r", encoding="utf-8") as f:
    anseong_text = f.read()

# 3. 평택
pyeongtaek_path = os.path.join(base_reports_dir, "평택", "평택시_부동산시장분석_PropX데이터솔루션활용보고서.md")
with open(pyeongtaek_path, "r", encoding="utf-8") as f:
    pyeongtaek_text = f.read()

# 4. 천안
cheonan_path = os.path.join(base_reports_dir, "천안", "천안시_부동산시장분석_PropX데이터솔루션활용보고서.md")
with open(cheonan_path, "r", encoding="utf-8") as f:
    cheonan_text = f.read()

# 5. 청주
cheongju_path = os.path.join(base_reports_dir, "청주", "청주시_부동산시장분석_PropX데이터솔루션활용보고서.md")
with open(cheongju_path, "r", encoding="utf-8") as f:
    cheongju_text = f.read()

regional_data = [
    {
        "id": "bongdam",
        "name": "화성(봉담) · 서수원(오목천)",
        "badge": "10만 세대급 메가 서남부 신성장 생활권",
        "standardDate": "2026.11 기준",
        "headline": "지자체 경계를 초월한 수인분당선-신분당선 연계 메가 주거·산업 융합 벨트",
        "summary": "효행지구(1.2만 호)를 중심으로 수원 권선구와 화성 봉담이 단일 생활권으로 통합. 2024년 대규모 입주 피크 통과 후 극심한 공급 절벽 도래, 미분양 사실상 제로화(수원 21호, 화성 57호). 삼성디지털시티·현대차 남양연구소 등 배후 자족 일자리 풍부.",
        "metrics": {
            "unsold": "수원 21호 · 화성 57호 (완전 소진 Clean)",
            "supply": "2024년 정점(7,222호) ➔ 2026년 806호 (공급 절벽)",
            "demographics": "화성 100만 돌파 / 봉담권역 10만 계획인구",
            "traffic": "신분당선 봉담연장, 인천발 KTX 어천역(2026), 수인분당선 오목천역",
            "risk": "수원 군공항 고도제한 및 소음권역, 신분당선 조기 착공 시차"
        },
        "keyPoints": [
            "효행지구(1만~1.2만 세대) 조성을 매개로 수원 권선구 오목천동과 화성 봉담읍 완전 일체화",
            "신분당선 호매실-봉담 연장(제4차 국가철도망) 및 인천발 KTX 어천역(2026 개통 연계) 쾌속 교통망",
            "배후 산업: 삼성디지털시티(매탄동), 삼성전자 화성·기흥, 현대차 남양연구소, 고색 델타플렉스",
            "2026년 공급 가뭄에 따른 신축 아파트 희소성 부각 및 매매/전세 하방 경직성 확보"
        ],
        "contentMarkdown": bongdam_text
    },
    {
        "id": "anseong",
        "name": "경기도 안성시",
        "badge": "용인·평택 반도체 메가클러스터 남부 배후 주거지",
        "standardDate": "2026.11 (2026.08 K-Atlas 기준)",
        "headline": "아양지구 신규 분양 소진 국면 및 2026~2028년 극심한 입주 가뭄 진입",
        "summary": "2024.07 기준 1,113세대였던 미분양이 소진세를 보이다 2026.01 아양지구 분양으로 951세대로 일시 반등 후 919세대로 안정화 중. 2024년 5,008세대 입주 후 2026년 1,989세대, 2027년 976세대로 공급 급감. 공도읍 중심 가구 연소득 4,074만~5,259만원 형성.",
        "metrics": {
            "unsold": "919세대 (2026.07 기준, 점진적 소진 중)",
            "supply": "2024년 5,008세대 ➔ 2026년 1,989세대 ➔ 2027년 976세대 (입주 가뭄)",
            "demographics": "인구 196,592명 / 97,042세대 (1~2인 가구 분화 지속)",
            "traffic": "수도권내륙선 광역철도(동탄-안성-청주공항) 추진, 제2경부고속도로 안성구간 개통",
            "risk": "아양지구 미분양 잔여물량 및 구도심 노후화"
        },
        "keyPoints": [
            "2024년 5,000세대 역대 최대 입주 후 향후 3~4년간 강력한 공급 공백(입주 가뭄) 발생",
            "공도읍 중심 가구 금융체력 안정적 (공도KCC스위첸 등 연소득 5,259만원대 중상위 가구)",
            "용인 남사·원삼 반도체 클러스터 및 평택 브레인시티 인접 배후 주거 수요 지속 유입",
            "안성테크노밸리, 제5일반산단 등 관내 일자리 확충과 광역상수도 인프라 개선"
        ],
        "contentMarkdown": anseong_text
    },
    {
        "id": "pyeongtaek",
        "name": "경기도 평택시",
        "badge": "2040 기본계획 105만 거점 · 펜타역세권 평택지제역",
        "standardDate": "2026.11 기준 (행안부 2025)",
        "headline": "3,500세대 미분양 속 분상제 옥석가리기 & 향후 4개년 4.2만 세대 대규모 공급",
        "summary": "미분양 3,511세대(2026.07 기준) 적체 속 분양가상한제 평택고덕우미린프레스티지 등 핵심 단지만 완판. 브레인시티 등 외곽은 대규모 미달 양극화. 2025~2028년 4개년 합산 42,591세대 매머드급 입주로 전세가 변동성 확대. 고덕동 중심 경기 남부 최고 소득망(연 5,223만).",
        "metrics": {
            "unsold": "3,511세대 (고덕·브레인시티 양극화)",
            "supply": "2025~2028년 4년간 42,591세대 매머드급 집중 입주",
            "demographics": "인구 610,402명 (2008년 대비 +50.1% 폭증, 29.2만 세대)",
            "traffic": "평택지제역(SRT, KTX, GTX-A/C 연장 추진, 1호선), 안중역 서해선 직결",
            "risk": "단기 4.2만 세대 입주에 따른 전세가 하방 압력 및 마피 매물 속출"
        },
        "keyPoints": [
            "평택지제역 복합환승센터: SRT, 수원발 KTX, GTX-A/C 연장 확정의 펜타 역세권 허브",
            "삼성전자 평택캠퍼스 + 브레인시티 카이스트 평택캠퍼스 + 화성 기아차 우정벨트 고소득 통근망",
            "서평택 안중역 서해선-경부고속선 직결(여의도 30분대) 및 화양지구 2만세대 자족 성장",
            "단기 대량 입주 리스크에 따른 전세 세팅 시 안전 마진 확보 필수"
        ],
        "contentMarkdown": pyeongtaek_text
    },
    {
        "id": "cheonan",
        "name": "충청남도 천안시",
        "badge": "성성호수공원 골든벨트 & 아산 탕정 고소득 연계",
        "standardDate": "2026.11 기준",
        "headline": "5,100세대 미분양 급반등 속 2026년 일시적 입주절벽(689호) ➔ 2029년 입주폭탄",
        "summary": "2026년 한 해만 1.1만 세대 분양으로 미분양 5,100세대(2026.07) 폭증. 엘리프성성호수공원(26.2:1), 천안아이파크시티는 완판 흥행, 외곽지는 미달. 2026년 입주물량 단 689세대로 단기 전세 불안 발생 후 2029년 1.25만세대 입주 대기. 불당2동(연소득 6,684만원) 선도.",
        "metrics": {
            "unsold": "5,100세대 (2026.07 기준, 신규 분양 러시로 폭증)",
            "supply": "2026년 689세대 (입주 가뭄) ➔ 2029년 12,598세대 (입주 폭탄)",
            "demographics": "인구 664,322명 / 317,941세대 (불당2동 충청권 1위 부촌)",
            "traffic": "과성교 개통(2027), 부성역(2029), 천안역 GTX-C 연장 추진",
            "risk": "미분양관리지역 근접 및 2029년 초대형 입주 리스크"
        },
        "keyPoints": [
            "성성호수공원 및 천안아이파크시티 완판 등 대장주 프리미엄과 외곽 미달의 극단적 디커플링",
            "삼성디스플레이 탕정 캠퍼스 통근(연소득 7,407만원) 및 1.5% 저리 사내대출 복지 수혜",
            "직산읍 1.2조원 규모 AI 데이터센터(AIDC) 유치로 '전세권(電勢權)' 신성장 동력 확보",
            "2026년 입주 절벽기 단기 전세가 급등에 따른 갭투자 기회와 2029년 입주 전 출구 전략 수립"
        ],
        "contentMarkdown": cheonan_text
    },
    {
        "id": "cheongju",
        "name": "충청북도 청주시",
        "badge": "가경아이파크 15만 통장 쇄도 & SK하이닉스 M15X 호재",
        "standardDate": "2026.11 기준",
        "headline": "전국 최상위권 초건전성(미분양 402호)과 폭발적인 신축 청약 갈아타기 열풍",
        "summary": "천안의 5,100세대 미분양과 대조적으로 청주시는 미분양 402세대에 불과한 전국 최고 수준의 소화력 입증. 2026.10 가경아이파크 7·8단지 1순위에만 14.9만 개 통장 쇄도(최고 194.6:1). SK하이닉스 HBM M15X 팹 증설, 테크노폴리스 고소득 일자리, 21년 이상 노후도 51.8%의 강력한 갈아타기 수요.",
        "metrics": {
            "unsold": "402세대 (전국 최상위 청정 건전성, 완전 소화력)",
            "supply": "2026년 5,804세대 ➔ 2027년 9,709세대 (흥덕·서원구 수급 정점)",
            "demographics": "인구 856,152명 (역대 최대치, 40.9만 세대)",
            "traffic": "충청권 광역급행철도(CTX, 도심-세종-대전 30분대), KTX 오송역 2복선화",
            "risk": "2027년 입주 정점(9,709세대) 일시적 매물 집중"
        },
        "keyPoints": [
            "미분양 402호로 사실상 바닥 수준, 인근 권역 대비 압도적인 실수요 탄력성",
            "청주가경아이파크 7·8단지 1순위 149,730명 청약 접수 (최고 경쟁률 194.6:1)",
            "SK하이닉스 청주 M15X(HBM 차세대 팹) 대규모 투자로 아파트 매매가 상승세 주도",
            "21년 이상 구축 비율 51.8%로 풍부한 신축 갈아타기 대기 수요가 2027년 입주량 완충"
        ],
        "contentMarkdown": cheongju_text
    }
]

# JSON 저장
json_out = os.path.join(out_dir, "regional_reports_data.json")
with open(json_out, "w", encoding="utf-8") as f:
    json.dump(regional_data, f, ensure_ascii=False, indent=2)

# TypeScript 저장
ts_out = os.path.join(out_dir, "regional_reports_data.ts")
ts_content = f"""// 02_지역분석자료 기반 5대 권역 통합 리포트 데이터셋
export interface RegionalReport {{
  id: string;
  name: string;
  badge: string;
  standardDate: string;
  headline: string;
  summary: string;
  metrics: {{
    unsold: string;
    supply: string;
    demographics: string;
    traffic: string;
    risk: string;
  }};
  keyPoints: string[];
  contentMarkdown: string;
}}

export const REGIONAL_REPORTS: RegionalReport[] = {json.dumps(regional_data, ensure_ascii=False, indent=2)};
"""
with open(ts_out, "w", encoding="utf-8") as f:
    f.write(ts_content)

print(f"Generated regional reports dataset successfully!")
print(f"- JSON: {json_out} ({len(json.dumps(regional_data))} bytes)")
print(f"- TS: {ts_out} ({len(ts_content)} bytes)")
