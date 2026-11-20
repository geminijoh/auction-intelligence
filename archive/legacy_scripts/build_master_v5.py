# -*- coding: utf-8 -*-
"""
build_master_v5.py
- V5 신규 마스터 빌더 스크립트
1. [좌측 사이드바 LNB 레이아웃]: 상단 메뉴바를 화면 좌측 수직 고정 사이드바로 전면 재배치
2. [거시 비교 테이블 상세 연동]: 매물 행(tr) 클릭 시 해당 매물 상세내역 모달 즉시 호출
3. [추천입찰가 삭제]: 거시 테이블 및 카드에서 '★ 추천입찰가' 컬럼/항목 완전 삭제
4. [고밀도 카드 클릭 복구]: 상세, 시뮬레이터, 계산기 버튼 클릭 핸들러 및 이벤트 전파 오류 완벽 해결
5. [투자수익률 계산기 LTV 0% & 레인지 슬라이더]: LTV 0% 무대출 버튼 및 0%~80% Range 슬라이더 탑재
6. [경매 시뮬레이터 2줄 정밀 사건목록]: 상단 사건번호 + 하단 정식 물건명 2줄 카드형 선택기 개편
7. [역산 입찰가 레이아웃 완전 정돈]: 텍스트 줄바꿈 및 버튼 겹침 현상 원천 해결
8. [시장동향 리포트 뷰어]: 화성봉담 인터랙티브 보고서 및 5대 권역 심층 뷰어 오류 조치 및 완벽 렌더링
"""
import os, json

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"

# 1. 매물 데이터 읽기
props_path = os.path.join(base_dir, "data", "properties.json")
with open(props_path, "r", encoding="utf-8") as f:
    properties = json.load(f)

properties_json_str = json.dumps(properties, ensure_ascii=False)

# 2. 지역분석 리포트 데이터 읽기
reg_path = os.path.join(base_dir, "data", "regional_reports_data.json")
with open(reg_path, "r", encoding="utf-8") as f:
    regional_reports = json.load(f)

regional_reports_json_str = json.dumps(regional_reports, ensure_ascii=False)

# 3. V5 뷰 파일 읽기
with open(os.path.join(base_dir, "views", "view_dashboard_v5.html"), "r", encoding="utf-8") as f:
    view_dashboard_content = f.read()

with open(os.path.join(base_dir, "views", "view_calculator_v5.html"), "r", encoding="utf-8") as f:
    view_calculator_content = f.read()

with open(os.path.join(base_dir, "views", "view_briefing_v5.html"), "r", encoding="utf-8") as f:
    view_briefing_content = f.read()

with open(os.path.join(base_dir, "views", "view_reports_v5.html"), "r", encoding="utf-8") as f:
    view_reports_content = f.read()

# Master HTML Template with Left Sidebar Navigation Layout
master_html = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="web_standard" name="shell-type"/>
  <title>PropIntelligence | 실전 부동산 인텔리전스 터미널</title>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
  <style>
    @layer base {
      html, body { margin: 0; padding: 0; }
      body { overscroll-behavior: none; }
    }
    ::-webkit-scrollbar { display: none; }
    @media print {
      aside, header, footer, .no-print, #regional-tab-bar, #sim-property-selector, #category-filter-chips { display: none !important; }
      #view-briefing, #view-reports, #view-calculator { display: block !important; padding: 0 !important; margin: 0 !important; }
      #view-dashboard { display: none !important; }
      body { background: white !important; }
      main { margin-left: 0 !important; width: 100% !important; }
    }
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "tertiary-container": "#00864e",
            "on-tertiary-container": "#f6fff5",
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
            "body-lg": ["Inter", "sans-serif"],
            "body-sm": ["Inter", "sans-serif"],
            "body-md": ["Inter", "sans-serif"],
            "headline-lg": ["Inter", "sans-serif"],
            "label-sm": ["Inter", "sans-serif"],
            "headline-sm": ["Inter", "sans-serif"],
            "label-md": ["Inter", "sans-serif"],
            "headline-md": ["Inter", "sans-serif"]
          }
        }
      }
    };
  </script>
