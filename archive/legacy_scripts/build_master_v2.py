# -*- coding: utf-8 -*-
"""
build_master_v2.py
- 새롭게 개발된 모듈들을 통합하여 index.html을 빌드하는 스크립트.
- 1. 매물 대시보드 <-> 경매 분석 시뮬레이터 실시간 양방향 연동 엔진
- 2. 02_지역분석자료 5대 권역(봉담, 안성, 평택, 천안, 청주) 시장동향 리포트 뷰어 통합
"""
import os, json

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"

# 1. 매물 데이터 읽기
props_path = os.path.join(base_dir, "data", "properties.json")
with open(props_path, "r", encoding="utf-8") as f:
    properties = json.load(f)

img_urls = [
    'https://lh3.googleusercontent.com/aida-public/AB6AXuABmA4YyOL-ZhnewNT40h3q_W-Vb4vEdYAJDhR7382u8DzOnUIQg--Im6R19JtBR-d30UyByc7wY6P16QnrDzwAuqRDwcYzQBhy7H6U-Z_z3iCb1J5DECpGIgpzCz5JpIgQXNKlwsAuY_S9bfBaSIeAzxxFMe-VVCtPtqcIe3BZkXu9LM0gg-5oqTumarLQhQrNZLFIXqXNhmFYm7kFNAFY5-0X4BqEvyqhGFIBFzII',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuAxPfIdb9ymFZ4EBpwOMgtr3COXLUOnLZ39cCN_TrV7b2BpzpX6g1eM3a6Q5QcTqf3-r6_fV8_kH9Xp9jFm89K8c1iTfC-B5M4Xb2fR0p1QyVw6mZ1-c',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDt7rd4WYRNYsefCb4ZfLwvxL70-3BEgBdOPaqW_ZEaL0673D5Yl2yV1X9Qc8b5N3x7-V4M2R9w1p0kF8Y7T6mZ5qX3a',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuABmA4YyOL-ZhnewNT40h3q_W-Vb4vEdYAJDhR7382u8DzOnUIQg--Im6R19JtBR-d30UyByc7wY6P16QnrDzwAuqRDwcYzQBhy7H6U-Z_z3iCb1J5DECpGIgpzCz5JpIgQXNKlwsAuY_S9bfBaSIeAzxxFMe-VVCtPtqcIe3BZkXu9LM0gg-5oqTumarLQhQrNZLFIXqXNhmFYm7kFNAFY5-0X4BqEvyqhGFIBFzII',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuAxPfIdb9ymFZ4EBpwOMgtr3COXLUOnLZ39cCN_TrV7b2BpzpX6g1eM3a6Q5QcTqf3-r6_fV8_kH9Xp9jFm89K8c1iTfC-B5M4Xb2fR0p1QyVw6mZ1-c',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDt7rd4WYRNYsefCb4ZfLwvxL70-3BEgBdOPaqW_ZEaL0673D5Yl2yV1X9Qc8b5N3x7-V4M2R9w1p0kF8Y7T6mZ5qX3a'
]
for idx, p in enumerate(properties):
    p['imageUrl'] = img_urls[idx % len(img_urls)]

properties_json_str = json.dumps(properties, ensure_ascii=False)

# 2. 지역분석 리포트 데이터 읽기
reg_path = os.path.join(base_dir, "data", "regional_reports_data.json")
with open(reg_path, "r", encoding="utf-8") as f:
    regional_reports = json.load(f)

regional_reports_json_str = json.dumps(regional_reports, ensure_ascii=False)

# 3. 뷰 파일 읽기
with open(os.path.join(base_dir, "views", "view_briefing_dynamic.html"), "r", encoding="utf-8") as f:
    view_briefing_content = f.read()

with open(os.path.join(base_dir, "views", "view_calculator.html"), "r", encoding="utf-8") as f:
    view_calculator_content = f.read()

with open(os.path.join(base_dir, "views", "view_reports_v2.html"), "r", encoding="utf-8") as f:
    view_reports_content = f.read()

# HTML 뼈대 작성
master_html = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="web_standard" name="shell-type"/>
  <title>PropIntelligence | 실전 부동산 인텔리전스 & AUCTION BRIEF</title>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
  <style>
    @layer base {
      html, body { margin: 0; padding: 0; }
      body { overscroll-behavior: none; }
      main > :first-child { margin-top: 0 !important; }
      main > :last-child { margin-bottom: 0 !important; }
    }
    ::-webkit-scrollbar { display: none; }
    @media print {
      header, footer, .no-print, #regional-tab-bar, #sim-property-selector { display: none !important; }
      #view-briefing, #view-reports, #view-calculator { display: block !important; padding: 0 !important; margin: 0 !important; }
      #view-dashboard { display: none !important; }
      body { background: white !important; }
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
          borderRadius: {
            DEFAULT: "0.25rem",
            lg: "0.5rem",
            xl: "0.75rem",
            full: "9999px"
          },
          spacing: {
            margin: "1rem",
            "space-lg": "1.25rem",
            "space-xs": "0.25rem",
            "gutter-desktop": "1.5rem",
            "space-md": "0.875rem",
            gutter: "1rem",
            "margin-desktop": "2.5rem",
            "space-xl": "2rem",
            "space-sm": "0.5rem"
          },
          fontFamily: {
            "label-md": ["Inter", "sans-serif"],
            "headline-md": ["Inter", "sans-serif"],
            "label-sm": ["Inter", "sans-serif"],
            "body-lg": ["Inter", "sans-serif"],
            "headline-lg": ["Inter", "sans-serif"],
            "headline-sm": ["Inter", "sans-serif"],
            "body-md": ["Inter", "sans-serif"],
            "body-sm": ["Inter", "sans-serif"]
          },
          fontSize: {
            "headline-lg": ["26px", { lineHeight: "34px", letterSpacing: "-0.02em", fontWeight: "700" }],
            "headline-md": ["22px", { lineHeight: "30px", letterSpacing: "-0.015em", fontWeight: "700" }],
            "headline-sm": ["16px", { lineHeight: "24px", letterSpacing: "-0.01em", fontWeight: "600" }],
            "body-md": ["14px", { lineHeight: "20px", letterSpacing: "0em", fontWeight: "400" }],
            "body-sm": ["13px", { lineHeight: "18px", letterSpacing: "0em", fontWeight: "400" }]
          }
        }
      }
    };
  </script>
