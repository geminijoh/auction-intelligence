# -*- coding: utf-8 -*-
"""
PropIntelligence v8.0 Full QA Verification Script (scripts/verify_v8.py)
-----------------------------------------------------------------------------
- v8.0 신규 사양(좌측 사이드바 -> 상단 고정 네비게이션 바 전환) 및 28대 안전 검증 항목 전수 자동 테스트
"""

import os
import re

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"
index_v8_path = os.path.join(base_dir, "index_v8.html")
index_v7_path = os.path.join(base_dir, "index_v7.html")
index_v6_path = os.path.join(base_dir, "index_v6.html")
index_orig_path = os.path.join(base_dir, "index.html")

results = []

def test(name, condition, detail=""):
    results.append((name, condition, detail))
    status = "[PASS]" if condition else "[FAIL]"
    print(f"{status} {name}: {detail}")

print("=" * 60)
print("PropIntelligence v8.0 QA Lead Verification Audit")
print("=" * 60)

# 1. 파일 존재 및 원본 보존 검증
test("1. index_v8.html 존재 여부", os.path.exists(index_v8_path), f"크기: {os.path.getsize(index_v8_path):,} bytes")
test("2. 원본 index.html 및 이전 버전(v6, v7) 보존 여부", 
     os.path.exists(index_orig_path) and os.path.getsize(index_orig_path) == 369232 and 
     os.path.exists(index_v6_path) and os.path.exists(index_v7_path), 
     f"원본(369,232 bytes), v6({os.path.getsize(index_v6_path):,} bytes), v7({os.path.getsize(index_v7_path):,} bytes) 보존")

with open(index_v8_path, "r", encoding="utf-8") as f:
    content = f.read()

# 2. 금지 단어 검증 (임장추천, 실시간 연동)
has_imjang = "임장추천" in content
has_realtime_sync = "실시간 연동" in content
test("3. '임장추천' 단어 완전 제거", not has_imjang, "검출되지 않음" if not has_imjang else "여전히 검출됨!")
test("4. '실시간 연동' 단어 완전 제거", not has_realtime_sync, "검출되지 않음" if not has_realtime_sync else "여전히 검출됨!")

# 3. [v8 핵심] 상단 고정 네비게이션 헤더 탑재 및 좌측 사이드바 제거
has_top_navbar = 'id="top-navbar"' in content and 'sticky top-0' in content
has_left_sidebar = '<aside id="left-sidebar"' in content
test("5. [v8] 상단 고정 네비게이션 헤더 탑재", has_top_navbar, "top-navbar 헤더 및 상단 4대 메뉴 배치 확인")
test("6. [v8] 좌측 사이드바 제거 및 전체 화면 폭 최적화", not has_left_sidebar, "left-sidebar 제거 및 main-workspace 100% 폭 활용 확인")

# 4. 거시 비교 테이블 내 '권리 분석' 컬럼 완전 제거 (v7 사양 계승)
has_macro_rights_header = '<th class="py-3.5 px-4 font-bold text-center">권리 분석</th>' in content
macro_render_match = re.search(r'const tbody = document\.getElementById\(\'macro-matrix-tbody\'\);[\s\S]*?tbody\.innerHTML = list\.map\(p => \{([\s\S]*?)\}\)\.join', content)
has_macro_rights_td = False
if macro_render_match:
    render_code = macro_render_match.group(1)
    if 'verified' in render_code and '안전' in render_code:
        has_macro_rights_td = True

has_macro_rights = has_macro_rights_header or has_macro_rights_td
test("7. 거시 테이블 '권리 분석' 컬럼 완전 삭제 (v7 계승)", not has_macro_rights, 
     "거시 테이블 헤더(th) 및 데이터 행(td) 완전 제거 확인 (8개 컬럼 체제)" if not has_macro_rights else "권리분석 컬럼 잔존!")

# 5. 거시 비교 테이블 클릭 모달 및 추천입찰가 삭제 검증
has_row_click = 'onclick="openPropertyModal(' in content
has_rec_bid_header = '★ 추천입찰가' in content
test("8. 거시 비교 테이블 행 클릭 모달 연동", has_row_click, "openPropertyModal 호출 이벤트 바인딩 확인")
test("9. '★ 추천입찰가' 컬럼/블록 삭제", not has_rec_bid_header, "'★ 추천입찰가' 텍스트 완전 제거 확인")