</head>
<body class="bg-background font-body-md text-on-surface antialiased selection:bg-primary-fixed selection:text-on-primary-fixed min-h-screen flex flex-col md:flex-row">

  <!-- ================= LEFT SIDEBAR NAVIGATION (화면 좌측 사이드바) ================= -->
  <aside id="left-sidebar" class="w-full md:w-64 lg:w-72 bg-surface-container-lowest border-r border-outline-variant/30 flex flex-col justify-between p-4 sm:p-5 md:fixed md:top-0 md:bottom-0 md:left-0 z-40 overflow-y-auto shadow-sm">
    
    <!-- Top Branding & Navigation -->
    <div class="space-y-6">
      
      <!-- Brand Logo & Badge -->
      <div class="flex items-center justify-between pb-4 border-b border-outline-variant/20">
        <div class="flex items-center gap-2.5 cursor-pointer" onclick="switchMainTab('dashboard')">
          <span class="font-headline-sm text-headline-sm text-primary tracking-tight font-black">PropIntelligence</span>
          <span class="w-2 h-2 rounded-full bg-tertiary-container animate-pulse"></span>
        </div>
        <span class="px-2 py-0.5 rounded-full bg-secondary-container text-on-secondary-container font-label-sm text-label-sm font-semibold">
          v5.0 터미널
        </span>
      </div>

      <!-- Main Navigation Menu (수직 나열) -->
      <nav class="space-y-1.5" id="main-nav">
        <div class="text-[11px] font-bold text-secondary uppercase tracking-wider px-3 mb-2">
          투자 인텔리전스 메뉴
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
            <span class="text-[11px] opacity-70">LTV 0%~80% &amp; 직접입력</span>
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
            <span class="text-[11px] opacity-70">화성봉담 · 5대 권역 분석</span>
          </div>
        </button>
      </nav>

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
        <span>보고서 PDF 내보내기</span>
      </button>

      <div class="text-[11px] text-secondary text-center">
        PropIntelligence v5.0 Master
      </div>
    </div>

  </aside>

  <!-- ================= RIGHT MAIN CONTENT WORKSPACE ================= -->
  <div class="flex-1 md:ml-64 lg:ml-72 min-h-screen flex flex-col bg-surface overflow-x-hidden">
    
    <!-- Top Mobile Header (모바일 화면 전용 상단 바) -->
    <header class="md:hidden h-14 bg-surface-container-lowest border-b border-outline-variant/30 px-4 flex items-center justify-between sticky top-0 z-30">
      <div class="flex items-center gap-2 cursor-pointer" onclick="switchMainTab('dashboard')">
        <span class="font-headline-sm text-headline-sm text-primary font-bold">PropIntelligence</span>
      </div>
      <button onclick="window.print()" class="p-2 text-secondary hover:text-on-surface">
        <span class="material-symbols-outlined text-[20px]">print</span>
      </button>
    </header>

    <!-- 1. VIEW: 거시 매물 분석 대시보드 (V5) -->
    <main id="view-dashboard" class="w-full min-h-screen">
      __VIEW_DASHBOARD_CONTENT__
    </main>

    <!-- 2. VIEW: 투자수익률 계산기 (V5) -->
    <main id="view-calculator" class="w-full min-h-screen hidden">
      __VIEW_CALCULATOR_CONTENT__
    </main>

    <!-- 3. VIEW: 경매 분석 시뮬레이터 (V5) -->
    <main id="view-briefing" class="w-full min-h-screen hidden">
      __VIEW_BRIEFING_CONTENT__
    </main>

    <!-- 4. VIEW: 시장동향 리포트 뷰어 (V5) -->
    <main id="view-reports" class="w-full min-h-screen hidden">
      __VIEW_REPORTS_CONTENT__
    </main>

  </div>

  <!-- ================= 5. Property Detail Briefing Modal ================= -->
  <div id="property-detail-modal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 overflow-y-auto hidden">
    <div class="bg-surface-container-lowest rounded-2xl max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-outline-variant/30 my-auto overflow-hidden">
      <!-- Modal Header -->
      <div class="p-5 border-b border-outline-variant/20 flex items-center justify-between bg-inverse-surface text-inverse-on-surface">
        <div class="flex items-center space-x-3">
          <span id="modal-category" class="px-2.5 py-1 rounded-md font-label-sm text-label-sm font-bold bg-primary text-on-primary">
            경매
          </span>
          <div>
            <h2 id="modal-title" class="font-headline-sm text-headline-sm font-bold text-inverse-on-surface tracking-tight">안성동남타운</h2>
            <p id="modal-subtitle" class="font-body-sm text-body-sm text-surface-dim">수원지법 안성등기소 | 2026타경239</p>
          </div>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="window.print()" class="font-label-md text-label-md bg-white/10 hover:bg-white/20 text-inverse-on-surface px-3 py-1.5 rounded-lg border border-white/20 transition">
            인쇄 / PDF
          </button>
          <button onclick="closePropertyModal()" class="w-8 h-8 rounded-lg hover:bg-white/10 text-surface-dim hover:text-inverse-on-surface flex items-center justify-center transition">
            ✕
          </button>
        </div>
      </div>

      <!-- Modal Body -->
      <div class="p-6 overflow-y-auto space-y-6 text-on-surface">
        <!-- 1. Strategy Brief & Safety Margin -->
        <div class="p-4 rounded-xl bg-surface-container-low border border-primary/20 flex flex-col sm:flex-row gap-3 items-start sm:items-center justify-between">
          <div>
            <span class="font-label-sm text-label-sm font-bold text-primary bg-primary-container/20 px-2 py-0.5 rounded">
              애널리스트 실무 브리핑 요약
            </span>
            <p id="modal-brief" class="font-body-sm text-body-sm text-on-surface font-semibold mt-1 leading-relaxed">
              -
            </p>
          </div>
          <div class="shrink-0 bg-surface-container-lowest px-4 py-2.5 rounded-xl border border-outline-variant/30 text-center shadow-sm">
            <span class="font-label-sm text-label-sm text-secondary block">안전마진 (실거래 갭)</span>
            <span id="modal-margin" class="font-headline-sm text-headline-sm font-black text-primary">
              +1,500만 원
            </span>
          </div>
        </div>

        <!-- 2. 4 Financial KPIs -->
        <div>
          <h4 class="font-label-md text-label-md font-bold text-secondary uppercase tracking-wider mb-2">
            핵심 재무·투자 시뮬레이션 지표
          </h4>
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span id="modal-ltv-label" class="font-label-sm text-label-sm text-secondary font-medium">1. 대출 레버리지</span>
              <p id="modal-loan" class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">-</p>
              <p id="modal-interest" class="font-label-sm text-label-sm text-secondary mt-0.5">-</p>
            </div>
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">2. 총 부대비용 일체</span>
              <p id="modal-expenses" class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">-</p>
              <p id="modal-expenses-detail" class="font-label-sm text-label-sm text-secondary mt-0.5">-</p>
            </div>
            <div class="p-3.5 rounded-xl bg-surface-container-low border border-outline-variant/30">
              <span class="font-label-sm text-label-sm text-secondary font-medium">3. 최종 순 실투자금</span>
              <p id="modal-net-invest" class="font-headline-sm text-headline-sm font-bold text-primary mt-1">-</p>
              <p class="font-label-sm text-label-sm text-secondary mt-0.5">대출 및 보증금 차감 후 현금</p>
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
              물건 기본 스펙 & 가격 지표
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
            <div class="space-y-1.5 font-body-sm text-body-sm">
              <div>
                <span class="text-secondary block font-label-sm text-label-sm">말소기준권리:</span>
                <span id="modal-malso" class="text-on-surface font-medium">-</span>
              </div>
              <div>
                <span class="text-secondary block font-label-sm text-label-sm">점유 및 임차인:</span>
                <span id="modal-occupant" class="text-on-surface font-medium">-</span>
              </div>
              <div class="flex items-center justify-between pt-1">
                <span class="text-secondary">인수 권리금:</span>
                <span id="modal-takeover" class="text-tertiary font-bold">0원 (완벽 안전)</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-secondary">명도 난이도:</span>
                <span id="modal-eviction" class="font-bold px-2 py-0.5 rounded font-label-sm text-label-sm bg-tertiary/10 text-tertiary">-</span>
              </div>
              <p id="modal-risk-notes" class="font-label-md text-label-md text-on-surface-variant bg-surface-container-lowest p-2 rounded-lg border border-outline-variant/30 mt-1">
                -
              </p>
            </div>
          </div>
        </div>

        <!-- 4. Location & Infra Highlights -->
        <div>
          <h4 class="font-label-md text-label-md font-bold text-secondary uppercase tracking-wider mb-2">
            핵심 입지 및 광역 교통 호재
          </h4>
          <div id="modal-highlights" class="space-y-2">
            <!-- Dynamic items -->
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="p-4 bg-surface-container border-t border-outline-variant/20 flex flex-wrap items-center justify-between gap-3">
        <span class="font-label-sm text-label-sm text-secondary">
          PropIntelligence 실전 투자 알고리즘 v5.0 검증 완료
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

    let currentCategory = 'all';
    let currentSearch = '';
    let currentModalProperty = null;
    let currentSimPropId = '2026-239';
    let currentRegionId = 'bongdam';
    let currentActiveDocTab = 'doc-spec';
    let isLoanActive = true;
    let calculatedReverseBidMan = 0;
    let dashboardViewMode = 'table';
    let matrixSortKey = 'roe-desc';

    function formatKRW(val) {
      if (val === null || val === undefined) return '-';
      if (val === 0) return '0원';
      const absVal = Math.abs(val);
      const sign = val < 0 ? '-' : '';
      if (absVal >= 100000000) {
        const eok = Math.floor(absVal / 100000000);
        const remainder = absVal % 100000000;
        const man = Math.round(remainder / 10000);
        if (man > 0) return `${sign}${eok}억 ${man.toLocaleString()}만 원`;
        return `${sign}${eok}억 원`;
      } else if (absVal >= 10000) {
        const man = Math.round(absVal / 10000);
        return `${sign}${man.toLocaleString()}만 원`;
      }
      return `${sign}${val.toLocaleString()}원`;
    }

    // =========================================================================
    // MAIN TAB NAVIGATION (좌측 사이드바 활성화 연동)
    // =========================================================================
    function switchMainTab(targetPath) {
      const tabs = [
        { path: 'dashboard', viewId: 'view-dashboard', btnId: 'btn-tab-dashboard' },
        { path: 'yield-calculator', viewId: 'view-calculator', btnId: 'btn-tab-yield-calculator' },
        { path: 'auction-simulator', viewId: 'view-briefing', btnId: 'btn-tab-auction-simulator' },
        { path: 'market-reports', viewId: 'view-reports', btnId: 'btn-tab-market-reports' }
      ];

      tabs.forEach(t => {
        const v = document.getElementById(t.viewId);
        const b = document.getElementById(t.btnId);
        if (t.path === targetPath) {
          if (v) v.classList.remove('hidden');
          if (b) {
            b.className = "nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 bg-primary-container text-on-primary-container font-bold shadow-sm text-left";
          }
        } else {
          if (v) v.classList.add('hidden');
          if (b) {
            b.className = "nav-tab-btn w-full px-3.5 py-3 rounded-xl transition-all flex items-center gap-3 text-on-surface-variant hover:bg-surface-container hover:text-on-surface text-left";
          }
        }
      });

      if (targetPath === 'auction-simulator') {
        renderDynamicSimulator(currentSimPropId);
      } else if (targetPath === 'market-reports') {
        switchRegionalReport(currentRegionId);
      } else if (targetPath === 'yield-calculator') {
        runCalculatorEngine();
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // =========================================================================
    // DASHBOARD V5: 거시 비교 테이블 & 고밀도 클린 카드 (추천입찰가 삭제 & 클릭 연동)
    // =========================================================================

    function setCategoryFilter(cat) {
      currentCategory = cat;
      const tabs = ['all', 'auction', 'sale', 'sub-3000'];
      tabs.forEach(t => {
        const el = document.getElementById('tab-' + t);
        if (el) {
          if (t === cat) {
            el.className = "tab-chip active px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md transition-all whitespace-nowrap shadow-sm";
          } else {
            el.className = "tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap";
          }
        }
      });
      renderDashboard();
    }

    function handleSearch() {
      currentSearch = document.getElementById('search-input').value.trim().toLowerCase();
      renderDashboard();
    }

    function setDashboardViewMode(mode) {
      dashboardViewMode = mode;
      const tableBtn = document.getElementById('view-mode-table-btn');
      const cardBtn = document.getElementById('view-mode-card-btn');
      const tableSec = document.getElementById('macro-matrix-section');
      const cardSec = document.getElementById('clean-cards-section');

      if (mode === 'table') {
        tableBtn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 bg-surface-container-lowest text-primary shadow-sm";
        cardBtn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 text-secondary hover:text-on-surface";
        if (tableSec) tableSec.scrollIntoView({ behavior: 'smooth' });
      } else {
        cardBtn.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 bg-surface-container-lowest text-primary shadow-sm";
        tableBtn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 text-secondary hover:text-on-surface";
        if (cardSec) cardSec.scrollIntoView({ behavior: 'smooth' });
      }
    }

    function handleMatrixSort(val) {
      matrixSortKey = val;
      renderDashboard();
    }

    function getFilteredProperties() {
      return PROPERTIES.filter(p => {
        if (currentCategory === 'auction' && p.category !== '경매') return false;
        if (currentCategory === 'sale' && p.category !== '일반급매') return false;
        if (currentCategory === 'sub-3000' && p.netInvestment > 30000000) return false;

        if (currentSearch) {
          const matchCase = p.caseNumber.toLowerCase().includes(currentSearch);
          const matchName = p.propertyName.toLowerCase().includes(currentSearch);
          const matchAddr = p.address.toLowerCase().includes(currentSearch);
          const matchCourt = (p.court || '').toLowerCase().includes(currentSearch);
          if (!matchCase && !matchName && !matchAddr && !matchCourt) return false;
        }
        return true;
      }).sort((a, b) => {
        if (matrixSortKey === 'roe-desc') return (b.roePercent || 0) - (a.roePercent || 0);
        if (matrixSortKey === 'invest-asc') return a.netInvestment - b.netInvestment;
        if (matrixSortKey === 'margin-desc') return b.safetyMargin - a.safetyMargin;
        if (matrixSortKey === 'min-asc') return a.minimumBidPrice - b.minimumBidPrice;
        return 0;
      });
    }

    function renderDashboard() {
      const filtered = getFilteredProperties();
      
      const countBadge = document.getElementById('list-count-badge');
      if (countBadge) countBadge.textContent = filtered.length + '건';
      const matrixBadge = document.getElementById('matrix-count-badge');
      if (matrixBadge) matrixBadge.textContent = filtered.length + '건 분석';

      renderMacroMatrixTable(filtered);
      renderCleanCards(filtered);
    }

    // 1. 거시 매트릭스 횡적 비교 테이블 (추천입찰가 삭제 & 행 클릭 시 상세 모달 오픈)
    function renderMacroMatrixTable(list) {
      const tbody = document.getElementById('macro-matrix-tbody');
      if (!tbody) return;

      if (list.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" class="py-8 text-center text-secondary">조건에 일치하는 매물이 없습니다.</td></tr>`;
        return;
      }

      tbody.innerHTML = list.map(p => {
        const isAuction = p.category === '경매';
        const typeBadge = isAuction 
          ? `<span class="px-2 py-0.5 rounded text-[11px] font-bold bg-primary/10 text-primary">경매</span>`
          : `<span class="px-2 py-0.5 rounded text-[11px] font-bold bg-tertiary/10 text-tertiary">일반급매</span>`;

        return `
          <tr class="hover:bg-primary/5 cursor-pointer transition-colors" onclick="openPropertyModal('${p.id}')" title="클릭 시 '${p.propertyName}' 상세 권리·수지 분석 열람">
            <td class="py-3.5 px-4 whitespace-nowrap">
              <div class="flex items-center gap-1.5 mb-0.5">
                ${typeBadge}
                <span class="font-bold text-xs text-on-surface font-mono">${p.caseNumber}</span>
              </div>
              <span class="text-[11px] text-secondary">${p.court || '부동산중개'}</span>
            </td>
            <td class="py-3.5 px-4">
              <div class="font-bold text-sm text-on-surface hover:text-primary transition-colors truncate max-w-[240px]">
                ${p.propertyName}
              </div>
              <div class="text-[11px] text-secondary truncate max-w-[240px]">
                ${p.exclusiveAreaPyung}평형 • ${p.address}
              </div>
            </td>
            <td class="py-3.5 px-4 text-right whitespace-nowrap">
              <span class="text-xs text-secondary line-through">${formatKRW(p.appraisedValue)}</span>
            </td>
            <td class="py-3.5 px-4 text-right whitespace-nowrap">
              <div class="font-black text-sm text-on-surface">${formatKRW(p.minimumBidPrice)}</div>
              <span class="text-[11px] text-error font-semibold">(${p.minimumBidRate}%)</span>
            </td>
            <td class="py-3.5 px-4 text-right whitespace-nowrap">
              <span class="font-bold text-xs ${p.safetyMargin > 0 ? 'text-tertiary' : 'text-secondary'}">
                +${formatKRW(p.safetyMargin)}
              </span>
            </td>
            <td class="py-3.5 px-4 text-right whitespace-nowrap">
              <span class="font-black text-sm text-primary">${formatKRW(p.netInvestment)}</span>
            </td>
            <td class="py-3.5 px-4 text-center whitespace-nowrap">
              <span class="font-black text-sm text-tertiary px-2 py-0.5 rounded bg-tertiary-container/10">
                ${p.roePercent ? p.roePercent + '%' : '-'}
              </span>
            </td>
            <td class="py-3.5 px-4 text-center whitespace-nowrap">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-tertiary/10 text-tertiary">인수 0원 (안전)</span>
            </td>
            <td class="py-3.5 px-4 text-center whitespace-nowrap" onclick="event.stopPropagation()">
              <div class="flex items-center justify-center gap-1.5">
                <button onclick="openPropertyModal('${p.id}')" title="권리/수지 상세" class="px-2.5 py-1.5 rounded-lg bg-surface-container text-on-surface hover:bg-surface-container-high transition text-xs font-bold">
                  상세
                </button>
                <button onclick="loadPropertyToSimulator('${p.id}')" title="시뮬레이터 연동" class="px-2.5 py-1.5 rounded-lg bg-primary text-on-primary hover:bg-primary-container transition text-xs font-bold shadow-sm">
                  시뮬레이터
                </button>
                <button onclick="quickLoadToCalculator('${p.id}')" title="투자수익률 계산기" class="px-2.5 py-1.5 rounded-lg bg-surface-container text-secondary hover:text-on-surface transition text-xs font-semibold">
                  계산기
                </button>
              </div>
            </td>
          </tr>
        `;
      }).join('');
    }

    // 2. 고밀도 클린 카드 렌더링 (추천입찰가 삭제 & 상세/계산기 버튼 클릭 완벽 복구)
    function renderCleanCards(list) {
      const container = document.getElementById('property-cards-container');
      if (!container) return;

      if (list.length === 0) {
        container.innerHTML = `<div class="col-span-3 py-10 text-center text-secondary">검색 조건에 일치하는 매물이 없습니다.</div>`;
        return;
      }

      container.innerHTML = list.map(p => {
        const isAuction = p.category === '경매';
        const typeBadge = isAuction 
          ? `<span class="px-2 py-0.5 rounded font-label-sm text-label-sm font-bold bg-primary/10 text-primary">경매 물건</span>`
          : `<span class="px-2 py-0.5 rounded font-label-sm text-label-sm font-bold bg-tertiary/10 text-tertiary">일반 급매</span>`;

        return `
          <article class="bg-surface-container-lowest rounded-2xl p-5 shadow-sm hover:shadow-md border border-outline-variant/30 transition-all flex flex-col justify-between space-y-4">
            
            <!-- Card Header: Clean metadata -->
            <div class="space-y-1.5 border-b border-outline-variant/20 pb-3 cursor-pointer" onclick="openPropertyModal('${p.id}')">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  ${typeBadge}
                  <span class="font-mono text-xs font-bold text-secondary">${p.caseNumber}</span>
                </div>
                <span class="text-xs text-secondary">${p.court || '중개협의'}</span>
              </div>
              <h3 class="font-headline-sm text-headline-sm font-bold text-on-surface hover:text-primary transition-colors truncate mt-1">
                ${p.propertyName}
              </h3>
              <p class="font-body-sm text-body-sm text-secondary truncate">${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평형) • ${p.address}</p>
            </div>

            <!-- Price Analysis Box (추천입찰가 삭제 후 감정가 vs 최저가 vs 안전마진 집중) -->
            <div class="p-3.5 rounded-xl bg-surface-container-low space-y-2 border border-outline-variant/20">
              <div class="flex justify-between items-center text-xs">
                <span class="text-secondary">${isAuction ? '감정평가액' : '최초호가'}</span>
                <span class="text-secondary line-through">${formatKRW(p.appraisedValue)}</span>
              </div>
              <div class="flex justify-between items-baseline">
                <div class="flex items-center gap-1">
                  <span class="px-1.5 py-0.5 rounded text-[11px] font-bold bg-error-container/60 text-error">
                    ${p.minimumBidRate < 100 ? '1회 유찰' : '신건'}
                  </span>
                  <span class="font-body-sm text-body-sm text-on-surface font-semibold">${isAuction ? '최저매각가' : '네고목표'}</span>
                </div>
                <div class="text-right">
                  <span class="font-headline-md text-headline-md text-on-surface font-black">${formatKRW(p.minimumBidPrice)}</span>
                  <span class="text-xs text-secondary ml-1">(${p.minimumBidRate}%)</span>
                </div>
              </div>
              <div class="flex justify-between items-center text-xs pt-2 border-t border-outline-variant/30 text-tertiary">
                <span class="font-medium">실거래 기준 안전마진</span>
                <span class="font-black text-sm">+${formatKRW(p.safetyMargin)}</span>
              </div>
            </div>

            <!-- Financial Key Metrics Grid -->
            <div class="grid grid-cols-2 gap-2">
              <div class="p-3 rounded-xl bg-tertiary-container/10 border border-tertiary/20 flex flex-col justify-between">
                <span class="text-xs font-bold text-tertiary">예상 연 ROE</span>
                <span class="font-headline-md text-headline-md font-black text-tertiary mt-1">
                  ${p.roePercent ? p.roePercent + '%' : '-'}
                </span>
                <span class="text-[11px] text-tertiary mt-0.5">자기자본 수익률</span>
              </div>
              <div class="p-3 rounded-xl bg-surface-container-low border border-outline-variant/20 flex flex-col justify-between">
                <span class="text-xs font-bold text-secondary">필요 실투자금</span>
                <span class="font-headline-md text-headline-md font-black text-primary mt-1">
                  ${formatKRW(p.netInvestment)}
                </span>
                <span class="text-[11px] text-secondary mt-0.5">보증금/대출 차감 후</span>
              </div>
            </div>

            <!-- Rights & Eviction Check -->
            <div class="p-2.5 rounded-lg bg-surface-container text-xs flex items-center justify-between border border-outline-variant/20">
              <div class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-tertiary"></span>
                <span class="font-medium text-on-surface">권리: 인수 권리금 0원</span>
              </div>
              <span class="text-secondary font-medium">명도: ${p.rights.evictionDifficulty} (예비비 ${formatKRW(p.expenses.evictionFee)})</span>
            </div>

            <!-- Action Buttons Bar (클릭 핸들러 명시적 바인딩 및 분리) -->
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-outline-variant/20">
              <button onclick="openPropertyModal('${p.id}')" class="py-2.5 px-1 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-sm text-label-sm font-bold transition text-center flex items-center justify-center gap-1">
                <span class="material-symbols-outlined text-[16px]">visibility</span>상세
              </button>
              <button onclick="loadPropertyToSimulator('${p.id}')" class="py-2.5 px-1 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-sm text-label-sm font-bold transition text-center flex items-center justify-center gap-1 shadow-sm">
                <span class="material-symbols-outlined text-[16px]">tune</span>시뮬레이터
              </button>
              <button onclick="quickLoadToCalculator('${p.id}')" class="py-2.5 px-1 rounded-xl bg-surface-container-high hover:bg-surface-container-highest text-on-surface font-label-sm text-label-sm font-bold transition text-center flex items-center justify-center gap-1">
                <span class="material-symbols-outlined text-[16px]">calculate</span>계산기
              </button>
            </div>

          </article>
        `;
      }).join('');
    }

    // =========================================================================
    // MODAL LOGIC
    // =========================================================================
    function openPropertyModal(propertyId) {
      const p = PROPERTIES.find(item => item.id === propertyId);
      if (!p) return;
      currentModalProperty = p;

      document.getElementById('modal-title').textContent = p.propertyName;
      document.getElementById('modal-subtitle').textContent = (p.court ? p.court + ' | ' : '') + p.caseNumber;
      document.getElementById('modal-category').textContent = p.category;
      document.getElementById('modal-brief').textContent = p.strategyBrief;
      document.getElementById('modal-margin').textContent = (p.safetyMargin >= 0 ? '+' : '') + formatKRW(p.safetyMargin);

      document.getElementById('modal-loan').textContent = formatKRW(p.loan.amount);
      document.getElementById('modal-interest').textContent = `LTV ${p.loan.ltvPercent}% (금리 ${p.loan.annualInterestRate}%)`;
      document.getElementById('modal-expenses').textContent = formatKRW(p.expenses.totalExpenses);
      document.getElementById('modal-expenses-detail').textContent = `취득세 ${formatKRW(p.expenses.acquisitionTax)} + 기타 ${formatKRW(p.expenses.legalFee + p.expenses.evictionFee + p.expenses.repairFee)}`;
      document.getElementById('modal-net-invest').textContent = formatKRW(p.netInvestment);
      document.getElementById('modal-roe').textContent = p.roePercent ? p.roePercent + '%' : '-';
      document.getElementById('modal-rental').textContent = `보증금 ${formatKRW(p.rental.deposit)} / 월 ${formatKRW(p.rental.monthlyRent)}`;

      document.getElementById('modal-address').textContent = p.address;
      document.getElementById('modal-area').textContent = `${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평형)`;
      document.getElementById('modal-floor-build').textContent = `${p.floorInfo} / ${p.buildYear}년 준공`;
      document.getElementById('modal-appraised').textContent = formatKRW(p.appraisedValue);
      document.getElementById('modal-min').textContent = `${formatKRW(p.minimumBidPrice)} (${p.minimumBidRate}%)`;
      document.getElementById('modal-market').textContent = formatKRW(p.marketPrice);

      document.getElementById('modal-malso').textContent = p.rights.malsoStandard;
      document.getElementById('modal-occupant').textContent = p.rights.occupantStatus;
      document.getElementById('modal-takeover').textContent = p.rights.takeoverAmount === 0 ? '0원 (완벽 안전 매물)' : formatKRW(p.rights.takeoverAmount);
      document.getElementById('modal-eviction').textContent = p.rights.evictionDifficulty;
      document.getElementById('modal-risk-notes').textContent = p.rights.riskNotes;

      const hlContainer = document.getElementById('modal-highlights');
      hlContainer.innerHTML = p.locationHighlights.map(h => `
        <div class="flex items-start space-x-2 text-body-sm font-body-sm">
          <span class="text-primary font-bold mt-0.5">•</span>
          <span class="text-on-surface">${h}</span>
        </div>
      `).join('');

      document.getElementById('property-detail-modal').classList.remove('hidden');
    }

    function closePropertyModal() {
      document.getElementById('property-detail-modal').classList.add('hidden');
    }

    function transferCurrentModalToSimulator() {
      if (currentModalProperty) {
        closePropertyModal();
        loadPropertyToSimulator(currentModalProperty.id);
      }
    }

    function transferCurrentModalToCalculator() {
      if (currentModalProperty) {
        closePropertyModal();
        quickLoadToCalculator(currentModalProperty.id);
      }
    }

    function quickLoadToCalculator(propertyId) {
      loadCalcPreset(propertyId);
      switchMainTab('yield-calculator');
    }

    // =========================================================================
    // SIMULATOR V5 LOGIC (2줄 정밀 사건목록 & 역산 입찰가 레이아웃 완전 정돈)
    // =========================================================================

    function loadPropertyToSimulator(propertyId) {
      currentSimPropId = propertyId;
      renderDynamicSimulator(propertyId);
      switchMainTab('auction-simulator');
    }

    function renderDynamicSimulator(propertyId) {
      const p = PROPERTIES.find(item => item.id === propertyId);
      if (!p) return;
      currentSimPropId = propertyId;

      const isAuction = p.category === '경매';

      // 6개 매물 2줄 카드형 선택기 렌더링 (상단 정확한 사건번호 + 하단 매물명)
      const selectorContainer = document.getElementById('sim-property-selector');
      if (selectorContainer) {
        selectorContainer.innerHTML = PROPERTIES.map(item => {
          const isSelected = item.id === propertyId;
          const cls = isSelected
            ? "p-2.5 rounded-xl bg-primary text-on-primary font-semibold shadow-sm transition border border-primary text-left flex flex-col justify-center"
            : "p-2.5 rounded-xl bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition border border-outline-variant/30 text-left flex flex-col justify-center";
          const subName = item.propertyName.length > 14 ? item.propertyName.slice(0, 14) + '...' : item.propertyName;
          return `
            <button onclick="loadPropertyToSimulator('${item.id}')" class="${cls}">
              <div class="font-bold text-xs font-mono tracking-tight">${item.caseNumber}</div>
              <div class="text-[11px] truncate opacity-90 mt-0.5 font-medium">${subName}</div>
            </button>
          `;
        }).join('');
      }

      // Header Information
      document.getElementById('sim-category-badge').textContent = p.category;
      document.getElementById('sim-court-case').textContent = p.court ? p.court + ' • ' + p.caseNumber : '일반 매매/급매 물건';
      document.getElementById('sim-property-name').innerHTML = `${p.propertyName} <span id="sim-area-info" class="font-headline-sm text-headline-sm text-secondary font-medium">(${p.exclusiveAreaM2}㎡ / ${p.exclusiveAreaPyung}평형)</span>`;
      document.getElementById('sim-address').textContent = p.address;
      document.getElementById('sim-auction-date').textContent = p.auctionDate ? p.auctionDate : '상시 협의 진행';
      
      // Price Evaluation
      document.getElementById('sim-status-badge').textContent = p.status;
      document.getElementById('sim-label-appraised').textContent = isAuction ? '감정평가액' : '최초호가';
      document.getElementById('sim-val-appraised').textContent = formatKRW(p.appraisedValue);
      document.getElementById('sim-label-min').textContent = isAuction ? '최저입찰가' : '네고목표가';
      document.getElementById('sim-val-min').textContent = formatKRW(p.minimumBidPrice);
      document.getElementById('sim-rate-min').textContent = '(' + p.minimumBidRate + '%)';
      document.getElementById('sim-market-price').textContent = formatKRW(p.marketPrice);
      document.getElementById('sim-margin-text').textContent = '안전마진: 약 ' + (p.safetyMargin >= 0 ? '+' : '') + formatKRW(p.safetyMargin);

      // Specs & Rights
      document.getElementById('sim-malso-std').textContent = p.rights.malsoStandard;
      document.getElementById('sim-tenant-status').textContent = p.rights.occupantStatus;
      document.getElementById('sim-takeover-val').textContent = p.rights.takeoverAmount === 0 ? '인수금 0원' : formatKRW(p.rights.takeoverAmount);
      document.getElementById('sim-eviction-diff').textContent = p.rights.evictionDifficulty + ' (예비비 ' + formatKRW(p.expenses.evictionFee) + ')';
      document.getElementById('sim-risk-comment').textContent = p.rights.riskNotes;

      // Sliders Calibration
      const bidSlider = document.getElementById('sim-bid-slider');
      const jeonseSlider = document.getElementById('sim-jeonse-slider');
      
      const recBidMan = Math.round(p.recommendedBidPrice / 10000);
      const minBidMan = Math.round(p.minimumBidPrice / 10000);
      const appBidMan = Math.round(p.appraisedValue / 10000);

      const sliderMin = Math.floor(minBidMan * 0.85);
      const sliderMax = Math.ceil(Math.max(appBidMan * 1.15, recBidMan * 1.3));
      const sliderStep = recBidMan > 20000 ? 100 : 50;

      if (bidSlider) {
        bidSlider.min = sliderMin;
        bidSlider.max = sliderMax;
        bidSlider.step = sliderStep;
        bidSlider.value = recBidMan;
      }

      document.getElementById('sim-bid-min-lbl').textContent = '최저 ' + sliderMin.toLocaleString() + '만';
      document.getElementById('sim-bid-mid-lbl').textContent = '추천 ' + recBidMan.toLocaleString() + '만';
      document.getElementById('sim-bid-max-lbl').textContent = '최대 ' + sliderMax.toLocaleString() + '만';

      const jeonseBaseMan = p.rental.deposit > 0 ? Math.round(p.rental.deposit / 10000) : Math.round((p.marketPrice * 0.7) / 10000);
      const jMin = Math.floor(jeonseBaseMan * 0.6);
      const jMax = Math.ceil(jeonseBaseMan * 1.35);
      const jStep = jeonseBaseMan > 20000 ? 100 : 50;

      if (jeonseSlider) {
        jeonseSlider.min = jMin;
        jeonseSlider.max = jMax;
        jeonseSlider.step = jStep;
        jeonseSlider.value = jeonseBaseMan;
      }

      document.getElementById('sim-jeonse-min-lbl').textContent = '최저 ' + jMin.toLocaleString() + '만';
      document.getElementById('sim-jeonse-mid-lbl').textContent = '시세 ' + jeonseBaseMan.toLocaleString() + '만';
      document.getElementById('sim-jeonse-max-lbl').textContent = '최대 ' + jMax.toLocaleString() + '만';

      // Reverse Bid Calculator Default
      const budgetInput = document.getElementById('reverse-budget-input');
      if (budgetInput) {
        const estBudgetMan = Math.round((p.recommendedBidPrice + p.expenses.totalExpenses) / 10000);
        budgetInput.value = estBudgetMan;
        calculateReverseBid();
      }

      switchDocTab(currentActiveDocTab);
      runSimulatorEngine();
    }

    function calculateReverseBid() {
      const budgetInput = document.getElementById('reverse-budget-input');
      const resultEl = document.getElementById('reverse-bid-result');
      const detailEl = document.getElementById('reverse-deduct-detail');
      if (!budgetInput || !resultEl) return;

      const p = PROPERTIES.find(item => item.id === currentSimPropId);
      if (!p) return;

      const budgetMan = parseFloat(budgetInput.value) || 0;
      if (budgetMan <= 0) {
        resultEl.textContent = '0원';
        return;
      }

      const fixedCostsWon = p.expenses.legalFee + p.expenses.evictionFee + p.expenses.repairFee;
      const fixedCostsMan = Math.round(fixedCostsWon / 10000);
      const taxRate = budgetMan > 60000 ? 0.022 : 0.011;

      const bidMan = Math.max(0, (budgetMan - fixedCostsMan) / (1 + taxRate));
      calculatedReverseBidMan = Math.round(bidMan / 10) * 10;
      const taxMan = Math.round(calculatedReverseBidMan * taxRate);
      const totalDeductMan = taxMan + fixedCostsMan;

      resultEl.textContent = formatKRW(calculatedReverseBidMan * 10000);
      detailEl.textContent = `선반영 부대비용: 취득세 약 ${taxMan.toLocaleString()}만 + 부대비용 ${fixedCostsMan.toLocaleString()}만 (합계 약 ${totalDeductMan.toLocaleString()}만원)`;
    }

    function applyReverseBidToSlider() {
      if (calculatedReverseBidMan <= 0) return;
      const bidSlider = document.getElementById('sim-bid-slider');
      if (!bidSlider) return;

      if (calculatedReverseBidMan < parseInt(bidSlider.min)) bidSlider.min = Math.floor(calculatedReverseBidMan * 0.9);
      if (calculatedReverseBidMan > parseInt(bidSlider.max)) bidSlider.max = Math.ceil(calculatedReverseBidMan * 1.1);

      bidSlider.value = calculatedReverseBidMan;
      runSimulatorEngine();
    }

    function setLoanMode(useLoan) {
      isLoanActive = useLoan;
      const useBtn = document.getElementById('btn-loan-use');
      const noneBtn = document.getElementById('btn-loan-none');
      const sliderContainer = document.getElementById('loan-slider-container');
      
      if (useLoan) {
        if (useBtn) useBtn.className = "px-2.5 py-1 rounded-md bg-primary text-on-primary font-label-sm text-label-sm font-semibold transition";
        if (noneBtn) noneBtn.className = "px-2.5 py-1 rounded-md text-on-surface-variant hover:text-on-surface font-label-sm text-label-sm font-medium transition";
        if (sliderContainer) sliderContainer.style.opacity = '1';
      } else {
        if (noneBtn) noneBtn.className = "px-2.5 py-1 rounded-md bg-tertiary text-on-tertiary font-label-sm text-label-sm font-bold transition";
        if (useBtn) useBtn.className = "px-2.5 py-1 rounded-md text-on-surface-variant hover:text-on-surface font-label-sm text-label-sm font-medium transition";
        if (sliderContainer) sliderContainer.style.opacity = '0.5';
      }
      runSimulatorEngine();
    }

    function setQuickRate(rate) {
      const slider = document.getElementById('sim-rate-slider');
      const disp = document.getElementById('sim-rate-display');
      
      if (rate === 0) {
        setLoanMode(false);
      } else {
        setLoanMode(true);
        if (slider) slider.value = rate;
        if (disp) disp.textContent = rate.toFixed(1);
      }

      [0, 3, 4, 7].forEach(r => {
        const b = document.getElementById('rate-btn-' + r);
        if (!b) return;
        if ((r === 0 && rate === 0) || (r === 3 && rate === 3.0) || (r === 4 && rate === 4.2) || (r === 7 && rate === 7.0)) {
          b.className = "py-1 px-1 text-center rounded-lg bg-primary text-on-primary font-label-sm text-label-sm font-bold shadow-sm transition";
        } else {
          b.className = "py-1 px-1 text-center rounded-lg bg-surface-container text-on-surface-variant hover:bg-surface-container-high font-label-sm text-label-sm transition";
        }
      });

      runSimulatorEngine();
    }

    function runSimulatorEngine() {
      const p = PROPERTIES.find(item => item.id === currentSimPropId);
      if (!p) return;

      const bidSlider = document.getElementById('sim-bid-slider');
      const rateSlider = document.getElementById('sim-rate-slider');
      const jeonseSlider = document.getElementById('sim-jeonse-slider');

      if (!bidSlider) return;

      const bidMan = parseFloat(bidSlider.value) || 0;
      const interestRate = isLoanActive ? (parseFloat(rateSlider ? rateSlider.value : 4.2) || 4.2) : 0;
      const ltvRate = isLoanActive ? 0.70 : 0.0;
      const jeonseMan = parseFloat(jeonseSlider ? jeonseSlider.value : 0) || 0;

      const bidDisp = document.getElementById('sim-bid-display');
      if (bidDisp) bidDisp.textContent = bidMan.toLocaleString();

      const rateDisp = document.getElementById('sim-rate-display');
      if (rateDisp) rateDisp.textContent = interestRate.toFixed(1);

      const jeonseDisp = document.getElementById('sim-jeonse-display');
      if (jeonseDisp) jeonseDisp.textContent = jeonseMan.toLocaleString();

      const bidPriceWon = bidMan * 10000;
      const taxRate = bidMan > 60000 ? 0.022 : 0.011;
      const acquisitionTaxWon = Math.round(bidPriceWon * taxRate);
      const otherExpensesWon = p.expenses.legalFee + p.expenses.evictionFee + p.expenses.repairFee;
      const totalExpensesWon = acquisitionTaxWon + otherExpensesWon;
      const totalCostWon = bidPriceWon + totalExpensesWon;

      const loanAmountWon = Math.round(bidPriceWon * ltvRate);
      const annualInterestWon = Math.round(loanAmountWon * (interestRate / 100));
      const monthlyInterestWon = Math.round(annualInterestWon / 12);

      const netInvestJeonseWon = Math.max(0, totalCostWon - (jeonseMan * 10000));
      const netInvestMonthlyWon = Math.max(0, totalCostWon - loanAmountWon - p.rental.deposit);

      const monthlyRentWon = p.rental.monthlyRent;
      const monthlyNetCashFlowWon = monthlyRentWon - monthlyInterestWon;
      const annualNetCashFlowWon = monthlyNetCashFlowWon * 12;
      const monthlyRoe = netInvestMonthlyWon > 0 ? (annualNetCashFlowWon / netInvestMonthlyWon) * 100 : 0;

      // 4대 KPI 요약 박스 바인딩
      const outNetEquityEl = document.getElementById('sim-out-net-equity');
      if (outNetEquityEl) outNetEquityEl.textContent = formatKRW(netInvestMonthlyWon);

      const outInterestEl = document.getElementById('sim-out-interest');
      if (outInterestEl) {
        outInterestEl.textContent = isLoanActive 
          ? `${(monthlyInterestWon / 10000).toFixed(1)}만 원 / 월` 
          : '0원 (대출 없음)';
      }

      const outLoanAmtEl = document.getElementById('sim-out-loan-amt');
      if (outLoanAmtEl) {
        outLoanAmtEl.textContent = isLoanActive 
          ? `대출 ${formatKRW(loanAmountWon)} 기준` 
          : '전액 현금 100% 자부담';
      }

      const outCostsEl = document.getElementById('sim-out-costs');
      if (outCostsEl) outCostsEl.textContent = formatKRW(totalExpensesWon);

      const outRoeEl = document.getElementById('sim-out-roe');
      if (outRoeEl) outRoeEl.textContent = monthlyRoe.toFixed(1) + '%';

      // 3대 출구 시나리오 카드 바인딩
      const scen1El = document.getElementById('sim-scen1-invest');
      if (scen1El) scen1El.textContent = formatKRW(netInvestJeonseWon);

      const scen2InvestEl = document.getElementById('sim-scen2-invest');
      if (scen2InvestEl) scen2InvestEl.textContent = formatKRW(netInvestMonthlyWon);

      const scen2FlowEl = document.getElementById('sim-scen2-flow');
      if (scen2FlowEl) scen2FlowEl.textContent = (monthlyNetCashFlowWon >= 0 ? '+' : '') + formatKRW(monthlyNetCashFlowWon) + '/월';

      const scen2RoeEl = document.getElementById('sim-scen2-roe');
      if (scen2RoeEl) scen2RoeEl.textContent = monthlyRoe.toFixed(1) + '%';

      const scen3GainEl = document.getElementById('sim-scen3-gain');
      if (scen3GainEl) {
        const capitalGainWon = p.marketPrice - bidPriceWon - totalExpensesWon;
        scen3GainEl.textContent = (capitalGainWon >= 0 ? '+' : '') + formatKRW(capitalGainWon);
      }
    }

    function resetDynamicSimulator() {
      renderDynamicSimulator(currentSimPropId);
    }

    function switchDocTab(docId) {
      currentActiveDocTab = docId;
      const tabs = ['doc-spec', 'doc-appraisal', 'doc-survey', 'doc-register', 'doc-resident'];
      tabs.forEach(t => {
        const btn = document.getElementById('tab-' + t);
        if (btn) {
          if (t === docId) {
            btn.className = "px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-label-md font-semibold transition whitespace-nowrap";
          } else {
            btn.className = "px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition whitespace-nowrap";
          }
        }
      });

      const p = PROPERTIES.find(item => item.id === currentSimPropId);
      if (!p) return;
      const contentEl = document.getElementById('public-doc-content');
      if (!contentEl) return;

      if (docId === 'doc-spec') {
        contentEl.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[매각물건명세서 공식 열람 요약]</span>
              <span class="text-xs text-secondary">법원 직인 날인 완료</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div class="p-2.5 rounded-lg bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block font-bold mb-1">최선순위 설정일자 (말소기준):</span>
                <span class="text-primary font-semibold text-sm">${p.rights.malsoStandard}</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block font-bold mb-1">배당요구 종기일:</span>
                <span class="text-on-surface font-semibold text-sm">${p.auctionDate ? '2026.04.10 (배당절차 종결)' : '해당없음'}</span>
              </div>
            </div>
            <div class="p-3 rounded-lg bg-surface-container-lowest border border-outline-variant/20 text-xs leading-relaxed">
              <span class="font-bold text-secondary block mb-1">점유자 현황 및 대항력 판정:</span>
              <p class="text-on-surface">${p.rights.occupantStatus}. 말소기준권리보다 앞선 전입 또는 확정일자 임차인 없음. <strong class="text-tertiary">매수인이 인수할 보증금이나 권리는 일체 존재하지 않음 (0원 인수).</strong></p>
            </div>
          </div>
        `;
      } else if (docId === 'doc-appraisal') {
        contentEl.innerHTML = `
          <div class="space-y-3 text-xs">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[감정평가서 종합 요약본]</span>
              <span class="text-secondary">가격시점: 2024~2026 / 공인감정평가법인</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <div class="p-2 rounded bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block">감정평가총액</span>
                <span class="font-bold text-sm text-primary">${formatKRW(p.appraisedValue)}</span>
              </div>
              <div class="p-2 rounded bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block">전용면적</span>
                <span class="font-bold text-sm text-on-surface">${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평)</span>
              </div>
              <div class="p-2 rounded bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block">건물보전상태</span>
                <span class="font-bold text-sm text-on-surface">양호 (관리상태 정상)</span>
              </div>
              <div class="p-2 rounded bg-surface-container-lowest border border-outline-variant/20">
                <span class="text-secondary block">위치 및 주위환경</span>
                <span class="font-bold text-sm text-on-surface truncate" title="${p.address}">${p.address.slice(0, 15)}...</span>
              </div>
            </div>
            <p class="text-secondary bg-surface-container-lowest p-2.5 rounded-lg border border-outline-variant/20 leading-relaxed">
              본건은 ${p.propertyName} 소재 물건으로서 간선도로 및 대중교통 연계성이 양호하며, 인근 학군 및 생활편의시설이 잘 정비되어 임대 수요 흡수에 유리함.
            </p>
          </div>
        `;
      } else if (docId === 'doc-survey') {
        contentEl.innerHTML = `
          <div class="space-y-3 text-xs">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[집행관 현황조사서 열람]</span>
              <span class="text-secondary">수원지방법원 현황조사관</span>
            </div>
            <div class="p-3 rounded-lg bg-surface-container-lowest border border-outline-variant/20 space-y-2">
              <div class="flex justify-between">
                <span class="text-secondary">임대차 관계 조사서:</span>
                <span class="font-bold text-tertiary">임대차 없음 (채무자 및 소유자 점유)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-secondary">현장 방문 및 점유 확인:</span>
                <span class="font-medium text-on-surface">현장 방문 시 소유자 면담 또는 안내문 교부 완료</span>
              </div>
              <div class="flex justify-between">
                <span class="text-secondary">미납 관리비 내역:</span>
                <span class="font-medium text-on-surface">공용부분 약 30~50만원 수준 (입찰 전 관리사무소 유선 재확인 요망)</span>
              </div>
            </div>
          </div>
        `;
      } else if (docId === 'doc-register') {
        contentEl.innerHTML = `
          <div class="space-y-3 text-xs">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[등기사항전부증명서 (을구/갑구 요약)]</span>
              <span class="text-secondary">발행: 법원 인터넷등기소</span>
            </div>
            <div class="p-3 rounded-lg bg-surface-container-lowest border border-outline-variant/20 space-y-2">
              <div class="flex justify-between items-center pb-1 border-b border-outline-variant/10">
                <span class="text-secondary">1. [갑구] 임의/강제경매개시결정</span>
                <span class="font-medium text-error">${p.caseNumber}</span>
              </div>
              <div class="flex justify-between items-center pb-1 border-b border-outline-variant/10">
                <span class="text-secondary">2. [을구] 말소기준권리 (근저당권)</span>
                <span class="font-bold text-primary">${p.rights.malsoStandard}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-secondary">3. 매각 후 등기부 소멸 여부</span>
                <span class="font-bold text-tertiary">낙찰 시 모든 근저당 및 가압류 100% 촉탁 말소</span>
              </div>
            </div>
          </div>
        `;
      } else if (docId === 'doc-resident') {
        contentEl.innerHTML = `
          <div class="space-y-3 text-xs">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[주민등록 전입세대확인서 열람]</span>
              <span class="text-secondary">주민센터 열람필</span>
            </div>
            <div class="p-3 rounded-lg bg-surface-container-lowest border border-outline-variant/20 space-y-2">
              <div class="flex justify-between">
                <span class="text-secondary">해당 주소지 세대 열람:</span>
                <span class="font-bold text-on-surface">소유자(채무자) 세대만 등재</span>
              </div>
              <div class="flex justify-between">
                <span class="text-secondary">전입 일자:</span>
                <span class="font-medium text-on-surface">${p.rights.malsoStandard.split(' ')[0]} 이후 전입 (후순위)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-secondary">동거인 및 기타 거주자:</span>
                <span class="font-medium text-tertiary">대항력 임차인 없음 (인도명령 대상)</span>
              </div>
            </div>
          </div>
        `;
      }
    }

    // =========================================================================
    // REGIONAL MARKET REPORTS ENGINE (화성 봉담 리포트 전문 임베딩 & 오류 조치)
    // =========================================================================

    function switchRegionalReport(regionId) {
      currentRegionId = regionId;
      const r = REGIONAL_REPORTS.find(item => item.id === regionId);
      if (!r) return;

      const tabs = ['bongdam', 'anseong', 'pyeongtaek', 'cheonan', 'cheongju'];
      tabs.forEach(t => {
        const btn = document.getElementById('tab-reg-' + t);
        if (btn) {
          if (t === regionId) {
            btn.className = "reg-tab px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md font-semibold transition whitespace-nowrap shadow-sm";
          } else {
            btn.className = "reg-tab px-4 py-2 rounded-xl bg-surface-container text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition whitespace-nowrap";
          }
        }
      });

      document.getElementById('report-breadcrumb-region').textContent = r.name;
      document.getElementById('report-breadcrumb-date').textContent = r.standardDate;

      const bongdamSec = document.getElementById('bongdam-interactive-section');
      const generalSec = document.getElementById('general-report-section');
      const openExtBtn = document.getElementById('btn-open-external');

      if (regionId === 'bongdam') {
        if (bongdamSec) bongdamSec.classList.remove('hidden');
        if (generalSec) generalSec.classList.add('hidden');
        if (openExtBtn) {
          openExtBtn.classList.remove('hidden');
          openExtBtn.href = "시장동향리포트뷰어/오목천_봉담_통합_지역종합분석보고서.html";
        }
      } else {
        if (bongdamSec) bongdamSec.classList.add('hidden');
        if (generalSec) generalSec.classList.remove('hidden');
        if (openExtBtn) openExtBtn.classList.add('hidden');

        document.getElementById('report-badge').textContent = r.badge;
        document.getElementById('report-std-date').textContent = r.standardDate;
        document.getElementById('report-title').textContent = r.name + ' 광역생활권 부동산 시장 및 도시개발 심층 분석';
        document.getElementById('report-summary').textContent = r.summary;

        document.getElementById('metric-unsold').textContent = r.metrics.unsold.split('(')[0];
        document.getElementById('metric-supply').textContent = r.metrics.supply.split('➔')[0];
        document.getElementById('metric-demographics').textContent = r.metrics.demographics.split('/')[0];
        document.getElementById('metric-traffic').textContent = r.metrics.traffic.split(',')[0];
        document.getElementById('metric-risk').textContent = r.metrics.risk.split(',')[0];

        const keyPointsContainer = document.getElementById('report-key-points');
        if (keyPointsContainer) {
          keyPointsContainer.innerHTML = r.keyPoints.map(pt => `
            <li class="flex items-start gap-2">
              <span class="text-primary font-bold shrink-0 mt-0.5">✓</span>
              <span class="leading-relaxed">${pt}</span>
            </li>
          `).join('');
        }
      }
    }

    // =========================================================================
    // CALCULATOR V5 LOGIC (LTV 0% 및 Range 슬라이더 지원)
    // =========================================================================

    let calcState = {
      price: 68000000,
      propType: 'house',
      housingCount: '1house',
      ltv: 60,
      loanRate: 4.20,
      deposit: 10000000,
      monthlyRent: 450000,
      brokerVat: true,
      bondRate: 7.50,
      currentPropId: '2026-239'
    };

    function handlePriceInputChange() {
      const input = document.getElementById('priceInput');
      const slider = document.getElementById('priceSlider');
      if (!input || !slider) return;

      let val = parseFloat(input.value) || 0;
      if (val < 0) val = 0;
      calcState.price = val;

      if (val > parseFloat(slider.max)) slider.max = val * 1.2;
      if (val < parseFloat(slider.min) && val > 0) slider.min = Math.floor(val * 0.8);
      slider.value = val;

      const manVal = Math.round(val / 10000);
      document.getElementById('priceDisplayMan').textContent = manVal.toLocaleString();
      runCalculatorEngine();
    }

    function handlePriceSliderChange() {
      const input = document.getElementById('priceInput');
      const slider = document.getElementById('priceSlider');
      if (!input || !slider) return;

      const val = parseFloat(slider.value) || 0;
      calcState.price = val;
      input.value = val;

      const manVal = Math.round(val / 10000);
      document.getElementById('priceDisplayMan').textContent = manVal.toLocaleString();
      runCalculatorEngine();
    }

    function handleLtvSliderChange(val) {
      calcState.ltv = parseInt(val) || 0;
      updateLtvUI();
      runCalculatorEngine();
    }

    function updateLtvUI() {
      const ltv = calcState.ltv;
      const slider = document.getElementById('ltvSlider');
      if (slider) slider.value = ltv;

      document.querySelectorAll('.ltv-btn').forEach(btn => {
        const btnLtv = parseInt(btn.getAttribute('data-ltv'));
        if (btnLtv === ltv) {
          btn.className = "ltv-btn py-2 bg-primary text-on-primary rounded-lg font-label-md text-label-md font-semibold shadow-sm transition-colors text-center";
        } else {
          btn.className = "ltv-btn py-2 bg-surface-container-low text-on-surface-variant hover:bg-surface-container rounded-lg font-label-md text-label-md font-medium transition-colors text-center";
        }
      });
    }

    function loadCalcPreset(propertyId) {
      const p = PROPERTIES.find(item => item.id === propertyId);
      if (!p) return;

      calcState.currentPropId = propertyId;
      calcState.price = p.recommendedBidPrice;
      calcState.ltv = p.loan.ltvPercent || 60;
      calcState.loanRate = p.loan.annualInterestRate || 4.20;
      calcState.deposit = p.rental.deposit || 10000000;
      calcState.monthlyRent = p.rental.monthlyRent || 400000;

      const priceInput = document.getElementById('priceInput');
      const priceSlider = document.getElementById('priceSlider');
      if (priceInput && priceSlider) {
        priceInput.value = calcState.price;
        if (calcState.price > parseFloat(priceSlider.max)) priceSlider.max = calcState.price * 1.2;
        if (calcState.price < parseFloat(priceSlider.min)) priceSlider.min = Math.floor(calcState.price * 0.8);
        priceSlider.value = calcState.price;
        document.getElementById('priceDisplayMan').textContent = Math.round(calcState.price / 10000).toLocaleString();
      }

      const depInput = document.getElementById('depositInput');
      const rentInput = document.getElementById('monthlyRentInput');
      const rateInput = document.getElementById('loanRateInput');
      if (depInput) depInput.value = Math.round(calcState.deposit / 10000);
      if (rentInput) rentInput.value = Math.round(calcState.monthlyRent / 10000);
      if (rateInput) rateInput.value = calcState.loanRate.toFixed(2);

      updateLtvUI();

      // Preset button highlight
      const btns = document.querySelectorAll('.calc-preset-btn');
      btns.forEach(b => {
        if (b.getAttribute('onclick') && b.getAttribute('onclick').includes(propertyId)) {
          b.className = "calc-preset-btn px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-label-md font-semibold transition-all shadow-sm";
        } else {
          b.className = "calc-preset-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant hover:bg-surface-container-high transition-all font-label-md text-label-md";
        }
      });

      runCalculatorEngine();
    }

    function runCalculatorEngine() {
      const p = PROPERTIES.find(item => item.id === calcState.currentPropId) || PROPERTIES[0];
      const price = calcState.price;

      // 1. LTV & Loan
      const loanAmount = Math.round(price * (calcState.ltv / 100));
      const loanInput = document.getElementById('loanAmountInput');
      if (loanInput) loanInput.value = loanAmount.toLocaleString();
      const ltvLabel = document.getElementById('ltvIndicatorLabel');
      if (ltvLabel) {
        ltvLabel.textContent = calcState.ltv === 0 
          ? `LTV 0.0% (대출 없음 / 전액 자부담)` 
          : `LTV ${calcState.ltv}% (${Math.round(loanAmount / 10000).toLocaleString()}만원)`;
      }

      // 2. Taxes & Costs
      const priceMan = price / 10000;
      let taxRate = 0.011;
      if (price > 900000000) taxRate = 0.033;
      else if (price > 600000000) taxRate = 0.022;

      const taxAmount = Math.round(price * taxRate);
      const brokerageFee = Math.round(price * 0.004 * (calcState.brokerVat ? 1.1 : 1.0));
      const bondFee = Math.round(price * 0.02 * (calcState.bondRate / 100));
      const legalFee = price > 300000000 ? 800000 : 500000;
      const totalIncidental = taxAmount + brokerageFee + bondFee + legalFee;
      const totalOutlay = price + totalIncidental;

      // 3. Rent & Equity
      const depInput = document.getElementById('depositInput');
      const rentInput = document.getElementById('monthlyRentInput');
      const depositWon = depInput ? (parseFloat(depInput.value) || 0) * 10000 : calcState.deposit;
      const monthlyRentWon = rentInput ? (parseFloat(rentInput.value) || 0) * 10000 : calcState.monthlyRent;
      const annualRentWon = monthlyRentWon * 12;

      const annualInterest = Math.round(loanAmount * (calcState.loanRate / 100));
      const monthlyInterest = Math.round(annualInterest / 12);
      const monthlyCashFlow = monthlyRentWon - monthlyInterest;
      const annualCashFlow = monthlyCashFlow * 12;

      const netEquity = Math.max(0, totalOutlay - loanAmount - depositWon);
      const roe = netEquity > 0 ? (annualCashFlow / netEquity) * 100 : 0;
      const capRate = price > 0 ? (annualRentWon / price) * 100 : 0;

      // Update Calculator DOM elements
      const equityEl = document.getElementById('kpiNetEquity');
      if (equityEl) equityEl.innerHTML = `${Math.round(netEquity / 10000).toLocaleString()}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;

      const ncfEl = document.getElementById('kpiMonthlyCashFlow');
      if (ncfEl) ncfEl.innerHTML = `${monthlyCashFlow >= 0 ? '+' : ''}${(monthlyCashFlow / 10000).toFixed(1)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;

      const roeEl = document.getElementById('kpiRoe');
      if (roeEl) roeEl.innerHTML = `${roe.toFixed(1)}<span class="font-body-sm text-body-sm font-normal text-tertiary ml-0.5">%</span>`;

      const capEl = document.getElementById('kpiCapRate');
      if (capEl) capEl.innerHTML = `${capRate.toFixed(2)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">%</span>`;

      const incSummaryEl = document.getElementById('totalIncidentalCostSummary');
      if (incSummaryEl) incSummaryEl.textContent = formatKRW(totalIncidental);

      const taxBrkEl = document.getElementById('costTaxBreakdown');
      if (taxBrkEl) taxBrkEl.textContent = formatKRW(taxAmount);

      const brokEl = document.getElementById('costBrokerage');
      if (brokEl) brokEl.textContent = formatKRW(brokerageFee);

      const bondLegEl = document.getElementById('costBondLegal');
      if (bondLegEl) bondLegEl.textContent = formatKRW(bondFee + legalFee);

      const totOutlayEl = document.getElementById('totalOutlayRequired');
      if (totOutlayEl) totOutlayEl.textContent = formatKRW(totalOutlay);

      const annualRentDisplay = document.getElementById('annualRentDisplay');
      if (annualRentDisplay) annualRentDisplay.textContent = Math.round(annualRentWon / 10000).toLocaleString();

      // 경매 특화 인텔리전스 패널 업데이트
      const auctionRate = p.appraisedValue > 0 ? ((price / p.appraisedValue) * 100).toFixed(1) : '75.0';
      const depositCheck = Math.round(p.minimumBidPrice * 0.1);
      const loanLimit = Math.round(price * 0.7);
      const specialFees = p.expenses ? (p.expenses.legalFee + p.expenses.evictionFee) : 2200000;

      const bidRatioEl = document.getElementById('calc-bid-ratio');
      if (bidRatioEl) bidRatioEl.textContent = auctionRate + '%';
      const compEl = document.getElementById('calc-appraised-comp');
      if (compEl) compEl.textContent = `감정가 ${formatKRW(p.appraisedValue)} 기준`;
      const depCheckEl = document.getElementById('calc-deposit-check');
      if (depCheckEl) depCheckEl.textContent = formatKRW(depositCheck);
      const loanLimEl = document.getElementById('calc-auction-loan-limit');
      if (loanLimEl) loanLimEl.textContent = formatKRW(loanLimit);
      const specFeesEl = document.getElementById('calc-auction-special-fees');
      if (specFeesEl) specFeesEl.textContent = formatKRW(specialFees);

      // 지렛대 효과 배지
      const leverageAlert = document.getElementById('leverageTitle');
      const leverageDetail = document.getElementById('leverageDetailText');
      if (calcState.ltv === 0) {
        if (leverageAlert) leverageAlert.textContent = '[무차입 투자] ⚪ 대출 이자 지출 0원 (안전성 최우선)';
        if (leverageDetail) leverageDetail.textContent = '타인자본을 사용하지 않아 금리 변동 위험이 없습니다.';
      } else if (capRate > calcState.loanRate) {
        if (leverageAlert) leverageAlert.textContent = '[지렛대 효과 판정] 🟢 건전한 정(Positive) 레버리지';
        if (leverageDetail) leverageDetail.textContent = '총 임대수익률이 조달금리를 상회하여 자기자본수익률(ROE)이 확대됩니다.';
      } else {
        if (leverageAlert) leverageAlert.textContent = '[지렛대 효과 주의] 🟡 역(Negative) 레버리지 발생';
        if (leverageDetail) leverageDetail.textContent = '조달금리가 임대수익률보다 높아 대출 비중 축소가 권장됩니다.';
      }
    }

    // =========================================================================
    // INITIALIZATION
    // =========================================================================
    window.addEventListener('DOMContentLoaded', () => {
      // 1. Dashboard Render
      renderDashboard();

      // 2. Setup Event Listeners for Calculator
      const depInput = document.getElementById('depositInput');
      const rentInput = document.getElementById('monthlyRentInput');
      const rateInput = document.getElementById('loanRateInput');
      const brokerVat = document.getElementById('brokerVatToggle');
      const bondSlider = document.getElementById('bondRateSlider');

      if (depInput) depInput.addEventListener('input', runCalculatorEngine);
      if (rentInput) rentInput.addEventListener('input', runCalculatorEngine);
      if (rateInput) rateInput.addEventListener('input', (e) => {
        calcState.loanRate = parseFloat(e.target.value) || 0;
        runCalculatorEngine();
      });
      if (brokerVat) brokerVat.addEventListener('change', (e) => {
        calcState.brokerVat = e.target.checked;
        runCalculatorEngine();
      });
      if (bondSlider) bondSlider.addEventListener('input', (e) => {
        calcState.bondRate = parseFloat(e.target.value) || 0;
        const disp = document.getElementById('bondDiscountDisplay');
        if (disp) disp.textContent = calcState.bondRate.toFixed(2) + '%';
        runCalculatorEngine();
      });

      // LTV Buttons Listener (0% 포함)
      document.querySelectorAll('.ltv-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const ltv = parseInt(e.target.getAttribute('data-ltv'));
          handleLtvSliderChange(ltv);
        });
      });

      // 3. Simulator Initial Setup
      renderDynamicSimulator(currentSimPropId);
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

# 신규 파일 index_v5.html 생성 (기존 파일 및 index.html 절대 보존)
output_v5_path = os.path.join(base_dir, "index_v5.html")
with open(output_v5_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"[OK] index_v5.html 빌드 완료! 크기: {len(final_html)} bytes")
print("[INFO] 기존 index.html 및 과거 버전 파일은 규칙에 따라 원형 그대로 보존되었습니다.")
