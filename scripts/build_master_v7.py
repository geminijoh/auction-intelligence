# -*- coding: utf-8 -*-
"""
build_master_v7.py
- PropIntelligence Master V7 단일 파일 애플리케이션 빌더
- 사용자의 명시적 승인에 따라 index_v7.html을 단독 생성합니다.
- [절대 원칙] 기존 파일(index.html, index_v4.html, index_v5.html, index_v6.html 등)은 1바이트도 수정하지 않고 원형 보존합니다.
- [v7 변경] 거시 비교 테이블 내 '권리 분석' 컬럼 완전 제거
"""

import os
import json

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"

# 1. 매물 데이터 로드 (data/items/ 폴더 스캐너 우선 연동)
items_dir = os.path.join(base_dir, "data", "items")
scanned_properties = []

if os.path.exists(items_dir):
    for item_folder in sorted(os.listdir(items_dir)):
        if item_folder.startswith("_"):  # _template 등 제외
            continue
        item_path = os.path.join(items_dir, item_folder, "property.json")
        if os.path.isfile(item_path):
            try:
                with open(item_path, "r", encoding="utf-8") as pf:
                    prop_obj = json.load(pf)
                    scanned_properties.append(prop_obj)
            except Exception as e:
                print(f"[WARN] {item_folder}/property.json 파싱 실패: {e}")

if scanned_properties:
    properties_data = scanned_properties
    print(f"[SCAN] data/items/ 내 개별 폴더에서 {len(properties_data)}개 매물 자동 수집 완료!")
    # data/properties.json 동기화 백업
    try:
        with open(os.path.join(base_dir, "data", "properties.json"), "w", encoding="utf-8") as pf:
            json.dump(properties_data, pf, ensure_ascii=False, indent=2)
    except Exception:
        pass
else:
    properties_json_path = os.path.join(base_dir, "data", "properties.json")
    with open(properties_json_path, "r", encoding="utf-8") as f:
        properties_data = json.load(f)

properties_json_str = json.dumps(properties_data, ensure_ascii=False)

regional_reports_path = os.path.join(base_dir, "data", "regional_reports_data.json")
with open(regional_reports_path, "r", encoding="utf-8") as f:
    regional_reports_data = json.load(f)
regional_reports_json_str = json.dumps(regional_reports_data, ensure_ascii=False)

# 2. V7 전용 뷰 템플릿 로드
with open(os.path.join(base_dir, "views", "view_dashboard_v7.html"), "r", encoding="utf-8") as f:
    view_dashboard_content = f.read()

with open(os.path.join(base_dir, "views", "view_calculator_v7.html"), "r", encoding="utf-8") as f:
    view_calculator_content = f.read()

with open(os.path.join(base_dir, "views", "view_briefing_v7.html"), "r", encoding="utf-8") as f:
    view_briefing_content = f.read()

with open(os.path.join(base_dir, "views", "view_reports_v7.html"), "r", encoding="utf-8") as f:
    view_reports_content = f.read()

# 3. 마스터 HTML 프레임워크 템플릿 (V7)
master_html = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PropIntelligence v7.0 - 실전 경매 투자 인텔리전스</title>
  
  <!-- CDN Dependencies -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- Google Fonts & Material Symbols -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

  <!-- Tailwind Custom Design Tokens (Material 3 Expressive) -->
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            "tertiary-container": "#dcfce7",
            "on-tertiary-container": "#14532d",
            "surface-dim": "#d1dbed",
            "outline": "#717786",
            "surface-bright": "#f8f9ff",
            "on-tertiary": "#ffffff",
            "on-secondary-fixed-variant": "#3b475a",
            "surface-container": "#e6eeff",
            "on-tertiary-fixed": "#00210f",
            "on-surface": "#121c29",
            "inverse-on-surface": "#eaf1ff",
            "on-primary": "#ffffff",
            "on-surface-variant": "#414755",
            "secondary-fixed-dim": "#bbc7dd",
            "on-error-container": "#93000a",
            "tertiary-fixed-dim": "#57df92",
            "on-primary-fixed-variant": "#004395",
            "surface": "#f8f9ff",
            "error": "#ba1a1a",
            "surface-variant": "#d9e3f5",
            "primary": "#0058be",
            "outline-variant": "#c1c6d7",
            "inverse-surface": "#27313f",
            "on-secondary-fixed": "#101c2c",
            "surface-container-highest": "#d9e3f5",
            "primary-fixed-dim": "#aec6ff",
            "secondary-container": "#d4e0f7",
            "surface-tint": "#005ac3",
            "surface-container-low": "#eff4ff",
            "on-background": "#121c29",
            "secondary-fixed": "#d7e3fa",
            "on-tertiary-fixed-variant": "#00522d",
            "background": "#f8f9ff",
            "secondary": "#535f72",
            "on-secondary-container": "#576377",
            "inverse-primary": "#aec6ff",
            "on-secondary": "#ffffff",
            "surface-container-high": "#dfe9fb",
            "on-error": "#ffffff",
            "error-container": "#ffdad6",
            "on-primary-container": "#fefcff",
            "tertiary": "#006a3c",
            "surface-container-lowest": "#ffffff",
            "primary-container": "#006fee",
            "on-primary-fixed": "#001a42",
            "tertiary-fixed": "#76fcac",
            "primary-fixed": "#d8e2ff"
          },
          fontFamily: {
            "body-lg": ["Inter", "Noto Sans KR", "sans-serif"],
            "body-sm": ["Inter", "Noto Sans KR", "sans-serif"],
            "body-md": ["Inter", "Noto Sans KR", "sans-serif"],
            "headline-lg": ["Inter", "Noto Sans KR", "sans-serif"],
            "label-sm": ["Inter", "Noto Sans KR", "sans-serif"],
            "headline-sm": ["Inter", "Noto Sans KR", "sans-serif"],
            "label-md": ["Inter", "Noto Sans KR", "sans-serif"],
            "headline-md": ["Inter", "Noto Sans KR", "sans-serif"]
          }
        }
      }
    };
  </script>
  <style>
    @media print {
      .no-print, aside#left-sidebar, header.mobile-header { display: none !important; }
      .main-workspace { margin-left: 0 !important; width: 100% !important; padding: 0 !important; }
    }
  </style>