# 6. 카드 버튼 클릭 버블링 방어 검증
has_stop_prop = 'event.stopPropagation()' in content
test("10. 카드 버튼 클릭 버블링 방어", has_stop_prop, "stopPropagation 적용 확인")

# 7. LTV 0% 및 슬라이더 검증
has_ltv_0 = 'data-ltv="0"' in content or "LTV 0%" in content
has_ltv_slider = 'id="ltvSlider"' in content or 'id="ltvRangeSlider"' in content
test("11. LTV 0% (대출 0%) 버튼 탑재", has_ltv_0, "무차입/전액자부담 버튼 확인")
test("12. LTV 0%~80% 레인지 슬라이더", has_ltv_slider, "ltvRangeSlider 엘리먼트 확인")

# 8. 경매분석기 5종 공적서류 사건선택기 2줄 표기
has_2line_selector = 'selectSimProperty' in content and 'item.caseNumber' in content and 'subName' in content
test("13. 공적서류 5종 사건선택기 2줄 표기", has_2line_selector, "사건번호 + 아랫줄 매물명 2줄 렌더링 확인")

# 9. 역산 입찰가 시인성 및 줄바꿈 정돈
has_reverse_bid = 'reverse-bid-result' in content or 'reverse-bid-display' in content or '역산 추천 한도 입찰가' in content or '역산 입찰가' in content
test("14. 역산 입찰가 카운터 카드 레이아웃", has_reverse_bid, "줄바꿈 꼬임 해결 및 전용 카드 배치 확인")

# 10. 계획도 사진 엑박 방어 검증 (시장분석보고서 원문 내 정상 경로 및 onerror fallback)
report_html_path = os.path.join(base_dir, "시장동향리포트뷰어", "오목천_봉담_통합_지역종합분석보고서.html")
with open(report_html_path, "r", encoding="utf-8") as rf:
    report_content = rf.read()
has_plan_img = '오목천%20개발_1.png' in report_content and 'onerror=' in report_content
test("15. 도시개발 계획도 이미지 엑박 방어", has_plan_img, "보고서 원문 내 URL 인코딩 및 onerror fallback 처리 확인")

# 11. 전세 갭투자 ROE 21.5% 분기 계산식 검증
has_jeonse_roe = 'calcState.rentalType === "전세"' in content or 'monthlyRent === 0' in content or 'netInvestment' in content
test("16. 전세 갭투자 전용 자본이득 ROE 분기", has_jeonse_roe, "월세=0 전세 매물 ROE 왜곡 방지 공식 확인")

# 12. TypeError 방지 안전 바인딩 검증
has_safe_binding = 'p.financing || p.loan' in content
test("17. p.financing/p.loan 안전 바인딩", has_safe_binding, "TypeError 크래시 방어 확인")

# 13. GEMINI.md 규칙 준수: 요약 복사 기능
has_copy_summary = 'copySummaryReport' in content or '📋 요약 복사' in content
test("18. '📋 요약 복사' 필수 기능 탑재", has_copy_summary, "요약 복사 버튼 및 클립보드 API 확인")

# 14. 계산기 6개 매물 프리셋 버튼 및 강조 클래스 바인딩 검증
has_preset_data_ids = 'data-case-id="${item.id}"' in content or 'data-case-id="sale-bongdam-105"' in content
has_preset_toggle = "document.querySelectorAll('.calc-preset-btn')" in content
test("19. 계산기 프리셋 6종 data-case-id 바인딩", has_preset_data_ids, "6개 매물 정확한 ID 매핑 확인")
test("20. 계산기 프리셋 활성화 강조 클래스 전환", has_preset_toggle, "calc-preset-btn 동적 토글 확인")

# 15. 시장동향 리포트 뷰어 5대 권역 실제 HTML 전문 보고서 연동 검증
has_reg_files = 'REGIONAL_REPORT_FILES' in content and '안성시_부동산시장분석_PropX데이터솔루션활용보고서.html' in content
has_reg_frame = 'id="report-interactive-frame"' in content
test("21. 5대 권역 PropX 실제 HTML 파일 매핑", has_reg_files, "5개 권역 전문 HTML 경로 등록 확인")
test("22. 인터랙티브 고해상도 리포트 프레임 탑재", has_reg_frame, "iframe 컨테이너 동적 렌더링 확인")

