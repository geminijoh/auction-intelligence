import React from 'react';
import { PropertyItem } from '../types/property';

interface PropertyCardProps {
  property: PropertyItem;
  onSelect: (property: PropertyItem) => void;
}

/**
 * 금액을 한국어 원/만원/억원 단위로 포맷팅하는 헬퍼 함수
 */
export const formatKRW = (val?: number): string => {
  if (val === undefined || val === null) return '-';
  if (Math.abs(val) >= 100000000) {
    const uk = Math.floor(val / 100000000);
    const man = Math.round((val % 100000000) / 10000);
    return man > 0 ? `${uk}억 ${man.toLocaleString()}만 원` : `${uk}억 원`;
  }
  return `${Math.round(val / 10000).toLocaleString()}만 원`;
};

/**
 * 개별 매물 카드 컴포넌트
 * - 의도: 감정가 대비 저감률, 추천 입찰가, 실투자금 및 ROE를 한눈에 파악할 수 있도록 간결하게 정보 배치
 */
export const PropertyCard: React.FC<PropertyCardProps> = ({ property, onSelect }) => {
  const isAuction = property.category === '경매';

  // 상태 뱃지 스타일 분기
  const getStatusBadgeClass = (status: string) => {
    switch (status) {
      case '적극추천':
        return 'bg-rose-100 text-rose-700 border-rose-200';
      case '추천':
        return 'bg-emerald-100 text-emerald-700 border-emerald-200';
      case '보류/유찰대기':
        return 'bg-amber-100 text-amber-800 border-amber-200';
      default:
        return 'bg-slate-100 text-slate-700 border-slate-200';
    }
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-all duration-200 flex flex-col justify-between overflow-hidden">
      {/* 1. 상단 메타데이터 */}
      <div className="p-5 pb-3 border-b border-slate-100">
        <div className="flex items-center justify-between gap-2 mb-2">
          <span
            className={`text-[11px] font-bold px-2 py-0.5 rounded border ${
              isAuction ? 'bg-blue-50 text-blue-700 border-blue-200' : 'bg-emerald-50 text-emerald-700 border-emerald-200'
            }`}
          >
            {property.category}
          </span>
          <span className={`text-[11px] font-bold px-2 py-0.5 rounded border ${getStatusBadgeClass(property.status)}`}>
            {property.status}
          </span>
          {property.auctionDate && (
            <span className="text-[11px] text-slate-400 font-mono ml-auto">
              기일: {property.auctionDate}
            </span>
          )}
        </div>

        <h3 className="text-base font-bold text-slate-900 truncate" title={property.propertyName}>
          {property.propertyName}
        </h3>
        <p className="text-xs text-slate-500 font-mono mt-0.5">{property.caseNumber}</p>
        <p className="text-xs text-slate-500 truncate mt-1">
          {property.floorInfo} · 전용 {property.exclusiveAreaPyung}평 ({property.exclusiveAreaM2}㎡)
        </p>
      </div>

      {/* 2. 핵심 가격 수치 */}
      <div className="p-5 py-3 space-y-2.5 bg-slate-50/60">
        <div className="flex justify-between items-baseline text-xs">
          <span className="text-slate-500">{isAuction ? '감정평가액' : '최초호가'}</span>
          <span className="font-semibold text-slate-700">{formatKRW(property.appraisedValue)}</span>
        </div>
        <div className="flex justify-between items-baseline text-xs">
          <span className="text-slate-500">{isAuction ? '최저매각가' : '네고목표가'}</span>
          <span className="font-bold text-blue-700">
            {formatKRW(property.minimumBidPrice)}{' '}
            <span className="text-[10px] text-slate-400 font-normal">({property.minimumBidRate}%)</span>
          </span>
        </div>
        <div className="flex justify-between items-baseline text-xs pt-1 border-t border-slate-200">
          <span className="font-semibold text-slate-800">{isAuction ? '★ 추천입찰가' : '★ 추천매수가'}</span>
          <span className="font-black text-rose-600 text-sm">{formatKRW(property.recommendedBidPrice)}</span>
        </div>
      </div>

      {/* 3. 수익률 및 실투자금 하이라이트 */}
      <div className="p-5 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
        <div>
          <span className="text-slate-400 block text-[11px]">필요 실투자금</span>
          <span className="font-bold text-slate-800 text-sm">{formatKRW(property.netInvestment)}</span>
        </div>
        <div className="text-right">
          <span className="text-slate-400 block text-[11px]">예상 수익률(ROE)</span>
          <span className="font-bold text-emerald-600 text-sm">
            {property.roePercent ? `${property.roePercent}%` : '-'}
          </span>
        </div>
      </div>

      {/* 4. 브리핑 보기 버튼 */}
      <div className="p-4 pt-0">
        <button
          onClick={() => onSelect(property)}
          className="w-full py-2 px-3 bg-slate-900 hover:bg-blue-600 text-white rounded-lg text-xs font-semibold flex items-center justify-center gap-1.5 transition-colors shadow-sm"
        >
          <span>상세 브리핑 및 수지분석 보기</span>
        </button>
      </div>
    </div>
  );
};
