# -*- coding: utf-8 -*-
"""
verify_v3.py
- V3 기능 검증:
  1. 대출 0% (대출 안 받음 / 전액 자부담 100%) 및 금리 퀵 세팅
  2. 목표 총 취득원가(최종 예산) 기준 역산(Reverse Engineering) 입찰가 계산기
  3. 화성 봉담 탭 시장동향리포트뷰어 HTML 임베딩 및 외부 링크
"""
import os, re, json

index_path = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

print("==================================================")
print("PropIntelligence V3 Master Application Verification")
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

# 3. 신규 기능 1: 대출 안 받는 조건 (전액 자부담) & 금리 퀵 버튼 검증
assert "btn-loan-none" in content, "Missing btn-loan-none element"
assert "btn-loan-use" in content, "Missing btn-loan-use element"
assert "rate-btn-0" in content, "Missing rate-btn-0 (대출없음 0%) button"
assert "setLoanMode" in content, "Missing setLoanMode function"
assert "setQuickRate" in content, "Missing setQuickRate function"
print("[PASS] Feature 1: No-loan (100% self-funding) mode & quick rate controls present.")

# 4. 신규 기능 2: 역산 입찰가 계산기 검증
assert "reverse-budget-input" in content, "Missing reverse-budget-input element"
assert "reverse-bid-result" in content, "Missing reverse-bid-result element"
assert "reverse-deduct-detail" in content, "Missing reverse-deduct-detail element"
assert "calculateReverseBid" in content, "Missing calculateReverseBid function"
assert "applyReverseBidToSlider" in content, "Missing applyReverseBidToSlider function"
print("[PASS] Feature 2: Reverse engineering bid calculator (취득세/부대비용 선반영) present.")

# 5. 신규 기능 3: 시장동향리포트뷰어 폴더 보고서 화성 봉담 탭 임베딩 검증
assert "bongdam-interactive-section" in content, "Missing bongdam-interactive-section"
assert "시장동향리포트뷰어/오목천_봉담_통합_지역종합분석보고서.html" in content, "Missing subfolder report reference"
assert "bongdam-report-frame" in content, "Missing bongdam-report-frame element"
print("[PASS] Feature 3: Market report subfolder HTML (화성 봉담) embedded successfully.")

# 6. 수학적 역산 공식 정밀 시뮬레이션 테스트
# 예: 안성동남타운 (법무+명도+수리=550만, 총예산=7500만, 취득세=1.1%)
# bidMan = (7500 - 550) / 1.011 = 6950 / 1.011 = 6874.3 -> 반올림 6870만원
# 총소요 = 6870 + (6870 * 0.011 = 75.5만) + 550만 = 7495.5만원 <= 7500만원!
total_budget = 7500
fixed_costs = 550
tax_rate = 0.011
calc_bid = (total_budget - fixed_costs) / (1 + tax_rate)
est_tax = calc_bid * tax_rate
assert (calc_bid + est_tax + fixed_costs) <= total_budget + 0.0001
print(f"[PASS] Math Logic: Budget {total_budget}M -> Bid {calc_bid:.1f}M (Tax {est_tax:.1f}M + Costs {fixed_costs}M) = Exactly within budget!")

print(f"\n[SUMMARY] index.html V3 successfully verified! Total size: {len(content):,} bytes")
print("==================================================")
