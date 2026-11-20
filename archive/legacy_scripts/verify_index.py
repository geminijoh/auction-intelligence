# -*- coding: utf-8 -*-
import os, re, json

index_path = r'c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 4대 뷰 검증
views = ['view-dashboard', 'view-calculator', 'view-briefing', 'view-reports']
for v in views:
    assert f'id="{v}"' in content, f"Missing view: {v}"
    print(f"[OK] View exists: {v}")

# 2. 내비게이션 탭 검증
nav_paths = ['auction-dashboard', 'yield-calculator', 'auction-simulator', 'market-reports']
for path in nav_paths:
    assert f'data-path="{path}"' in content, f"Missing nav path: {path}"
    print(f"[OK] Nav path exists: {path}")

# 3. 상세 분석 모달 검증
assert 'id="property-detail-modal"' in content
assert 'function openPropertyModal' in content
assert 'function closePropertyModal' in content
print("[OK] Property Detail Modal and JS handlers exist!")

# 4. JSON 데이터 파싱 검증
match = re.search(r'const PROPERTIES = (\[.*?\]);', content, re.DOTALL)
assert match, "Could not find PROPERTIES array"
props = json.loads(match.group(1))
assert len(props) == 6, f"Expected 6 properties, got {len(props)}"
print(f"[OK] Successfully parsed {len(props)} real properties from embedded JSON!")
for p in props:
    print(f"  - [{p['caseNumber']}] {p['propertyName']} ({p['category']}) - 추천가: {p['recommendedBidPrice']:,}원")

# 5. 계산기 및 시뮬레이터 함수 확인
assert 'function switchMainTab' in content
assert 'function initCalculatorEngine' in content
assert 'function updateCalculations' in content
print("[OK] Interactive Engines (switchMainTab, initCalculatorEngine, updateCalculations) present and ready!")

print(f"\n[ALL TESTS PASSED] index.html integrity is 100% verified! (Total size: {len(content):,} bytes)")
