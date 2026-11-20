# -*- coding: utf-8 -*-
"""
verify_v2.py
- V2 통합 웹 애플리케이션의 4대 뷰 무결성, 실시간 연동 로직, 5대 권역 리포트 데이터 검증.
"""
import os, re, json

index_path = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

print("==================================================")
print("PropIntelligence V2 Master Application Verification")
print("==================================================")

# 1. 4대 메인 뷰 검증
views = ['view-dashboard', 'view-calculator', 'view-briefing', 'view-reports']
for v in views:
    assert f'id="{v}"' in content, f"Missing view: {v}"
    print(f"[PASS] Main View present: {v}")

# 2. 플레이스홀더 잔존 여부 확인
leftover_placeholders = re.findall(r'__[A-Z0-9_]+__', content)
assert len(leftover_placeholders) == 0, f"Leftover placeholders found: {leftover_placeholders}"
print("[PASS] Zero leftover template placeholders.")

# 3. 매물 데이터 (PROPERTIES) 검증
match_props = re.search(r'const PROPERTIES = (\[.*?\]);\s*\n\s*const REGIONAL_REPORTS', content, re.DOTALL)
assert match_props, "Could not extract PROPERTIES array"
props = json.loads(match_props.group(1))
assert len(props) == 6, f"Expected 6 properties, got {len(props)}"
print(f"[PASS] Embedded PROPERTIES parsed: {len(props)} real properties.")
for p in props:
    print(f"  - [{p['caseNumber']}] {p['propertyName']} -> 추천 {p['recommendedBidPrice']:,}원")

# 4. 02_지역분석자료 5대 권역 리포트 데이터 검증
match_reports = re.search(r'const REGIONAL_REPORTS = (\[.*?\]);\s*\n\s*let currentCategory', content, re.DOTALL)
assert match_reports, "Could not extract REGIONAL_REPORTS array"
reports = json.loads(match_reports.group(1))
assert len(reports) == 5, f"Expected 5 regional reports, got {len(reports)}"
print(f"[PASS] Embedded REGIONAL_REPORTS parsed: {len(reports)} regions.")
for r in reports:
    print(f"  - [{r['id']}] {r['name']} ({r['badge']}) - {len(r['contentMarkdown'])} chars")

# 5. 매물 대시보드 <-> 경매 분석 시뮬레이터 연동 검증
assert "loadPropertyToSimulator" in content, "Missing loadPropertyToSimulator function"
assert "renderDynamicSimulator" in content, "Missing renderDynamicSimulator function"
assert "runSimulatorEngine" in content, "Missing runSimulatorEngine function"
assert "id=\"sim-property-selector\"" in content, "Missing sim-property-selector element"
assert "id=\"sim-bid-slider\"" in content, "Missing sim-bid-slider element"
assert "id=\"sim-rate-slider\"" in content, "Missing sim-rate-slider element"
assert "id=\"sim-jeonse-slider\"" in content, "Missing sim-jeonse-slider element"
assert "id=\"public-doc-content\"" in content, "Missing public-doc-content element"
print("[PASS] Dashboard <-> Auction Simulator dynamic linkage engine fully present.")

# 6. 시장동향 리포트 뷰어 (02_지역분석자료) 5대 권역 탭 및 렌더러 검증
assert "switchRegionalReport" in content, "Missing switchRegionalReport function"
assert "renderMarkdownReport" in content, "Missing renderMarkdownReport function"
for reg in ['bongdam', 'anseong', 'pyeongtaek', 'cheonan', 'cheongju']:
    assert f'tab-reg-{reg}' in content, f"Missing regional tab: tab-reg-{reg}"
print("[PASS] 5 Regional tabs (bongdam, anseong, pyeongtaek, cheonan, cheongju) and Markdown parser present.")

print(f"\n[SUMMARY] index.html successfully verified! File size: {len(content):,} bytes")
print("==================================================")