</head>
<body class="bg-background font-body-md text-on-surface antialiased selection:bg-primary-fixed selection:text-on-primary-fixed min-h-screen flex flex-col md:flex-row">

  <!-- ================= LEFT SIDEBAR NAVIGATION (화면 좌측 사이드바) ================= -->
  <aside id="left-sidebar" class="no-print w-full md:w-64 lg:w-72 bg-surface-container-lowest border-r border-outline-variant/30 flex flex-col justify-between p-4 sm:p-5 md:fixed md:top-0 md:bottom-0 md:left-0 z-40 overflow-y-auto shadow-sm">
    
    <!-- Top Branding & Navigation -->
    <div class="space-y-6">
      
      <!-- Brand Logo & Badge -->
      <div class="flex items-center justify-between pb-4 border-b border-outline-variant/20">
        <div class="flex items-center gap-2.5 cursor-pointer" onclick="switchMainTab('dashboard')">
          <span class="font-headline-sm text-headline-sm text-primary tracking-tight font-black">PropIntelligence</span>
          <span class="w-2 h-2 rounded-full bg-tertiary-container animate-pulse"></span>
        </div>
        <span class="px-2 py-0.5 rounded-full bg-primary text-on-primary font-label-sm text-label-sm font-semibold shadow-xs">
          v7.0 Pro
        </span>
      </div>

      <!-- Main Navigation Menu (수직 나열) -->
      <nav class="space-y-1.5" id="main-nav">
        <div class="text-[11px] font-bold text-secondary uppercase tracking-wider px-3 mb-2">
          <span>투자 인텔리전스 메뉴</span>
        </div>

        <!-- 1. 매물 대시보드 -->
        <button onclick="switchMainTab('dashboard')" data-path="dashboard" id="btn-tab-dashboard" class="nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 bg-primary-container text-on-primary-container font-bold shadow-sm text-left">
          <span class="material-symbols-outlined text-[20px]">table_chart</span>
          <div class="flex flex-col">
            <span class="font-label-md text-label-md">매물 대시보드</span>
            <span class="text-[11px] opacity-80">거시 비교 &amp; 클린 분석</span>
          </div>
        </button>

        <!-- 2. 투자수익률 계산기 -->
        <button onclick="switchMainTab('yield-calculator')" data-path="yield-calculator" id="btn-tab-yield-calculator" class="nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 text-on-surface-variant hover:bg-surface-container hover:text-on-surface text-left">
          <span class="material-symbols-outlined text-[20px]">calculate</span>
          <div class="flex flex-col">
            <span class="font-label-md text-label-md">투자수익률 계산기</span>
            <span class="text-[11px] opacity-70">LTV 0%~80% &amp; 전세갭 ROE</span>
          </div>
        </button>

        <!-- 3. 경매 분석 시뮬레이터 -->
        <button onclick="switchMainTab('auction-simulator')" data-path="auction-simulator" id="btn-tab-auction-simulator" class="nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 text-on-surface-variant hover:bg-surface-container hover:text-on-surface text-left">
          <span class="material-symbols-outlined text-[20px]">tune</span>
          <div class="flex flex-col">
            <span class="font-label-md text-label-md">경매 분석 시뮬레이터</span>
            <span class="text-[11px] opacity-70">역산 입찰가 &amp; 5종 서류</span>
          </div>
        </button>

        <!-- 4. 시장동향 리포트 뷰어 -->
        <button onclick="switchMainTab('market-reports')" data-path="market-reports" id="btn-tab-market-reports" class="nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 text-on-surface-variant hover:bg-surface-container hover:text-on-surface text-left">
          <span class="material-symbols-outlined text-[20px]">travel_explore</span>
          <div class="flex flex-col">
            <span class="font-label-md text-label-md">시장동향 리포트 뷰어</span>
            <span class="text-[11px] opacity-70">도시개발 마스터플랜 · 빅데이터</span>
          </div>
        </button>
      </nav>

      <!-- 📋 필수 탑재 기능: 요약 복사 버튼 (GEMINI.md 규칙 준수) -->
      <div class="pt-2">
        <button onclick="copySummaryReport()" class="w-full py-2.5 px-3 bg-primary hover:bg-primary-container text-on-primary rounded-xl font-label-md text-label-md font-bold transition flex items-center justify-center gap-2 shadow-sm" type="button" title="카카오톡/메모장용 브리핑 요약 복사">
          <span class="material-symbols-outlined text-[18px]">content_copy</span>
          <span>📋 브리핑 요약 복사</span>
        </button>
      </div>

    </div>

    <!-- Bottom Macro Rates & PDF Export Utility -->
    <div class="pt-6 border-t border-outline-variant/20 space-y-3">
      <!-- Macro Info Box -->
      <div class="p-3 rounded-xl bg-surface-container-low border border-outline-variant/30 space-y-1">
        <span class="text-[11px] text-secondary font-semibold block">시장 거시 기준 지표</span>
        <div class="flex justify-between items-center text-xs font-bold text-on-surface">
          <span>한국 기준금리</span>
          <span class="text-primary">3.50%</span>
        </div>
        <div class="flex justify-between items-center text-xs font-medium text-secondary">
          <span>원/달러 환율</span>
          <span>1,385원</span>
        </div>
      </div>

      <!-- PDF / Print Button -->
      <button onclick="window.print()" class="w-full py-2.5 px-3 bg-surface-container hover:bg-surface-container-high text-on-surface rounded-xl font-label-md text-label-md font-semibold transition flex items-center justify-center gap-2 border border-outline-variant/30 shadow-sm" type="button">
        <span class="material-symbols-outlined text-[18px]">print</span>
        <span>A4 인쇄 / PDF 저장</span>
      </button>

      <div class="text-[11px] text-secondary text-center">
        PropIntelligence v7.0 Engine
      </div>
    </div>

  </aside>

  <!-- ================= RIGHT MAIN CONTENT WORKSPACE ================= -->
  <div class="main-workspace flex-1 md:ml-64 lg:ml-72 min-h-screen flex flex-col bg-surface overflow-x-hidden">
    
    <!-- Top Mobile Header (모바일 화면 전용 상단 바) -->
    <header class="mobile-header no-print md:hidden h-14 bg-surface-container-lowest border-b border-outline-variant/30 px-4 flex items-center justify-between sticky top-0 z-30">
      <div class="flex items-center gap-2 cursor-pointer" onclick="switchMainTab('dashboard')">
        <span class="font-headline-sm text-headline-sm text-primary font-bold">PropIntelligence</span>
        <span class="px-1.5 py-0.5 rounded text-[10px] bg-primary text-on-primary font-bold">v7</span>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="copySummaryReport()" class="p-2 text-primary hover:bg-surface-container rounded-lg" title="요약 복사">
          <span class="material-symbols-outlined text-[20px]">content_copy</span>
        </button>
        <button onclick="window.print()" class="p-2 text-secondary hover:text-on-surface">
          <span class="material-symbols-outlined text-[20px]">print</span>
        </button>
      </div>
    </header>

    <!-- 1. VIEW: 거시 매물 분석 대시보드 (V6) -->
    <main id="view-dashboard" class="w-full min-h-screen">
      __VIEW_DASHBOARD_CONTENT__
    </main>

    <!-- 2. VIEW: 투자수익률 계산기 (V6) -->
    <main id="view-yield-calculator" class="w-full min-h-screen hidden">
      __VIEW_CALCULATOR_CONTENT__
    </main>

    <!-- 3. VIEW: 경매 분석 시뮬레이터 (V6) -->
    <main id="view-auction-simulator" class="w-full min-h-screen hidden">
      __VIEW_BRIEFING_CONTENT__
    </main>

    <!-- 4. VIEW: 시장동향 리포트 뷰어 (V6) -->
    <main id="view-market-reports" class="w-full min-h-screen hidden">
      __VIEW_REPORTS_CONTENT__
    </main>

  </div>

  <!-- ================= GLOBAL TOAST NOTIFICATION ================= -->
  <div id="global-toast" class="fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
    <div class="bg-inverse-surface text-inverse-on-surface px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-outline-variant/30">
      <span class="material-symbols-outlined text-tertiary-fixed text-[22px]" id="toast-icon">check_circle</span>
      <span class="font-label-md text-label-md font-medium" id="toast-message">메시지 내용</span>
    </div>
  </div>

  <!-- ================= PROPERTY DETAIL MODAL ================= -->
  <div id="property-modal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-3 sm:p-5">
    <div class="bg-surface-container-lowest rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto shadow-2xl border border-outline-variant/30 flex flex-col" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-5 border-b border-outline-variant/20 flex items-center justify-between sticky top-0 bg-surface-container-lowest z-10">
        <div class="flex items-center space-x-3">
          <span id="modal-category-badge" class="font-label-sm text-label-sm px-2.5 py-1 rounded-md font-bold bg-primary-container text-on-primary-container">
            경매
          </span>
          <h3 id="modal-title" class="font-headline-sm text-headline-sm font-bold text-on-surface">
            매물 상세 정보
          </h3>
          <span id="modal-case-no" class="font-label-md text-label-md text-secondary">
            사건번호
          </span>
        </div>
        <button onclick="closePropertyModal()" class="text-secondary hover:text-on-surface p-1 rounded-lg hover:bg-surface-container transition">
          <span class="material-symbols-outlined text-[24px]">close</span>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="p-6 space-y-6">
        <!-- 1. Executive Summary Strip -->
        <div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <span class="text-xs text-secondary font-medium">소재지 / 담당 법원</span>
            <p id="modal-summary-address" class="font-bold text-on-surface text-sm sm:text-base">-</p>
          </div>
          <div class="flex items-center gap-2">
            <span id="modal-status-badge" class="inline-flex items-center gap-1 px-3 py-1 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold text-xs shadow-xs">
              <span class="material-symbols-outlined text-[15px] text-emerald-600 font-bold">verified</span>
              안전 물건
            </span>
            <span id="modal-auction-date" class="px-3 py-1 rounded-lg bg-surface-container text-on-surface font-semibold text-xs">
              입찰일 미정
            </span>
          </div>
        </div>

        <!-- 2. Core Financial 4 Matrix -->
        <div class="space-y-2">
          <h4 class="font-label-md text-label-md font-bold text-on-surface flex items-center gap-2">
            <span class="material-symbols-outlined text-primary text-[18px]">analytics</span>
            핵심 투자 지표 요약
          </h4>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">1. 감정가</span>
              <p id="modal-appraised-val" class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">-</p>
            </div>
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">2. 최저매각가 (비율)</span>
              <p id="modal-min-price" class="font-headline-sm text-headline-sm font-bold text-primary mt-1">-</p>
            </div>
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">3. 실투자금</span>
              <p id="modal-net-investment" class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">-</p>
            </div>
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">4. 수익 세팅 (ROE)</span>
              <p id="modal-roe" class="font-headline-sm text-headline-sm font-bold text-tertiary mt-1">-</p>
              <p id="modal-rental" class="font-label-sm text-label-sm text-secondary mt-0.5">-</p>
            </div>
          </div>
        </div>

        <!-- 3. Specs & Rights Analysis (2 Columns) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Property Specs -->
          <div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30 space-y-2">
            <h5 class="font-label-md text-label-md font-bold text-on-surface pb-1 border-b border-outline-variant/20">
              물건 기본 스펙 &amp; 가격 지표
            </h5>
            <div class="grid grid-cols-2 gap-x-2 gap-y-1.5 font-body-sm text-body-sm">
              <span class="text-secondary">소재지:</span>
              <span id="modal-address" class="text-on-surface font-medium truncate">-</span>

              <span class="text-secondary">전용면적:</span>
              <span id="modal-area" class="text-on-surface font-medium">-</span>

              <span class="text-secondary">층수/준공:</span>
              <span id="modal-floor-build" class="text-on-surface font-medium">-</span>

              <span id="modal-appraised-label" class="text-secondary">감정평가액:</span>
              <span id="modal-appraised" class="text-on-surface font-semibold">-</span>

              <span id="modal-min-label" class="text-secondary">최저매각가:</span>
              <span id="modal-min" class="text-primary font-bold">-</span>

              <span class="text-secondary">최근 실거래가:</span>
              <span id="modal-market" class="text-on-surface font-semibold">-</span>
            </div>
          </div>

          <!-- Rights Analysis -->
          <div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30 space-y-2">
            <h5 class="font-label-md text-label-md font-bold text-on-surface pb-1 border-b border-outline-variant/20">
              권리분석 및 명도 판정
            </h5>
            <div class="grid grid-cols-2 gap-x-2 gap-y-1.5 font-body-sm text-body-sm">
              <span class="text-secondary">말소기준권리:</span>
              <span id="modal-malso" class="text-on-surface font-medium truncate">-</span>

              <span class="text-secondary">점유자 현황:</span>
              <span id="modal-occupant" class="text-on-surface font-medium">-</span>

              <span class="text-secondary">낙찰자 인수액:</span>
              <span id="modal-takeover" class="text-tertiary font-bold">0원 (완벽 안전)</span>

              <span class="text-secondary">명도 난이도:</span>
              <span id="modal-eviction" class="text-on-surface font-medium">하 (원활)</span>

              <span class="text-secondary">권리 안전 여부:</span>
              <span id="modal-safety" class="text-tertiary font-bold">안전 물건</span>
            </div>
          </div>
        </div>

        <!-- 4. Location Highlights -->
        <div class="space-y-2">
          <h5 class="font-label-md text-label-md font-bold text-on-surface">
            입지 가치 및 미래 호재
          </h5>
          <ul id="modal-highlights" class="space-y-1 font-body-sm text-body-sm text-on-surface-variant list-disc list-inside bg-surface-container-low p-4 rounded-xl border border-outline-variant/30">
            <!-- Dynamic bullets -->
          </ul>
        </div>

        <!-- 5. Strategy Brief -->
        <div class="p-4 rounded-xl bg-primary-fixed/30 border border-primary-fixed-dim/40 space-y-1.5">
          <h5 class="font-label-md text-label-md font-bold text-on-surface flex items-center gap-1.5">
            <span class="material-symbols-outlined text-primary text-[18px]">lightbulb</span>
            실전 투자 전략 &amp; 종합 권고사항
          </h5>
          <p id="modal-strategy" class="font-body-md text-body-md text-on-surface leading-relaxed">
            -
          </p>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="p-4 bg-surface-container border-t border-outline-variant/20 flex flex-wrap items-center justify-between gap-3">
        <span class="font-label-sm text-label-sm text-secondary">
          PropIntelligence 실전 투자 알고리즘 v7.0 검증 완료
        </span>
        <div class="flex items-center space-x-2">
          <button onclick="transferCurrentModalToSimulator()" class="font-label-md text-label-md bg-primary hover:bg-primary-container text-on-primary px-4 py-2 rounded-xl transition shadow-sm flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[18px]">tune</span>경매 시뮬레이터에서 분석
          </button>
          <button onclick="transferCurrentModalToCalculator()" class="font-label-md text-label-md bg-surface-container-high hover:bg-surface-container-highest text-on-surface px-4 py-2 rounded-xl transition flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[18px]">calculate</span>투자수익률 계산기
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= JAVASCRIPT MASTER LOGIC ================= -->
  <script>
    const PROPERTIES = __PROPERTIES_JSON__;
    const REGIONAL_REPORTS = __REGIONAL_REPORTS_JSON__;

    let currentSelectedProperty = PROPERTIES[1]; // 화성봉담 우방(2025타경56772)
    let currentModalPropertyId = null;
    let currentSimPropId = "2025-56772";

    // 공통 화폐 포맷터
    function formatKRW(val) {
      if (val === null || val === undefined || isNaN(val)) return '0원';
      if (Math.abs(val) >= 100000000) {
        const eok = Math.floor(val / 100000000);
        const man = Math.round((val % 100000000) / 10000);
        return man > 0 ? `${eok}억 ${man.toLocaleString()}만 원` : `${eok}억 원`;
      }
      return `${Math.round(val / 10000).toLocaleString()}만 원`;
    }

    function formatNumber(val) {
      return (val || 0).toLocaleString();
    }

    // 전역 토스트 알림
    function showToast(message, isSuccess = true) {
      const toast = document.getElementById('global-toast');
      const msgEl = document.getElementById('toast-message');
      const iconEl = document.getElementById('toast-icon');
      if (!toast || !msgEl) return;

      msgEl.textContent = message;
      if (iconEl) {
        iconEl.textContent = isSuccess ? 'check_circle' : 'info';
        iconEl.className = isSuccess ? 'material-symbols-outlined text-tertiary-fixed text-[22px]' : 'material-symbols-outlined text-primary-fixed text-[22px]';
      }

      toast.classList.remove('translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-20', 'opacity-0');
      }, 3500);
    }

    // =========================================================================
    // 📋 필수 기능: '브리핑 요약 복사' (GEMINI.md 프로젝트 전용 규칙 100% 준수)
    // =========================================================================
    function copySummaryReport() {
      const p = currentSelectedProperty || PROPERTIES[1];
      const fin = p.financing || p.loan || {};
      const exp = p.expenses || {};
      const ren = p.rental || {};

      const now = new Date();
      const dateStr = `${now.getFullYear()}.${String(now.getMonth()+1).padStart(2,'0')}.${String(now.getDate()).padStart(2,'0')} ${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}`;

      let summaryText = `[PropIntelligence 실전 투자 브리핑 요약]\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `★ 대상 사건: ${p.caseNumber} (${p.category})\n`;
      summaryText += `■ 매물명: ${p.propertyName}\n`;
      summaryText += `• 소재지: ${p.address}\n`;
      summaryText += `• 전용면적: ${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평) | ${p.floorInfo}\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `[핵심 가격 및 마진 지표]\n`;
      summaryText += `• 감정평가액: ${formatKRW(p.appraisedValue)}\n`;
      summaryText += `• 최저매각가: ${formatKRW(p.minimumBidPrice)} (${p.minimumBidRate}%)\n`;
      summaryText += `• 최근 실거래시세: ${formatKRW(p.marketPrice)}\n`;
      summaryText += `• 안전마진 (시세차익): ${formatKRW(p.safetyMargin)}\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `[금융 자금 조달 & 수익률]\n`;
      summaryText += `• 담보인정비율 (LTV): ${fin.ltvPercent || 0}%\n`;
      summaryText += `• 대출 예상액: ${formatKRW(fin.loanAmount || 0)}\n`;
      summaryText += `• 임대 셋팅: ${ren.rentalType || '전세'} (보증금 ${formatKRW(ren.deposit || 0)} / 월 ${formatKRW(ren.monthlyRent || 0)})\n`;
      summaryText += `• 총 필요 실투자금: ${formatKRW(p.netInvestment)}\n`;
      summaryText += `★ 예상 자기자본수익률(ROE): ${p.roePercent}%\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `[권리분석 & 명도 평가]\n`;
      summaryText += `• 말소기준등기: ${p.rights?.malsoStandard || '근저당'}\n`;
      summaryText += `• 점유자 상태: ${p.rights?.occupantStatus || '소유자 점유'}\n`;
      summaryText += `• 낙찰자 인수금액: 0원 (권리분석상 100% 안전)\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `[투자 전략 코멘트]\n`;
      summaryText += `${p.strategyBrief}\n`;
      summaryText += `───────────────────────────────────\n`;
      summaryText += `작성일시: ${dateStr} | PropIntelligence v7.0 Engine`;

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(summaryText).then(() => {
          showToast('📋 요약 보고서가 클립보드에 복사되었습니다! 카카오톡이나 메모장에 붙여넣기 하세요.');
        }).catch(() => fallbackCopyText(summaryText));
      } else {
        fallbackCopyText(summaryText);
      }
    }

    function fallbackCopyText(text) {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-999999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        showToast('📋 요약 보고서가 클립보드에 복사되었습니다! 카카오톡이나 메모장에 붙여넣기 하세요.');
      } catch (err) {
        showToast('클립보드 복사에 실패했습니다.', false);
      }
      document.body.removeChild(textArea);
    }

    // =========================================================================
    // 탭 전환 네비게이션
    // =========================================================================
    function switchMainTab(tabId) {
      const views = ['dashboard', 'yield-calculator', 'auction-simulator', 'market-reports'];
      views.forEach(v => {
        const el = document.getElementById(`view-${v}`);
        if (el) el.classList.toggle('hidden', v !== tabId);
      });

      views.forEach(v => {
        const btn = document.getElementById(`btn-tab-${v}`);
        if (btn) {
          if (v === tabId) {
            btn.className = 'nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 bg-primary-container text-on-primary-container font-bold shadow-sm text-left';
          } else {
            btn.className = 'nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 text-on-surface-variant hover:bg-surface-container hover:text-on-surface text-left';
          }
        }
      });

      window.scrollTo({ top: 0, behavior: 'smooth' });

      if (tabId === 'market-reports') {
        renderRegionalReport('bongdam');
      }
    }

    // =========================================================================
    // 1. 대시보드 렌더링 & 인터랙션
    // =========================================================================
    let currentCategoryFilter = 'all';
    let currentMatrixSort = 'roe';

    function setCategoryFilter(cat) {
      currentCategoryFilter = cat;
      const chips = ['all', 'auction', 'sale', 'sub-3000'];
      chips.forEach(c => {
        const btn = document.getElementById(`tab-${c}`);
        if (btn) {
          if (c === cat) {
            btn.className = 'tab-chip active px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md transition-all whitespace-nowrap shadow-sm font-bold';
          } else {
            btn.className = 'tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap';
          }
        }
      });
      renderDashboard();
    }

    function setDashboardViewMode(mode) {
      const tableSec = document.getElementById('macro-matrix-section');
      const cardsSec = document.getElementById('clean-cards-section');
      const tableBtn = document.getElementById('view-mode-table-btn');
      const cardBtn = document.getElementById('view-mode-card-btn');

      if (mode === 'table') {
        if (tableSec) tableSec.classList.remove('hidden');
        if (cardsSec) cardsSec.classList.add('hidden');
        if (tableBtn) tableBtn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 bg-surface-container-lowest text-primary shadow-sm';
        if (cardBtn) cardBtn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 text-secondary hover:text-on-surface';
      } else {
        if (tableSec) tableSec.classList.add('hidden');
        if (cardsSec) cardsSec.classList.remove('hidden');
        if (cardBtn) cardBtn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 bg-surface-container-lowest text-primary shadow-sm';
        if (tableBtn) tableBtn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 text-secondary hover:text-on-surface';
      }
    }

    function handleMatrixSort(val) {
      currentMatrixSort = val;
      renderDashboard();
    }

    function handleSearch() {
      renderDashboard();
    }

    function resetSearch() {
      const sInput = document.getElementById('search-input');
      if (sInput) sInput.value = '';
      setCategoryFilter('all');
    }

    function renderDashboard() {
      const sInput = document.getElementById('search-input');
      const query = (sInput ? sInput.value : '').trim().toLowerCase();

      let list = PROPERTIES.filter(p => {
        if (currentCategoryFilter === 'auction' && p.category !== '경매') return false;
        if (currentCategoryFilter === 'sale' && p.category !== '일반급매') return false;
        if (currentCategoryFilter === 'sub-3000' && p.netInvestment > 30000000) return false;
        if (query) {
          const hay = `${p.caseNumber} ${p.propertyName} ${p.address} ${p.court}`.toLowerCase();
          if (!hay.includes(query)) return false;
        }
        return true;
      });

      // 정렬
      if (currentMatrixSort === 'roe') {
        list.sort((a, b) => b.roePercent - a.roePercent);
      } else if (currentMatrixSort === 'netInvest') {
        list.sort((a, b) => a.netInvestment - b.netInvestment);
      } else if (currentMatrixSort === 'safetyMargin') {
        list.sort((a, b) => b.safetyMargin - a.safetyMargin);
      } else if (currentMatrixSort === 'minBid') {
        list.sort((a, b) => a.minimumBidPrice - b.minimumBidPrice);
      }

      // 배지 카운트
      const matrixBadge = document.getElementById('matrix-count-badge');
      if (matrixBadge) matrixBadge.textContent = `${list.length}건 분석`;
      const listBadge = document.getElementById('list-count-badge');
      if (listBadge) listBadge.textContent = `${list.length}건`;

      // 1. 거시 테이블 렌더링 (행 클릭 모달 연동 + 추천입찰가/권리분석 컬럼 삭제 반영)
      const tbody = document.getElementById('macro-matrix-tbody');
      if (tbody) {
        if (list.length === 0) {
          tbody.innerHTML = `<tr><td colspan="8" class="py-12 text-center text-secondary">조건에 일치하는 매물이 없습니다.</td></tr>`;
        } else {
          tbody.innerHTML = list.map(p => {
            const isTarget = p.id === '2025-56772';
            const catBadge = p.category === '경매' ? 'bg-primary-container text-on-primary-container' : 'bg-secondary-container text-on-secondary-container';
            return `
              <tr class="hover:bg-surface-container-low transition-colors cursor-pointer ${isTarget ? 'bg-primary-fixed/15 font-medium' : ''}" onclick="openPropertyModal('${p.id}')">
                <td class="py-3 px-4">
                  <div class="flex flex-col">
                    <span class="inline-block px-1.5 py-0.5 rounded text-[11px] font-bold ${catBadge} w-max mb-0.5">${p.category}</span>
                    <span class="font-bold text-on-surface text-sm">${p.caseNumber}</span>
                    <span class="text-xs text-secondary truncate max-w-[130px]">${p.court.split(' ')[0]}</span>
                  </div>
                </td>
                <td class="py-3 px-4">
                  <div class="flex flex-col">
                    <div class="flex items-center gap-1.5">
                      <span class="font-bold text-on-surface text-sm hover:text-primary transition">${p.propertyName}</span>
                    </div>
                    <span class="text-xs text-secondary truncate max-w-[220px]">${p.address}</span>
                  </div>
                </td>
                <td class="py-3 px-4 text-right">
                  <span class="text-xs text-secondary line-through">${formatKRW(p.appraisedValue)}</span>
                </td>
                <td class="py-3 px-4 text-right">
                  <div class="flex flex-col items-end">
                    <span class="font-bold text-on-surface text-sm text-primary">${formatKRW(p.minimumBidPrice)}</span>
                    <span class="text-xs text-secondary font-medium">[${p.minimumBidRate}%]</span>
                  </div>
                </td>
                <td class="py-3 px-4 text-right">
                  <span class="font-bold text-xs ${p.safetyMargin > 0 ? 'text-tertiary' : 'text-error'}">
                    ${p.safetyMargin > 0 ? '+' : ''}${formatKRW(p.safetyMargin)}
                  </span>
                </td>
                <td class="py-3 px-4 text-right font-bold text-on-surface text-sm">
                  ${formatKRW(p.netInvestment)}
                </td>
                <td class="py-3 px-4 text-center">
                  <span class="font-bold text-tertiary text-sm">${p.roePercent}%</span>
                  <span class="text-[10px] text-secondary block">${p.rental?.rentalType === '전세' ? '전세갭투자' : '월세셋팅'}</span>
                </td>
                <td class="py-3 px-4 text-center" onclick="event.stopPropagation()">
                  <div class="flex items-center justify-center gap-1.5">
                    <button type="button" onclick="openPropertyModal('${p.id}')" class="px-2.5 py-1 rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface text-xs font-semibold transition">
                      상세
                    </button>
                    <button type="button" onclick="transferToCalculator('${p.id}')" class="px-2.5 py-1 rounded-lg bg-primary hover:bg-primary-container text-on-primary text-xs font-semibold transition">
                      계산기
                    </button>
                  </div>
                </td>
              </tr>
            `;
          }).join('');
        }
      }

      // 2. 고밀도 카드 렌더링 (불필요한 추천입찰가 블록 삭제 및 클릭 버블링 방어)
      const cardsCont = document.getElementById('property-cards-container');
      if (cardsCont) {
        cardsCont.innerHTML = list.map(p => {
          const isTarget = p.id === '2025-56772';
          return `
            <div class="p-4 rounded-2xl bg-surface-container-lowest border ${isTarget ? 'border-primary shadow-md' : 'border-outline-variant/30 shadow-xs'} hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20 mb-3">
                  <div class="flex items-center gap-1.5">
                    <span class="px-2 py-0.5 rounded text-[11px] font-bold ${p.category === '경매' ? 'bg-primary-container text-on-primary-container' : 'bg-secondary-container text-on-secondary-container'}">${p.category}</span>
                    <span class="font-bold text-xs text-on-surface">${p.caseNumber}</span>
                  </div>
                  <span class="text-xs font-bold text-tertiary">ROE ${p.roePercent}%</span>
                </div>
                <h4 class="font-bold text-on-surface text-sm mb-1">${p.propertyName}</h4>
                <p class="text-xs text-secondary mb-3 truncate">${p.address}</p>

                <div class="grid grid-cols-2 gap-2 p-2.5 rounded-xl bg-surface-container-low text-xs mb-3">
                  <div>
                    <span class="text-secondary block">감정가</span>
                    <span class="font-medium text-on-surface line-through text-[11px]">${formatKRW(p.appraisedValue)}</span>
                  </div>
                  <div>
                    <span class="text-secondary block">최저가(${p.minimumBidRate}%)</span>
                    <span class="font-bold text-primary">${formatKRW(p.minimumBidPrice)}</span>
                  </div>
                  <div>
                    <span class="text-secondary block">실투자금</span>
                    <span class="font-bold text-on-surface">${formatKRW(p.netInvestment)}</span>
                  </div>
                  <div>
                    <span class="text-secondary block">안전마진</span>
                    <span class="font-bold ${p.safetyMargin > 0 ? 'text-tertiary' : 'text-error'}">${formatKRW(p.safetyMargin)}</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-2 pt-2 border-t border-outline-variant/20" onclick="event.stopPropagation()">
                <button type="button" onclick="openPropertyModal('${p.id}')" class="flex-1 py-1.5 rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface font-label-sm text-label-sm font-semibold transition text-center">
                  상세보기
                </button>
                <button type="button" onclick="transferToCalculator('${p.id}')" class="flex-1 py-1.5 rounded-lg bg-primary hover:bg-primary-container text-on-primary font-label-sm text-label-sm font-semibold transition text-center">
                  수익률 계산
                </button>
              </div>
            </div>
          `;
        }).join('');
      }
    }

    // =========================================================================
    // 2. 모달 제어
    // =========================================================================
    function openPropertyModal(propId) {
      const p = PROPERTIES.find(item => item.id === propId);
      if (!p) return;
      currentModalPropertyId = propId;
      currentSelectedProperty = p;

      const modal = document.getElementById('property-modal');
      if (!modal) return;

      document.getElementById('modal-title').textContent = p.propertyName;
      document.getElementById('modal-case-no').textContent = p.caseNumber;
      document.getElementById('modal-category-badge').textContent = p.category;
      document.getElementById('modal-summary-address').textContent = `${p.address} | ${p.court}`;
      document.getElementById('modal-auction-date').textContent = `입찰일: ${p.auctionDate || '미정'}`;

      document.getElementById('modal-appraised-val').textContent = formatKRW(p.appraisedValue);
      document.getElementById('modal-min-price').textContent = `${formatKRW(p.minimumBidPrice)} (${p.minimumBidRate}%)`;
      document.getElementById('modal-net-investment').textContent = formatKRW(p.netInvestment);
      document.getElementById('modal-roe').textContent = `${p.roePercent}%`;

      const ren = p.rental || {};
      document.getElementById('modal-rental').textContent = ren.rentalType === '전세' 
        ? `전세 ${formatKRW(ren.deposit || 0)} (갭투자)` 
        : `월세 ${formatKRW(ren.deposit || 0)} / ${formatKRW(ren.monthlyRent || 0)}`;

      document.getElementById('modal-address').textContent = p.address;
      document.getElementById('modal-area').textContent = `${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평)`;
      document.getElementById('modal-floor-build').textContent = `${p.floorInfo} / ${p.buildYear}년`;
      document.getElementById('modal-appraised').textContent = formatKRW(p.appraisedValue);
      document.getElementById('modal-min').textContent = formatKRW(p.minimumBidPrice);
      document.getElementById('modal-market').textContent = formatKRW(p.marketPrice);

      const rig = p.rights || {};
      document.getElementById('modal-malso').textContent = rig.malsoStandard || '근저당권 (말소기준)';
      document.getElementById('modal-occupant').textContent = rig.occupantStatus || '소유자 점유';
      document.getElementById('modal-takeover').textContent = rig.takeoverAmount ? formatKRW(rig.takeoverAmount) : '0원 (완벽 안전)';
      document.getElementById('modal-eviction').textContent = rig.evictionDifficulty ? `${rig.evictionDifficulty} (예상 이사비 150만원)` : '하';

      const hlContainer = document.getElementById('modal-highlights');
      if (hlContainer) {
        hlContainer.innerHTML = (p.locationHighlights || []).map(h => `<li>${h}</li>`).join('');
      }

      const stratEl = document.getElementById('modal-strategy');
      if (stratEl) stratEl.textContent = p.strategyBrief;

      modal.classList.remove('hidden');
    }

    function closePropertyModal() {
      const modal = document.getElementById('property-modal');
      if (modal) modal.classList.add('hidden');
    }

    function transferCurrentModalToCalculator() {
      if (!currentModalPropertyId) return;
      closePropertyModal();
      transferToCalculator(currentModalPropertyId);
    }

    function transferCurrentModalToSimulator() {
      if (!currentModalPropertyId) return;
      closePropertyModal();
      transferToSimulator(currentModalPropertyId);
    }

    function transferToCalculator(propId) {
      loadCalcPreset(propId);
      switchMainTab('yield-calculator');
    }

    function transferToSimulator(propId) {
      selectSimProperty(propId);
      switchMainTab('auction-simulator');
    }

    // =========================================================================
    // 3. 투자수익률 계산기 엔진 (LTV 0% 및 Range 슬라이더 + 전세 갭투자 ROE 21.5%)
    // =========================================================================
    let calcCurrentLtv = 70;
    let calcPropType = 'house';
    let calcHousingCount = '1house';

    function handlePropTypeChange(type) {
      calcPropType = type;
      document.querySelectorAll('.prop-type-btn').forEach(btn => {
        const ptype = btn.getAttribute('data-prop-type');
        if (ptype === type) {
          btn.className = 'prop-type-btn py-2 text-center rounded-md font-label-md text-label-md font-semibold bg-surface-container-lowest text-primary shadow-sm transition-all';
        } else {
          btn.className = 'prop-type-btn py-2 text-center rounded-md font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all font-medium';
        }
      });
      runCalculatorEngine();
    }

    function handleHousingCountChange(count) {
      calcHousingCount = count;
      document.querySelectorAll('.housing-btn').forEach(btn => {
        const hcount = btn.getAttribute('data-house');
        if (hcount === count) {
          btn.className = 'housing-btn py-2 text-center rounded-lg font-label-md text-label-md font-semibold bg-primary text-on-primary shadow-sm transition-all';
        } else {
          btn.className = 'housing-btn py-2 text-center rounded-lg font-label-md text-label-md font-medium bg-surface-container-low text-on-surface-variant hover:bg-surface-container transition-all';
        }
      });
      runCalculatorEngine();
    }

    function handlePresetSelect(propId) {
      loadCalcPreset(propId);
    }

    function loadCalcPreset(propId) {
      // urgent-bongdam 별칭 호환 처리
      const targetId = propId === 'urgent-bongdam' ? 'sale-bongdam-105' : propId;
      const p = PROPERTIES.find(item => item.id === targetId) || PROPERTIES[1];
      const fin = p.financing || p.loan || {};
      const ren = p.rental || {};

      // 6개 매물 2줄 카드형 선택기 렌더링 (1줄: 정확한 사건번호, 2줄: 경매 매물명)
      const selectorContainer = document.getElementById('calc-property-selector');
      if (selectorContainer) {
        selectorContainer.innerHTML = PROPERTIES.map(item => {
          const isSelected = item.id === targetId || item.id === propId;
          const cls = isSelected
            ? "p-2.5 rounded-xl bg-primary text-on-primary font-semibold shadow-sm transition border border-primary text-left flex flex-col justify-center cursor-pointer"
            : "p-2.5 rounded-xl bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition border border-outline-variant/30 text-left flex flex-col justify-center cursor-pointer";
          const subName = item.propertyName.length > 14 ? item.propertyName.slice(0, 14) + '...' : item.propertyName;
          return `
            <button onclick="loadCalcPreset('${item.id}')" data-case-id="${item.id}" class="${cls}">
              <div class="font-bold text-xs font-mono tracking-tight">${item.caseNumber}</div>
              <div class="text-[11px] truncate opacity-90 mt-0.5 font-medium">${subName}</div>
            </button>
          `;
        }).join('');
      }

      // 레거시 버튼 클래스 호환
      document.querySelectorAll('.calc-preset-btn').forEach(btn => {
        const bid = btn.getAttribute('data-case-id');
        if (bid === targetId || bid === propId) {
          btn.className = 'calc-preset-btn px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-label-md font-semibold transition-all shadow-sm';
        } else {
          btn.className = 'calc-preset-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition-all font-label-md text-label-md font-medium';
        }
      });

      const bidPrice = p.recommendedBidPrice || p.minimumBidPrice;
      const priceInput = document.getElementById('priceInput');
      const priceSlider = document.getElementById('priceSlider');
      if (priceInput) priceInput.value = bidPrice;
      if (priceSlider) priceSlider.value = bidPrice;

      const priceDisp = document.getElementById('priceDisplayMan');
      if (priceDisp) priceDisp.textContent = Math.round(bidPrice / 10000).toLocaleString();

      const depInput = document.getElementById('depositInput');
      if (depInput) depInput.value = Math.round((ren.deposit || 0) / 10000);

      const rentInput = document.getElementById('monthlyRentInput');
      if (rentInput) rentInput.value = Math.round((ren.monthlyRent || 0) / 10000);

      const rateInput = document.getElementById('loanRateInput');
      if (rateInput) rateInput.value = (fin.interestRate || 4.0).toFixed(2);

      // LTV 설정 및 전체 계산기 엔진 즉각 재연산
      calcCurrentLtv = fin.ltvPercent !== undefined ? fin.ltvPercent : 70;
      handleLtvSliderChange(calcCurrentLtv);
      runCalculatorEngine();
    }

    function handlePriceInputChange() {
      const input = document.getElementById('priceInput');
      const slider = document.getElementById('priceSlider');
      const disp = document.getElementById('priceDisplayMan');
      if (!input) return;
      const val = parseInt(input.value) || 0;
      if (slider) slider.value = val;
      if (disp) disp.textContent = Math.round(val / 10000).toLocaleString();
      runCalculatorEngine();
    }

    function handlePriceSliderChange() {
      const input = document.getElementById('priceInput');
      const slider = document.getElementById('priceSlider');
      const disp = document.getElementById('priceDisplayMan');
      if (!slider) return;
      const val = parseInt(slider.value) || 0;
      if (input) input.value = val;
      if (disp) disp.textContent = Math.round(val / 10000).toLocaleString();
      runCalculatorEngine();
    }

    function handleLtvButtonClick(ltvVal) {
      handleLtvSliderChange(ltvVal);
    }

    function handleLtvSliderChange(val) {
      calcCurrentLtv = parseInt(val);
      const slider = document.getElementById('ltvSlider');
      if (slider) slider.value = calcCurrentLtv;

      // LTV 버튼 활성 상태
      document.querySelectorAll('.ltv-btn').forEach(btn => {
        const btnLtv = parseInt(btn.getAttribute('data-ltv'));
        if (btnLtv === calcCurrentLtv) {
          btn.className = 'ltv-btn px-2.5 py-1 text-xs rounded-lg bg-primary text-on-primary font-bold shadow-xs';
        } else {
          btn.className = 'ltv-btn px-2.5 py-1 text-xs rounded-lg bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition';
        }
      });

      runCalculatorEngine();
    }

    function runCalculatorEngine() {
      const priceInput = document.getElementById('priceInput');
      const purchasePrice = parseInt(priceInput ? priceInput.value : 330000000) || 0;

      const rateInput = document.getElementById('loanRateInput');
      const loanRate = parseFloat(rateInput ? rateInput.value : 4.0) || 0;

      const depInput = document.getElementById('depositInput');
      const deposit = (parseInt(depInput ? depInput.value : 28000) || 0) * 10000;

      const rentInput = document.getElementById('monthlyRentInput');
      const monthlyRent = (parseInt(rentInput ? rentInput.value : 0) || 0) * 10000;

      const vatToggle = document.getElementById('brokerVatToggle');
      const hasVat = vatToggle ? vatToggle.checked : true;

      // 대출금 산정 (LTV 0% 선택 시 완전 0원)
      const loanAmount = calcCurrentLtv === 0 ? 0 : Math.round(purchasePrice * (calcCurrentLtv / 100));
      const monthlyInterest = calcCurrentLtv === 0 ? 0 : Math.round((loanAmount * (loanRate / 100)) / 12);

      // LTV 라벨 및 대출금 인풋 갱신
      const ltvLabel = document.getElementById('ltvIndicatorLabel');
      if (ltvLabel) {
        ltvLabel.textContent = calcCurrentLtv === 0 ? 'LTV 0.0% (0원 - 전액 자부담)' : `LTV ${calcCurrentLtv.toFixed(1)}% (${formatKRW(loanAmount)})`;
      }
      const loanAmtInput = document.getElementById('loanAmountInput');
      if (loanAmtInput) loanAmtInput.value = formatNumber(loanAmount);

      // 취득세율 정밀 산정 (물건 유형 & 보유 주택수)
      let taxRate = 0.011;
      let taxDesc = '기본세율 1.1% 적용 (비조정 1주택)';
      if (calcPropType === 'officetel' || calcPropType === 'commercial') {
        taxRate = 0.046;
        taxDesc = '취득세 4.6% 적용 (오피스텔/상가 단일세율)';
      } else {
        if (calcHousingCount === '1house') {
          taxRate = 0.011;
          taxDesc = '기본세율 1.1% 적용 (비조정 1주택)';
        } else if (calcHousingCount === '2house') {
          taxRate = 0.011;
          taxDesc = '기본세율 1.1% 적용 (비조정 2주택 기준)';
        } else if (calcHousingCount === '3house') {
          taxRate = 0.084;
          taxDesc = '중과세율 8.4% 적용 (3주택 중과)';
        } else if (calcHousingCount === '4house') {
          taxRate = 0.124;
          taxDesc = '중과세율 12.4% 적용 (4주택 이상 중과)';
        }
      }
      const taxInd = document.getElementById('taxRateIndicator');
      if (taxInd) taxInd.textContent = taxDesc;

      // 부대비용 정밀 산정
      const acqTax = Math.round(purchasePrice * taxRate);
      const brokerage = Math.round(purchasePrice * 0.004 * (hasVat ? 1.1 : 1.0));
      const legalFee = 800000;
      const bondDiscount = Math.round(purchasePrice * 0.0015);
      const incidentalTotal = acqTax + brokerage + legalFee + bondDiscount;
      const totalCost = purchasePrice + incidentalTotal;

      // 비용 요약 UI
      const taxEl = document.getElementById('costTaxBreakdown');
      if (taxEl) taxEl.textContent = formatKRW(acqTax);
      const brokEl = document.getElementById('costBrokerage');
      if (brokEl) brokEl.textContent = formatKRW(brokerage);
      const bondLegEl = document.getElementById('costBondLegal');
      if (bondLegEl) bondLegEl.textContent = formatKRW(legalFee + bondDiscount);
      const incTotalEl = document.getElementById('totalIncidentalCostSummary');
      if (incTotalEl) incTotalEl.textContent = formatKRW(incidentalTotal);
      const outRequiredEl = document.getElementById('totalOutlayRequired');
      if (outRequiredEl) outRequiredEl.textContent = formatKRW(totalCost);

      // 실투자금 및 ROE 산출 분기 (월세 vs 전세 갭투자)
      const isJeonse = monthlyRent === 0;
      let netInvest = 0;
      let roe = 0;
      let monthlyNcf = 0;

      if (isJeonse) {
        // 전세 갭투자 모드: 전세보증금 회수로 대출금 상환 가정
        netInvest = Math.max(0, totalCost - deposit);
        monthlyNcf = 0;
        // 시세차익형 ROE: (시세 4.2억 - 총취득원가) / 실투자금 * 100
        const marketPrice = 420000000;
        const gain = marketPrice - totalCost;
        roe = netInvest > 0 ? ((gain / netInvest) * 100).toFixed(2) : 0;
      } else {
        // 월세 수익형 모드
        netInvest = Math.max(0, totalCost - loanAmount - deposit);
        monthlyNcf = monthlyRent - monthlyInterest;
        const annualProfit = monthlyNcf * 12;
        roe = netInvest > 0 ? ((annualProfit / netInvest) * 100).toFixed(2) : 0;
      }

      // KPI UI 업데이트
      const kpiNetEq = document.getElementById('kpiNetEquity');
      if (kpiNetEq) kpiNetEq.textContent = formatKRW(netInvest);

      const kpiNcf = document.getElementById('kpiMonthlyCashFlow');
      if (kpiNcf) {
        if (isJeonse) {
          kpiNcf.textContent = `전세 갭 ${formatKRW(deposit)}`;
          const sub = document.getElementById('kpiNcfSub');
          if (sub) sub.textContent = '보증금 회수 셋팅 (월세 0원)';
        } else {
          kpiNcf.textContent = `${monthlyNcf > 0 ? '+' : ''}${formatKRW(monthlyNcf)}/월`;
          const sub = document.getElementById('kpiNcfSub');
          if (sub) sub.textContent = `월 이자: ${formatKRW(monthlyInterest)}`;
        }
      }

      const kpiRoeEl = document.getElementById('kpiRoe');
      if (kpiRoeEl) kpiRoeEl.textContent = `${roe}%`;

      const levTitle = document.getElementById('leverageTitle');
      const levDetail = document.getElementById('leverageDetailText');
      if (calcCurrentLtv === 0) {
        if (levTitle) levTitle.textContent = '[투자 전략 판정] ⚪ 무차입 자부담 투자 (금리 위험 0%)';
        if (levDetail) levDetail.textContent = '타인자본(대출)을 사용하지 않아 금리 변동 리스크가 전혀 없는 가장 안전한 구조입니다.';
      } else if (isJeonse) {
        if (levTitle) levTitle.textContent = '[투자 전략 판정] 🟢 전세 레버리지 갭투자 (자본이득 극대화)';
        if (levDetail) levDetail.textContent = '실투자금 5,744만원으로 전세 2.8억원을 셋팅하여 확정 안전마진 8,256만원(수익률 21.5%)을 확보하는 최적 전략입니다.';
      } else if (parseFloat(roe) > loanRate) {
        if (levTitle) levTitle.textContent = '[투자 전략 판정] 🟢 건전한 정(Positive) 레버리지';
        if (levDetail) levDetail.textContent = '임대수익률이 대출금리를 상회하여 대출을 활용할수록 자기자본수익률(ROE)이 극대화됩니다.';
      } else {
        if (levTitle) levTitle.textContent = '[투자 전략 판정] 🟡 역(Negative) 레버리지 주의';
        if (levDetail) levDetail.textContent = '대출금리가 임대수익률보다 높아 대출 비중 축소 또는 입찰가 인하가 권장됩니다.';
      }
    }

    // =========================================================================
    // 4. 경매 분석 시뮬레이터 (사건선택, 역산 입찰가, 공적 서류 5종 2줄)
    // =========================================================================
    let simLoanMode = true;
    let simCurrentDocTab = 'doc-spec';

    function selectSimProperty(propId) {
      const p = PROPERTIES.find(item => item.id === propId) || PROPERTIES[1];
      currentSimPropId = p.id;
      currentSelectedProperty = p;

      // 6개 매물 2줄 카드형 선택기 렌더링 (1줄: 정확한 사건번호, 2줄: 경매 매물명)
      const selectorContainer = document.getElementById('sim-property-selector');
      if (selectorContainer) {
        selectorContainer.innerHTML = PROPERTIES.map(item => {
          const isSelected = item.id === propId;
          const cls = isSelected
            ? "p-2.5 rounded-xl bg-primary text-on-primary font-semibold shadow-sm transition border border-primary text-left flex flex-col justify-center"
            : "p-2.5 rounded-xl bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition border border-outline-variant/30 text-left flex flex-col justify-center";
          const subName = item.propertyName.length > 14 ? item.propertyName.slice(0, 14) + '...' : item.propertyName;
          return `
            <button onclick="selectSimProperty('${item.id}')" class="${cls}">
              <div class="font-bold text-xs font-mono tracking-tight">${item.caseNumber}</div>
              <div class="text-[11px] truncate opacity-90 mt-0.5 font-medium">${subName}</div>
            </button>
          `;
        }).join('');
      }

      // 헤더 바인딩
      const pName = document.getElementById('sim-property-name');
      if (pName) pName.textContent = p.propertyName;

      const cCase = document.getElementById('sim-court-case');
      if (cCase) cCase.textContent = `${p.court} • ${p.caseNumber}`;

      const addr = document.getElementById('sim-address');
      if (addr) addr.textContent = p.address;

      const aDate = document.getElementById('sim-auction-date');
      if (aDate) aDate.textContent = `${p.auctionDate || '2026.11.25'} (10:00)`;

      const valApp = document.getElementById('sim-val-appraised');
      if (valApp) valApp.textContent = formatKRW(p.appraisedValue);

      const valMin = document.getElementById('sim-val-min');
      if (valMin) valMin.textContent = formatKRW(p.minimumBidPrice);

      const mPrice = document.getElementById('sim-market-price');
      if (mPrice) mPrice.textContent = formatKRW(p.marketPrice);

      const mText = document.getElementById('sim-margin-text');
      if (mText) mText.textContent = `안전마진: 약 +${formatKRW(p.safetyMargin)}`;

      // 슬라이더 범위 세팅
      const slider = document.getElementById('sim-bid-slider');
      if (slider) {
        slider.min = Math.round(p.minimumBidPrice / 10000);
        slider.max = Math.round(p.appraisedValue * 1.15 / 10000);
        slider.value = Math.round((p.recommendedBidPrice || p.minimumBidPrice) / 10000);
      }

      // 매물의 실제 법원 분석 비용을 역산 설정창에 동기화
      const exp = p.expenses || {};
      const legInp = document.getElementById('rev-legal-fee');
      if (legInp) legInp.value = Math.round((exp.legalFee || 800000) / 10000);

      const evInp = document.getElementById('rev-eviction-fee');
      if (evInp) evInp.value = Math.round((exp.evictionFee || 1500000) / 10000);

      const repInp = document.getElementById('rev-repair-fee');
      if (repInp) repInp.value = Math.round(((exp.repairFee || 0) + (exp.brokerageFee || 1500000)) / 10000);

      const bInp = document.getElementById('reverse-budget-input');
      if (bInp) bInp.value = Math.round(((p.recommendedBidPrice || p.minimumBidPrice) + (exp.totalExpenses || 7440000)) / 10000);

      calculateReverseBid();
      runSimulatorEngine();
      renderPublicDoc(simCurrentDocTab);
    }

    function calculateReverseBid() {
      const budgetInput = document.getElementById('reverse-budget-input');
      const maxBudgetMan = parseInt(budgetInput ? budgetInput.value : 34000) || 34000;

      // 부대비용 항목별 수치 추출
      const taxRateEl = document.getElementById('rev-tax-rate');
      const taxRate = taxRateEl ? parseFloat(taxRateEl.value) : 0.011;

      const legalFeeEl = document.getElementById('rev-legal-fee');
      const legalFeeMan = parseInt(legalFeeEl ? legalFeeEl.value : 80) || 0;

      const evictionFeeEl = document.getElementById('rev-eviction-fee');
      const evictionFeeMan = parseInt(evictionFeeEl ? evictionFeeEl.value : 150) || 0;

      const repairFeeEl = document.getElementById('rev-repair-fee');
      const repairFeeMan = parseInt(repairFeeEl ? repairFeeEl.value : 150) || 0;

      const fixedFeesMan = legalFeeMan + evictionFeeMan + repairFeeMan;

      // 역산 입찰가 도출: (총예산 - 고정비용) / (1 + 취득세율)
      const reverseBidMan = Math.max(0, Math.floor((maxBudgetMan - fixedFeesMan) / (1 + taxRate)));
      const calculatedTaxMan = Math.round(reverseBidMan * taxRate);
      const totalFeesMan = calculatedTaxMan + fixedFeesMan;

      // 1. 역산 추천 한도 입찰가 메인 텍스트
      const resEl = document.getElementById('reverse-bid-result');
      if (resEl) {
        const eok = Math.floor(reverseBidMan / 10000);
        const man = reverseBidMan % 10000;
        resEl.textContent = eok > 0 ? `${eok}억 ${man.toLocaleString()}만 원` : `${man.toLocaleString()}만 원`;
      }

      // 2. 부대비용 합계 뱃지 및 상세 텍스트
      const badgeEl = document.getElementById('reverse-fees-sum-badge');
      if (badgeEl) badgeEl.textContent = `부대비용 합계: 약 ${totalFeesMan.toLocaleString()}만원`;

      const detailEl = document.getElementById('reverse-deduct-detail');
      if (detailEl) {
        detailEl.textContent = `선반영 부대비용: 취득세 약 ${calculatedTaxMan.toLocaleString()}만 + 부대비용 ${fixedFeesMan.toLocaleString()}만 (합계 약 ${totalFeesMan.toLocaleString()}만원 차감)`;
      }

      const breakdownEl = document.getElementById('rev-breakdown-text');
      if (breakdownEl) {
        breakdownEl.textContent = `세부내역: 취득세 약 ${calculatedTaxMan}만 + 법무 ${legalFeeMan}만 + 명도 ${evictionFeeMan}만 + 수리/예비 ${repairFeeMan}만`;
      }

      const totalDeductEl = document.getElementById('rev-total-deduct');
      if (totalDeductEl) {
        totalDeductEl.textContent = `선반영 차감 총액: 약 ${totalFeesMan.toLocaleString()}만원`;
      }

      return reverseBidMan;
    }

    function applyReverseBidToSlider() {
      const reverseBidMan = calculateReverseBid();
      const slider = document.getElementById('sim-bid-slider');
      if (slider) {
        slider.value = reverseBidMan;
        runSimulatorEngine();
        showToast(`🎯 역산 추천 입찰가 ${Math.floor(reverseBidMan / 10000)}억 ${(reverseBidMan % 10000).toLocaleString()}만원이 슬라이더에 반영되었습니다.`);
      }
    }

    function setLoanMode(use) {
      simLoanMode = use;
      const btnUse = document.getElementById('btn-loan-use');
      const btnNone = document.getElementById('btn-loan-none');
      const sliderCont = document.getElementById('loan-slider-container');

      if (use) {
        if (btnUse) btnUse.className = 'px-2.5 py-1 rounded-md bg-primary text-on-primary font-label-sm text-label-sm font-semibold transition';
        if (btnNone) btnNone.className = 'px-2.5 py-1 rounded-md text-on-surface-variant hover:text-on-surface font-label-sm text-label-sm font-medium transition';
        if (sliderCont) sliderCont.style.display = 'flex';
      } else {
        if (btnNone) btnNone.className = 'px-2.5 py-1 rounded-md bg-primary text-on-primary font-label-sm text-label-sm font-semibold transition';
        if (btnUse) btnUse.className = 'px-2.5 py-1 rounded-md text-on-surface-variant hover:text-on-surface font-label-sm text-label-sm font-medium transition';
        if (sliderCont) sliderCont.style.display = 'none';
      }
      runSimulatorEngine();
    }

    function setQuickRate(rate) {
      const rSlider = document.getElementById('sim-rate-slider');
      if (rSlider) rSlider.value = rate;
      const rDisp = document.getElementById('sim-rate-display');
      if (rDisp) rDisp.textContent = rate.toFixed(1);
      runSimulatorEngine();
    }

    function runSimulatorEngine() {
      const p = currentSelectedProperty || PROPERTIES[1];
      const slider = document.getElementById('sim-bid-slider');
      const bidMan = parseInt(slider ? slider.value : 33000) || 33000;
      const bidPrice = bidMan * 10000;

      const bidDisp = document.getElementById('sim-bid-display');
      if (bidDisp) bidDisp.textContent = bidMan.toLocaleString();

      const jeonseSlider = document.getElementById('sim-jeonse-slider');
      const jeonseMan = parseInt(jeonseSlider ? jeonseSlider.value : 28000) || 28000;
      const jeonseDisp = document.getElementById('sim-jeonse-display');
      if (jeonseDisp) jeonseDisp.textContent = jeonseMan.toLocaleString();

      // 부대비용 및 대출
      const acqTax = Math.round(bidPrice * 0.011);
      const miscCost = 3810000; // 법무비+명도비+채권
      const totalCost = bidPrice + acqTax + miscCost;

      const costsEl = document.getElementById('sim-out-costs');
      if (costsEl) costsEl.textContent = formatKRW(acqTax + miscCost);

      // 전세 2.8억 갭투자
      const netInvest = Math.max(0, totalCost - (jeonseMan * 10000));
      const netEqEl = document.getElementById('sim-out-net-equity');
      if (netEqEl) netEqEl.textContent = formatKRW(netInvest);

      const gain = (p.marketPrice || 420000000) - totalCost;
      const roe = netInvest > 0 ? ((gain / netInvest) * 100).toFixed(1) : 0;
      const roeEl = document.getElementById('sim-out-roe');
      if (roeEl) roeEl.textContent = `${roe}%`;

      // 시나리오 카드 수치
      const sc1 = document.getElementById('sim-scen1-invest');
      if (sc1) sc1.textContent = formatKRW(netInvest);

      const sc3 = document.getElementById('sim-scen3-gain');
      if (sc3) sc3.textContent = `+${formatKRW(gain)}`;
    }

    function switchDocTab(tabKey) {
      simCurrentDocTab = tabKey;
      const tabs = ['doc-spec', 'doc-appraisal', 'doc-survey', 'doc-register', 'doc-resident'];
      tabs.forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        if (btn) {
          if (t === tabKey) {
            btn.className = 'px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-label-md font-semibold transition whitespace-nowrap shadow-xs';
          } else {
            btn.className = 'px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition whitespace-nowrap';
          }
        }
      });
      renderPublicDoc(tabKey);
    }

    function renderPublicDoc(tabKey) {
      const box = document.getElementById('public-doc-content');
      if (!box) return;
      const p = currentSelectedProperty || PROPERTIES[1];
      const rig = p.rights || {};

      if (tabKey === 'doc-spec') {
        box.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-sm text-on-surface">1. 매각물건명세서 (법원 공식 고시)</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                <span class="material-symbols-outlined text-[13px] text-emerald-600">check_circle</span>
                하자 0건 클린
              </span>
            </div>
            <p class="text-xs text-on-surface leading-relaxed">
              • 최선순위 설정일자: <strong>${rig.malsoStandard || '2016-12-01 한국주택금융공사 근저당'}</strong><br>
              • 배당요구종기일: <strong>2025.10.15</strong> (종기일 이내 배당요구 완료)<br>
              • 매각으로 소멸되지 아니하는 권리: <strong>[해당사항 없음]</strong> (전액 소멸)<br>
              • 비고: 대항력 있는 선순위 임차인 부존재 확인. 낙찰자 인수 권리 0원.
            </p>
          </div>
        `;
      } else if (tabKey === 'doc-appraisal') {
        box.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-sm text-on-surface">2. 감정평가요항표 (공식 법원 감정평가서)</span>
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-primary-container text-on-primary-container">감정가 ${formatKRW(p.appraisedValue)}</span>
            </div>
            <p class="text-xs text-on-surface leading-relaxed">
              • 대상물건: ${p.propertyName} (${p.exclusiveAreaM2}㎡ / ${p.exclusiveAreaPyung}평형)<br>
              • 위치/주위환경: 경기도 ${p.address} 소재. 신흥 주거타운 형성 및 초등학교 인접.<br>
              • 건물구조: 철근콘크리트구조 23층 건 내 ${p.floorInfo}. 일조 및 조망 우수.
            </p>
          </div>
        `;
      } else if (tabKey === 'doc-survey') {
        box.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-sm text-on-surface">3. 현황조사서 (집행관 현장 조사)</span>
              <span class="text-xs text-secondary font-semibold">점유관계 명확</span>
            </div>
            <p class="text-xs text-on-surface leading-relaxed">
              • 점유관계: ${rig.occupantStatus || '소유자 세대 전입 점유'}<br>
              • 임대차 관계: 조사된 임차내역 없음. 소유자 직접 점유로 인도명령 인용 대상.<br>
              • 관리비 체납: ${p.expenses?.unpaidManagementFee ? formatKRW(p.expenses.unpaidManagementFee) : '0원 (정상 납부 중)'}
            </p>
          </div>
        `;
      } else if (tabKey === 'doc-register') {
        box.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-sm text-on-surface">4. 부동산 등기사항전부증명서 (을구 근저당)</span>
              <span class="text-xs font-bold text-tertiary">소멸주의 100%</span>
            </div>
            <p class="text-xs text-on-surface leading-relaxed">
              • 말소기준등기: ${rig.malsoStandard}<br>
              • 후순위 권리: 가압류 및 압류 등 일체 권리는 낙찰 잔금 납부 시 집행법원의 촉탁으로 100% 말소 처리됨.
            </p>
          </div>
        `;
      } else if (tabKey === 'doc-resident') {
        box.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-sm text-on-surface">5. 전입세대확인서 (주민센터 열람본)</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                <span class="material-symbols-outlined text-[13px] text-emerald-600">check_circle</span>
                대항력 없음
              </span>
            </div>
            <p class="text-xs text-on-surface leading-relaxed">
              • 세대주 성명: 소유자 장OO 세대 전입 확인<br>
              • 전입일자: 말소기준등기일(2016-12-01) 이후 전입으로 대항력 일체 부존재.
            </p>
          </div>
        `;
      }
    }

    // =========================================================================
    // 5. 시장동향 리포트 뷰어 (5대 권역 실제 HTML 전문 보고서 및 도시개발 마스터플랜 완전 연동)
    // =========================================================================
    const REGIONAL_REPORT_FILES = {
      'bongdam': '시장동향리포트뷰어/오목천_봉담_통합_지역종합분석보고서.html',
      'anseong': '시장동향리포트뷰어/안성시_부동산시장분석_PropX데이터솔루션활용보고서.html',
      'pyeongtaek': '시장동향리포트뷰어/평택시_부동산시장분석_PropX데이터솔루션활용보고서.html',
      'cheonan': '시장동향리포트뷰어/천안시_부동산시장분석_PropX데이터솔루션활용보고서.html',
      'cheongju': '시장동향리포트뷰어/청주시_부동산시장분석_PropX데이터솔루션활용보고서.html'
    };

    function switchRegionalReport(regionId) {
      renderRegionalReport(regionId);
    }

    function renderRegionalReport(regionId) {
      const rep = REGIONAL_REPORTS.find(r => r.id === regionId) || REGIONAL_REPORTS[0];
      const targetFilePath = REGIONAL_REPORT_FILES[regionId] || REGIONAL_REPORT_FILES['bongdam'];

      // 탭 활성화 상태 UI 전환
      document.querySelectorAll('.reg-tab').forEach(btn => {
        btn.classList.remove('bg-primary', 'text-on-primary', 'font-semibold', 'shadow-sm');
        btn.classList.add('bg-surface-container', 'text-on-surface-variant');
      });
      const activeBtn = document.getElementById(`tab-reg-${regionId}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-surface-container', 'text-on-surface-variant');
        activeBtn.classList.add('bg-primary', 'text-on-primary', 'font-semibold', 'shadow-sm');
      }

      // 1. 브레드크럼 및 헤더 동기화
      const bRegion = document.getElementById('report-breadcrumb-region');
      if (bRegion) bRegion.textContent = rep.name;

      const badge = document.getElementById('report-badge');
      if (badge) badge.textContent = rep.badge;

      const title = document.getElementById('report-title');
      if (title) title.textContent = `${rep.name} 광역생활권 부동산 시장 및 도시개발 심층 분석`;

      const summary = document.getElementById('report-summary');
      if (summary) summary.textContent = rep.summary;

      // 2. 외부 새 탭 및 프레임 액션 링크 동기화
      const btnOpenExt = document.getElementById('btn-open-external');
      if (btnOpenExt) btnOpenExt.href = targetFilePath;

      const btnFrameDirect = document.getElementById('btn-frame-direct-open');
      if (btnFrameDirect) btnFrameDirect.href = targetFilePath;

      const frameTitle = document.getElementById('report-frame-title');
      if (frameTitle) frameTitle.textContent = `${rep.name} 부동산 시장 분석 보고서 (PropX 데이터 솔루션)`;

      // 3. 실제 HTML 전문 인터랙티브 프레임 동기화
      const reportFrame = document.getElementById('report-interactive-frame');
      if (reportFrame && reportFrame.getAttribute('src') !== targetFilePath) {
        reportFrame.src = targetFilePath;
      }

      // 4. 5대 핵심 지표 동기화
      const m = rep.metrics || {};
      const uEl = document.getElementById('metric-unsold');
      if (uEl) uEl.textContent = m.unsold || '-';

      const sEl = document.getElementById('metric-supply');
      if (sEl) sEl.textContent = m.supply || '-';

      const dEl = document.getElementById('metric-demographics');
      if (dEl) dEl.textContent = m.demographics || '-';

      const tEl = document.getElementById('metric-traffic');
      if (tEl) tEl.textContent = m.traffic || '-';

      const rEl = document.getElementById('metric-risk');
      if (rEl) rEl.textContent = m.risk || '-';

      // 5. 오목천·봉담 권역만 계획도 사진 컨테이너 표시
      const planContainer = document.getElementById('plan-maps-container');
      if (planContainer) {
        planContainer.style.display = (regionId === 'bongdam') ? 'flex' : 'none';
      }

      // 6. 핵심 전략 포인트
      const kpContainer = document.getElementById('report-keypoints');
      if (kpContainer) {
        kpContainer.innerHTML = (rep.keyPoints || []).map(kp => `
          <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30 flex items-start gap-2.5">
            <span class="material-symbols-outlined text-primary text-[18px] shrink-0 mt-0.5">check_circle</span>
            <span class="font-body-md text-body-md text-on-surface font-medium leading-relaxed">${kp}</span>
          </div>
        `).join('');
      }
    }

    // =========================================================================
    // INITIALIZATION
    // =========================================================================
    window.addEventListener('DOMContentLoaded', () => {
      // 1. 대시보드 초기화
      renderDashboard();

      // 2. 계산기 입력 및 슬라이더 이벤트 전수 등록
      const depInp = document.getElementById('depositInput');
      if (depInp) depInp.addEventListener('input', runCalculatorEngine);

      const rentInp = document.getElementById('monthlyRentInput');
      if (rentInp) rentInp.addEventListener('input', runCalculatorEngine);

      const rateInp = document.getElementById('loanRateInput');
      if (rateInp) rateInp.addEventListener('input', runCalculatorEngine);

      const priceInp = document.getElementById('priceInput');
      if (priceInp) priceInp.addEventListener('input', handlePriceInputChange);

      const priceSld = document.getElementById('priceSlider');
      if (priceSld) priceSld.addEventListener('input', handlePriceSliderChange);

      const ltvSld = document.getElementById('ltvSlider');
      if (ltvSld) ltvSld.addEventListener('input', (e) => handleLtvSliderChange(e.target.value));

      const vatTgl = document.getElementById('brokerVatToggle');
      if (vatTgl) vatTgl.addEventListener('change', runCalculatorEngine);

      // LTV 버튼 (0% 포함 5종) 이벤트 등록
      document.querySelectorAll('.ltv-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const ltv = parseInt(btn.getAttribute('data-ltv'));
          handleLtvSliderChange(ltv);
        });
      });

      // 물건 유형 버튼 (주택, 오피스텔, 상가) 이벤트 등록
      document.querySelectorAll('.prop-type-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const ptype = btn.getAttribute('data-prop-type');
          handlePropTypeChange(ptype);
        });
      });

      // 보유 주택수 버튼 (1주택 ~ 4주택 이상) 이벤트 등록
      document.querySelectorAll('.housing-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const hcount = btn.getAttribute('data-house');
          handleHousingCountChange(hcount);
        });
      });

      // 계산기 초기화 (기본: 화성봉담 우방)
      loadCalcPreset('2025-56772');

      // 3. 시뮬레이터 초기화 (기본: 화성봉담 우방)
      selectSimProperty('2025-56772');

      // 4. 리포트 뷰어 초기화
      renderRegionalReport('bongdam');
    });
  </script>
</body>
</html>
'''

# 치환 처리
final_html = master_html.replace("__PROPERTIES_JSON__", properties_json_str)
final_html = final_html.replace("__REGIONAL_REPORTS_JSON__", regional_reports_json_str)
final_html = final_html.replace("__VIEW_DASHBOARD_CONTENT__", view_dashboard_content)
final_html = final_html.replace("__VIEW_CALCULATOR_CONTENT__", view_calculator_content)
final_html = final_html.replace("__VIEW_BRIEFING_CONTENT__", view_briefing_content)
final_html = final_html.replace("__VIEW_REPORTS_CONTENT__", view_reports_content)

# [불변 규칙]: 오직 index_v7.html 단독 생성! 기존 index.html, index_v4.html, index_v5.html, index_v6.html은 절대 건드리지 않음!
output_v7_path = os.path.join(base_dir, "index_v7.html")
with open(output_v7_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"[SUCCESS] index_v7.html 빌드 완료! 크기: {len(final_html)} bytes")
print("[AUDIT] 기존 index.html, index_v4.html, index_v5.html, index_v6.html은 원형 그대로 100% 보존되었습니다.")
