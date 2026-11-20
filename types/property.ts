/**
 * 부동산 매물 (경매 / 일반급매) 마스터 인터페이스 정의
 * - 의도: 경매 물건의 권리분석 및 낙찰 수지 분석과 일반 급매물의 네고 수지 분석을 단일 구조로 통합 관리
 */

export type PropertyType = '경매' | '일반급매';
export type RecommendationStatus = '추천' | '적극추천' | '보류/유찰대기' | '관심';

/** 부대비용 상세 내역 */
export interface AcquisitionExpenses {
  acquisitionTax: number;      // 취득세 + 지방교육세
  legalFee: number;            // 법무사 등기보수
  evictionFee: number;         // 명도비 (이사비/집행 예비비)
  repairFee: number;           // 수리/인테리어비
  unpaidManagementFee: number; // 체납 관리비 (공용부 인수 추정액)
  brokerageFee: number;        // 중개보수 (매수 또는 매도 시)
  loanInterest: number;        // 단기 대출이자 및 금융비용
  totalExpenses: number;       // 총 부대비용 합계
}

/** 대출 및 금융 레버리지 조건 */
export interface FinancingConditions {
  ltvPercent: number;          // 대출 비율 (예: 70%)
  loanAmount: number;          // 예상 대출 금액
  interestRate: number;        // 연간 대출 금리 (%)
  monthlyInterest: number;     // 월 예상 대출 이자
}

/** 임대 세팅 및 수익 조건 */
export interface RentalConditions {
  rentalType: '월세' | '전세' | '단기매도';
  deposit: number;             // 임대 보증금
  monthlyRent: number;         // 월 임대료
  expectedSalePrice: number;   // 정상 시세 / 예상 매도가
}

/** 권리분석 및 리스크 현황 */
export interface RightsAnalysis {
  malsoStandard: string;       // 말소기준권리 (날짜 및 권리자)
  occupantStatus: string;      // 점유자 현황 (소유자, 임차인, 외국인 등)
  isSafe: boolean;             // 대항력 등 인수 권리 안전 여부
  takeoverAmount: number;      // 낙찰자 인수 금액 (안전 물건은 0원)
  evictionDifficulty: '상' | '중' | '하'; // 명도 난이도
  riskNotes: string;           // 특이사항 및 리스크 요약
}

/** 통합 부동산 매물 인터페이스 */
export interface PropertyItem {
  id: string;                  // 고유 식별자 (예: '2026-239' or 'sale-bongdam-105')
  caseNumber: string;          // 사건번호 또는 관리번호 (예: '2026타경239', '급매-화성우방1단지')
  category: PropertyType;      // '경매' | '일반급매'
  status: RecommendationStatus;// '추천' | '적극추천' | '보류/유찰대기' | '관심'
  court?: string;              // 관할 법원 (예: '수원지방법원 평택지원 경매4계')
  auctionDate?: string;        // 매각기일 또는 거래 목표일 (YYYY-MM-DD)
  
  // 기본 물건 정보
  propertyName: string;        // 단지명/물건명 (예: '안성동남타운 102동 1202호')
  address: string;             // 도로명/지번 주소
  buildingType: string;        // 아파트, 다세대, 오피스텔 등
  exclusiveAreaM2: number;     // 전용면적 (㎡)
  exclusiveAreaPyung: number;  // 전용면적 (평)
  floorInfo: string;           // 층수 정보 (예: '12 / 18층 (로얄층)')
  buildYear: number;           // 준공년도
  totalUnits: number;          // 총 세대수
  
  // 가격 지표 (단위: 원)
  appraisedValue: number;      // 감정평가액 (급매는 최초호가)
  minimumBidPrice: number;     // 최저매각가격 (급매는 네고목표가)
  minimumBidRate: number;      // 감정가 대비 비율 (%)
  recommendedBidPrice: number; // 권고/추천 입찰가 (급매는 추천 매수가)
  marketPrice: number;         // 최근 실거래 시세
  safetyMargin: number;        // 안전마진 (실거래가 - 추천입찰가 - 부대비용)
  
  // 투자 분석 지표
  expenses: AcquisitionExpenses;
  financing: FinancingConditions;
  rental: RentalConditions;
  netInvestment: number;       // 최종 실투자금 (총취득원가 - 대출금 - 보증금)
  expectedNetMonthlyProfit: number; // 월 순현금유입 (월세 - 월이자)
  annualNetCashflow: number;   // 연간 순현금유입
  roePercent: number;          // 자기자본수익률 (ROE %)
  roiCapitalGainPercent?: number; // 매도시 예상 자본수익률 (%)
  
  // 권리 및 입지 정보
  rights: RightsAnalysis;
  locationHighlights: string[];// 입지 및 교통/개발 호재 목록
  strategyBrief: string;       // 전문가 실무 종합 전략 및 의사결정 브리핑
}
