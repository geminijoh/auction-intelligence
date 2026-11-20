# -*- coding: utf-8 -*-
import json, os

props_path = r'c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\data\properties.json'
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

html_content = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta content="web_standard" name="shell-type">
  <title>AUCTION BRIEF | 경매 매물 분석 및 브리핑 시스템</title>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
  <style>
    @layer base {
      html, body { margin: 0; padding: 0; }
      body { overscroll-behavior: none; }
      main > :first-child { margin-top: 0 !important; }
      main > :last-child { margin-bottom: 0 !important; }
    }
    ::-webkit-scrollbar { display: none; }
    @media print {
      header, .no-print { display: none !important; }
      #view-briefing { display: block !important; padding: 0 !important; margin: 0 !important; }
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
            "surface-dim": "#d1dbed",
            "on-primary-fixed": "#001a42",
            "on-secondary": "#ffffff",
            "secondary-fixed": "#d7e3fa",
            "surface-container-lowest": "#ffffff",
            "tertiary-fixed-dim": "#57df92",
            "tertiary-container": "#00864e",
            "on-tertiary-fixed-variant": "#00522d",
            "primary-container": "#006fee",
            "on-primary-container": "#fefcff",
            "on-primary": "#ffffff",
            "background": "#f8f9ff",
            "surface-tint": "#005ac3",
            "outline-variant": "#c1c6d7",
            "on-tertiary-container": "#f6fff5",
            "secondary-container": "#d4e0f7",
            "primary": "#0058be",
            "on-primary-fixed-variant": "#004395",
            "error-container": "#ffdad6",
            "secondary": "#535f72",
            "on-secondary-container": "#576377",
            "inverse-on-surface": "#eaf1ff",
            "on-secondary-fixed-variant": "#3b475a",
            "tertiary": "#006a3c",
            "surface-container-high": "#dfe9fb",
            "inverse-surface": "#27313f",
            "on-error": "#ffffff",
            "secondary-fixed-dim": "#bbc7dd",
            "outline": "#717786",
            "on-surface": "#121c29",
            "surface-variant": "#d9e3f5",
            "surface-container": "#e6eeff",
            "on-tertiary-fixed": "#00210f",
            "surface": "#f8f9ff",
            "surface-container-low": "#eff4ff",
            "primary-fixed-dim": "#aec6ff",
            "on-surface-variant": "#414755",
            "on-secondary-fixed": "#101c2c",
            "error": "#ba1a1a",
            "tertiary-fixed": "#76fcac",
            "on-background": "#121c29",
            "surface-container-highest": "#d9e3f5",
            "inverse-primary": "#aec6ff",
            "on-tertiary": "#ffffff",
            "surface-bright": "#f8f9ff",
            "on-error-container": "#93000a",
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
            "label-md": ["Inter"],
            "headline-md": ["Inter"],
            "label-sm": ["Inter"],
            "body-lg": ["Inter"],
            "headline-lg": ["Inter"],
            "headline-sm": ["Inter"],
            "body-md": ["Inter"],
            "body-sm": ["Inter"]
          },
          fontSize: {
            "label-md": ["12px", { lineHeight: "16px", letterSpacing: "0.01em", fontWeight: "600" }],
            "headline-md": ["22px", { lineHeight: "30px", letterSpacing: "-0.015em", fontWeight: "700" }],
            "label-sm": ["11px", { lineHeight: "14px", letterSpacing: "0.02em", fontWeight: "500" }],
            "body-lg": ["15px", { lineHeight: "22px", letterSpacing: "-0.005em", fontWeight: "500" }],
            "headline-lg": ["26px", { lineHeight: "34px", letterSpacing: "-0.02em", fontWeight: "700" }],
            "headline-sm": ["16px", { lineHeight: "24px", letterSpacing: "-0.01em", fontWeight: "600" }],
            "body-md": ["14px", { lineHeight: "20px", letterSpacing: "0em", fontWeight: "400" }],
            "body-sm": ["13px", { lineHeight: "18px", letterSpacing: "0em", fontWeight: "400" }]
          }
        }
      }
    };
  </script>
