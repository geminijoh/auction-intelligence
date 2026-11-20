import React from 'react';
import { PropertyItem } from '../types/property';
import { formatKRW } from './PropertyCard';

interface PropertyDetailModalProps {
  property: PropertyItem | null;
  onClose: () => void;
}

/**
 * 상세 브리핑 팝업 모달 컴포넌트
 * - 의도: 고객 상담 시 프레젠테이션 또는 A4 보고서 출력용으로 최적화된 상세 수지분석 및 권리분석 화면 제공
 */
export const PropertyDetailModal: React.FC<PropertyDetailModalProps> = ({ property, onClose }) => {
  if (!property) return null;

  const isAuction = property.category === '경매';

  return (
    <div className="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-white rounded-2xl max-w-4xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 my-auto overflow-hidden">
        
        {/* 모달 상단 헤더 (스크롤 고정) */}
        <div className="p-5 border-b border-slate-200 flex items-center justify-between bg-slate-900 text-white">
          <div className="flex items-center space-x-3">
            <span
              className={`px-2.5 py-1 rounded-md text-xs font-bold ${
                isAuction ? 'bg-blue-600 text-white' : 'bg-emerald-600 text-white'
              }`}
            >
              {property.category}
            </span>
            <div>
              <h2 className="text-lg font-bold text-white tracking-tight">{property.propertyName}</h2>
              <p className="text-xs text-slate-400">
                {property.court || ''} | {property.caseNumber} | 매각기일: {property.auctionDate || '-'}
              </p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <button
              onClick={() => window.print()}
              className="text-xs bg-slate-800 hover:bg-slate-700 text-white px-3 py-1.5 rounded-lg border border-slate-600 transition"
            >
              인쇄 / PDF
            </button>
            <button
              onClick={onClose}
              className="w-8 h-8 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition"
            >
              ✕
            </button>
          </div>
        </div>

        {/* 모달 본문 */}
        <div className="p-6 overflow-y-auto space-y-6 text-slate-800">
          
          {/* 1. 상단 전문가 요약 브리핑 */}
          <div className="p-4 rounded-xl bg-blue-50/80 border border-blue-200 flex flex-col sm:flex-row gap-3 items-start sm:items-center justify-between">
            <div>
              <span className="text-[11px] font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded">
                애널리스트 실무 브리핑 요약
              </span>
              <p className="text-xs text-blue-950 font-semibold mt-1 leading-relaxed">
                {property.strategyBrief}
              </p>
            </div>
            <div className="shrink-0 bg-white px-3 py-2 rounded-lg border border-blue-200 text-center">
              <span className="text-[10px] text-slate-500 block">안전마진 (실거래 갭)</span>
              <span className={`text-sm font-black ${property.safetyMargin >= 0 ? 'text-blue-600' : 'text-rose-600'}`}>
                {formatKRW(property.safetyMargin)}
              </span>
            </div>
          </div>

          {/* 2. 4분할 핵심 투자 지표 카드 */}
          <div>
            <h4 className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2">
              핵심 재무·투자 시뮬레이션 지표
            </h4>
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
                <span className="text-[11px] text-slate-500 font-medium">1. 대출 레버리지 (LTV {property.financing.ltvPercent}%)</span>
                <p className="text-base font-bold text-slate-900 mt-1">{formatKRW(property.financing.loanAmount)}</p>
                <p className="text-[11px] text-slate-500 mt-0.5">
                  월 이자: 약 {formatKRW(property.financing.monthlyInterest)} (연 {property.financing.interestRate}%)
                </p>
              </div>
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
                <span className="text-[11px] text-slate-500 font-medium">2. 총 부대비용 일체</span>
                <p className="text-base font-bold text-slate-900 mt-1">{formatKRW(property.expenses.totalExpenses)}</p>
                <p className="text-[11px] text-slate-500 mt-0.5">
                  취득세 {formatKRW(property.expenses.acquisitionTax)} + 수리/명도
                </p>
              </div>
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
                <span className="text-[11px] text-slate-500 font-medium">3. 최종 순 실투자금</span>
                <p className="text-base font-bold text-rose-600 mt-1">{formatKRW(property.netInvestment)}</p>
                <p className="text-[11px] text-slate-500 mt-0.5">대출 및 보증금 차감 후 현금</p>
              </div>
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
                <span className="text-[11px] text-slate-500 font-medium">4. 수익 세팅 (ROE)</span>
                <p className="text-base font-bold text-emerald-600 mt-1">
                  {property.roePercent ? `${property.roePercent}%` : '-'}
                </p>
                <p className="text-[11px] text-slate-500 mt-0.5">
                  {property.rental.rentalType}: 보증금 {formatKRW(property.rental.deposit)}{' '}
                  {property.rental.monthlyRent > 0 ? `/ 월 ${formatKRW(property.rental.monthlyRent)}` : ''}
                </p>
              </div>
            </div>
          </div>

          {/* 3. 2열 구성: 물건 스펙 & 권리분석 */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* 기본 스펙 */}
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h5 className="text-xs font-bold text-slate-700 pb-1 border-b border-slate-200">
                물건 기본 스펙 & 가격 지표
              </h5>
              <div className="grid grid-cols-2 gap-x-2 gap-y-1.5 text-xs">
                <span className="text-slate-500">소재지:</span>
                <span className="text-slate-800 font-medium truncate" title={property.address}>{property.address}</span>

                <span className="text-slate-500">전용면적:</span>
                <span className="text-slate-800 font-medium">{property.exclusiveAreaM2}㎡ ({property.exclusiveAreaPyung}평)</span>

                <span className="text-slate-500">층수/준공:</span>
                <span className="text-slate-800 font-medium">{property.floorInfo} / {property.buildYear}년</span>

                <span className="text-slate-500">{isAuction ? '감정평가액' : '최초호가'}:</span>
                <span className="text-slate-800 font-semibold">{formatKRW(property.appraisedValue)}</span>

                <span className="text-slate-500">{isAuction ? '최저매각가' : '네고목표가'}:</span>
                <span className="text-slate-800 font-bold text-blue-700">
                  {formatKRW(property.minimumBidPrice)} ({property.minimumBidRate}%)
                </span>

                <span className="text-slate-500">최근 실거래가:</span>
                <span className="text-slate-800 font-semibold">{formatKRW(property.marketPrice)}</span>

                <span className="text-slate-500 font-bold text-rose-700">추천 {isAuction ? '입찰가' : '매수가'}:</span>
                <span className="text-rose-700 font-black">{formatKRW(property.recommendedBidPrice)}</span>
              </div>
            </div>

            {/* 권리분석 */}
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <h5 className="text-xs font-bold text-slate-700 pb-1 border-b border-slate-200">
                권리분석 및 명도 판정
              </h5>
              <div className="space-y-1.5 text-xs">
                <div>
                  <span className="text-slate-500 block text-[11px]">말소기준권리:</span>
                  <span className="text-slate-800 font-medium">{property.rights.malsoStandard}</span>
                </div>
                <div>
                  <span className="text-slate-500 block text-[11px]">점유 및 임차인:</span>
                  <span className="text-slate-800 font-medium">{property.rights.occupantStatus}</span>
                </div>
                <div className="flex items-center justify-between pt-1">
                  <span className="text-slate-500">인수 권리금:</span>
                  <span className="text-emerald-700 font-bold">
                    {property.rights.takeoverAmount === 0 ? '0원 (완벽 안전)' : formatKRW(property.rights.takeoverAmount)}
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-slate-500">명도 난이도:</span>
                  <span
                    className={`font-bold px-2 py-0.5 rounded text-[11px] ${
                      property.rights.evictionDifficulty === '하' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                    }`}
                  >
                    난이도 {property.rights.evictionDifficulty} (예비비 {formatKRW(property.expenses.evictionFee)})
                  </span>
                </div>
                <p className="text-[11px] text-slate-600 bg-white p-2 rounded border border-slate-200 mt-1">
                  {property.rights.riskNotes}
                </p>
              </div>
            </div>
          </div>

          {/* 4. 부대비용 상세 */}
          <div className="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <h5 className="text-xs font-bold text-slate-700 mb-2">취득 부대비용 상세 세부 내역표</h5>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
              <div className="bg-white p-2 rounded border border-slate-200">
                <span className="text-slate-400 block text-[10px]">취득세+지방교육세</span>
                <span className="font-semibold">{formatKRW(property.expenses.acquisitionTax)}</span>
              </div>
              <div className="bg-white p-2 rounded border border-slate-200">
                <span className="text-slate-400 block text-[10px]">법무사 등기보수</span>
                <span className="font-semibold">{formatKRW(property.expenses.legalFee)}</span>
              </div>
              <div className="bg-white p-2 rounded border border-slate-200">
                <span className="text-slate-400 block text-[10px]">명도비(이사비 협의)</span>
                <span className="font-semibold">{formatKRW(property.expenses.evictionFee)}</span>
              </div>
              <div className="bg-white p-2 rounded border border-slate-200">
                <span className="text-slate-400 block text-[10px]">수리/인테리어비</span>
                <span className="font-semibold">{formatKRW(property.expenses.repairFee)}</span>
              </div>
            </div>
          </div>

          {/* 5. 입지 및 호재 */}
          <div className="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <h5 className="text-xs font-bold text-slate-700 mb-2">입지 환경 및 미래 개발 호재</h5>
            <ul className="space-y-1.5 text-xs text-slate-700">
              {property.locationHighlights.map((highlight, idx) => (
                <li key={idx} className="flex items-start gap-1.5">
                  <span className="text-blue-600 font-bold shrink-0">✓</span>
                  <span>{highlight}</span>
                </li>
              ))}
            </ul>
          </div>

        </div>

        {/* 모달 푸터 */}
        <div className="p-4 border-t border-slate-200 bg-slate-50 flex items-center justify-between">
          <div className="text-xs text-slate-500">
            안티그래비티 부동산 자산관리 컨설팅 | 실전 투자 매물 브리핑
          </div>
          <button
            onClick={onClose}
            className="px-5 py-2 text-xs font-semibold bg-slate-800 hover:bg-slate-900 text-white rounded-lg transition"
          >
            닫기
          </button>
        </div>

      </div>
    </div>
  );
};