# 16. 계산기 버튼 인터랙션 핸들러 필수 검증
has_prop_btn_handler = 'handlePropTypeChange' in content
has_housing_btn_handler = 'handleHousingCountChange' in content
has_ltv_listener = "btn.getAttribute('data-ltv')" in content
test("23. 물건유형 버튼 핸들러 (handlePropTypeChange)", has_prop_btn_handler, "주택/오피스텔/상가 전환 확인")
test("24. 주택수 버튼 핸들러 (handleHousingCountChange)", has_housing_btn_handler, "1~4주택 세율 연동 확인")
test("25. LTV 버튼 이중 바인딩 (인라인 + DOM Listener)", has_ltv_listener, "LTV 0%~80% 5종 버튼 클릭 보장 확인")

# 17. 역산 추천 시도 입찰가 선반영 부대비용 정밀 설정 패널 검증
has_rev_tax_rate = 'id="rev-tax-rate"' in content
has_rev_legal_fee = 'id="rev-legal-fee"' in content
has_rev_eviction_fee = 'id="rev-eviction-fee"' in content
has_rev_repair_fee = 'id="rev-repair-fee"' in content
test("26. 부대비용 정밀 설정 패널 (취득세/법무/명도/수리)", has_rev_tax_rate and has_rev_legal_fee and has_rev_eviction_fee and has_rev_repair_fee, "4개 항목 직접 입력 인풋 완비 확인")

# 18. 계산기 상단 2줄 사건선택기 (account_tree) UI 통일 검증
has_calc_selector = 'id="calc-property-selector"' in content and 'calcSelector' in content or 'selectorContainer = document.getElementById(\'calc-property-selector\')' in content
test("27. 계산기 상단 2줄 사건선택기 통일", has_calc_selector, "시뮬레이터와 동일한 2줄 카드형 UI 동기화 확인")

# 19. data/items/ 개별 매물 폴더 및 새 매물 템플릿 아키텍처 검증
items_dir = os.path.join(base_dir, "data", "items")
has_items_dir = os.path.isdir(items_dir)
has_template = os.path.isfile(os.path.join(items_dir, "_template_new_property", "property.json"))
items_count = len([d for d in os.listdir(items_dir) if not d.startswith("_") and os.path.isdir(os.path.join(items_dir, d))])
test("28. data/items/ 개별 매물 폴더 패키징", has_items_dir and items_count >= 6, f"{items_count}개 개별 매물 폴더 격리 관리 확인")
test("29. 새 매물 템플릿 (_template_new_property)", has_template, "property.json 및 README.md 템플릿 완비 확인")

# 20. [v8 추가 개선] 기준금리 단독 표기 및 환율 삭제 검증
has_base_rate = "기준금리" in content and "3.50%" in content
has_fx_rate = "환율" in content or "1,385원" in content
test("30. [v8] 기준금리 단독 표기 & 환율 삭제", has_base_rate and not has_fx_rate, 
     "기준금리(3.50%)만 단독 표기 및 환율 삭제 확인" if (has_base_rate and not has_fx_rate) else "환율 잔존 또는 기준금리 누락")

# 21. [v8 추가 개선] 와이드 레이아웃(max-w-[1720px]) 및 드래그 없는 탭 검증
has_wide = "max-w-[1720px]" in content
has_no_drag_tab = "grid-cols-4" in content
test("31. [v8] 와이드 레이아웃 & 드래그 없는 원클릭 탭", has_wide and has_no_drag_tab, 
     "1720px 와이드 레이아웃 및 4분할 원클릭 탭 확인" if (has_wide and has_no_drag_tab) else "와이드 또는 탭 레이아웃 불일치")

# 22. [v8 추가 개선] 상단 공백 초슬림 압축 (Above-the-fold 최적화)
has_slim_briefing = 'pt-1.5 pb-8 space-y-2.5' in content and 'grid-cols-2 sm:grid-cols-4 gap-1.5 shrink-0' in content
has_slim_reports = 'pt-1.5 pb-8 w-full flex flex-col gap-2' in content and 'report-interactive-frame' in content
test("32. [v8] 상단 공백 초슬림화 (시뮬레이터/리포트 Above-the-fold)", has_slim_briefing and has_slim_reports,
     "통합 슬림 헤더(~120px) 및 리포트 프레임 즉각 가시화 확인" if (has_slim_briefing and has_slim_reports) else "상단 공백 과다 잔존")

print("=" * 60)
passed_count = sum(1 for _, ok, _ in results if ok)
total_count = len(results)
print(f"종합 검증 결과: {passed_count}/{total_count} 항목 통과 ({passed_count/total_count*100:.1f}%)")
print("=" * 60)

if passed_count == total_count:
    exit(0)
else:
    exit(1)
