# -*- coding: utf-8 -*-
"""
verify_v4.py
- V4 빌드 결과물(index_v4.html, index.html) 전수 검증
"""
import os

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"
target_file = os.path.join(base_dir, "index_v4.html")

print("[START] V4 검증 시작...")
assert os.path.exists(target_file), "index_v4.html 파일이 존재하지 않습니다."

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

checks = []

# 1. 파일 크기
size_kb = len(content.encode('utf-8')) / 1024
checks.append(("파일 크기 적합성 (> 200KB)", size_kb > 200, f"{size_kb:.1f} KB"))

# 2. 대시보드 사진 제거 검증
has_clean_cards = "renderCleanCards" in content
clean_cards_slice = content[content.find("function renderCleanCards"):content.find("function openPropertyModal")]
has_img_in_cards = "imageUrl" in clean_cards_slice or "<img" in clean_cards_slice
checks.append(("매물 카드 내 사진(이미지) 완전 제거", not has_img_in_cards, "이미지 태그 및 imageUrl 부재 확인"))

# 3. 좌측 상단 배지('적극추천', '추천') 제거 검증 (카드 렌더러 내부)
has_status_badge_in_cards = "statusBadgeClass" in clean_cards_slice or "${p.status}" in clean_cards_slice
checks.append(("매물 카드 좌측 상단 배지 제거", not has_status_badge_in_cards, "추천/적극추천 배지 부재 확인"))

# 4. 거시 매트릭스 비교 테이블 검증
has_macro_matrix = "macro-matrix-section" in content and "renderMacroMatrixTable" in content
checks.append(("거시 매물 횡적 비교 매트릭스 테이블 탑재", has_macro_matrix, "Macro Matrix 확인"))

# 5. 투자수익률 계산기 직접 입력창 및 슬라이더 연동
has_direct_price_input = 'id="priceInput"' in content and "handlePriceInputChange()" in content and "handlePriceSliderChange()" in content
checks.append(("취득 희망 매매가 직접 원단위 숫자 입력 연동", has_direct_price_input, "priceInput & 실시간 핸들러 확인"))

# 6. 투자수익률 계산기 경매 특화 패널
has_auction_calc_intel = all(tag in content for tag in [
    'id="calc-deposit-check"',
    'id="calc-auction-loan-limit"',
    'id="calc-auction-special-fees"',
    'id="calc-bid-ratio"'
])
checks.append(("투자수익률 계산기 경매 특화 인텔리전스 패널 (보증금10%, 경락대출, 특수비용)", has_auction_calc_intel, "경매 특화 4대 지표 확인"))

# 7. 경매 시뮬레이터 대출 0% 조건 및 역산 입찰가 계산기
has_zero_loan = 'id="btn-loan-none"' in content and "setLoanMode(" in content and 'id="rate-btn-0"' in content
has_reverse_bid = 'id="reverse-budget-input"' in content and "calculateReverseBid()" in content
checks.append(("경매 시뮬레이터 대출 0% (자부담 100%) 모드", has_zero_loan, "btn-loan-none & setLoanMode 확인"))
checks.append(("경매 시뮬레이터 역산 입찰가 계산기", has_reverse_bid, "reverse-budget-input 확인"))

# 8. 시장동향 리포트 화성 봉담 보고서 실시간 임베딩
has_report_embed = "오목천_봉담_통합_지역종합분석보고서.html" in content and "<iframe" in content
checks.append(("화성 봉담 시장동향 종합분석보고서 실시간 임베딩", has_report_embed, "아이프레임 전문 임베딩 확인"))

print("\n================ V4 검증 결과 리포트 ================")
all_pass = True
for name, passed, detail in checks:
    status = " PASS " if passed else "! FAIL !"
    print(f"[{status}] {name} : {detail}")
    if not passed:
        all_pass = False

print("=====================================================")
if all_pass:
    print(">>> 모든 V4 요구사항 검증을 100% 성공적으로 통과하였습니다! <<<")
else:
    print(">>> 일부 검증 실패가 발생하였습니다. <<<")
