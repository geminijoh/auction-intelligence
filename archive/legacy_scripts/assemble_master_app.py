# -*- coding: utf-8 -*-
import json, os

base_dir = r'c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상'

props_path = os.path.join(base_dir, 'data', 'properties.json')
with open(props_path, 'r', encoding='utf-8') as f:
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

# 뷰 파일들 읽기
with open(os.path.join(base_dir, 'views', 'view_reports.html'), 'r', encoding='utf-8') as f:
    view_reports_content = f.read()

with open(os.path.join(base_dir, 'views', 'view_calculator.html'), 'r', encoding='utf-8') as f:
    view_calculator_content = f.read()

with open(os.path.join(base_dir, 'views', 'view_briefing.html'), 'r', encoding='utf-8') as f:
    view_briefing_content = f.read()

# 최종 index.html 조립
html_template = f'''<!DOCTYPE html>
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
      html, body {{ margin: 0; padding: 0; }}
      body {{ overscroll-behavior: none; }}
      main > :first-child {{ margin-top: 0 !important; }}
      main > :last-child {{ margin-bottom: 0 !important; }}
    }}
    ::-webkit-scrollbar {{ display: none; }}
    @media print {{
      header, footer, .no-print {{ display: none !important; }}
      #view-briefing, #view-reports, #view-calculator {{ display: block !important; padding: 0 !important; margin: 0 !important; }}
      #view-dashboard {{ display: none !important; }}
      body {{ background: white !important; }}
    }}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
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
          }},
          borderRadius: {{
            DEFAULT: "0.25rem",
            lg: "0.5rem",
            xl: "0.75rem",
            full: "9999px"
          }},
          spacing: {{
            margin: "1rem",
            "space-lg": "1.25rem",
            "space-xs": "0.25rem",
            "gutter-desktop": "1.5rem",
            "space-md": "0.875rem",
            gutter: "1rem",
            "margin-desktop": "2.5rem",
            "space-xl": "2rem",
            "space-sm": "0.5rem"
          }},
          fontFamily: {{
            "label-md": ["Inter", "sans-serif"],
            "headline-md": ["Inter", "sans-serif"],
            "label-sm": ["Inter", "sans-serif"],
            "body-lg": ["Inter", "sans-serif"],
            "headline-lg": ["Inter", "sans-serif"],
            "headline-sm": ["Inter", "sans-serif"],
            "body-md": ["Inter", "sans-serif"],
            "body-sm": ["Inter", "sans-serif"]
          }},
          fontSize: {{
            "label-md": ["12px", {{ lineHeight: "16px", letterSpacing: "0.01em", fontWeight: "600" }}],
            "headline-md": ["22px", {{ lineHeight: "30px", letterSpacing: "-0.015em", fontWeight: "700" }}],
            "label-sm": ["11px", {{ lineHeight: "14px", letterSpacing: "0.02em", fontWeight: "500" }}],
            "body-lg": ["15px", {{ lineHeight: "22px", letterSpacing: "-0.005em", fontWeight: "500" }}],
            "headline-lg": ["26px", {{ lineHeight: "34px", letterSpacing: "-0.02em", fontWeight: "700" }}],
            "headline-sm": ["16px", {{ lineHeight: "24px", letterSpacing: "-0.01em", fontWeight: "600" }}],
            "body-md": ["14px", {{ lineHeight: "20px", letterSpacing: "0em", fontWeight: "400" }}],
            "body-sm": ["13px", {{ lineHeight: "18px", letterSpacing: "0em", fontWeight: "400" }}]
          }}
        }}
      }}
    }};
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
        <button id="nav-btn-dashboard" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm rounded-lg transition-colors bg-primary-container text-on-primary-container font-semibold" onclick="switchMainTab('auction-dashboard')">
          매물 대시보드
        </button>
        <button id="nav-btn-calculator" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('yield-calculator')">
          투자수익률 계산기
        </button>
        <button id="nav-btn-briefing" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('auction-simulator')">
          경매 분석 시뮬레이터
        </button>
        <button id="nav-btn-reports" class="nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors" onclick="switchMainTab('market-reports')">
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
              <span class="font-label-md text-label-md text-on-surface">실전자료 1차 정제 완료</span>
              <span class="text-secondary font-body-sm text-body-sm">·</span>
              <span class="font-body-sm text-body-sm text-on-surface-variant">안성동남타운 · 화성봉담우방(경매/급매) · 안성대덕신라 등 6건 실무 데이터 동기화</span>
            </div>
            <div class="flex items-center gap-space-xs">
              <span class="font-label-sm text-label-sm text-secondary bg-surface-container px-2.5 py-1 rounded-lg">분석기준일: 2026-11-20</span>
              <button onclick="renderCards()" class="text-primary hover:text-primary-container font-label-md text-label-md px-2 py-1 flex items-center gap-1 transition-colors">
                <span class="material-symbols-outlined text-[16px]">refresh</span>데이터 새로고침
              </button>
            </div>
          </div>

          <!-- Search Input Block -->
          <div class="w-full bg-surface-container-lowest rounded-xl p-3 shadow-sm flex flex-col md:flex-row items-center gap-3">
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

          <!-- Segmented Tabs & KPI Ribbon -->
          <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
            <!-- Category Tabs -->
            <div class="flex items-center gap-2 overflow-x-auto pb-1 lg:pb-0 scrollbar-none" id="category-tabs">
              <button onclick="setCategoryFilter('all')" id="tab-all" class="tab-chip active px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md transition-all whitespace-nowrap shadow-sm">
                전체 (6)
              </button>
              <button onclick="setCategoryFilter('recommend')" id="tab-recommend" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
                ★ 추천 매물 (3)
              </button>
              <button onclick="setCategoryFilter('auction')" id="tab-auction" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
                ⚖️ 경매 매물 (5)
              </button>
              <button onclick="setCategoryFilter('sale')" id="tab-sale" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
                🏢 일반 급매 (1)
              </button>
              <button onclick="setCategoryFilter('hold')" id="tab-hold" class="tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap">
                ⚠️ 보류/유찰대기 (1)
              </button>
            </div>

            <!-- Quick KPI Stats Ribbon -->
            <div class="flex items-center gap-3 overflow-x-auto pb-1 lg:pb-0">
              <div class="px-3.5 py-1.5 rounded-xl bg-surface-container flex items-center gap-2 shrink-0">
                <span class="font-label-sm text-label-sm text-secondary">총 분석 매물</span>
                <span class="font-headline-sm text-headline-sm text-primary">6건</span>
              </div>
              <div class="px-3.5 py-1.5 rounded-xl bg-surface-container flex items-center gap-2 shrink-0">
                <span class="font-label-sm text-label-sm text-secondary">추천 평균수익률</span>
                <span class="font-headline-sm text-headline-sm text-tertiary">18.0%</span>
              </div>
              <div class="px-3.5 py-1.5 rounded-xl bg-surface-container flex items-center gap-2 shrink-0">
                <span class="font-label-sm text-label-sm text-secondary">최대 안전마진</span>
                <span class="font-headline-sm text-headline-sm text-on-surface">8,256만</span>
              </div>
              <div class="px-3.5 py-1.5 rounded-xl bg-error-container flex items-center gap-2 shrink-0">
                <span class="font-label-sm text-label-sm text-error">임박 매각기일</span>
                <span class="font-headline-sm text-headline-sm text-error">2건</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Interactive Utility Prompts & Briefing Showcase Banner -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-space-lg mb-10">
          <!-- Showcase 1: Briefing Mode Trigger Card -->
          <div class="col-span-1 md:col-span-2 p-6 rounded-xl bg-gradient-to-r from-primary to-primary-container text-on-primary shadow-sm flex flex-col justify-between relative overflow-hidden">
            <div class="absolute -right-6 -bottom-6 w-44 h-44 rounded-full bg-surface-container-lowest/10 pointer-events-none blur-xl"></div>
            <div class="flex items-start justify-between z-10">
              <div>
                <span class="px-2.5 py-1 rounded-md bg-on-primary/20 text-on-primary font-label-sm text-label-sm mb-3 inline-block">화면 2 · 프리젠테이션 특화 브리핑</span>
                <h2 class="font-headline-md text-headline-md tracking-tight mb-2">핵심 투자 리포트 모드</h2>
                <p class="font-body-md text-body-md text-on-primary/80 max-w-lg">권리분석, 대출, 수익률 시뮬레이션을 불필요한 노이즈 없이 한눈에 검토하는 전용 심층 분석 뷰로 전환합니다.</p>
              </div>
              <span class="material-symbols-outlined text-[36px] text-on-primary/80">co_present</span>
            </div>
            <div class="mt-6 flex flex-wrap items-center gap-3 z-10">
              <button onclick="switchMainTab('auction-simulator')" class="px-4 py-2.5 rounded-xl bg-surface-container-lowest text-primary hover:bg-surface-container font-label-md text-label-md shadow-sm transition-all flex items-center gap-1.5">
                <span class="material-symbols-outlined text-[18px]">visibility</span>심층 시뮬레이터 열기
              </button>
              <button onclick="switchMainTab('market-reports')" class="px-4 py-2.5 rounded-xl bg-primary-container text-on-primary font-label-md text-label-md shadow-sm transition-all flex items-center gap-1.5 border border-white/20">
                <span class="material-symbols-outlined text-[18px]">travel_explore</span>지역 리서치 리포트
              </button>
            </div>
          </div>

          <!-- Showcase 2: Real-time Korean Currency Converter Calculator Widget -->
          <div class="p-6 rounded-xl bg-surface-container-lowest shadow-sm flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-3">
                <div class="flex items-center gap-1.5">
                  <span class="material-symbols-outlined text-primary text-[20px]">calculate</span>
                  <span class="font-label-md text-label-md text-on-surface">실시간 한글 금액 변환기</span>
                </div>
                <span class="px-2 py-0.5 rounded-md bg-surface-container-high text-secondary font-label-sm text-label-sm">입력 보조</span>
              </div>
              <p class="font-body-sm text-body-sm text-secondary mb-4">투자금 또는 대출금 숫자를 입력하면 한글 단위로 즉시 변환합니다.</p>
              <div class="relative mb-2">
                <input id="calc-input" oninput="convertKoreanCurrency()" class="w-full px-3.5 py-2.5 rounded-xl bg-surface-container border border-outline-variant/40 outline-none font-headline-sm text-headline-sm text-on-surface text-right pr-12" placeholder="350000000" type="number" value="68000000"/>
                <span class="absolute right-3.5 top-3.5 font-label-md text-label-md text-secondary">원</span>
              </div>
              <div class="min-h-[24px] flex items-center justify-end">
                <span id="calc-output" class="font-headline-sm text-headline-sm text-primary tracking-tight">6,800만 원</span>
              </div>
            </div>
            <div class="pt-4 border-t border-outline-variant/20 flex items-center justify-between text-secondary font-label-sm text-label-sm">
              <span>취득세(1.1% 추산)</span>
              <span id="calc-tax" class="font-semibold text-on-surface">74.8만 원</span>
            </div>
          </div>
        </section>

        <!-- Section Header -->
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-2">
            <h2 class="font-headline-md text-headline-md tracking-tight text-on-surface">분석 매물 리스트</h2>
            <span id="list-count-badge" class="px-2 py-0.5 rounded-full bg-surface-container-high text-on-surface-variant font-label-sm text-label-sm">6건 검색됨</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-secondary font-medium">정렬: 추천순</span>
          </div>
        </div>

        <!-- [화면 1] 매물 카드 그리드 (3열 반응형) -->
        <section id="property-cards-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- JavaScript로 6개 실전 매물 렌더링 -->
        </section>
      </div>
    </div>
  </main>

  <!-- ================= 2. VIEW: 투자수익률 계산기 ================= -->
  <main id="view-calculator" class="w-full pt-16 bg-surface min-h-screen hidden">
    {view_calculator_content}
  </main>

  <!-- ================= 3. VIEW: 경매 분석 시뮬레이터 / 매물 상세분석 ================= -->
  <main id="view-briefing" class="w-full pt-16 bg-surface min-h-screen hidden">
    {view_briefing_content}
  </main>

  <!-- ================= 4. VIEW: 시장동향 리포트 뷰어 ================= -->
  <main id="view-reports" class="w-full pt-16 bg-surface min-h-screen hidden">
    {view_reports_content}
  </main>

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
    const PROPERTIES = {properties_json_str};
    let currentCategory = 'all';
    let currentSearch = '';

    // 금액 한글 포맷팅 함수
    function formatKRW(val) {{
      if (val === undefined || val === null) return '-';
      if (Math.abs(val) >= 100000000) {{
        const uk = Math.floor(val / 100000000);
        const man = Math.round((val % 100000000) / 10000);
        return man > 0 ? `${{uk}}억 ${{man.toLocaleString()}}만 원` : `${{uk}}억 원`;
      }}
      return `${{Math.round(val / 10000).toLocaleString()}}만 원`;
    }}

    // 4대 탭 화면 전환 라우터
    function switchMainTab(targetPath) {{
      const tabs = [
        {{ path: 'auction-dashboard', viewId: 'view-dashboard', btnId: 'nav-btn-dashboard' }},
        {{ path: 'yield-calculator', viewId: 'view-calculator', btnId: 'nav-btn-calculator' }},
        {{ path: 'auction-simulator', viewId: 'view-briefing', btnId: 'nav-btn-briefing' }},
        {{ path: 'market-reports', viewId: 'view-reports', btnId: 'nav-btn-reports' }}
      ];

      tabs.forEach(t => {{
        const v = document.getElementById(t.viewId);
        const b = document.getElementById(t.btnId);
        if (t.path === targetPath) {{
          if (v) v.classList.remove('hidden');
          if (b) {{
            b.className = "nav-tab-btn px-3 py-2 font-body-sm text-body-sm rounded-lg transition-colors bg-primary-container text-on-primary-container font-semibold";
          }}
        }} else {{
          if (v) v.classList.add('hidden');
          if (b) {{
            b.className = "nav-tab-btn px-3 py-2 font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container hover:text-on-surface rounded-lg transition-colors";
          }}
        }}
      }});

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // 카테고리 필터
    function setCategoryFilter(cat) {{
      currentCategory = cat;
      const tabs = ['all', 'recommend', 'auction', 'sale', 'hold'];
      tabs.forEach(t => {{
        const el = document.getElementById(`tab-${{t}}`);
        if (el) {{
          if (t === cat) {{
            el.className = "tab-chip active px-4 py-2 rounded-xl bg-primary text-on-primary font-label-md text-label-md transition-all whitespace-nowrap shadow-sm";
          }} else {{
            el.className = "tab-chip px-4 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-all whitespace-nowrap";
          }}
        }}
      }});
      renderCards();
    }}

    // 검색 핸들러
    function handleSearch() {{
      currentSearch = document.getElementById('search-input').value.trim().toLowerCase();
      renderCards();
    }}

    // 한글 금액 변환
    function convertKoreanCurrency() {{
      const val = parseFloat(document.getElementById('calc-input').value) || 0;
      document.getElementById('calc-output').textContent = formatKRW(val);
      document.getElementById('calc-tax').textContent = formatKRW(val * 0.011);
    }}

    // 매물 카드 렌더링
    function renderCards() {{
      const container = document.getElementById('property-cards-container');
      const filtered = PROPERTIES.filter(p => {{
        if (currentCategory === 'recommend' && !['적극추천', '추천'].includes(p.status)) return false;
        if (currentCategory === 'auction' && p.category !== '경매') return false;
        if (currentCategory === 'sale' && p.category !== '일반급매') return false;
        if (currentCategory === 'hold' && p.status !== '보류/유찰대기') return false;

        if (currentSearch) {{
          const matchCase = p.caseNumber.toLowerCase().includes(currentSearch);
          const matchName = p.propertyName.toLowerCase().includes(currentSearch);
          const matchAddr = p.address.toLowerCase().includes(currentSearch);
          if (!matchCase && !matchName && !matchAddr) return false;
        }}
        return true;
      }});

      document.getElementById('list-count-badge').textContent = `${{filtered.length}}건 검색됨`;

      container.innerHTML = filtered.map(p => {{
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
            <div class="relative w-full h-48 bg-surface-container overflow-hidden">
              <div class="w-full h-full bg-cover bg-center group-hover:scale-105 transition-transform duration-500" style="background-image: url('${{p.imageUrl}}');"></div>
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              
              <div class="absolute top-3 left-3 flex items-center gap-1.5">
                <span class="px-2.5 py-1 rounded-md bg-surface-container-lowest/90 backdrop-blur-sm text-primary font-label-sm text-label-sm font-semibold">
                  ${{p.category}}
                </span>
                <span class="px-2 py-1 rounded-md ${{statusBadgeClass}} font-label-sm text-label-sm flex items-center gap-1 font-semibold">
                  ${{p.status}}
                </span>
              </div>

              <div class="absolute top-3 right-3 flex items-center gap-1">
                <button class="w-8 h-8 rounded-full bg-surface-container-lowest/90 backdrop-blur-sm text-error hover:bg-surface-container-lowest flex items-center justify-center transition-colors">
                  <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">favorite</span>
                </button>
              </div>

              <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-on-primary">
                <span class="font-label-sm text-label-sm font-semibold tracking-wide">${{p.caseNumber}}</span>
                <span class="font-label-sm text-label-sm text-on-primary/90">${{p.court || ''}}</span>
              </div>
            </div>

            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <div class="mb-3">
                  <h3 class="font-headline-sm text-headline-sm text-on-surface truncate group-hover:text-primary transition-colors" title="${{p.propertyName}}">
                    ${{p.propertyName}}
                  </h3>
                  <p class="font-body-sm text-body-sm text-secondary truncate mt-0.5">${{p.address}}</p>
                </div>

                <div class="p-3.5 rounded-xl bg-surface-container mb-4">
                  <div class="flex justify-between items-center mb-1.5">
                    <span class="font-body-sm text-body-sm text-secondary">${{isAuction ? '감정평가액' : '최초호가'}}</span>
                    <span class="font-label-md text-label-md text-secondary line-through">${{formatKRW(p.appraisedValue)}}</span>
                  </div>
                  <div class="flex justify-between items-baseline">
                    <div class="flex items-center gap-1.5">
                      <span class="font-label-sm text-label-sm ${{p.minimumBidRate < 100 ? 'text-error bg-error-container/60' : 'text-secondary bg-surface-container-high'}} px-1.5 py-0.5 rounded font-semibold">
                        ${{isAuction ? (p.minimumBidRate < 100 ? '1회 유찰' : '신건') : '네고목표'}}
                      </span>
                      <span class="font-headline-sm text-headline-sm text-on-surface">${{isAuction ? '최저매각가' : '네고목표가'}}</span>
                    </div>
                    <div class="text-right">
                      <span class="font-headline-md text-headline-md text-primary tracking-tight">${{formatKRW(p.minimumBidPrice)}}</span>
                      <span class="font-label-sm text-label-sm text-secondary ml-1">(${{p.minimumBidRate}}%)</span>
                    </div>
                  </div>
                  <div class="flex justify-between items-baseline mt-2 pt-2 border-t border-outline-variant/30">
                    <span class="text-xs font-bold text-on-surface">★ 추천 ${{isAuction ? '입찰가' : '매수가'}}</span>
                    <span class="text-base font-black text-primary">${{formatKRW(p.recommendedBidPrice)}}</span>
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2 mb-4">
                  <div class="p-2.5 rounded-xl bg-tertiary-container/10 flex flex-col">
                    <span class="font-label-sm text-label-sm text-tertiary">예상 연 ROE</span>
                    <span class="font-headline-sm text-headline-sm text-tertiary mt-0.5 font-black">${{p.roePercent ? p.roePercent + '%' : '-'}}</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-secondary-container/50 flex flex-col">
                    <span class="font-label-sm text-label-sm text-secondary">필요 실투자금</span>
                    <span class="font-headline-sm text-headline-sm text-on-surface mt-0.5 font-black">${{formatKRW(p.netInvestment)}}</span>
                  </div>
                </div>

                <div class="mb-4">
                  <span class="font-label-sm text-label-sm text-secondary block mb-2">핵심 입지 & 개발 호재</span>
                  <div class="flex flex-wrap gap-1.5">
                    ${{p.locationHighlights.slice(0, 3).map(h => `
                      <span class="px-2 py-0.5 rounded-md bg-surface-container-low text-on-surface-variant font-label-sm text-label-sm truncate max-w-[200px]" title="${{h}}">
                        ${{h}}
                      </span>
                    `).join('')}}
                  </div>
                </div>
              </div>

              <div class="pt-4 border-t border-surface-container flex items-center justify-between gap-2">
                <button onclick="switchMainTab('auction-simulator')" class="flex-1 py-2.5 px-4 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md flex items-center justify-center gap-1.5 shadow-sm transition-all" type="button">
                  <span class="material-symbols-outlined text-[18px]">assignment</span>투자 분석 시뮬레이터
                </button>
              </div>
            </div>
          </article>
        `;
      }}).join('');
    }}

    // JSON 내보내기
    function exportDataJSON() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(PROPERTIES, null, 2));
      const anchor = document.createElement('a');
      anchor.setAttribute("href", dataStr);
      anchor.setAttribute("download", `propintelligence_db_${{new Date().toISOString().slice(0, 10)}}.json`);
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
    }}

    // 초기 실행
    document.addEventListener('DOMContentLoaded', () => {{
      renderCards();
      convertKoreanCurrency();
      if (typeof updateCalculations === 'function') {{
        updateCalculations();
      }}
    }});
  </script>

  <!-- ================= 2. 계산기 스크립트 엔진 ================= -->
  <script>
    (function initCalculatorEngine() {{
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

      const PRESETS = {{
        '800m': {{ price: 800000000, ltv: 60, deposit: 10000, rent: 220, rate: 4.10, type: 'house', exceed: false }},
        '250m': {{ price: 250000000, ltv: 70, deposit: 1000, rent: 95, rate: 4.40, type: 'officetel', exceed: false }},
        '150m': {{ price: 150000000, ltv: 60, deposit: 1000, rent: 60, rate: 4.50, type: 'house', exceed: false }},
        '1500m': {{ price: 1500000000, ltv: 50, deposit: 20000, rent: 380, rate: 4.05, type: 'house', exceed: true }}
      }};

      function formatNumber(num) {{
        return Math.round(num).toLocaleString('ko-KR');
      }}

      function calculateTaxRate(price, type, countKey, isExceed85) {{
        let baseRate = 0.01;
        let eduRate = 0.001;
        let specialRuralRate = isExceed85 ? 0.002 : 0;

        if (type === 'officetel' || type === 'commercial') {{
          return 0.04 + 0.004 + 0.002;
        }}

        if (countKey === 'corp' || countKey === '3_multi') {{
          baseRate = 0.12;
          eduRate = 0.004;
        }} else if (countKey === '2_adj') {{
          baseRate = 0.08;
          eduRate = 0.004;
        }} else {{
          if (price <= 600000000) {{
            baseRate = 0.01;
            eduRate = 0.001;
          }} else if (price <= 900000000) {{
            baseRate = ((price * 2 / 300000000) - 3) / 100;
            eduRate = baseRate * 0.1;
          }} else {{
            baseRate = 0.03;
            eduRate = 0.003;
          }}
        }}
        return baseRate + eduRate + specialRuralRate;
      }}

      function computeBrokerage(price, type, includeVat) {{
        let rate = 0.004;
        if (type === 'officetel') rate = 0.005;
        if (type === 'commercial') rate = 0.009;
        if (type === 'house') {{
          if (price < 50000000) rate = 0.006;
          else if (price < 200000000) rate = 0.005;
          else if (price < 900000000) rate = 0.004;
          else if (price < 1200000000) rate = 0.005;
          else rate = 0.007;
        }}
        let fee = price * rate;
        if (includeVat) fee *= 1.1;
        return fee;
      }}

      function recalculate() {{
        if (!priceSlider) return;
        const price = parseFloat(priceSlider.value);
        const ltv = currentLtvPercent;
        const loan = price * (ltv / 100);
        if (loanAmountInput) loanAmountInput.value = formatNumber(loan);
        if (ltvIndicatorLabel) ltvIndicatorLabel.textContent = `LTV ${{ltv.toFixed(1)}}% (${{formatNumber(loan / 10000)}}만원)`;

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
        if (bondDiscountDisplay && bondRateSlider) bondDiscountDisplay.textContent = `${{parseFloat(bondRateSlider.value).toFixed(2)}}%`;

        if (kpiNetEquity) kpiNetEquity.innerHTML = `${{formatNumber(netEquity / 10000)}}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;
        const sign = netMonthlyCashFlow >= 0 ? '+' : '';
        if (kpiMonthlyCashFlow) kpiMonthlyCashFlow.innerHTML = `${{sign}}${{(netMonthlyCashFlow / 10000).toFixed(1)}}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">만원</span>`;
        if (kpiRoe) kpiRoe.innerHTML = `${{roe.toFixed(2)}}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">%</span>`;
        if (kpiCapRate) kpiCapRate.innerHTML = `${{capRate.toFixed(2)}}<span class="font-body-sm text-body-sm font-normal text-on-surface-variant ml-0.5">%</span>`;

        if (totalIncidentalCostSummary) totalIncidentalCostSummary.textContent = `${{formatNumber(totalIncidental / 10000)}}만원`;
        if (costTaxBreakdown) costTaxBreakdown.textContent = `${{formatNumber(taxes / 10000)}}만원`;
        if (costBrokerage) costBrokerage.textContent = `${{formatNumber(brokerage / 10000)}}만원`;
        if (costBondLegal) costBondLegal.textContent = `${{formatNumber(bondLegal / 10000)}}만원`;
        if (totalOutlayRequired) totalOutlayRequired.textContent = `${{formatNumber(totalAcquisitionCost / 10000)}}만원`;

        if (tableRentIn) tableRentIn.textContent = `+${{monthlyRentMan.toFixed(1)}}만원`;
        if (tableInterestOut) tableInterestOut.textContent = `-${{formatNumber(monthlyInterest / 10000)}}만원`;
        if (tableNetCashFlow) tableNetCashFlow.textContent = `${{sign}}${{(netMonthlyCashFlow / 10000).toFixed(1)}}만원`;

        if (leverageAlertBox && leverageDetailText) {{
          if (capRate < loanRate) {{
            leverageAlertBox.className = "p-4 rounded-xl bg-error-container text-on-error-container flex items-start gap-3 shadow-sm transition-all";
            leverageDetailText.innerHTML = `총 임대수익률(<span class="font-bold">${{capRate.toFixed(2)}}%</span>)이 대출이자율(<span class="font-bold">${{loanRate.toFixed(2)}}%</span>)보다 낮습니다. 차입금 비중이 커질수록 자기자본수익률(ROE)이 잠식됩니다.`;
            const icon = leverageAlertBox.querySelector('span.material-symbols-outlined');
            if (icon) {{ icon.textContent = 'warning'; icon.className = 'material-symbols-outlined text-error text-[24px] flex-shrink-0 mt-0.5'; }}
            const title = leverageAlertBox.querySelector('span.font-label-md');
            if (title) {{ title.className = 'font-label-md text-label-md font-bold tracking-tight text-error'; title.textContent = '[지렛대 효과 판정] 🔴 역마진 주의'; }}
          }} else {{
            leverageAlertBox.className = "p-4 rounded-xl bg-surface-container-high text-on-surface flex items-start gap-3 shadow-sm transition-all";
            leverageDetailText.innerHTML = `총 임대수익률(<span class="font-bold text-tertiary">${{capRate.toFixed(2)}}%</span>)이 조달금리(<span class="font-bold">${{loanRate.toFixed(2)}}%</span>)를 상회합니다. 정(Positive)의 레버리지 효과로 자본수익률이 극대화됩니다.`;
            const icon = leverageAlertBox.querySelector('span.material-symbols-outlined');
            if (icon) {{ icon.textContent = 'check_circle'; icon.className = 'material-symbols-outlined text-tertiary text-[24px] flex-shrink-0 mt-0.5'; }}
            const title = leverageAlertBox.querySelector('span.font-label-md');
            if (title) {{ title.className = 'font-label-md text-label-md font-bold tracking-tight text-tertiary'; title.textContent = '[지렛대 효과 판정] 🟢 건전한 정(Positive) 레버리지'; }}
          }}
        }}
      }}

      priceSlider?.addEventListener('input', recalculate);
      houseHoldCount?.addEventListener('change', recalculate);
      taxExceed85?.addEventListener('change', recalculate);
      loanRateInput?.addEventListener('input', recalculate);
      depositInput?.addEventListener('input', recalculate);
      monthlyRentInput?.addEventListener('input', recalculate);
      brokerVatToggle?.addEventListener('change', recalculate);
      bondRateSlider?.addEventListener('input', recalculate);

      propTypeBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          propTypeBtns.forEach(b => b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all");
          btn.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md font-semibold bg-surface-container-lowest text-primary shadow-sm transition-all";
          currentPropType = btn.dataset.propType;
          recalculate();
        }});
      }});

      ltvBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          ltvBtns.forEach(b => b.className = "ltv-btn py-2 bg-surface-container-low text-on-surface-variant hover:bg-surface-container rounded-lg font-label-md text-label-md font-medium transition-colors");
          btn.className = "ltv-btn py-2 bg-primary text-on-primary rounded-lg font-label-md text-label-md font-semibold shadow-sm transition-colors";
          currentLtvPercent = parseFloat(btn.dataset.ltv);
          recalculate();
        }});
      }});

      presetBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
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

          ltvBtns.forEach(b => {{
            if (parseFloat(b.dataset.ltv) === preset.ltv) {{
              b.className = "ltv-btn py-2 bg-primary text-on-primary rounded-lg font-label-md text-label-md font-semibold shadow-sm transition-colors";
            }} else {{
              b.className = "ltv-btn py-2 bg-surface-container-low text-on-surface-variant hover:bg-surface-container rounded-lg font-label-md text-label-md font-medium transition-colors";
            }}
          }});

          propTypeBtns.forEach(b => {{
            if (b.dataset.propType === preset.type) {{
              b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md font-semibold bg-surface-container-lowest text-primary shadow-sm transition-all";
            }} else {{
              b.className = "prop-type-btn py-2 text-center rounded-md font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all";
            }}
          }});
          currentPropType = preset.type;
          recalculate();
        }});
      }});

      saveHistoryBtn?.addEventListener('click', () => {{
        saveHistoryBtn.innerHTML = `<span class="material-symbols-outlined text-[20px]">check</span> IndexedDB 보관함 저장 완료`;
        saveHistoryBtn.classList.replace('bg-primary', 'bg-tertiary');
        setTimeout(() => {{
          saveHistoryBtn.innerHTML = `<span class="material-symbols-outlined text-[20px]">save</span> 계산 결과 히스토리에 저장하기`;
          saveHistoryBtn.classList.replace('bg-tertiary', 'bg-primary');
        }}, 1800);
      }});

      recalculate();
    }})();
  </script>

  <!-- ================= 3. 경매 시뮬레이터 파라미터 엔진 ================= -->
  <script>
    function updateCalculations() {{
      const bidSlider = document.getElementById('bid-price-slider');
      const rateSlider = document.getElementById('interest-rate-slider');
      const jeonseSlider = document.getElementById('jeonse-price-slider');
      if (!bidSlider) return;

      const bidPrice = parseFloat(bidSlider.value);
      const rate = parseFloat(rateSlider.value);
      const jeonse = parseFloat(jeonseSlider.value);

      document.getElementById('bid-price-display').innerText = bidPrice.toFixed(2);
      document.getElementById('interest-rate-display').innerText = rate.toFixed(1);
      document.getElementById('jeonse-price-display').innerText = jeonse.toFixed(1);

      const taxAndFees = (bidPrice * 0.033) + 0.135;
      const totalRequired = bidPrice + taxAndFees;
      const netInvestment = totalRequired - jeonse;

      const loanAmount = bidPrice * 0.7;
      const monthlyInterest = (loanAmount * 100000000 * (rate / 100)) / 12;

      const netInvestmentWon = Math.round(netInvestment * 10000);
      const netBillion = Math.floor(netInvestmentWon / 10000);
      const netMillion = Math.abs(netInvestmentWon % 10000);

      document.getElementById('calc-net-investment').innerText = 
        netBillion + '억 ' + netMillion.toLocaleString() + '만 원';

      document.getElementById('calc-monthly-interest').innerText = 
        Math.round(monthlyInterest / 10000).toLocaleString() + '만 원 / 월';

      const costsWon = Math.round(taxAndFees * 10000);
      document.getElementById('calc-costs').innerText = costsWon.toLocaleString() + '만 원';
    }}

    function resetSimulator() {{
      const b = document.getElementById('bid-price-slider');
      const r = document.getElementById('interest-rate-slider');
      const j = document.getElementById('jeonse-price-slider');
      if (b) b.value = 15.6;
      if (r) r.value = 4.2;
      if (j) j.value = 11.5;
      updateCalculations();
    }}
  </script>
</body>
</html>
'''

out_path = os.path.join(base_dir, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Master app assembled successfully. Output: {out_path}, Size: {len(html_template)} bytes")

