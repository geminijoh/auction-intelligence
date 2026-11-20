import { PropertyItem } from '../types/property';

export const PROPERTY_DATA: PropertyItem[] = [
  {
    id: '2026-239',
    caseNumber: '2026타경239',
    category: '경매',
    status: '적극추천',
    court: '수원지방법원 평택지원 경매4계',
    auctionDate: '2026-11-30',
    propertyName: '안성동남타운 102동 1202호',
    address: '경기도 안성시 금석동 81 (도로명: 안성맞춤대로 1320-21)',
    buildingType: '아파트',
    exclusiveAreaM2: 58.74,
    exclusiveAreaPyung: 17.76,
    floorInfo: '12 / 18층 (일조·조망 우수 로얄층)',
    buildYear: 1998,
    totalUnits: 499,
    appraisedValue: 91000000,
    minimumBidPrice: 63700000,
    minimumBidRate: 70,
    recommendedBidPrice: 68000000,
    marketPrice: 75000000,
    safetyMargin: 7000000,
    expenses: {
      acquisitionTax: 748000,      // 공시가 1억 이하 주택 (취득세 1.1% 단일세율 중과배제)
      legalFee: 450000,           // 소액 아파트 표준 등기 법무사 비용
      evictionFee: 1500000,       // 소유자 단독 점유 이사비 협의 예산
      repairFee: 6000000,         // 도배, 장판, 싱크대, 욕실 실속 올수리 패키지
      unpaidManagementFee: 1000000,// 관리사무소 탐문 체납관리비 인수 예비비
      brokerageFee: 505000,       // 임대차 및 추후 매도 중개수수료
      loanInterest: 0,
      totalExpenses: 10203000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 47600000,
      interestRate: 4.5,
      monthlyInterest: 178500
    },
    rental: {
      rentalType: '월세',
      deposit: 10000000,
      monthlyRent: 450000,
      expectedSalePrice: 75000000
    },
    netInvestment: 20603000,
    expectedNetMonthlyProfit: 254800,
    annualNetCashflow: 3058000,
    roePercent: 14.84,
    roiCapitalGainPercent: 18.2,
    rights: {
      malsoStandard: '2021-09-17 우리은행 근저당 (5,390만 원)',
      occupantStatus: '소유자(심재의) 단독 전입 점유',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '하',
      riskNotes: '대항력 있는 선순위 임차인 없음. 말소기준권리 이하 모든 가압류(BNK캐피탈, 국민행복기금 등) 매각으로 100% 소멸. 낙찰자 인수 권리 0원 완벽 안전 물건.'
    },
    locationHighlights: [
      '서울-세종고속도로(세종-포천선) 구리~안성 구간 개통 수혜지 (수도권 광역 이동 30분대 진입)',
      '단지 바로 앞 버스정류장 위치 및 38번 국도(서동대로) 인접으로 평택/용인 20분대 이동',
      '국립 한경대학교 도보권(1.2km) 및 백성초/안성중/안성여고 인접으로 임대 수요 탄탄',
      '공시가격 5,340만 원으로 다주택자도 취득세 중과 배제 (단일 1.1% 혜택)'
    ],
    strategyBrief: '최근 실거래가(7,500만) 대비 최저가가 6,370만 원까지 하락한 절대적 가격 메리트 보유. 6,800만 원 권고 입찰 시 LTV 70% 대출과 보증금 1,000만 원 회수를 통해 실투자금 2,060만 원으로 연 14.8% 고배당 순현금흐름을 확정하는 월세 셋팅 최적 추천 매물입니다.'
  },
  {
    id: '2025-56772',
    caseNumber: '2025타경56772',
    category: '경매',
    status: '추천',
    court: '수원지방법원 본원 경매4계',
    auctionDate: '2026-11-25',
    propertyName: '화성 봉담 우방아이유쉘1단지 102동 1301호',
    address: '경기도 화성시 봉담읍 수영리 674',
    buildingType: '아파트',
    exclusiveAreaM2: 85.0,
    exclusiveAreaPyung: 25.71,
    floorInfo: '13 / 23층 (로얄동 로얄층)',
    buildYear: 2017,
    totalUnits: 888,
    appraisedValue: 405000000,
    minimumBidPrice: 283500000,
    minimumBidRate: 70,
    recommendedBidPrice: 330000000,
    marketPrice: 420000000,
    safetyMargin: 82560000,
    expenses: {
      acquisitionTax: 3630000,     // 6억 이하 1주택 기준 (1.1%)
      legalFee: 800000,
      evictionFee: 1500000,        // 소유자 점유 통상적 이사비
      repairFee: 0,                // 2017년식 준신축으로 도배/청소 외 대규모 수리 불필요
      unpaidManagementFee: 0,
      brokerageFee: 1680000,       // 매도시 0.4%
      loanInterest: 2310000,       // 3개월 브릿지 이자
      totalExpenses: 7440000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 231000000,
      interestRate: 4.0,
      monthlyInterest: 770000
    },
    rental: {
      rentalType: '전세',
      deposit: 280000000,
      monthlyRent: 0,
      expectedSalePrice: 420000000
    },
    netInvestment: 57440000,
    expectedNetMonthlyProfit: 0,
    annualNetCashflow: 0,
    roePercent: 21.5,
    roiCapitalGainPercent: 21.5,
    rights: {
      malsoStandard: '2016-12-01 한국주택금융공사 근저당 (1억 5,915만 원)',
      occupantStatus: '조사된 임차인 없음 (소유자 장OO 세대 전입)',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '하',
      riskNotes: '말소기준권리 이후 후순위 권리 전액 소멸. 소유자 점유 추정으로 통상적인 협의 이사비 150만원 배정으로 원활한 명도 가능.'
    },
    locationHighlights: [
      '수인분당선 오목천역 및 봉담IC 인근, 신분당선 호매실-봉담 연장 노선 호재권',
      '봉담 1·2지구와 효행지구 중심축 연결로 대규모 신흥 주거타운 형성 중',
      '수영초등학교 도보 통학 및 봉담 호수공원 녹지 인프라 우수',
      '2017년식 준신축 888세대 대단지로 환금성과 거래 회전율 우수'
    ],
    strategyBrief: '실거래 4.2억원 대비 최저가 2.835억원(70%)으로 가격 메리트 극대화. 3.3억원에 낙찰받을 경우 총 취득원가는 3억 3,744만원이며, 전세 2.8억 셋팅(갭 5,744만) 또는 4.2억 단기 매도시 순차익 약 7,256만원(수익률 21.5%)을 기대할 수 있는 우량 물건입니다. 동일 단지 105동 일반 급매(3.4억 네고)와 병행 전략 추천.'
  },
  {
    id: 'sale-bongdam-105',
    caseNumber: '급매-화성우방1단지',
    category: '일반급매',
    status: '추천',
    court: '일반 부동산 중개 (대박공인 031-299-1234)',
    auctionDate: '2026-12-30',
    propertyName: '화성 봉담 우방아이유쉘1단지 105동 1502호',
    address: '경기도 화성시 봉담읍 수영리 674',
    buildingType: '아파트',
    exclusiveAreaM2: 84.99,
    exclusiveAreaPyung: 25.71,
    floorInfo: '15 / 23층 (로얄동 고층 뻥뷰)',
    buildYear: 2017,
    totalUnits: 888,
    appraisedValue: 360000000,
    minimumBidPrice: 340000000,
    minimumBidRate: 94.4,
    recommendedBidPrice: 340000000,
    marketPrice: 420000000,
    safetyMargin: 72080000,
    expenses: {
      acquisitionTax: 3740000,
      legalFee: 800000,
      evictionFee: 0,              // 정상 매매로 명도비 0원
      repairFee: 1500000,         // 경미 보수 및 입주청소
      unpaidManagementFee: 0,
      brokerageFee: 1360000,      // 매수 중개보수 0.4%
      loanInterest: 2380000,
      totalExpenses: 7920000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 238000000,
      interestRate: 4.0,
      monthlyInterest: 793000
    },
    rental: {
      rentalType: '전세',
      deposit: 280000000,
      monthlyRent: 0,
      expectedSalePrice: 420000000
    },
    netInvestment: 67920000,
    expectedNetMonthlyProfit: 0,
    annualNetCashflow: 0,
    roePercent: 17.8,
    roiCapitalGainPercent: 17.8,
    rights: {
      malsoStandard: '정상 소유권 이전 등기 (말소 대상 근저당 잔금시 상환말소)',
      occupantStatus: '소유자 직접 거주 (잔금일 정상 인도 협의)',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '하',
      riskNotes: '명도 리스크 전혀 없음. 잔금 일정(최대 3개월) 협의 가능하며 내부 인테리어 상태 사전 확인 완료.'
    },
    locationHighlights: [
      '105동 고층(15층)으로 단지 내 가장 선호되는 막힘없는 조망권 및 일조권 확보',
      '신분당선 봉담 연장 계획 호재 및 수원역 20분 생활권',
      '단지 내 커뮤니티, 어린이집 및 수영초등학교 근접동'
    ],
    strategyBrief: '소유자의 해외 이사로 급처분 희망 물건. 경매 매물(102동 1301호)의 추천 낙찰가(3.3억)와 실질 매입단가 차이가 약 1,000만원에 불과합니다. 경매의 강제집행/명도 리스크와 잔금 압박을 회피하고 싶다면, 본 급매물을 3.4억원 이하로 네고 매수하는 것이 훨씬 안전하고 합리적인 선택입니다.'
  },
  {
    id: '2026-50882',
    caseNumber: '2026타경50882',
    category: '경매',
    status: '보류/유찰대기',
    court: '수원지방법원 평택지원 경매3계',
    auctionDate: '2026-11-23',
    propertyName: '안성 대덕 신라아파트 나동 505호',
    address: '경기도 안성시 대덕면 내리 675',
    buildingType: '아파트',
    exclusiveAreaM2: 35.28,
    exclusiveAreaPyung: 10.67,
    floorInfo: '5 / 15층',
    buildYear: 1996,
    totalUnits: 588,
    appraisedValue: 85000000,
    minimumBidPrice: 85000000,
    minimumBidRate: 100,
    recommendedBidPrice: 55000000, // 1회 유찰 시 추천가
    marketPrice: 74500000,
    safetyMargin: -10500000,       // 신건 상태에서는 역마진
    expenses: {
      acquisitionTax: 935000,
      legalFee: 600000,
      evictionFee: 2000000,       // 외국인 점유로 명도비 보수적 편성
      repairFee: 4000000,
      unpaidManagementFee: 500000,
      brokerageFee: 400000,
      loanInterest: 669000,
      totalExpenses: 8504000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 38500000,
      interestRate: 4.5,
      monthlyInterest: 144375
    },
    rental: {
      rentalType: '월세',
      deposit: 10000000,
      monthlyRent: 400000,
      expectedSalePrice: 72000000
    },
    netInvestment: 16500000,
    expectedNetMonthlyProfit: 255625,
    annualNetCashflow: 3067500,
    roePercent: 18.5,
    rights: {
      malsoStandard: '2019-06-28 가압류 (안성축협 7,150만 원)',
      occupantStatus: '외국인 2명 전입 (대항력 없는 후순위 전입자)',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '중',
      riskNotes: '외국인 점유자로 의사소통 및 송달 난이도 중상급. 감정평가액(8,500만원)이 실제 거래시세(7,450만원)보다 약 1,000만원 이상 비싸게 책정됨.'
    },
    locationHighlights: [
      '중앙대학교 다빈치캠퍼스 인근으로 대학생 및 외국인 근로자 소형 원룸/투룸 수요 풍부',
      '38번 국도변에 위치하여 안성 시내 및 평택 고덕 방면 대중교통 이용 용이',
      '소액 투자(실투자 1천만원대)로 월세 셋팅 가능한 전형적인 고수익 원룸형 아파트'
    ],
    strategyBrief: '★주의 경고: 현재 1차 신건(8,500만원)은 실거래 시세(7,450만원)보다 1,000만원 이상 비싸므로 절대 입찰 금지! 최소 1회 유찰(최저가 5,950만원) 이후 또는 2회 유찰(4,165만원) 시점에 5,000만~5,500만원 선에 낙찰받아 보증금 1,000/월 40만원 월세 세팅으로 공략해야 하는 물건입니다.'
  },
  {
    id: '2025-1691',
    caseNumber: '2025타경1691',
    category: '경매',
    status: '관심',
    court: '수원지방법원 본원 경매',
    auctionDate: '2026-12-15',
    propertyName: '수원 오목천동 남광하우스토리 105동 1102호',
    address: '경기도 수원시 권선구 오목천동 962',
    buildingType: '아파트',
    exclusiveAreaM2: 84.92,
    exclusiveAreaPyung: 25.68,
    floorInfo: '11 / 15층',
    buildYear: 2007,
    totalUnits: 420,
    appraisedValue: 380000000,
    minimumBidPrice: 266000000,
    minimumBidRate: 70,
    recommendedBidPrice: 305000000,
    marketPrice: 370000000,
    safetyMargin: 55000000,
    expenses: {
      acquisitionTax: 3355000,
      legalFee: 700000,
      evictionFee: 1500000,
      repairFee: 2000000,
      unpaidManagementFee: 0,
      brokerageFee: 1220000,
      loanInterest: 1800000,
      totalExpenses: 7075000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 213500000,
      interestRate: 4.2,
      monthlyInterest: 747250
    },
    rental: {
      rentalType: '전세',
      deposit: 250000000,
      monthlyRent: 0,
      expectedSalePrice: 370000000
    },
    netInvestment: 62075000,
    expectedNetMonthlyProfit: 0,
    annualNetCashflow: 0,
    roePercent: 19.3,
    rights: {
      malsoStandard: '근저당권 (말소기준등기)',
      occupantStatus: '소유자 점유 추정',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '하',
      riskNotes: '권리분석상 특이사항 없음. 감정평가액 대비 1회 유찰되어 가격적 진입 매력 발생.'
    },
    locationHighlights: [
      '수인분당선 오목천역 도보 10분 역세권 아파트',
      '수원 R&D 사이언스파크 개발 및 인근 고색동 인프라 공유',
      '오목초, 영신중, 영신여고 인접 학군 양호'
    ],
    strategyBrief: '화성 봉담 우방아이유쉘과 함께 서수원-봉담 벨트의 핵심 비교 대상 물건. 3억원 초반 낙찰 시 갭 6천만원 전세 셋팅 또는 실거주 갈아타기로 최적.'
  },
  {
    id: '2026-50683',
    caseNumber: '2026타경50683',
    category: '경매',
    status: '관심',
    court: '수원지방법원 평택지원 경매',
    auctionDate: '2026-12-08',
    propertyName: '안성 공도 송정그린빌 102동 901호',
    address: '경기도 안성시 공도읍 양기리 567',
    buildingType: '아파트',
    exclusiveAreaM2: 59.85,
    exclusiveAreaPyung: 18.1,
    floorInfo: '9 / 15층',
    buildYear: 2002,
    totalUnits: 720,
    appraisedValue: 125000000,
    minimumBidPrice: 87500000,
    minimumBidRate: 70,
    recommendedBidPrice: 98000000,
    marketPrice: 118000000,
    safetyMargin: 12000000,
    expenses: {
      acquisitionTax: 1078000,
      legalFee: 500000,
      evictionFee: 1500000,
      repairFee: 3000000,
      unpaidManagementFee: 0,
      brokerageFee: 472000,
      loanInterest: 700000,
      totalExpenses: 6550000
    },
    financing: {
      ltvPercent: 70,
      loanAmount: 68600000,
      interestRate: 4.5,
      monthlyInterest: 257250
    },
    rental: {
      rentalType: '월세',
      deposit: 15000000,
      monthlyRent: 500000,
      expectedSalePrice: 118000000
    },
    netInvestment: 20950000,
    expectedNetMonthlyProfit: 242750,
    annualNetCashflow: 2913000,
    roePercent: 13.9,
    rights: {
      malsoStandard: '근저당권 (말소기준등기)',
      occupantStatus: '임차인 조사 중',
      isSafe: true,
      takeoverAmount: 0,
      evictionDifficulty: '하',
      riskNotes: '안성 공도 대단지 소형 평형. 권리상 인수금액 0원 예상.'
    },
    locationHighlights: [
      '안성 공도 스타필드 안성 및 평택 용이지구 인접 생활권',
      '안성 제4일반산업단지 등 풍부한 배후 일자리 수요',
      '공시지가 1억 이하 구간 소액 갭/월세 셋팅 가능'
    ],
    strategyBrief: '안성 동남타운과 함께 안성권 소액 월세 파이프라인 구축 후보군. 1억원 언더로 낙찰받아 실투자 2,000만원에 월 순수익 24만원 이상 확정 가능.'
  }
];
