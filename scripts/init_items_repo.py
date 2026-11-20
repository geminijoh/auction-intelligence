# -*- coding: utf-8 -*-
import json
import os

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"
props_path = os.path.join(base_dir, "data", "properties.json")
items_dir = os.path.join(base_dir, "data", "items")
os.makedirs(items_dir, exist_ok=True)

with open(props_path, "r", encoding="utf-8") as f:
    properties = json.load(f)

folder_map = {
    "2025-56772": "2025타경56772_화성봉담우방1단지_102동1301호",
    "2026-239": "2026타경239_안성동남타운_102동1202호",
    "sale-bongdam-105": "급매_화성봉담우방1단지_105동1502호",
    "2026-50882": "2026타경50882_안성대덕신라_나동505호",
    "2025-1691": "2025타경1691_수원오목천남광하우스토리_105동1102호",
    "2026-50683": "2026타경50683_안성공도송정그린빌_102동901호"
}

for p in properties:
    pid = p.get("id")
    folder_name = folder_map.get(pid, f"{pid}")
    target_dir = os.path.join(items_dir, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    prop_file = os.path.join(target_dir, "property.json")
    with open(prop_file, "w", encoding="utf-8") as pf:
        json.dump(p, pf, ensure_ascii=False, indent=2)
    print(f"[Created] {folder_name}/property.json")

# 템플릿 폴더 생성
tmpl_dir = os.path.join(items_dir, "_template_new_property")
os.makedirs(tmpl_dir, exist_ok=True)
tmpl_data = {
  "id": "2026-99999",
  "caseNumber": "2026타경99999",
  "category": "경매",
  "status": "적극추천",
  "court": "수원지방법원 본원 경매1계",
  "auctionDate": "2026-12-20",
  "propertyName": "수원 영통 센트럴파크 101동 502호",
  "address": "경기도 수원시 영통구 매탄동 123",
  "buildingType": "아파트",
  "exclusiveAreaM2": 84.95,
  "exclusiveAreaPyung": 25.7,
  "floorInfo": "5 / 20층",
  "buildYear": 2018,
  "totalUnits": 950,
  "appraisedValue": 650000000,
  "minimumBidPrice": 455000000,
  "minimumBidRate": 70,
  "recommendedBidPrice": 510000000,
  "marketPrice": 630000000,
  "safetyMargin": 120000000,
  "expenses": {
    "acquisitionTax": 5610000,
    "legalFee": 800000,
    "evictionFee": 2000000,
    "repairFee": 3000000,
    "unpaidManagementFee": 0,
    "brokerageFee": 2040000,
    "loanInterest": 1500000,
    "totalExpenses": 14950000
  },
  "financing": {
    "ltvPercent": 70,
    "loanAmount": 357000000,
    "interestRate": 4.2,
    "monthlyInterest": 1249500
  },
  "rental": {
    "rentalType": "전세",
    "deposit": 420000000,
    "monthlyRent": 0,
    "expectedSalePrice": 630000000
  },
  "rights": {
    "malsoStandard": "2019-03-15 국민은행 근저당 (2억 4,000만원)",
    "occupantStatus": "소유자 점유 추정 (대항력 임차인 없음)",
    "isSafe": True,
    "takeoverAmount": 0,
    "evictionDifficulty": "하",
    "riskNotes": "선순위 인수권리 0원. 관리비 연체 없음."
  },
  "locationHighlights": [
    "수인분당선 영통역 도보 7분 역세권 대단지",
    "삼성전자 수원사업장 직주근접 최고 선호 입지",
    "초·중·고 도보 통학 및 영통 중심 학원가 인접"
  ],
  "strategyBrief": "감정가 대비 1회 유찰되어 시세 대비 안전마진 1.2억 확보. 5.1억 전후 입찰 시 전세 4.2억 셋팅(실투자 1억 초반) 또는 시세차익 실현 최적 물건."
}
with open(os.path.join(tmpl_dir, "property.json"), "w", encoding="utf-8") as tf:
    json.dump(tmpl_data, tf, ensure_ascii=False, indent=2)

readme_content = """# 새 경매 매물 추가 가이드
1. 본 `_template_new_property` 폴더를 복사하여 `[사건번호]_[물건명]`으로 폴더명을 변경합니다.
2. `property.json` 파일을 열어 해당 매물의 사건번호, 감정가, 최저가, 권리분석 내역을 수정합니다.
3. 현장 사진, 매각물건명세서 등 관련 서류 파일도 해당 폴더에 함께 보관합니다.
4. 터미널에서 `python scripts/build_master_v6.py`를 실행하면 대시보드와 계산기, 시뮬레이터에 새 매물이 2줄 카드로 즉시 자동 반영됩니다.
"""
with open(os.path.join(tmpl_dir, "README.md"), "w", encoding="utf-8") as rf:
    rf.write(readme_content)

print("[SUCCESS] data/items/ 독립 폴더 분리 및 _template_new_property 생성 완료!")
