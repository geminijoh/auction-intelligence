# -*- coding: utf-8 -*-
import os

base_dir = r'c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상'
script_path = os.path.join(base_dir, 'assemble_master_app.py')

with open(script_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update card template buttons
old_btn = '''              <div class="pt-4 border-t border-surface-container flex items-center justify-between gap-2">
                <button onclick="switchMainTab('auction-simulator')" class="flex-1 py-2.5 px-4 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md flex items-center justify-center gap-1.5 shadow-sm transition-all" type="button">
                  <span class="material-symbols-outlined text-[18px]">assignment</span>투자 분석 시뮬레이터
                </button>
              </div>'''

new_btn = '''              <div class="pt-4 border-t border-surface-container flex items-center justify-between gap-2">
                <button onclick="openPropertyModal('${p.id}')" class="flex-1 py-2 px-3 rounded-xl bg-surface-container hover:bg-surface-container-high text-on-surface font-label-md text-label-md flex items-center justify-center gap-1 transition-all" type="button">
                  <span class="material-symbols-outlined text-[16px]">visibility</span>권리·수지 상세
                </button>
                <button onclick="switchMainTab('auction-simulator')" class="flex-1 py-2 px-3 rounded-xl bg-primary hover:bg-primary-container text-on-primary font-label-md text-label-md flex items-center justify-center gap-1 shadow-sm transition-all" type="button">
                  <span class="material-symbols-outlined text-[16px]">tune</span>시뮬레이터
                </button>
              </div>'''

if old_btn in code:
    code = code.replace(old_btn, new_btn)
    print("Replaced card buttons.")
else:
    print("Card buttons already updated or not found.")

# 2. Add Modal Markup before Footer
modal_markup = '''  <!-- ================= 5. Property Detail Briefing Modal ================= -->
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
          <button onclick="switchMainTab('auction-simulator'); closePropertyModal();" class="px-4 py-2 font-label-md text-label-md font-semibold bg-primary hover:bg-primary-container text-on-primary rounded-xl transition">
            시뮬레이터로 이동
          </button>
          <button onclick="closePropertyModal()" class="px-4 py-2 font-label-md text-label-md font-semibold bg-surface-container hover:bg-surface-container-high text-on-surface rounded-xl transition">
            닫기
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= Footer ================= -->'''

if '<!-- ================= 5. Property Detail Briefing Modal ================= -->' not in code:
    code = code.replace('  <!-- ================= Footer ================= -->', modal_markup)
    print("Added Modal Markup.")

# 3. Add Modal Open/Close JS functions
modal_js = '''    // 모달 열기
    function openPropertyModal(id) {
      const p = PROPERTIES.find(item => item.id === id);
      if (!p) return;

      const isAuction = p.category === '경매';
      document.getElementById('modal-category').textContent = p.category;
      document.getElementById('modal-category').className = isAuction 
        ? "px-2.5 py-1 rounded-md font-label-sm text-label-sm font-bold bg-primary text-on-primary"
        : "px-2.5 py-1 rounded-md font-label-sm text-label-sm font-bold bg-tertiary text-on-tertiary";
      
      document.getElementById('modal-title').textContent = p.propertyName;
      document.getElementById('modal-subtitle').textContent = `${p.court || ''} | ${p.caseNumber} | ${isAuction ? '매각기일: ' + (p.auctionDate || '-') : '중개물건'}`;
      document.getElementById('modal-brief').textContent = p.strategyBrief;
      
      const marginEl = document.getElementById('modal-margin');
      marginEl.textContent = (p.safetyMargin >= 0 ? '+' : '') + formatKRW(p.safetyMargin);
      marginEl.className = p.safetyMargin >= 0 
        ? "font-headline-sm text-headline-sm font-black text-primary" 
        : "font-headline-sm text-headline-sm font-black text-error";

      document.getElementById('modal-ltv-label').textContent = `1. 대출 레버리지 (LTV ${p.financing.ltvPercent}%)`;
      document.getElementById('modal-loan').textContent = formatKRW(p.financing.loanAmount);
      document.getElementById('modal-interest').textContent = `월 이자: 약 ${formatKRW(p.financing.monthlyInterest)} (연 ${p.financing.interestRate}%)`;

      document.getElementById('modal-expenses').textContent = formatKRW(p.expenses.totalExpenses);
      document.getElementById('modal-expenses-detail').textContent = `취득세 ${formatKRW(p.expenses.acquisitionTax)} + 수리/명도`;

      document.getElementById('modal-net-invest').textContent = formatKRW(p.netInvestment);
      document.getElementById('modal-roe').textContent = p.roePercent ? `${p.roePercent}%` : '-';
      document.getElementById('modal-rental').textContent = `${p.rental.rentalType}: 보증금 ${formatKRW(p.rental.deposit)} ${p.rental.monthlyRent > 0 ? '/ 월 ' + formatKRW(p.rental.monthlyRent) : ''}`;

      document.getElementById('modal-address').textContent = p.address;
      document.getElementById('modal-area').textContent = `${p.exclusiveAreaM2}㎡ (${p.exclusiveAreaPyung}평)`;
      document.getElementById('modal-floor-build').textContent = `${p.floorInfo} / ${p.buildYear}년`;
      
      document.getElementById('modal-appraised-label').textContent = isAuction ? '감정평가액:' : '최초호가:';
      document.getElementById('modal-appraised').textContent = formatKRW(p.appraisedValue);

      document.getElementById('modal-min-label').textContent = isAuction ? '최저매각가:' : '네고목표가:';
      document.getElementById('modal-min').textContent = `${formatKRW(p.minimumBidPrice)} (${p.minimumBidRate}%)`;
      document.getElementById('modal-market').textContent = formatKRW(p.marketPrice);

      document.getElementById('modal-bid-label').textContent = `추천 ${isAuction ? '입찰가' : '매수가'}:`;
      document.getElementById('modal-bid').textContent = formatKRW(p.recommendedBidPrice);

      document.getElementById('modal-malso').textContent = p.rights.malsoStandard;
      document.getElementById('modal-occupant').textContent = p.rights.occupantStatus;
      document.getElementById('modal-takeover').textContent = p.rights.takeoverAmount === 0 ? '0원 (완벽 안전)' : formatKRW(p.rights.takeoverAmount);
      
      const evictEl = document.getElementById('modal-eviction');
      evictEl.textContent = `난이도 ${p.rights.evictionDifficulty} (예비비 ${formatKRW(p.expenses.evictionFee)})`;
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
'''

# Note: in assemble_master_app.py, the script is inside an f-string, so curly braces in JS need to be doubled!
modal_js_escaped = modal_js.replace('{', '{{').replace('}', '}}')

if 'function openPropertyModal' not in code:
    code = code.replace('    // JSON 내보내기', modal_js_escaped + '\n    // JSON 내보내기')
    print("Added Modal JS functions.")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated assemble_master_app.py successfully.")