</head>
<body class="bg-surface font-body-md text-on-surface antialiased selection:bg-secondary-container selection:text-on-secondary-fixed">

  <!-- 1. Global Navigation Bar (AUCTION BRIEF) -->
  <header class="fixed top-0 left-0 w-full z-50 bg-surface-container-lowest border-b border-outline-variant/30 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
    <div class="h-16 max-w-7xl mx-auto px-6 flex items-center justify-between">
      <div class="flex items-center gap-space-md">
        <a class="font-headline-sm text-headline-sm text-on-surface tracking-tight flex items-center gap-space-xs cursor-pointer" onclick="switchView('dashboard')">
          AUCTION BRIEF
        </a>
        <span class="px-2 py-0.5 rounded-md bg-surface-container-high text-on-surface-variant font-label-sm text-label-sm border border-outline-variant/40">
          v1.0 실전자료 정제
        </span>
      </div>

      <nav class="hidden md:flex items-center gap-space-sm">
        <button id="nav-dashboard" onclick="switchView('dashboard')" class="px-3 py-2 transition-colors bg-surface-container-high text-on-surface font-headline-sm rounded-lg text-sm">
          매물 대시보드
        </button>
        <button id="nav-briefing" onclick="switchView('briefing')" class="px-3 py-2 rounded-lg text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-md text-body-md transition-colors text-sm">
          투자 분석 상세
        </button>
      </nav>

      <div class="flex items-center gap-space-sm">
        <button onclick="exportJSON()" class="px-3.5 py-2 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md transition-colors flex items-center gap-1.5" type="button">
          <span class="material-symbols-outlined text-[16px]">download</span>
          데이터 백업/복원
        </button>
        <button onclick="alert('정제된 6개 마스터 매물이 로드되어 있습니다. 새로운 PDF/엑셀은 자동화 폴더를 통해 추가하실 수 있습니다.')" class="px-4 py-2 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md shadow-[0_4px_16px_rgba(53,65,83,0.08)] flex items-center gap-1 transition-all" type="button">
          <span class="material-symbols-outlined text-[16px]">add</span>
          새 경매 물건 등록
        </button>
        <div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold text-xs shadow-sm">
          P
        </div>
      </div>
    </div>
  </header>

  <!-- ================= VIEW 1: 매물 대시보드 (_1 디자인 100% 동일) ================= -->
  <main id="view-dashboard" class="w-full pt-16 bg-surface">
    <div class="max-w-7xl mx-auto px-6 py-8">
      <div class="flex flex-col w-full">

        <!-- Top Control, Search & Filter Hub -->
        <section class="w-full flex flex-col gap-space-lg mb-8">
          <!-- Status & Operational Banner -->
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
              <input id="search-input" oninput="handleSearch()" class="w-full bg-transparent border-0 outline-none font-body-md text-body-md text-on-surface placeholder:text-outline" placeholder="사건번호, 물건명(예: 안성동남타운, 봉담우방), 지역명 검색" type="text">
              <button class="text-outline hover:text-on-surface p-1 rounded-full flex items-center justify-center">
                <span class="material-symbols-outlined text-[18px]">mic</span>
              </button>
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
              <button onclick="openBriefing('2026-239')" class="px-4 py-2.5 rounded-xl bg-surface-container-lowest text-primary hover:bg-surface-container font-label-md text-label-md shadow-sm transition-all flex items-center gap-1.5">
                <span class="material-symbols-outlined text-[18px]">visibility</span>상세 리포트 열기
              </button>
              <span class="font-label-sm text-label-sm text-on-primary/70">★ 안성동남타운 102동 1202호 (2026타경239) 분석 리포트 사전 로드됨</span>
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
                <input id="calc-input" oninput="convertKoreanCurrency()" class="w-full px-3.5 py-2.5 rounded-xl bg-surface-container border border-outline-variant/40 outline-none font-headline-sm text-headline-sm text-on-surface text-right pr-12" placeholder="350000000" type="number" value="68000000">
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

  <!-- ================= VIEW 2: 투자 분석 상세 브리핑 (_7 디자인 100% 동일) ================= -->
  <main id="view-briefing" class="w-full pt-16 bg-surface hidden">
    <!-- Breadcrumb & Top Bar -->
    <div class="bg-surface-container-lowest border-b border-outline-variant/30 py-3 no-print">
      <div class="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <div class="flex items-center gap-2 text-xs text-secondary">
          <button onclick="switchView('dashboard')" class="hover:text-primary font-semibold flex items-center gap-1 transition-colors">
            <span class="material-symbols-outlined text-[16px]">arrow_back</span>매물 대시보드로 돌아가기
          </button>
          <span>/</span>
          <span id="briefing-breadcrumb-name" class="text-on-surface font-medium">안성동남타운 102동 1202호</span>
        </div>

        <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-end">
          <!-- 매물 전환 셀렉트박스 -->
          <select id="briefing-select" onchange="loadBriefingDetail(this.value)" class="bg-surface-container border border-outline-variant/40 text-on-surface text-xs rounded-lg px-2.5 py-1.5 font-medium outline-none">
            <!-- 옵션 동적 추가 -->
          </select>
          <button onclick="window.print()" class="px-3 py-1.5 rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface font-label-sm text-label-sm flex items-center gap-1 transition-colors">
            <span class="material-symbols-outlined text-[16px]">print</span>출력 / PDF 저장
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content Container -->
    <div class="max-w-7xl mx-auto px-6 py-6">
      
      <!-- Top Title & Badge Header Section -->
      <div class="mb-6 p-6 rounded-2xl bg-surface-container-lowest shadow-sm border border-outline-variant/20 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span id="detail-category-badge" class="px-2.5 py-0.5 rounded-md bg-primary text-on-primary font-label-sm text-label-sm font-bold">
              경매 매물
            </span>
            <span id="detail-status-badge" class="px-2 py-0.5 rounded-md bg-tertiary-container/20 text-tertiary font-label-sm text-label-sm font-bold">
              ★ 적극추천
            </span>
            <span id="detail-case-no" class="text-secondary font-label-md text-label-md font-mono">
              평택지원 2026타경239
            </span>
          </div>
          <h1 id="detail-title" class="text-2xl font-extrabold tracking-tight text-on-surface">
            안성동남타운 102동 1202호 (24평형)
          </h1>
          <p id="detail-address" class="text-xs text-secondary mt-1">
            경기도 안성시 금석동 81 (도로명: 안성맞춤대로 1320-21)
          </p>
        </div>

        <div class="flex items-center gap-3 shrink-0">
          <div class="px-4 py-2.5 rounded-xl bg-surface-container text-right">
            <span class="text-[11px] text-secondary block">정상 실거래 시세</span>
            <span id="detail-market-price" class="text-base font-bold text-on-surface">7,500만 원</span>
          </div>
          <div class="px-4 py-2.5 rounded-xl bg-primary/10 text-right border border-primary/20">
            <span class="text-[11px] text-primary font-bold block">★ 권고 입찰가</span>
            <span id="detail-recommended-price" class="text-xl font-extrabold text-primary">6,800만 원</span>
          </div>
        </div>
      </div>

      <!-- Two-Column Balanced Grid (Stitch _7 원본 구조 100% 동일) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

        <!-- ================= LEFT COLUMN (lg:col-span-6) ================= -->
        <div class="lg:col-span-6 flex flex-col gap-6">
          
          <!-- 1. 가격 평가 및 입찰 가이드라인 카드 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-4">
            <div class="flex items-center justify-between pb-1 border-b border-outline-variant/20">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-primary text-[22px]">monetization_on</span>
                <h2 class="text-base font-bold text-on-surface">가격 평가 및 입찰 가이드라인</h2>
              </div>
              <span id="detail-discount-rate" class="text-xs font-bold text-error bg-error-container/40 px-2 py-0.5 rounded">신건 대비 -30% 할인</span>
            </div>

            <!-- Price Metrics Comparison Grid -->
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-[11px] text-secondary font-medium block">감정평가액</span>
                <span id="detail-appraised-price" class="text-sm font-bold text-on-surface mt-0.5 block">9,100만 원</span>
                <span class="text-[10px] text-secondary">100%</span>
              </div>
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-[11px] text-secondary font-medium block">최저매각가격</span>
                <span id="detail-minimum-price" class="text-sm font-bold text-on-surface mt-0.5 block">6,370만 원</span>
                <span class="text-[10px] text-error font-semibold">70% (1회 유찰)</span>
              </div>
              <div class="p-3 rounded-xl bg-primary-fixed/30 border border-primary/20">
                <span class="text-[11px] text-primary font-bold block">상한 적정 입찰가</span>
                <span id="detail-recom-card-price" class="text-sm font-extrabold text-primary mt-0.5 block">6,800만 원</span>
                <span class="text-[10px] text-primary font-semibold">낙찰확률 65%</span>
              </div>
            </div>

            <!-- Progress Bar -->
            <div>
              <div class="flex justify-between text-xs text-secondary mb-1">
                <span>최저가 (6,370만)</span>
                <span class="font-bold text-primary">추천가 (6,800만)</span>
                <span>정상시세 (7,500만)</span>
              </div>
              <div class="w-full h-2.5 rounded-full bg-surface-container overflow-hidden flex">
                <div class="h-full bg-secondary-fixed" style="width: 60%;"></div>
                <div class="h-full bg-primary" style="width: 15%;"></div>
                <div class="h-full bg-tertiary-fixed" style="width: 25%;"></div>
              </div>
              <p class="text-[11px] text-secondary mt-1.5">
                💡 정상 실거래가 대비 최소 <span id="detail-safety-margin-text" class="font-bold text-tertiary">700만 원 이상</span>의 시세 안전마진을 확보할 수 있는 구간입니다.
              </p>
            </div>
          </div>

          <!-- 2. 기본 제원 및 물리적 현황 카드 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-3">
            <div class="flex items-center gap-2 pb-1 border-b border-outline-variant/20">
              <span class="material-symbols-outlined text-primary text-[22px]">apartment</span>
              <h2 class="text-base font-bold text-on-surface">기본 제원 및 물리적 현황</h2>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">건물 면적</span>
                <span id="detail-spec-area" class="font-bold text-on-surface">전용 58.74㎡ (17.76평)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">층수 / 총층</span>
                <span id="detail-spec-floor" class="font-bold text-on-surface">12 / 18층 (로얄층)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">준공연도</span>
                <span id="detail-spec-year" class="font-bold text-on-surface">1998년 (28년차)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">총 세대수</span>
                <span id="detail-spec-units" class="font-bold text-on-surface">499세대 (2개동)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">난방 방식</span>
                <span class="font-bold text-on-surface">도시가스 개별난방</span>
              </div>
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">매각기일</span>
                <span id="detail-spec-date" class="font-bold text-primary">2026-11-30 10:00</span>
              </div>
            </div>
          </div>

          <!-- 3. 핵심 개발 호재 및 입지 분석 카드 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-3">
            <div class="flex items-center gap-2 pb-1 border-b border-outline-variant/20">
              <span class="material-symbols-outlined text-primary text-[22px]">near_me</span>
              <h2 class="text-base font-bold text-on-surface">핵심 개발 호재 및 입지 분석</h2>
            </div>
            <ul id="detail-location-highlights" class="space-y-2 text-xs text-on-surface">
              <!-- 동적 하이라이트 주입 -->
            </ul>
          </div>

          <!-- 4. 권리분석 · 임장 핵심 체크리스트 요약 카드 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-3">
            <div class="flex items-center gap-2 pb-1 border-b border-outline-variant/20">
              <span class="material-symbols-outlined text-tertiary text-[22px]">verified_user</span>
              <h2 class="text-base font-bold text-on-surface">권리분석 및 배당 판정표</h2>
            </div>
            <div class="space-y-2 text-xs">
              <div class="p-3 rounded-lg bg-surface-container-low flex justify-between items-center">
                <span class="text-secondary">말소기준권리:</span>
                <span id="detail-malso-text" class="font-bold text-on-surface">2021.09.17 우리은행 근저당 (전액소멸)</span>
              </div>
              <div class="p-3 rounded-lg bg-surface-container-low flex justify-between items-center">
                <span class="text-secondary">점유 및 임차인 현황:</span>
                <span id="detail-occupant-text" class="font-bold text-on-surface">소유자 단독 전입 (대항력 임차인 없음)</span>
              </div>
              <div class="p-3 rounded-lg bg-tertiary-container/10 border border-tertiary/20 flex justify-between items-center">
                <span class="text-tertiary font-bold">낙찰자 인수 권리금:</span>
                <span id="detail-takeover-text" class="font-extrabold text-tertiary text-sm">0원 (완벽한 절대 안전 물건)</span>
              </div>
              <div class="p-3 rounded-lg bg-surface-container-low flex justify-between items-center">
                <span class="text-secondary">명도 난이도:</span>
                <span id="detail-eviction-text" class="font-bold text-on-surface">난이도 '하' (협의 이사비 150만원 배정)</span>
              </div>
              <div class="p-3 rounded-lg bg-surface-container text-secondary text-[11px] leading-relaxed" id="detail-rights-notes">
                등기부상 모든 근저당 및 가압류는 매각으로 100% 말소 소멸됩니다.
              </div>
            </div>
          </div>

        </div>

        <!-- ================= RIGHT COLUMN (lg:col-span-6) ================= -->
        <div class="lg:col-span-6 flex flex-col gap-6">

          <!-- 1. 재무 · 투자 시뮬레이션 카드 (4분할 Grid) -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-4">
            <div class="flex items-center justify-between pb-1 border-b border-outline-variant/20">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-primary text-[22px]">payments</span>
                <h2 class="text-base font-bold text-on-surface">재무 · 투자 시뮬레이션</h2>
              </div>
              <span class="text-xs text-secondary font-medium">자금 조달 및 투자 계획</span>
            </div>

            <!-- 4분할 Grid 내부 -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              <!-- Plan 01: 경락잔금대출 -->
              <div class="bg-surface-container-low rounded-xl p-3.5 border border-outline-variant/15 flex flex-col justify-between gap-3">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] text-secondary font-bold uppercase tracking-wider">PLAN 01</span>
                  <span class="px-2 py-0.5 rounded text-[11px] bg-surface-container-high text-on-surface font-semibold">경락대출 (LTV 70%)</span>
                </div>
                <div>
                  <span class="text-xs text-secondary">예상 대출 가능액</span>
                  <div id="detail-loan-amount" class="text-xl font-extrabold text-on-surface mt-0.5">4,760만 원</div>
                  <span id="detail-loan-interest" class="text-[11px] text-secondary mt-1 block">월 이자: 약 17.8만 원 (연 4.5%)</span>
                </div>
              </div>

              <!-- Plan 02: 총 부대비용 -->
              <div class="bg-surface-container-low rounded-xl p-3.5 border border-outline-variant/15 flex flex-col justify-between gap-3">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] text-secondary font-bold uppercase tracking-wider">PLAN 02</span>
                  <span class="px-2 py-0.5 rounded text-[11px] bg-surface-container-high text-on-surface font-semibold">취득 부대비용</span>
                </div>
                <div>
                  <span class="text-xs text-secondary">총 부대비용 합계</span>
                  <div id="detail-total-expenses" class="text-xl font-extrabold text-on-surface mt-0.5">1,020만 원</div>
                  <span id="detail-tax-brief" class="text-[11px] text-secondary mt-1 block">취득세 74.8만 + 수리/명도비</span>
                </div>
              </div>

              <!-- Plan 03: 실투자금 -->
              <div class="bg-primary-fixed/20 rounded-xl p-3.5 border border-primary/20 flex flex-col justify-between gap-3">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] text-primary font-bold uppercase tracking-wider">PLAN 03</span>
                  <span class="px-2 py-0.5 rounded text-[11px] bg-primary text-on-primary font-bold">필요 실투자금</span>
                </div>
                <div>
                  <span class="text-xs text-secondary">순 현금 소요액</span>
                  <div id="detail-net-investment" class="text-2xl font-black text-primary mt-0.5">2,060만 원</div>
                  <span class="text-[11px] text-secondary mt-1 block">대출금 및 보증금 차감 후</span>
                </div>
              </div>

              <!-- Plan 04: 월세 수익률 -->
              <div class="bg-tertiary-container/15 rounded-xl p-3.5 border border-tertiary/20 flex flex-col justify-between gap-3">
                <div class="flex items-center justify-between">
                  <span class="text-[11px] text-tertiary font-bold uppercase tracking-wider">PLAN 04</span>
                  <span class="px-2 py-0.5 rounded text-[11px] bg-tertiary text-on-tertiary font-bold">예상 연 ROE</span>
                </div>
                <div>
                  <span class="text-xs text-secondary">연 순수익률</span>
                  <div id="detail-roe-percent" class="text-2xl font-black text-tertiary mt-0.5">14.84%</div>
                  <span id="detail-rental-flow" class="text-[11px] text-secondary mt-1 block">보증금 1,000만 / 월 45만 원</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 2. 취득 부대비용 상세 세부 명세서 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-3">
            <div class="flex items-center gap-2 pb-1 border-b border-outline-variant/20">
              <span class="material-symbols-outlined text-primary text-[22px]">receipt_long</span>
              <h2 class="text-base font-bold text-on-surface">취득 부대비용 상세 명세서</h2>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-secondary text-[11px] block">취득세 (1.1%)</span>
                <span id="detail-fee-tax" class="font-bold text-on-surface mt-0.5 block">74.8만 원</span>
              </div>
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-secondary text-[11px] block">법무사 등기보수</span>
                <span id="detail-fee-legal" class="font-bold text-on-surface mt-0.5 block">45.0만 원</span>
              </div>
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-secondary text-[11px] block">명도 이사비</span>
                <span id="detail-fee-eviction" class="font-bold text-on-surface mt-0.5 block">150.0만 원</span>
              </div>
              <div class="p-3 rounded-xl bg-surface-container-low">
                <span class="text-secondary text-[11px] block">실속 올수리비</span>
                <span id="detail-fee-repair" class="font-bold text-on-surface mt-0.5 block">600.0만 원</span>
              </div>
            </div>
          </div>

          <!-- 3. 즉석 입찰가 인터랙티브 시뮬레이터 슬라이더 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-4">
            <div class="flex items-center justify-between pb-1 border-b border-outline-variant/20">
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-primary text-[22px]">tune</span>
                <h2 class="text-base font-bold text-on-surface">즉석 입찰가 민감도 시뮬레이터</h2>
              </div>
              <span class="text-xs text-primary font-bold bg-primary/10 px-2 py-0.5 rounded">실시간 연동</span>
            </div>
            <p class="text-xs text-secondary">입찰가를 미세 조정하여 실투자금과 ROE 변화를 즉시 시뮬레이션하세요.</p>

            <div>
              <div class="flex justify-between items-baseline mb-2">
                <span class="text-xs text-secondary font-medium">테스트 입찰가 설정</span>
                <span id="sim-bid-price" class="text-lg font-black text-primary">68,000,000 원</span>
              </div>
              <input type="range" id="sim-slider" oninput="onSimulateBid()" class="w-full h-2 bg-surface-container rounded-lg appearance-none cursor-pointer accent-primary">
              <div class="flex justify-between text-[11px] text-secondary mt-1">
                <span id="sim-min-label">최저가</span>
                <span id="sim-max-label">감정가</span>
              </div>
            </div>

            <!-- 시뮬레이션 결과 3열 -->
            <div class="grid grid-cols-3 gap-2 text-center pt-2 border-t border-outline-variant/15 text-xs">
              <div class="p-2.5 rounded-lg bg-surface-container-low">
                <span class="text-secondary block text-[11px]">예상 대출금(70%)</span>
                <span id="sim-loan" class="font-bold text-on-surface mt-0.5 block">4,760만 원</span>
              </div>
              <div class="p-2.5 rounded-lg bg-primary/10 border border-primary/20">
                <span class="text-primary font-semibold block text-[11px]">필요 실투자금</span>
                <span id="sim-net-invest" class="font-black text-primary mt-0.5 block">2,060만 원</span>
              </div>
              <div class="p-2.5 rounded-lg bg-tertiary-container/15 border border-tertiary/20">
                <span class="text-tertiary font-semibold block text-[11px]">연 예상 ROE</span>
                <span id="sim-roe" class="font-black text-tertiary mt-0.5 block">14.8%</span>
              </div>
            </div>
          </div>

          <!-- 4. 애널리스트 실무 종합 전략 브리핑 -->
          <div class="bg-surface-container-lowest rounded-xl p-5 shadow-sm border border-outline-variant/20 flex flex-col gap-3">
            <div class="flex items-center gap-2 pb-1 border-b border-outline-variant/20">
              <span class="material-symbols-outlined text-primary text-[22px]">psychology</span>
              <h2 class="text-base font-bold text-on-surface">애널리스트 실무 종합 전략</h2>
            </div>
            <div class="p-4 rounded-xl bg-surface-container-low text-xs leading-relaxed text-on-surface space-y-2" id="detail-strategy-box">
              <!-- 전문가 종합 브리핑 주입 -->
            </div>
          </div>

        </div>

      </div>

    </div>
  </main>

  <!-- 데이터 및 클라이언트 스크립트 -->
  <script>
    const PROPERTIES = ''' + properties_json_str + ''';
    let currentCategory = 'all';
    let currentSearch = '';
    let selectedProperty = PROPERTIES[0];

    // 금액 한글 포맷팅 함수
    function formatKRW(val) {
      if (val === undefined || val === null) return '-';
      if (Math.abs(val) >= 100000000) {
        const uk = Math.floor(val / 100000000);
        const man = Math.round((val % 100000000) / 10000);
        return man > 0 ? `${uk}억 ${man.toLocaleString()}만 원` : `${uk}억 원`;
      }
      return `${Math.round(val / 10000).toLocaleString()}만 원`;
    }

    // 뷰 전환 (dashboard vs briefing)
    function switchView(viewName) {
      const vDash = document.getElementById('view-dashboard');
      const vBrief = document.getElementById('view-briefing');
      const navDash = document.getElementById('nav-dashboard');
      const navBrief = document.getElementById('nav-briefing');

      if (viewName === 'dashboard') {
        vDash.classList.remove('hidden');
        vBrief.classList.add('hidden');
        navDash.className = "px-3 py-2 transition-colors bg-surface-container-high text-on-surface font-headline-sm rounded-lg text-sm";
        navBrief.className = "px-3 py-2 rounded-lg text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-md text-body-md transition-colors text-sm";
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        vDash.classList.add('hidden');
        vBrief.classList.remove('hidden');
        navBrief.className = "px-3 py-2 transition-colors bg-surface-container-high text-on-surface font-headline-sm rounded-lg text-sm";
        navDash.className = "px-3 py-2 rounded-lg text-on-surface-variant hover:text-on-surface hover:bg-surface-container font-body-md text-body-md transition-colors text-sm";
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // 카테고리 필터링
    function setCategoryFilter(cat) {
      currentCategory = cat;
      const tabs = ['all', 'recommend', 'auction', 'sale', 'hold'];
      tabs.forEach(t => {
        const el = document.getElementById(`tab-${t}`);
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

    // 한글 금액 변환기
    function convertKoreanCurrency() {
      const val = parseFloat(document.getElementById('calc-input').value) || 0;
      document.getElementById('calc-output').textContent = formatKRW(val);
      document.getElementById('calc-tax').textContent = formatKRW(val * 0.011);
    }

    // 매물 카드 그리드 렌더링 (_1/code.html Stitch 카드 마크업 100% 동일)
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

      document.getElementById('list-count-badge').textContent = `${filtered.length}건 검색됨`;

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="col-span-full py-16 text-center bg-surface-container-lowest rounded-2xl border border-outline-variant/30">
            <span class="material-symbols-outlined text-[48px] text-outline mb-2">inbox</span>
            <p class="text-sm text-secondary">선택하신 조건에 해당하는 정제 매물이 없습니다.</p>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(p => {
        const isAuction = p.category === '경매';
        const isRecommended = ['적극추천', '추천'].includes(p.status);
        const statusBadgeClass = p.status === '적극추천'
          ? 'bg-error text-on-error'
          : p.status === '추천'
          ? 'bg-tertiary text-on-tertiary'
          : p.status === '보류/유찰대기'
          ? 'bg-secondary text-on-secondary'
          : 'bg-primary text-on-primary';

        return `
          <article class="group bg-surface-container-lowest rounded-2xl overflow-hidden shadow-sm hover:shadow-md border border-outline-variant/30 transition-all flex flex-col justify-between">
            <!-- Card Image & Status Overlays -->
            <div class="relative w-full h-48 bg-surface-container overflow-hidden">
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
                <button class="w-8 h-8 rounded-full bg-surface-container-lowest/90 backdrop-blur-sm text-error hover:bg-surface-container-lowest flex items-center justify-center transition-colors" title="관심 등록">
                  <span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">favorite</span>
                </button>
              </div>

              <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-on-primary">
                <span class="font-label-sm text-label-sm font-semibold tracking-wide">${p.caseNumber}</span>
                <span class="font-label-sm text-label-sm text-on-primary/90">${p.court || ''}</span>
              </div>
            </div>

            <!-- Card Core Information -->
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <!-- Title & Address -->
                <div class="mb-3">
                  <h3 class="font-headline-sm text-headline-sm text-on-surface truncate group-hover:text-primary transition-colors" title="${p.propertyName}">
                    ${p.propertyName}
                  </h3>
                  <p class="font-body-sm text-body-sm text-secondary truncate mt-0.5">
                    ${p.address}
                  </p>
                </div>

                <!-- Price Evaluation Metrics Block -->
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

                <!-- Key Financial Ratio Indicators -->
                <div class="grid grid-cols-2 gap-2 mb-4">
                  <div class="p-2.5 rounded-xl bg-tertiary-container/10 flex flex-col">
                    <span class="font-label-sm text-label-sm text-tertiary">예상 연 수익률(ROE)</span>
                    <span class="font-headline-sm text-headline-sm text-tertiary mt-0.5 font-black">${p.roePercent ? p.roePercent + '%' : '-'}</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-secondary-container/50 flex flex-col">
                    <span class="font-label-sm text-label-sm text-secondary">필요 실투자금</span>
                    <span class="font-headline-sm text-headline-sm text-on-surface mt-0.5 font-black">${formatKRW(p.netInvestment)}</span>
                  </div>
                </div>

                <!-- Catalyst / Development Tags -->
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

              <!-- Action Panel -->
              <div class="pt-4 border-t border-surface-container flex items-center justify-between gap-2">
                <div class="flex items-center gap-1">
                  <button onclick="alert('매물 수정 기능 (로컬 저장소 모드)')" class="w-9 h-9 rounded-xl hover:bg-surface-container text-secondary flex items-center justify-center transition-colors" title="매물 정보 수정">
                    <span class="material-symbols-outlined text-[18px]">edit</span>
                  </button>
                  <button onclick="alert('삭제 확인: 실무 마스터 데이터 보존을 위해 삭제가 제한되어 있습니다.')" class="w-9 h-9 rounded-xl hover:bg-error-container text-secondary hover:text-error flex items-center justify-center transition-colors" title="매물 삭제">
                    <span class="material-symbols-outlined text-[18px]">delete</span>
                  </button>
                </div>
                <button onclick="openBriefing('${p.id}')" class="flex-1 py-2.5 px-4 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md flex items-center justify-center gap-1.5 shadow-sm transition-all" type="button">
                  <span class="material-symbols-outlined text-[18px]">assignment</span>투자 분석 보기
                </button>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    // 상세 브리핑 뷰 로드 및 전환
    function openBriefing(id) {
      loadBriefingDetail(id);
      switchView('briefing');
    }

    // 상세 브리핑 데이터 바인딩 (_7/code.html과 100% 매핑)
    function loadBriefingDetail(id) {
      const p = PROPERTIES.find(item => item.id === id) || PROPERTIES[0];
      selectedProperty = p;

      // 셀렉트박스 동기화
      document.getElementById('briefing-select').value = p.id;
      document.getElementById('briefing-breadcrumb-name').textContent = p.propertyName;

      const isAuction = p.category === '경매';
      document.getElementById('detail-category-badge').textContent = isAuction ? '경매 매물' : '일반 급매';
      document.getElementById('detail-status-badge').textContent = `★ ${p.status}`;
      document.getElementById('detail-case-no').textContent = `${p.court || ''} | ${p.caseNumber}`;
      document.getElementById('detail-title').textContent = `${p.propertyName} (${p.exclusiveAreaPyung}평형)`;
      document.getElementById('detail-address').textContent = p.address;
      document.getElementById('detail-market-price').textContent = formatKRW(p.marketPrice);
      document.getElementById('detail-recommended-price').textContent = formatKRW(p.recommendedBidPrice);

      // 1. 가격 평가
      document.getElementById('detail-discount-rate').textContent = isAuction 
        ? (p.minimumBidRate < 100 ? `신건 대비 -${100 - p.minimumBidRate}% 할인` : '신건 진행 중')
        : `네고 목표 ${p.minimumBidRate}%`;
      document.getElementById('detail-appraised-price').textContent = formatKRW(p.appraisedValue);
      document.getElementById('detail-minimum-price').textContent = formatKRW(p.minimumBidPrice);
      document.getElementById('detail-recom-card-price').textContent = formatKRW(p.recommendedBidPrice);
      document.getElementById('detail-safety-margin-text').textContent = formatKRW(p.safetyMargin) + ' 이상';

      // 2. 기본 제원
      document.getElementById('detail-spec-area').textContent = `전용 ${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평)`;
      document.getElementById('detail-spec-floor').textContent = p.floorInfo;
      document.getElementById('detail-spec-year').textContent = `${p.buildYear}년 (${2026 - p.buildYear}년차)`;
      document.getElementById('detail-spec-units').textContent = `${p.totalUnits}세대`;
      document.getElementById('detail-spec-date').textContent = p.auctionDate ? `${p.auctionDate} 10:00` : '-';

      // 3. 호재 불릿
      document.getElementById('detail-location-highlights').innerHTML = p.locationHighlights.map(h => `
        <li class="flex items-start gap-2">
          <span class="text-primary font-bold shrink-0">✓</span>
          <span>${h}</span>
        </li>
      `).join('');

      // 4. 권리분석
      document.getElementById('detail-malso-text').textContent = p.rights.malsoStandard;
      document.getElementById('detail-occupant-text').textContent = p.rights.occupantStatus;
      document.getElementById('detail-takeover-text').textContent = p.rights.takeoverAmount === 0 
        ? '0원 (완벽한 인수 권리 없음)' 
        : formatKRW(p.rights.takeoverAmount);
      document.getElementById('detail-eviction-text').textContent = `난이도 '${p.rights.evictionDifficulty}' (이사비 ${formatKRW(p.expenses.evictionFee)} 배정)`;
      document.getElementById('detail-rights-notes').textContent = p.rights.riskNotes;

      // 5. 재무 시뮬레이션
      document.getElementById('detail-loan-amount').textContent = formatKRW(p.financing.loanAmount);
      document.getElementById('detail-loan-interest').textContent = `월 이자: 약 ${formatKRW(p.financing.monthlyInterest)} (연 ${p.financing.interestRate}%)`;
      document.getElementById('detail-total-expenses').textContent = formatKRW(p.expenses.totalExpenses);
      document.getElementById('detail-tax-brief').textContent = `취득세 ${formatKRW(p.expenses.acquisitionTax)} + 수리/명도`;
      document.getElementById('detail-net-investment').textContent = formatKRW(p.netInvestment);
      document.getElementById('detail-roe-percent').textContent = p.roePercent ? `${p.roePercent}%` : '-';
      document.getElementById('detail-rental-flow').textContent = `${p.rental.rentalType}: 보증금 ${formatKRW(p.rental.deposit)} ${p.rental.monthlyRent > 0 ? '/ 월 ' + formatKRW(p.rental.monthlyRent) : ''}`;

      // 6. 비용 상세
      document.getElementById('detail-fee-tax').textContent = formatKRW(p.expenses.acquisitionTax);
      document.getElementById('detail-fee-legal').textContent = formatKRW(p.expenses.legalFee);
      document.getElementById('detail-fee-eviction').textContent = formatKRW(p.expenses.evictionFee);
      document.getElementById('detail-fee-repair').textContent = formatKRW(p.expenses.repairFee);

      // 7. 슬라이더 초기화
      const slider = document.getElementById('sim-slider');
      slider.min = p.minimumBidPrice * 0.9;
      slider.max = p.appraisedValue * 1.05;
      slider.step = 1000000;
      slider.value = p.recommendedBidPrice;
      document.getElementById('sim-min-label').textContent = formatKRW(slider.min);
      document.getElementById('sim-max-label').textContent = formatKRW(slider.max);
      onSimulateBid();

      // 8. 전문가 전략 브리핑
      document.getElementById('detail-strategy-box').innerHTML = `
        <p class="font-semibold text-primary mb-1">[실무 전략 판단 & 포지셔닝]</p>
        <p>${p.strategyBrief}</p>
      `;
    }

    // 입찰가 실시간 민감도 시뮬레이션
    function onSimulateBid() {
      const bid = parseFloat(document.getElementById('sim-slider').value);
      document.getElementById('sim-bid-price').textContent = `${bid.toLocaleString()} 원 (${formatKRW(bid)})`;

      const p = selectedProperty;
      const loan = Math.round(bid * (p.financing.ltvPercent / 100));
      const taxRate = p.exclusiveAreaM2 <= 85 ? 0.011 : 0.013;
      const tax = Math.round(bid * taxRate);
      const otherExpenses = p.expenses.legalFee + p.expenses.evictionFee + p.expenses.repairFee + p.expenses.unpaidManagementFee;
      const totalCost = bid + tax + otherExpenses;
      const netInvest = Math.max(1000000, totalCost - loan - p.rental.deposit);

      const annualRent = (p.rental.monthlyRent || 0) * 12;
      const annualInterest = loan * (p.financing.interestRate / 100);
      const annualNetProfit = annualRent - annualInterest;
      const roe = netInvest > 0 ? ((annualNetProfit / netInvest) * 100).toFixed(2) : 0;

      document.getElementById('sim-loan').textContent = formatKRW(loan);
      document.getElementById('sim-net-invest').textContent = formatKRW(netInvest);
      document.getElementById('sim-roe').textContent = `${roe}%`;
    }

    // JSON 내보내기
    function exportJSON() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(PROPERTIES, null, 2));
      const anchor = document.createElement('a');
      anchor.setAttribute("href", dataStr);
      anchor.setAttribute("download", `auction_brief_master_db_${new Date().toISOString().slice(0, 10)}.json`);
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
    }

    // 초기화
    document.addEventListener('DOMContentLoaded', () => {
      // 셀렉트박스 옵션 채우기
      const select = document.getElementById('briefing-select');
      select.innerHTML = PROPERTIES.map(p => `
        <option value="${p.id}">${p.caseNumber} - ${p.propertyName}</option>
      `).join('');

      renderCards();
      loadBriefingDetail('2026-239');
      convertKoreanCurrency();
    });
  </script>
</body>
</html>
'''

out_file = r'c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상\index.html'
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Successfully generated index.html. Size:', len(html_content), 'bytes')
