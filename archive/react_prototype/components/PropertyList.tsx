import React, { useState, useMemo } from 'react';
import { PropertyItem } from '../types/property';
import { PropertyCard } from './PropertyCard';
import { PropertyDetailModal } from './PropertyDetailModal';

interface PropertyListProps {
  initialProperties: PropertyItem[];
}

type FilterType = 'all' | 'recommend' | 'auction' | 'sale' | 'hold';

/**
 * 부동산 매물 탐색 및 필터링 메인 컨테이너 컴포넌트
 * - 의도: React 상태(useState, useMemo)를 활용해 실시간 검색 및 다채로운 조건 필터링을 지원
 */
export const PropertyList: React.FC<PropertyListProps> = ({ initialProperties }) => {
  const [properties] = useState<PropertyItem[]>(initialProperties);
  const [activeFilter, setActiveFilter] = useState<FilterType>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedProperty, setSelectedProperty] = useState<PropertyItem | null>(null);

  // 필터 및 검색 적용된 매물 목록 연산
  const filteredProperties = useMemo(() => {
    return properties.filter((item) => {
      // 1. 탭 필터링
      if (activeFilter === 'recommend' && !['적극추천', '추천'].includes(item.status)) return false;
      if (activeFilter === 'auction' && item.category !== '경매') return false;
      if (activeFilter === 'sale' && item.category !== '일반급매') return false;
      if (activeFilter === 'hold' && item.status !== '보류/유찰대기') return false;

      // 2. 키워드 검색 (사건번호, 단지명, 주소)
      if (searchQuery.trim()) {
        const query = searchQuery.trim().toLowerCase();
        const matchCase = item.caseNumber.toLowerCase().includes(query);
        const matchName = item.propertyName.toLowerCase().includes(query);
        const matchAddr = item.address.toLowerCase().includes(query);
        if (!matchCase && !matchName && !matchAddr) return false;
      }

      return true;
    });
  }, [properties, activeFilter, searchQuery]);

  return (
    <div className="space-y-6">
      {/* 1. 검색 및 필터 바 */}
      <section className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col md:flex-row gap-3 items-center justify-between">
        <div className="flex flex-wrap items-center gap-1.5 w-full md:w-auto">
          <button
            onClick={() => setActiveFilter('all')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
              activeFilter === 'all' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            전체 ({properties.length})
          </button>
          <button
            onClick={() => setActiveFilter('recommend')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1 ${
              activeFilter === 'recommend' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
            추천 매물
          </button>
          <button
            onClick={() => setActiveFilter('auction')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
              activeFilter === 'auction' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            ⚖️ 경매 매물
          </button>
          <button
            onClick={() => setActiveFilter('sale')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
              activeFilter === 'sale' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            🏢 일반 급매
          </button>
          <button
            onClick={() => setActiveFilter('hold')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition ${
              activeFilter === 'hold' ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
            }`}
          >
            ⚠️ 보류/유찰대기
          </button>
        </div>

        {/* 검색 인풋 */}
        <div className="w-full md:w-72">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="사건번호, 단지명, 지역명 검색..."
            className="w-full px-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-slate-800"
          />
        </div>
      </section>

      {/* 2. 카드 그리드 */}
      <section>
        {filteredProperties.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {filteredProperties.map((property) => (
              <PropertyCard
                key={property.id}
                property={property}
                onSelect={(prop) => setSelectedProperty(prop)}
              />
            ))}
          </div>
        ) : (
          <div className="py-16 text-center bg-white rounded-xl border border-slate-200">
            <p className="text-sm text-slate-500">검색 조건에 일치하는 정제 매물이 없습니다.</p>
          </div>
        )}
      </section>

      {/* 3. 상세 모달 */}
      <PropertyDetailModal
        property={selectedProperty}
        onClose={() => setSelectedProperty(null)}
      />
    </div>
  );
};
