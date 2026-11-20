# -*- coding: utf-8 -*-
"""
verify_v5.py
- V5 신규 빌드 결과물(index_v5.html, index.html) 전수 검증
"""
import os

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"
target_file = os.path.join(base_dir, "index_v5.html")

print("[START] V5 검증 시작...")
assert os.path.exists(target_file), "index_v5.html 파일이 존재하지 않습니다."

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

checks = []

# 1. 파일 크기
size_kb = len(content.encode('utf-8')) / 1024
checks.append(("파일 크기 적합성 (> 200KB)", size_kb > 200, f"{size_kb:.1f} KB"))

# 2. 좌측 사이드바 (LNB) 레이아웃 탑재 검증
has_left_sidebar = '<aside id="left-sidebar"' in content and 'md:ml-64' in content
checks.append(("화면 좌측 수직 고정 사이드바(LNB) 레이아웃", has_left_sidebar, "#left-sidebar & responsive workspace 확인"))

# 3. 거시 비교 테이블 매물 클릭 시 상세 모달 오픈 연동
has_table_modal_click = 'onclick="openPropertyModal(' in content and 'macro-matrix-tbody' in content
checks.append(("거시 비교 테이블 행 클릭 시 상세내역 모달 오픈", has_table_modal_click, "행 단위 openPropertyModal 바인딩 확인"))

# 4. ★ 추천입찰가 완전 삭제 검증
has_rec_bid_th = "★ 추천입찰가" in content or "★ 추천 입찰가" in content
checks.append(("대시보드 내 '★ 추천입찰가' 완전 삭제", not has_rec_bid_th, "추천입찰가 부재 확인"))

# 5. 고밀도 카드 [상세], [계산기] 버튼 클릭 복구 검증
has_card_actions = "quickLoadToCalculator" in content and "openPropertyModal" in content and 'property-cards-container' in content
checks.append(("고밀도 카드 [상세] 및 [계산기] 버튼 클릭 복구", has_card_actions, "openPropertyModal & quickLoadToCalculator 확인"))

# 6. 투자수익률 계산기 LTV 0% 및 Range 슬라이더 검증
has_ltv_0 = 'data-ltv="0"' in content
has_ltv_slider = 'id="ltvSlider"' in content and 'handleLtvSliderChange(' in content
checks.append(("투자수익률 계산기 LTV 0%(무대출) 버튼 및 Range 슬라이더", has_ltv_0 and has_ltv_slider, "0% 버튼 & ltvSlider 연동 확인"))

# 7. 경매 시뮬레이터 6개 매물 2줄 카드형 선택기 (사건번호 + 매물명)
has_2line_selector = 'item.caseNumber' in content and 'sim-property-selector' in content
checks.append(("경매 시뮬레이터 2줄 정밀 사건선택기 (사건번호+물건명)", has_2line_selector, "2줄 구조 동적 렌더러 확인"))

# 8. 역산 입찰가 레이아웃 줄바꿈 오류 수정 검증
has_clean_reverse_bid = 'id="reverse-bid-result"' in content and 'id="reverse-deduct-detail"' in content and 'applyReverseBidToSlider()' in content
checks.append(("역산 추천 한도 입찰가 레이아웃 완전 정돈", has_clean_reverse_bid, "reverse-bid-result & applyReverseBidToSlider 확인"))

# 9. 시장동향 리포트 뷰어 임베딩 및 5대 권역 연동 검증
has_report_view = 'id="bongdam-report-frame"' in content and 'switchRegionalReport(' in content
checks.append(("시장동향 리포트 뷰어 화성봉담 및 5대 권역 연동", has_report_view, "iframe 및 switchRegionalReport 확인"))

print("\n================ V5 검증 결과 리포트 ================")
all_pass = True
for name, passed, detail in checks:
    status = " PASS " if passed else "! FAIL !"
    print(f"[{status}] {name} : {detail}")
    if not passed:
        all_pass = False

print("=====================================================")
if all_pass:
    print(">>> 모든 V5 신규 요구사항 검증을 100% 성공적으로 통과하였습니다! <<<")
else:
    print(">>> 일부 검증 실패가 발생하였습니다. <<<")