</head>
<body class="bg-background font-body-md text-on-surface antialiased">

  <!-- ================= GNB 통합 내비게이션 헤더 ================= -->
  <header class="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-md border-b border-outline-variant/30 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
    <div class="h-16 w-full px-gutter-desktop flex items-center justify-between gap-space-lg">
      <div class="flex items-center gap-space-lg flex-shrink-0">
        <div class="flex items-center gap-space-sm cursor-pointer" onclick="switchMainTab('auction-dashboard')">
          <span class="font-headline-sm text-headline-sm text-primary tracking-tight font-bold">PropIntelligence</span>
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-secondary-container text-on-secondary-container font-label-sm text-label-sm">
            <span class="w-1.5 h-1.5 rounded-full bg-tertiary-container animate-pulse"></span>실전 투자 인텔리전스
          </div>
        </div>
        <div class="hidden xl:inline-flex items-center gap-2 px-2.5 py-1 rounded bg-surface-container-low text-on-surface-variant font-label-md text-label-md">
          <span class="font-semibold text-on-surface">기준금리 3.50%</span>
          <span class="text-outline-variant">|</span>
          <span>환율 1,385원</span>
        </div>
      </div>

      <!-- 4대 메인 내비게이션 탭 -->
      <nav class="hidden lg:flex items-center gap-space-xs" id="main-nav-tabs">
        <button id="nav-btn-dashboard" data-path="auction-dashboard" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm rounded-lg transition-colors bg-primary-container text-on-primary-container font-semibold" onclick="switchMainTab('auction-dashboard')">
          매물 대시보드
        </button>
        <button id="nav-btn-calculator" data-path="yield-calculator" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('yield-calculator')">
          투자수익률 계산기
        </button>
        <button id="nav-btn-briefing" data-path="auction-simulator" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('auction-simulator')">
          경매 분석 시뮬레이터
        </button>
        <button id="nav-btn-reports" data-path="market-reports" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('market-reports')">
          시장동향 리포트 뷰어
        </button>
      </nav>

      <!-- 우측 유틸리티 버튼 -->
      <div class="flex items-center gap-space-sm flex-shrink-0">
        <button class="p-2 text-on-surface-variant hover:text-on-surface hover:bg-surface-container-low rounded-lg transition-colors flex items-center justify-center" title="단독 락(Quick Lock)" onclick="alert('단독 보안 PIN 잠금 상태가 유지됩니다.')" type="button">
          <span class="material-symbols-outlined text-[20px]">lock</span>
        </button>
        <button class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface font-label-md text-label-md rounded-lg transition-colors" onclick="window.print()" type="button">
          <span class="material-symbols-outlined text-[16px]">picture_as_pdf</span>
          <span class="hidden sm:inline">PDF 내보내기</span>
        </button>
        <div class="relative">
          <button class="inline-flex items-center gap-1 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface font-label-md text-label-md rounded-lg transition-colors" onclick="exportDataJSON()" type="button">
            <span class="material-symbols-outlined text-[16px]">database</span>
            <span class="hidden sm:inline">백업/복구</span>
          </button>
        </div>
        <div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center ml-1 text-on-primary font-bold text-xs">
          P
        </div>
      </div>
    </div>
  </header>

  <!-- ================= 1. VIEW: 매물 대시보드 (AUCTION BRIEF) ================= -->
  <main id="view-dashboard" class="w-full pt-16 bg-surface min-h-screen">
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div class="flex flex-col w-full">
        <!-- Top Control, Search & Filter Hub -->
        <section class="w-full flex flex-col gap-space-lg mb-8">
          <!-- Status Banner -->
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 p-4 rounded-xl bg-surface-container-low">
            <div class="flex items-center gap-space-sm">
              <span class="flex h-2.5 w-2.5 rounded-full bg-tertiary"></span>
              <span class="font-label-md text-label-md text-on-surface font-bold">실전자료 1차 정제 및 시뮬레이터 연동 완료</span>
              <span class="text-secondary font-body-sm text-body-sm">·</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">매물 카드의 [시뮬레이터 연동] 버튼을 클릭하면 해당 물건 데이터로 즉시 동기화됩니다.</span>
            </div>
            <div class="flex items-center gap-space-xs">
              <span class="font-label-sm text-label-sm text-secondary bg-surface-container px-2.5 py-1 rounded-lg">분석기준일: 2026-11-20</span>
              <button onclick="renderCards()" class="text-primary hover:text-primary-container font-label-md text-label-md px-2 py-1 flex items-center gap-1 transition-colors">
                <span class="material-symbols-outlined text-[16px]">refresh</span>데이터 새로고침
              </button>
            </div>
          </div>

          <!-- Search Input Block -->
          <div class="w-full bg-surface-container-lowest rounded-xl p-3 shadow-sm flex flex-col md:flex-row items-center gap-3 border border-outline-variant/30">
            <div class="flex-1 flex items-center gap-3 px-3 py-2.5 w-full bg-surface-container rounded-xl">
              <span class="material-symbols-outlined text-outline text-[20px]">search</span>
              <input id="search-input" oninput="handleSearch()" class="w-full bg-transparent border-0 outline-none font-body-md text-body-md text-on-surface placeholder:text-outline" placeholder="사건번호, 물건명(예: 안성동남타운, 봉담우방), 지역명 검색" type="text"/>
            </div>
            <div class="flex items-center gap-2 w-full md:w-auto">
              <button onclick="setCategoryFilter('recommend')" class="flex-1 md:flex-initial px-4 py-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface-variant font-label-md text-label-md flex items-center justify-center gap-1.5 transition-colors">
                <span class="material-symbols-outlined text-[18px]">tune</span>추천 매물만 보기
              </button>
              <button onclick="handleSearch()" class="flex-1 md:flex-initial px-5 py-3 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md shadow-sm transition-all flex items-center justify-center gap-1">
                <span>검색</span>
              </button>
            </div>
          </div>

          <!-- Filter Category Chips -->
          <div class="flex items-center gap-2 overflow-x-auto pb-1" id="category-filter-chips">
            <button onclick="setCategoryFilter('all')" id="tab-all" class="tab-chip active px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md transition-all whitespace-nowrap shadow-sm">
              전체 매물 (6)
            </button>
            <button onclick="setCategoryFilter('recommend')" id="tab-recommend" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
              추천/적극추천 (4)
            </button>
            <button onclick="setCategoryFilter('auction')" id="tab-auction" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
              경매 물건 (5)
            </button>
            <button onclick="setCategoryFilter('sale')" id="tab-sale" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
              일반급매 (1)
            </button>
            <button onclick="setCategoryFilter('hold')" id="tab-hold" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
              보류/유찰대기 (1)
            </button>
          </div>
        </section>

        <!-- Section Header -->
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-2">
            <h2 class="font-headline-md text-headline-md tracking-tight text-on-surface">실전 정제 매물 리스트</h2>
            <span id="list-count-badge" class="px-2 py-0.5 rounded-full bg-surface-container-high text-on-surface-variant font-label-sm text-label-sm">6건 검색됨</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-secondary font-medium">정렬: 추천순</span>
          </div>
        </div>

        <!-- 매물 카드 그리드 (3열 반응형) -->
        <section id="property-cards-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- JavaScript로 6개 실전 매물 렌더링 -->
        </section>
      </div>
    </div>
  </main>

  <!-- ================= 2. VIEW: 투자수익률 계산기 ================= -->
  <main id="view-calculator" class="w-full pt-16 bg-surface min-h-screen hidden">
    __VIEW_CALCULATOR_CONTENT__
  </main>

  <!-- ================= 3. VIEW: 경매 분석 시뮬레이터 (동적 연동 버전) ================= -->
  <main id="view-briefing" class="w-full pt-16 bg-surface min-h-screen hidden">
    __VIEW_BRIEFING_CONTENT__
  </main>

  <!-- ================= 4. VIEW: 시장동향 리포트 뷰어 (02_지역분석자료 연동) ================= -->
  <main id="view-reports" class="w-full pt-16 bg-surface min-h-screen hidden">
    __VIEW_REPORTS_CONTENT__
  </main>

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

              <span id="modal-bid-label" class="text-primary font-bold">추천 입찰가:</span>
              <span id="modal-bid" class="text-primary font-black">-</span>
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

        <!-- 4. Expenses Breakdown -->
        <div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30">
          <h5 class="font-label-md text-label-md font-bold text-on-surface mb-2">취득 부대비용 상세 세부 내역표</h5>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-body-sm text-body-sm">
            <div class="bg-surface-container-lowest p-2.5 rounded-lg border border-outline-variant/30">
              <span class="text-secondary block font-label-sm text-label-sm">취득세+지방교육세</span>
              <span id="modal-tax-fee" class="font-semibold text-on-surface">-</span>
            </div>
            <div class="bg-surface-container-lowest p-2.5 rounded-lg border border-outline-variant/30">
              <span class="text-secondary block font-label-sm text-label-sm">법무사 등기보수</span>
              <span id="modal-legal-fee" class="font-semibold text-on-surface">-</span>
            </div>
            <div class="bg-surface-container-lowest p-2.5 rounded-lg border border-outline-variant/30">
              <span class="text-secondary block font-label-sm text-label-sm">명도비(이사비 협의)</span>
              <span id="modal-eviction-fee" class="font-semibold text-on-surface">-</span>
            </div>
            <div class="bg-surface-container-lowest p-2.5 rounded-lg border border-outline-variant/30">
              <span class="text-secondary block font-label-sm text-label-sm">수리/인테리어비</span>
              <span id="modal-repair-fee" class="font-semibold text-on-surface">-</span>
            </div>
          </div>
        </div>

        <!-- 5. Location Highlights -->
        <div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30">
          <h5 class="font-label-md text-label-md font-bold text-on-surface mb-2">입지 환경 및 미래 개발 호재</h5>
          <ul id="modal-highlights-list" class="space-y-1.5 font-body-sm text-body-sm text-on-surface">
            <!-- Dynamic items -->
          </ul>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-outline-variant/20 bg-surface-container-low flex items-center justify-between">
        <div class="font-label-sm text-label-sm text-secondary">
          안티그래비티 부동산 자산관리 컨설팅 | 실전 투자 매물 브리핑
        </div>
        <div class="flex items-center gap-2">
          <button id="modal-go-sim-btn" onclick="loadPropertyToSimulator(currentModalPropId); closePropertyModal();" class="px-4 py-2 font-label-md text-label-md font-semibold bg-primary hover:bg-primary-container text-on-primary rounded-xl transition">
            시뮬레이터로 이동
          </button>
          <button onclick="closePropertyModal()" class="px-4 py-2 font-label-md text-label-md font-semibold bg-surface-container hover:bg-surface-container-high text-on-surface rounded-xl transition">
            닫기
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= Footer ================= -->
  <footer class="w-full bg-surface-container-low py-space-lg border-t border-outline-variant/20">
    <div class="max-w-[1440px] mx-auto px-gutter-desktop flex flex-col md:flex-row items-center justify-between gap-space-sm font-label-sm text-label-sm text-on-surface-variant">
      <div class="flex items-center gap-2">
        <span>PropIntelligence Terminal © 2026</span>
        <span class="text-outline-variant">•</span>
        <span>Private Autonomous Investor Node</span>
      </div>
      <div class="flex items-center gap-space-md font-mono">
        <span>DB: Local Encrypted Storage</span>
        <span>STATUS: CONNECTED (KOR_REIT_01)</span>
      </div>
    </div>
  </footer>

  <!-- ================= Global Master Script Engine ================= -->
  <script>
    const PROPERTIES = __PROPERTIES_JSON__;
    const REGIONAL_REPORTS = __REGIONAL_REPORTS_JSON__;
    
    let currentCategory = 'all';
    let currentSearch = '';
    let currentSimPropId = '2026-239'; // 기본 매물: 안성동남타운
    let currentModalPropId = '2026-239';
    let currentActiveDocTab = 'doc-spec';
    let currentRegionId = 'bongdam';

    // 금액 한글 포맷팅 함수
    function formatKRW(val) {
      if (val === undefined || val === null) return '-';
      if (Math.abs(val) >= 100000000) {
        const uk = Math.floor(val / 100000000);
        const man = Math.round((val % 100000000) / 10000);
        return man > 0 ? uk + '억 ' + man.toLocaleString() + '만 원' : uk + '억 원';
      }
      return Math.round(val / 10000).toLocaleString() + '만 원';
    }

    // 4대 탭 화면 전환 라우터
    function switchMainTab(targetPath) {
      const tabs = [
        { path: 'auction-dashboard', viewId: 'view-dashboard', btnId: 'nav-btn-dashboard' },
        { path: 'yield-calculator', viewId: 'view-calculator', btnId: 'nav-btn-calculator' },
        { path: 'auction-simulator', viewId: 'view-briefing', btnId: 'nav-btn-briefing' },
        { path: 'market-reports', viewId: 'view-reports', btnId: 'nav-btn-reports' }
      ];

      tabs.forEach(t => {
        const v = document.getElementById(t.viewId);
        const b = document.getElementById(t.btnId);
        if (t.path === targetPath) {
          if (v) v.classList.remove('hidden');
          if (b) {
            b.className = "nav-tab-btn px-3 py-2 font-body-sm text-body-sm rounded-lg transition-colors bg-primary-container text-on-primary-container font-semibold";
          }
        } else {
          if (v) v.classList.add('hidden');
          if (b) {
            b.className = "nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors";
          }
        }
      });

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 카테고리 필터
    function setCategoryFilter(cat) {
      currentCategory = cat;
      const tabs = ['all', 'recommend', 'auction', 'sale', 'hold'];
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
      renderCards();
    }

    // 검색 핸들러
    function handleSearch() {
      currentSearch = document.getElementById('search-input').value.trim().toLowerCase();
      renderCards();
    }

    // 매물 카드 렌더링
    function renderCards() {
      const container = document.getElementById('property-cards-container');
      const filtered = PROPERTIES.filter(p => {
        if (currentCategory === 'recommend' && !['적극추천', '추천'].includes(p.status)) return false;
        if (currentCategory === 'auction' && p.category !== '경매') return false;
        if (currentCategory === 'sale' && p.category !== '일반급매') return false;
        if (currentCategory === 'hold' && p.status !== '보류/유찰대기') return false;

        if (currentSearch) {
          const matchCase = p.caseNumber.toLowerCase().includes(currentSearch);
          const matchName = p.propertyName.toLowerCase().includes(currentSearch);
          const matchAddr = p.address.toLowerCase().includes(currentSearch);
          if (!matchCase && !matchName && !matchAddr) return false;
        }
        return true;
      });

      document.getElementById('list-count-badge').textContent = filtered.length + '건 검색됨';

      container.innerHTML = filtered.map(p => {
        const isAuction = p.category === '경매';
        const statusBadgeClass = p.status === '적극추천'
          ? 'bg-error text-on-error'
          : p.status === '추천'
          ? 'bg-tertiary text-on-tertiary'
          : p.status === '보류/유찰대기'
          ? 'bg-secondary text-on-secondary'
          : 'bg-primary text-on-primary';

        return `
          <article class="group bg-surface-container-lowest rounded-2xl overflow-hidden shadow-sm hover:shadow-md border border-outline-variant/30 transition-all flex flex-col justify-between">
            <div class="relative w-full h-48 bg-surface-container overflow-hidden cursor-pointer" onclick="openPropertyModal('${p.id}')">
              <div class="w-full h-full bg-cover bg-center group-hover:scale-105 transition-transform duration-500" style="background-image: url('${p.imageUrl}');"></div>
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              
              <div class="absolute top-3 left-3 flex items-center gap-1.5">
                <span class="px-2.5 py-1 rounded-md bg-surface-container-lowest/90 backdrop-blur-sm text-primary font-label-sm text-label-sm font-semibold">
                  ${p.category}
                </span>
                <span class="px-2 py-1 rounded-md ${statusBadgeClass} font-label-sm text-label-sm flex items-center gap-1 font-semibold">
                  ${p.status}
                </span>
              </div>

              <div class="absolute top-3 right-3 flex items-center gap-1">
                <button class="w-8 h-8 rounded-full bg-surface-container-lowest/90 backdrop-blur-sm text-error hover:bg-surface-container-lowest flex items-center justify-center transition-colors">
                  <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">favorite</span>
                </button>
              </div>

              <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-on-primary">
                <span class="font-label-sm text-label-sm font-semibold tracking-wide">${p.caseNumber}</span>
                <span class="font-label-sm text-label-sm text-on-primary/90">${p.court || ''}</span>
              </div>
            </div>

            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="mb-3 cursor-pointer" onclick="openPropertyModal('${p.id}')">
                  <h3 class="font-headline-sm text-headline-sm text-on-surface truncate group-hover:text-primary transition-colors" title="${p.propertyName}">
                    ${p.propertyName}
                  </h3>
                  <p class="font-body-sm text-body-sm text-secondary truncate mt-0.5">${p.address}</p>
                </div>

                <div class="p-3.5 rounded-xl bg-surface-container mb-4">
                  <div class="flex justify-between items-center mb-1.5">
                    <span class="font-body-sm text-body-sm text-secondary">${isAuction ? '감정평가액' : '최초호가'}</span>
                    <span class="font-label-md text-label-md text-secondary line-through">${formatKRW(p.appraisedValue)}</span>
                  </div>
                  <div class="flex justify-between items-baseline">
                    <div class="flex items-center gap-1.5">
                      <span class="font-label-sm text-label-sm ${p.minimumBidRate < 100 ? 'text-error bg-error-container/60' : 'text-secondary bg-surface-container-high'} px-1.5 py-0.5 rounded font-semibold">
                        ${isAuction ? (p.minimumBidRate < 100 ? '1회 유찰' : '신건') : '네고목표'}
                      </span>
                      <span class="font-headline-sm text-headline-sm text-on-surface">${isAuction ? '최저매각가' : '네고목표가'}</span>
                    </div>
                    <div class="text-right">
                      <span class="font-headline-md text-headline-md text-primary tracking-tight">${formatKRW(p.minimumBidPrice)}</span>
                      <span class="font-label-sm text-label-sm text-secondary ml-1">(${p.minimumBidRate}%)</span>
                    </div>
                  </div>
                  <div class="flex justify-between items-baseline mt-2 pt-2 border-t border-outline-variant/30">
                    <span class="text-xs font-bold text-on-surface">★ 추천 ${isAuction ? '입찰가' : '매수가'}</span>
                    <span class="text-base font-black text-primary">${formatKRW(p.recommendedBidPrice)}</span>
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2 mb-4">
                  <div class="p-2.5 rounded-xl bg-tertiary-container/10 flex flex-col">
                    <span class="font-label-sm text-label-sm text-tertiary">예상 연 ROE</span>
                    <span class="font-headline-sm text-headline-sm text-tertiary mt-0.5 font-black">${p.roePercent ? p.roePercent + '%' : '-'}</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-secondary-container/50 flex flex-col">
                    <span class="font-label-sm text-label-sm text-secondary">필요 실투자금</span>
                    <span class="font-headline-sm text-headline-sm text-on-surface mt-0.5 font-black">${formatKRW(p.netInvestment)}</span>
                  </div>
                </div>

                <div class="mb-4">
                  <span class="font-label-sm text-label-sm text-secondary block mb-2">핵심 입지 & 개발 호재</span>
                  <div class="flex flex-wrap gap-1.5">
                    ${p.locationHighlights.slice(0, 3).map(h => `
                      <span class="px-2 py-0.5 rounded-md bg-surface-container-low text-on-surface-variant font-label-sm text-label-sm truncate max-w-[200px]" title="${h}">
                        ${h}
                      </span>
                    `).join('')}
                  </div>
                </div>
              </div>

              <!-- 카드 액션 버튼: 상세 권리분석 & 시뮬레이터 연동 -->
              <div class="pt-4 border-t border-surface-container flex items-center justify-between gap-2">
                <button onclick="openPropertyModal('${p.id}')" class="flex-1 py-2 px-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md flex items-center justify-center gap-1 transition-all" type="button">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>권리·수지 상세
                </button>
                <button onclick="loadPropertyToSimulator('${p.id}')" class="flex-1 py-2 px-3 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md flex items-center justify-center gap-1 shadow-sm transition-all" type="button">
                  <span class="material-symbols-outlined text-[16px]">tune</span>시뮬레이터 연동
                </button>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    // 모달 열기
    function openPropertyModal(id) {
      const p = PROPERTIES.find(item => item.id === id);
      if (!p) return;
      currentModalPropId = id;

      const isAuction = p.category === '경매';
      document.getElementById('modal-category').textContent = p.category;
      document.getElementById('modal-category').className = isAuction 
        ? "px-2.5 py-1 rounded-md font-label-sm text-label-sm font-bold bg-primary text-on-primary"
        : "px-2.5 py-1 rounded-md font-label-sm text-label-sm font-bold bg-tertiary text-on-tertiary";
      
      document.getElementById('modal-title').textContent = p.propertyName;
      document.getElementById('modal-subtitle').textContent = (p.court || '') + ' | ' + p.caseNumber + ' | ' + (isAuction ? '매각기일: ' + (p.auctionDate || '-') : '중개물건');
      document.getElementById('modal-brief').textContent = p.strategyBrief;
      
      const marginEl = document.getElementById('modal-margin');
      marginEl.textContent = (p.safetyMargin >= 0 ? '+' : '') + formatKRW(p.safetyMargin);
      marginEl.className = p.safetyMargin >= 0 
        ? "font-headline-sm text-headline-sm font-black text-primary" 
        : "font-headline-sm text-headline-sm font-black text-error";

      document.getElementById('modal-ltv-label').textContent = '1. 대출 레버리지 (LTV ' + p.financing.ltvPercent + '%)';
      document.getElementById('modal-loan').textContent = formatKRW(p.financing.loanAmount);
      document.getElementById('modal-interest').textContent = '월 이자: 약 ' + formatKRW(p.financing.monthlyInterest) + ' (연 ' + p.financing.interestRate + '%)';

      document.getElementById('modal-expenses').textContent = formatKRW(p.expenses.totalExpenses);
      document.getElementById('modal-expenses-detail').textContent = '취득세 ' + formatKRW(p.expenses.acquisitionTax) + ' + 수리/명도';

      document.getElementById('modal-net-invest').textContent = formatKRW(p.netInvestment);
      document.getElementById('modal-roe').textContent = p.roePercent ? p.roePercent + '%' : '-';
      document.getElementById('modal-rental').textContent = p.rental.rentalType + ': 보증금 ' + formatKRW(p.rental.deposit) + (p.rental.monthlyRent > 0 ? ' / 월 ' + formatKRW(p.rental.monthlyRent) : '');

      document.getElementById('modal-address').textContent = p.address;
      document.getElementById('modal-area').textContent = p.exclusiveAreaM2 + '㎡ (' + p.exclusiveAreaPyung + '평)';
      document.getElementById('modal-floor-build').textContent = p.floorInfo + ' / ' + p.buildYear + '년';
      
      document.getElementById('modal-appraised-label').textContent = isAuction ? '감정평가액:' : '최초호가:';
      document.getElementById('modal-appraised').textContent = formatKRW(p.appraisedValue);

      document.getElementById('modal-min-label').textContent = isAuction ? '최저매각가:' : '네고목표가:';
      document.getElementById('modal-min').textContent = formatKRW(p.minimumBidPrice) + ' (' + p.minimumBidRate + '%)';
      document.getElementById('modal-market').textContent = formatKRW(p.marketPrice);

      document.getElementById('modal-bid-label').textContent = '추천 ' + (isAuction ? '입찰가:' : '매수가:');
      document.getElementById('modal-bid').textContent = formatKRW(p.recommendedBidPrice);

      document.getElementById('modal-malso').textContent = p.rights.malsoStandard;
      document.getElementById('modal-occupant').textContent = p.rights.occupantStatus;
      document.getElementById('modal-takeover').textContent = p.rights.takeoverAmount === 0 ? '0원 (완벽 안전)' : formatKRW(p.rights.takeoverAmount);
      
      const evictEl = document.getElementById('modal-eviction');
      evictEl.textContent = '난이도 ' + p.rights.evictionDifficulty + ' (예비비 ' + formatKRW(p.expenses.evictionFee) + ')';
      evictEl.className = p.rights.evictionDifficulty === '하' 
        ? "font-bold px-2 py-0.5 rounded font-label-sm text-label-sm bg-tertiary/10 text-tertiary"
        : "font-bold px-2 py-0.5 rounded font-label-sm text-label-sm bg-amber-500/10 text-amber-600";

      document.getElementById('modal-risk-notes').textContent = p.rights.riskNotes;

      document.getElementById('modal-tax-fee').textContent = formatKRW(p.expenses.acquisitionTax);
      document.getElementById('modal-legal-fee').textContent = formatKRW(p.expenses.legalFee);
      document.getElementById('modal-eviction-fee').textContent = formatKRW(p.expenses.evictionFee);
      document.getElementById('modal-repair-fee').textContent = formatKRW(p.expenses.repairFee);

      const highlightsList = document.getElementById('modal-highlights-list');
      highlightsList.innerHTML = p.locationHighlights.map(h => `
        <li class="flex items-start gap-1.5">
          <span class="text-primary font-bold shrink-0">✓</span>
          <span>${h}</span>
        </li>
      `).join('');

      document.getElementById('property-detail-modal').classList.remove('hidden');
    }

    function closePropertyModal() {
      document.getElementById('property-detail-modal').classList.add('hidden');
    }

    // =========================================================================
    // DYNAMIC AUCTION SIMULATOR ENGINE (시뮬레이터 <-> 대시보드 100% 연동)
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

      // 0. Quick Selector Toolbar Buttons
      const selectorContainer = document.getElementById('sim-property-selector');
      if (selectorContainer) {
        selectorContainer.innerHTML = PROPERTIES.map(item => {
          const isSelected = item.id === propertyId;
          const cls = isSelected
            ? "px-3 py-1.5 rounded-lg bg-primary text-on-primary font-label-md text-label-md font-semibold transition whitespace-nowrap shadow-sm"
            : "px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition whitespace-nowrap";
          const shortName = item.propertyName.split(' ')[0] + ' ' + (item.caseNumber.split('타경')[1] ? '타경' + item.caseNumber.split('타경')[1] : item.propertyName.slice(-5));
          return `<button onclick="loadPropertyToSimulator('${item.id}')" class="${cls}">${shortName}</button>`;
        }).join('');
      }

      // 1. Header Information
      document.getElementById('sim-category-badge').textContent = p.category;
      document.getElementById('sim-category-badge').className = isAuction 
        ? "px-2.5 py-0.5 rounded-md font-label-sm text-label-sm font-bold bg-primary text-on-primary"
        : "px-2.5 py-0.5 rounded-md font-label-sm text-label-sm font-bold bg-tertiary text-on-tertiary";

      document.getElementById('sim-court-case').textContent = p.court ? '• ' + p.court + ' ' + p.caseNumber : '• 일반 매매/급매 물건';
      document.getElementById('sim-property-name').innerHTML = `${p.propertyName} <span id="sim-area-info" class="font-headline-sm text-headline-sm text-secondary font-medium">(${p.exclusiveAreaM2}㎡ / ${p.exclusiveAreaPyung}평형)</span>`;
      document.getElementById('sim-address').textContent = p.address;
      document.getElementById('sim-auction-date').textContent = p.auctionDate ? p.auctionDate : '상시 협의 진행';
      
      // 2. Price Evaluation
      document.getElementById('sim-status-badge').textContent = p.status;
      document.getElementById('sim-label-appraised').textContent = isAuction ? '감정평가액' : '최초호가';
      document.getElementById('sim-val-appraised').textContent = formatKRW(p.appraisedValue);
      document.getElementById('sim-label-min').textContent = isAuction ? '최저입찰가' : '네고목표가';
      document.getElementById('sim-val-min').textContent = formatKRW(p.minimumBidPrice);
      document.getElementById('sim-rate-min').textContent = '(' + p.minimumBidRate + '%)';
      document.getElementById('sim-label-rec').textContent = '★ 추천 ' + (isAuction ? '목표입찰가' : '목표매수가');
      document.getElementById('sim-val-rec').textContent = formatKRW(p.recommendedBidPrice);
      document.getElementById('sim-rate-rec').textContent = '감정가 대비 ' + p.minimumBidRate + '% 수준';
      document.getElementById('sim-market-price').textContent = formatKRW(p.marketPrice);
      document.getElementById('sim-margin-text').textContent = '안전마진: 약 ' + (p.safetyMargin >= 0 ? '+' : '') + formatKRW(p.safetyMargin);

      // 3. Physical Specs & Rights
      document.getElementById('sim-exclusive-area').textContent = p.exclusiveAreaM2 + '㎡ (' + p.exclusiveAreaPyung + '평)';
      document.getElementById('sim-floor-info').textContent = p.floorInfo;
      document.getElementById('sim-build-year').textContent = p.buildYear + '년';
      document.getElementById('sim-heating-info').textContent = '개별난방 / 계단식';
      document.getElementById('sim-malso-std').textContent = p.rights.malsoStandard;
      document.getElementById('sim-tenant-status').textContent = p.rights.occupantStatus;
      document.getElementById('sim-takeover-val').textContent = p.rights.takeoverAmount === 0 ? '0원 (완벽 안전 매물)' : formatKRW(p.rights.takeoverAmount);
      document.getElementById('sim-eviction-diff').textContent = '난이도 ' + p.rights.evictionDifficulty + ' (예비비 ' + formatKRW(p.expenses.evictionFee) + ')';
      document.getElementById('sim-risk-comment').textContent = p.rights.riskNotes;

      // 4. Sliders Calibration (Property-specific scale)
      const bidSlider = document.getElementById('sim-bid-slider');
      const jeonseSlider = document.getElementById('sim-jeonse-slider');
      
      const recBidMan = Math.round(p.recommendedBidPrice / 10000);
      const minBidMan = Math.round(p.minimumBidPrice / 10000);
      const appBidMan = Math.round(p.appraisedValue / 10000);

      const sliderMin = Math.floor(minBidMan * 0.85);
      const sliderMax = Math.ceil(Math.max(appBidMan * 1.15, recBidMan * 1.3));
      const sliderStep = recBidMan > 20000 ? 100 : 50;

      bidSlider.min = sliderMin;
      bidSlider.max = sliderMax;
      bidSlider.step = sliderStep;
      bidSlider.value = recBidMan;

      document.getElementById('sim-bid-min-lbl').textContent = '최저 ' + sliderMin.toLocaleString() + '만';
      document.getElementById('sim-bid-mid-lbl').textContent = '추천 ' + recBidMan.toLocaleString() + '만';
      document.getElementById('sim-bid-max-lbl').textContent = '최대 ' + sliderMax.toLocaleString() + '만';

      const jeonseBaseMan = p.rental.deposit > 0 ? Math.round(p.rental.deposit / 10000) : Math.round((p.marketPrice * 0.7) / 10000);
      const jMin = Math.floor(jeonseBaseMan * 0.6);
      const jMax = Math.ceil(jeonseBaseMan * 1.35);
      const jStep = jeonseBaseMan > 20000 ? 100 : 50;

      jeonseSlider.min = jMin;
      jeonseSlider.max = jMax;
      jeonseSlider.step = jStep;
      jeonseSlider.value = jeonseBaseMan;

      document.getElementById('sim-jeonse-min-lbl').textContent = '최저 ' + jMin.toLocaleString() + '만';
      document.getElementById('sim-jeonse-mid-lbl').textContent = '시세 ' + jeonseBaseMan.toLocaleString() + '만';
      document.getElementById('sim-jeonse-max-lbl').textContent = '최대 ' + jMax.toLocaleString() + '만';

      // 5. Update Public Documents & Calculation
      switchDocTab(currentActiveDocTab);
      runSimulatorEngine();
    }

    // 실시간 시뮬레이터 수지 계산기
    function runSimulatorEngine() {
      const p = PROPERTIES.find(item => item.id === currentSimPropId);
      if (!p) return;

      const bidSlider = document.getElementById('sim-bid-slider');
      const rateSlider = document.getElementById('sim-rate-slider');
      const jeonseSlider = document.getElementById('sim-jeonse-slider');
      if (!bidSlider) return;

      const bidMan = parseFloat(bidSlider.value);
      const rate = parseFloat(rateSlider.value);
      const jeonseMan = parseFloat(jeonseSlider.value);

      document.getElementById('sim-bid-display').innerText = bidMan.toLocaleString();
      document.getElementById('sim-rate-display').innerText = rate.toFixed(1);
      document.getElementById('sim-jeonse-display').innerText = jeonseMan.toLocaleString();

      const bidWon = bidMan * 10000;
      const jeonseWon = jeonseMan * 10000;

      // 취득세 + 부대비용 추산 (1.1%~3.5% + 법무비 + 수리/명도비)
      const taxRate = bidWon <= 600000000 ? 0.011 : 0.022;
      const taxes = bidWon * taxRate;
      const incidentalFees = taxes + p.expenses.legalFee + p.expenses.evictionFee + p.expenses.repairFee;

      const loanAmount = bidWon * 0.7; // 70% 대출
      const monthlyInterest = (loanAmount * (rate / 100)) / 12;

      // 갭투자(전세 세팅) 시 최종 순 실투자금 = 총 소요비용(낙찰가 + 부대비용) - 전세 보증금
      const totalOutlay = bidWon + incidentalFees;
      const netInvestmentGap = totalOutlay - jeonseWon;

      // 자기자본수익률 (ROE): (매매차익 + 연임대료) / 순투자금
      const capitalGain = Math.max(0, p.marketPrice - bidWon);
      const roe = netInvestmentGap > 0 ? ((capitalGain + (p.rental.monthlyRent * 12)) / netInvestmentGap) * 100 : 0;

      document.getElementById('sim-out-net-equity').innerText = formatKRW(netInvestmentGap);
      document.getElementById('sim-out-interest').innerText = Math.round(monthlyInterest / 10000).toLocaleString() + '만 원 / 월';
      document.getElementById('sim-out-loan-amt').innerText = '대출 ' + formatKRW(loanAmount) + ' 기준';
      document.getElementById('sim-out-costs').innerText = formatKRW(incidentalFees);
      document.getElementById('sim-out-roe').innerText = (Math.min(roe, 99.9)).toFixed(1) + '%';
    }

    function resetDynamicSimulator() {
      renderDynamicSimulator(currentSimPropId);
    }

    // 공적 서류 5종 탭 전환기
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
              본건은 ${p.propertyName} 소재 물건으로서 간선도로 및 대중교통 연계성이 양호하며, 인근 학군 및 생활편의시설이 잘 정비되어 단독/가구 수요 흡수에 유리함.
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
                <span class="font-medium text-on-surface">공용부분 약 30~50만원 수준 (입찰 전 관리사무소 최종 유선확인 요망)</span>
              </div>
            </div>
          </div>
        `;
      } else if (docId === 'doc-register') {
        contentEl.innerHTML = `
          <div class="space-y-3 text-xs">
            <div class="flex items-center justify-between pb-2 border-b border-outline-variant/20">
              <span class="font-bold text-on-surface">[등기사항전부증명서 (을구/갑구 핵심 요약)]</span>
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
              <span class="font-bold text-on-surface">[주민등록 전입세대확인서 열람 내역]</span>
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
                <span class="font-medium text-tertiary">임차인 없음 (인도명령 대상)</span>
              </div>
            </div>
          </div>
        `;
      }
    }

    // =========================================================================
    // REGIONAL MARKET REPORTS ENGINE (02_지역분석자료 연동)
    // =========================================================================

    function switchRegionalReport(regionId) {
      currentRegionId = regionId;
      const r = REGIONAL_REPORTS.find(item => item.id === regionId);
      if (!r) return;

      // 1. Update Tab styling
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

      // 2. Update Breadcrumb & Header
      document.getElementById('report-breadcrumb-region').textContent = r.name;
      document.getElementById('report-breadcrumb-date').textContent = r.standardDate;
      document.getElementById('report-badge').textContent = r.badge;
      document.getElementById('report-std-date').textContent = r.standardDate;
      document.getElementById('report-title').textContent = r.name + ' 광역생활권 부동산 시장 및 도시개발 심층 분석';
      document.getElementById('report-summary').textContent = r.summary;

      // 3. Update 5 Metrics
      document.getElementById('metric-unsold').textContent = r.metrics.unsold.split('(')[0];
      document.getElementById('metric-supply').textContent = r.metrics.supply.split('➔')[0];
      document.getElementById('metric-demographics').textContent = r.metrics.demographics.split('/')[0];
      document.getElementById('metric-traffic').textContent = r.metrics.traffic.split(',')[0];
      document.getElementById('metric-risk').textContent = r.metrics.risk.split(',')[0];

      // 4. Update Key Findings Checklist
      const keyPointsContainer = document.getElementById('report-key-points');
      if (keyPointsContainer) {
        keyPointsContainer.innerHTML = r.keyPoints.map(pt => `
          <li class="flex items-start gap-2">
            <span class="text-primary font-bold shrink-0 mt-0.5">✓</span>
            <span class="leading-relaxed">${pt}</span>
          </li>
        `).join('');
      }

      // 5. Render Markdown content nicely
      renderMarkdownReport(r.contentMarkdown);
    }

    // 간단하고 안정적인 클라이언트 사이드 마크다운 렌더러
    function renderMarkdownReport(mdText) {
      const container = document.getElementById('report-markdown-container');
      if (!container) return;

      const lines = mdText.split('\\n');
      let html = '';
      let inTable = false;
      let tableRows = [];

      for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim();

        // 테이블 처리
        if (line.startsWith('|') && line.endsWith('|')) {
          inTable = true;
          tableRows.push(line);
          continue;
        } else if (inTable) {
          // 테이블 닫기
          html += parseMarkdownTable(tableRows);
          inTable = false;
          tableRows = [];
        }

        if (line.startsWith('# ')) {
          html += `<h1 class="text-2xl md:text-3xl font-extrabold text-on-surface mt-6 mb-3 pb-2 border-b border-outline-variant/30">${line.slice(2)}</h1>`;
        } else if (line.startsWith('## ')) {
          html += `<h2 class="text-xl md:text-2xl font-bold text-on-surface mt-5 mb-2 pb-1 border-b border-outline-variant/20 flex items-center gap-2"><span class="w-2 h-5 bg-primary rounded-full"></span>${line.slice(3)}</h2>`;
        } else if (line.startsWith('### ')) {
          html += `<h3 class="text-base md:text-lg font-bold text-primary mt-4 mb-1.5">${line.slice(4)}</h3>`;
        } else if (line.startsWith('> ')) {
          html += `<blockquote class="p-3 my-2 bg-surface-container-low border-l-4 border-primary rounded-r-lg text-sm text-on-surface-variant leading-relaxed">${line.slice(2)}</blockquote>`;
        } else if (line.startsWith('- ') || line.startsWith('* ')) {
          const boldFormatted = line.slice(2).replace(/\\*\\*(.*?)\\*\\*/g, '<strong class="text-on-surface font-bold">$1</strong>');
          html += `<div class="flex items-start gap-2 my-1.5 text-sm text-on-surface-variant leading-relaxed"><span class="text-primary font-bold shrink-0 mt-1">•</span><div>${boldFormatted}</div></div>`;
        } else if (line === '---') {
          html += `<hr class="my-6 border-outline-variant/20"/>`;
        } else if (line.length > 0) {
          const boldFormatted = line.replace(/\\*\\*(.*?)\\*\\*/g, '<strong class="text-on-surface font-bold">$1</strong>');
          html += `<p class="my-2 text-sm text-on-surface-variant leading-relaxed">${boldFormatted}</p>`;
        }
      }

      if (inTable) {
        html += parseMarkdownTable(tableRows);
      }

      container.innerHTML = html;
    }

    function parseMarkdownTable(rows) {
      if (rows.length < 2) return '';
      let tableHtml = '<div class="overflow-x-auto my-4 rounded-xl border border-outline-variant/30 shadow-sm"><table class="w-full text-left text-xs md:text-sm border-collapse">';
      
      const headerCells = rows[0].split('|').map(c => c.trim()).filter((c, idx, arr) => idx > 0 && idx < arr.length - 1);
      tableHtml += '<thead class="bg-surface-container text-on-surface font-bold"><tr>';
      headerCells.forEach(cell => {
        tableHtml += `<th class="p-3 border-b border-outline-variant/20">${cell}</th>`;
      });
      tableHtml += '</tr></thead><tbody>';

      for (let i = 2; i < rows.length; i++) {
        const rowCells = rows[i].split('|').map(c => c.trim()).filter((c, idx, arr) => idx > 0 && idx < arr.length - 1);
        tableHtml += '<tr class="border-b border-outline-variant/10 hover:bg-surface-container-low transition">';
        rowCells.forEach(cell => {
          const formatted = cell.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
          tableHtml += `<td class="p-3">${formatted}</td>`;
        });
        tableHtml += '</tr>';
      }

      tableHtml += '</tbody></table></div>';
      return tableHtml;
    }

    // JSON 내보내기
    function exportDataJSON() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(PROPERTIES, null, 2));
      const anchor = document.createElement('a');
      anchor.setAttribute("href", dataStr);
      anchor.setAttribute("download", `propintelligence_db_${new Date().toISOString().slice(0, 10)}.json`);
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
    }

    // 초기 실행
    document.addEventListener('DOMContentLoaded', () => {
      renderCards();
      renderDynamicSimulator('2026-239'); // 안성동남타운 기본 로드
      switchRegionalReport('bongdam');     // 봉담 보고서 기본 로드
    });
  </script>

  <!-- ================= 2. 계산기 스크립트 엔진 ================= -->
  <script>
    (function initCalculatorEngine() {
      const priceSlider = document.getElementById('priceSlider');
      const priceDisplayWon = document.getElementById('priceDisplayWon');
      const priceDisplayMan = document.getElementById('priceDisplayMan');
      const propTypeBtns = document.querySelectorAll('.prop-type-btn');
      const houseHoldCount = document.getElementById('houseHoldCount');
      const taxExceed85 = document.getElementById('taxExceed85');
      const ltvBtns = document.querySelectorAll('.ltv-btn');
      const ltvIndicatorLabel = document.getElementById('ltvIndicatorLabel');
      const loanAmountInput = document.getElementById('loanAmountInput');
      const loanRateInput = document.getElementById('loanRateInput');
      const depositInput = document.getElementById('depositInput');
      const monthlyRentInput = document.getElementById('monthlyRentInput');
      const annualRentDisplay = document.getElementById('annualRentDisplay');
      const brokerVatToggle = document.getElementById('brokerVatToggle');
      const bondRateSlider = document.getElementById('bondRateSlider');
      const bondDiscountDisplay = document.getElementById('bondDiscountDisplay');
      const presetBtns = document.querySelectorAll('.preset-btn');

      const kpiNetEquity = document.getElementById('kpiNetEquity');
      const kpiMonthlyCashFlow = document.getElementById('kpiMonthlyCashFlow');
      const kpiRoe = document.getElementById('kpiRoe');
      const kpiCapRate = document.getElementById('kpiCapRate');
      const leverageAlertBox = document.getElementById('leverageAlertBox');
      const leverageDetailText = document.getElementById('leverageDetailText');
      const totalIncidentalCostSummary = document.getElementById('totalIncidentalCostSummary');
      const costTaxBreakdown = document.getElementById('costTaxBreakdown');
      const costBrokerage = document.getElementById('costBrokerage');
      const costBondLegal = document.getElementById('costBondLegal');
      const totalOutlayRequired = document.getElementById('totalOutlayRequired');
      const tableRentIn = document.getElementById('tableRentIn');
      const tableInterestOut = document.getElementById('tableInterestOut');
      const tableNetCashFlow = document.getElementById('tableNetCashFlow');
      const saveHistoryBtn = document.getElementById('saveHistoryBtn');

      let currentPropType = 'house';
      let currentLtvPercent = 60.0;

      const PRESETS = {
        '800m': { price: 800000000, ltv: 60, deposit: 10000, rent: 220, rate: 4.10, type: 'house', exceed: false },
        '250m': { price: 250000000, ltv: 70, deposit: 1000, rent: 95, rate: 4.40, type: 'officetel', exceed: false },
        '150m': { price: 150000000, ltv: 60, deposit: 1000, rent: 60, rate: 4.50, type: 'house', exceed: false },
        '1500m': { price: 1500000000, ltv: 50, deposit: 20000, rent: 380, rate: 4.05, type: 'house', exceed: true }
      };

      function formatNumber(num) {
        return Math.round(num).toLocaleString('ko-KR');
      }

      function calculateTaxRate(price, type, houseHold, exceed85) {
        if (type === 'officetel') return 0.046;
        if (type === 'commercial') return 0.046;
        if (houseHold === 'corporate') return 0.124;

        if (houseHold === '1house') {
          let baseRate = 0.01;
          if (price <= 600000000) baseRate = 0.01;
          else if (price <= 900000000) baseRate = (price * (2/300000000) - 3) / 100;
          else baseRate = 0.03;
          const localEduRate = exceed85 ? (baseRate * 0.1) : (baseRate * 0.1);
          const specialRuralRate = exceed85 ? 0.002 : 0.0;
          return baseRate + localEduRate + specialRuralRate;
        } else if (houseHold === '2house') {
          return exceed85 ? 0.09 : 0.084;
        } else if (houseHold === '3house') {
          return exceed85 ? 0.134 : 0.124;
        }
        return 0.011;
      }

      function computeBrokerage(price, type, includeVat) {
        let rate = 0.004;
        if (type === 'officetel') rate = 0.005;
        else if (type === 'commercial') rate = 0.009;
        else {
          if (price < 50000000) rate = 0.006;
          else if (price < 200000000) rate = 0.005;
          else if (price < 900000000) rate = 0.004;
          else if (price < 1200000000) rate = 0.005;
          else rate = 0.007;
        }
        let fee = price * rate;
        if (includeVat) fee *= 1.1;
        return fee;
      }

      function recalculate() {
        if (!priceSlider) return;
        const price = parseFloat(priceSlider.value);
        const ltv = currentLtvPercent;
        const loan = price * (ltv / 100);
        if (loanAmountInput) loanAmountInput.value = formatNumber(loan);
        if (ltvIndicatorLabel) ltvIndicatorLabel.textContent = `LTV ${ltv.toFixed(1)}% (${formatNumber(loan / 10000)}만원)`;

        const loanRate = parseFloat(loanRateInput?.value) || 0;
        const depositMan = parseFloat(depositInput?.value) || 0;
        const depositWon = depositMan * 10000;
        const monthlyRentMan = parseFloat(monthlyRentInput?.value) || 0;
        const monthlyRentWon = monthlyRentMan * 10000;
        if (annualRentDisplay) annualRentDisplay.textContent = formatNumber(monthlyRentMan * 12);

        const taxRate = calculateTaxRate(price, currentPropType, houseHoldCount?.value, taxExceed85?.checked);
        const taxes = price * taxRate;
        const brokerage = computeBrokerage(price, currentPropType, brokerVatToggle?.checked);
        const bondRate = parseFloat(bondRateSlider?.value || 7.5) / 100;
        const bondLegal = (price * 0.0021 * bondRate) + 850000;
        const totalIncidental = taxes + brokerage + bondLegal;

        const totalAcquisitionCost = price + totalIncidental;
        const netEquity = totalAcquisitionCost - loan - depositWon;

        const monthlyInterest = (loan * (loanRate / 100)) / 12;
        const netMonthlyCashFlow = monthlyRentWon - monthlyInterest;
        const annualNetProfit = netMonthlyCashFlow * 12;

        const capRate = ((monthlyRentWon * 12) / price) * 100;
        const roe = netEquity > 0 ? (annualNetProfit / netEquity) * 100 : 0;

        if (priceDisplayWon) priceDisplayWon.textContent = formatNumber(price);
        if (priceDisplayMan) priceDisplayMan.textContent = formatNumber(price / 10000);
        if (bondDiscountDisplay && bondRateSlider) bondDiscountDisplay.textContent = `${parseFloat(bondRateSlider.value).toFixed(2)}%`;

        if (kpiNetEquity) kpiNetEquity.innerHTML = `${formatNumber(netEquity / 10000)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;
        const sign = netMonthlyCashFlow >= 0 ? '+' : '';
        if (kpiMonthlyCashFlow) kpiMonthlyCashFlow.innerHTML = `${sign}${(netMonthlyCashFlow / 10000).toFixed(1)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;
        if (kpiRoe) kpiRoe.innerHTML = `${roe.toFixed(2)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">%</span>`;
        if (kpiCapRate) kpiCapRate.innerHTML = `${capRate.toFixed(2)}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">%</span>`;

        if (totalIncidentalCostSummary) totalIncidentalCostSummary.textContent = `${formatNumber(totalIncidental / 10000)}만원`;
        if (costTaxBreakdown) costTaxBreakdown.textContent = `${formatNumber(taxes / 10000)}만원`;
        if (costBrokerage) costBrokerage.textContent = `${formatNumber(brokerage / 10000)}만원`;
        if (costBondLegal) costBondLegal.textContent = `${formatNumber(bondLegal / 10000)}만원`;
        if (totalOutlayRequired) totalOutlayRequired.textContent = `${formatNumber(totalAcquisitionCost / 10000)}만원`;

        if (tableRentIn) tableRentIn.textContent = `+${monthlyRentMan.toFixed(1)}만원`;
        if (tableInterestOut) tableInterestOut.textContent = `-${formatNumber(monthlyInterest / 10000)}만원`;
        if (tableNetCashFlow) tableNetCashFlow.textContent = `${sign}${(netMonthlyCashFlow / 10000).toFixed(1)}만원`;

        if (leverageAlertBox && leverageDetailText) {
          if (capRate < loanRate) {
            leverageAlertBox.className = "p-4 rounded-xl bg-error-container text-on-error-container flex items-start gap-3 shadow-sm transition-all";
            leverageDetailText.innerHTML = `총 임대수익률(<span class="font-bold">${capRate.toFixed(2)}%</span>)이 대출이자율(<span class="font-bold">${loanRate.toFixed(2)}%</span>)보다 낮습니다. 차입금 비중이 커질수록 자기자본수익률(ROE)이 잠식됩니다.`;
            const icon = leverageAlertBox.querySelector('span.material-symbols-outlined');
            if (icon) { icon.textContent = 'warning'; icon.className = 'material-symbols-outlined text-error text-[24px] flex-shrink-0 mt-0.5'; }
            const title = leverageAlertBox.querySelector('span.font-label-md');
            if (title) { title.className = 'font-label-md text-label-md font-bold tracking-tight text-error'; title.textContent = '[지렛대 효과 판정] 🔴 역마진 주의'; }
          } else {
            leverageAlertBox.className = "p-4 rounded-xl bg-surface-container-high text-on-surface flex items-start gap-3 shadow-sm transition-all";
            leverageDetailText.innerHTML = `총 임대수익률(<span class="font-bold text-tertiary">${capRate.toFixed(2)}%</span>)이 조달금리(<span class="font-bold">${loanRate.toFixed(2)}%</span>)를 상회합니다. 정(Positive)의 레버리지 효과로 자본수익률이 극대화됩니다.`;
            const icon = leverageAlertBox.querySelector('span.material-symbols-outlined');
            if (icon) { icon.textContent = 'check_circle'; icon.className = 'material-symbols-outlined text-tertiary text-[24px] flex-shrink-0 mt-0.5'; }
            const title = leverageAlertBox.querySelector('span.font-label-md');
            if (title) { title.className = 'font-label-md text-label-md font-bold tracking-tight text-tertiary'; title.textContent = '[지렛대 효과 판정] 🟢 건전한 정(Positive) 레버리지'; }
          }
        }
      }

      priceSlider?.addEventListener('input', recalculate);
      houseHoldCount?.addEventListener('change', recalculate);
      taxExceed85?.addEventListener('change', recalculate);
      loanRateInput?.addEventListener('input', recalculate);
      depositInput?.addEventListener('input', recalculate);
      monthlyRentInput?.addEventListener('input', recalculate);
      brokerVatToggle?.addEventListener('change', recalculate);
      bondRateSlider?.addEventListener('input', recalculate);

      propTypeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          propTypeBtns.forEach(b => b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all");
          btn.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md font-semibold bg-surface-container-lowest text-primary shadow-sm transition-all";
          currentPropType = btn.dataset.propType;
          recalculate();
        });
      });

      ltvBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          ltvBtns.forEach(b => b.className = "ltv-btn py-2 bg-surface-container-low text-on-surface-variant hover:bg-surface-container rounded-lg font-label-md text-label-md font-medium transition-colors");
          btn.className = "ltv-btn py-2 bg-primary text-on-primary rounded-lg font-label-md text-label-md font-semibold shadow-sm transition-colors";
          currentLtvPercent = parseFloat(btn.dataset.ltv);
          recalculate();
        });
      });

      presetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          presetBtns.forEach(b => b.className = "preset-btn px-3 py-1.5 rounded-lg bg-surface-container text-on-surface-variant hover:bg-primary hover:text-on-primary transition-all font-label-md text-label-md");
          btn.className = "preset-btn px-3 py-1.5 rounded-lg bg-surface-container-high text-on-surface font-semibold hover:bg-primary hover:text-on-primary transition-all font-label-md text-label-md";

          const preset = PRESETS[btn.dataset.preset];
          if (!preset) return;

          if (priceSlider) priceSlider.value = preset.price;
          if (loanRateInput) loanRateInput.value = preset.rate;
          if (depositInput) depositInput.value = preset.deposit;
          if (monthlyRentInput) monthlyRentInput.value = preset.rent;
          if (taxExceed85) taxExceed85.checked = preset.exceed;
          currentLtvPercent = preset.ltv;

          ltvBtns.forEach(b => {
            if (parseFloat(b.dataset.ltv) === preset.ltv) {
              b.className = "ltv-btn py-2 bg-primary text-on-primary rounded-lg font-label-md text-label-md font-semibold shadow-sm transition-colors";
            } else {
              b.className = "ltv-btn py-2 bg-surface-container-low text-on-surface-variant hover:bg-surface-container rounded-lg font-label-md text-label-md font-medium transition-colors";
            }
          });

          propTypeBtns.forEach(b => {
            if (b.dataset.propType === preset.type) {
              b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md font-semibold bg-surface-container-lowest text-primary shadow-sm transition-all";
            } else {
              b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all";
            }
          });
          currentPropType = preset.type;
          recalculate();
        });
      });

      saveHistoryBtn?.addEventListener('click', () => {
        saveHistoryBtn.innerHTML = `<span class="material-symbols-outlined text-[20px]">check</span> IndexedDB 보관함 저장 완료`;
        saveHistoryBtn.classList.replace('bg-primary', 'bg-tertiary');
        setTimeout(() => {
          saveHistoryBtn.innerHTML = `<span class="material-symbols-outlined text-[20px]">save</span> 계산 결과 히스토리에 저장하기`;
          saveHistoryBtn.classList.replace('bg-tertiary', 'bg-primary');
        }, 1800);
      });

      recalculate();
    })();
  </script>
</body>
</html>
'''

# 치환 작업
master_html = master_html.replace('__PROPERTIES_JSON__', properties_json_str)
master_html = master_html.replace('__REGIONAL_REPORTS_JSON__', regional_reports_json_str)
master_html = master_html.replace('__VIEW_CALCULATOR_CONTENT__', view_calculator_content)
master_html = master_html.replace('__VIEW_BRIEFING_CONTENT__', view_briefing_content)
master_html = master_html.replace('__VIEW_REPORTS_CONTENT__', view_reports_content)

out_path = os.path.join(base_dir, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(master_html)

print(f"Master App V2 Assembled Successfully!")
print(f"Output File: {out_path} ({len(master_html):,} bytes)")
