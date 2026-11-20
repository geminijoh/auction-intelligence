import json
import os

base_dir = r"c:\Users\finey\OneDrive\Desktop\Anti Gravity\부동산\경매\경매프로젝트\최초 구상"
reports_json_path = os.path.join(base_dir, "data", "regional_reports_data.json")

with open(reports_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

first_md = data[0]["contentMarkdown"]
out_dir = os.path.join(base_dir, "시장동향리포트뷰어")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "오목천_봉담_통합_지역종합분석보고서.html")

md_json_str = json.dumps(first_md, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>화성(봉담) · 서수원(오목천) 광역생활권 부동산 시장 및 도시개발 심층 분석</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
</head>
<body class="bg-slate-50 text-slate-900 font-sans p-4 sm:p-8">
  <div class="max-w-5xl mx-auto bg-white p-6 sm:p-10 rounded-2xl shadow-sm border border-slate-200">
    <div class="flex justify-between items-center pb-4 mb-6 border-b border-slate-200">
      <div class="flex items-center gap-2 text-blue-600 font-bold text-lg">
        <span class="material-symbols-outlined">analytics</span>
        <span>PropIntelligence 심층 리서치 랩 (화성봉담·서수원)</span>
      </div>
      <button onclick="window.print()" class="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-semibold hover:bg-blue-700">
        A4 인쇄 / PDF 저장
      </button>
    </div>
    
    <!-- 도시개발 마스터플랜 및 현장 배치도 섹션 -->
    <div class="mb-8 p-4 bg-slate-50 rounded-xl border border-slate-200">
      <h3 class="font-bold text-base text-slate-800 mb-3 flex items-center gap-1.5">
        <span class="material-symbols-outlined text-blue-600">map</span>
        오목천 · 봉담 권역 도시개발 마스터플랜 및 현장 배치도
      </h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="border rounded-xl p-3 bg-white shadow-xs">
          <p class="font-bold text-xs mb-2 text-slate-700">오목천 개발 계획도 1 (지구단위계획 및 수인분당선 역세권)</p>
          <img src="../오목천/오목천 개발_1.png" alt="오목천 개발 계획도 1" class="w-full h-auto rounded-lg object-contain" onerror="this.src='오목천/오목천 개발_1.png'">
        </div>
        <div class="border rounded-xl p-3 bg-white shadow-xs">
          <p class="font-bold text-xs mb-2 text-slate-700">오목천 개발 계획도 2 (효행지구 및 서수원-봉담 광역도로망)</p>
          <img src="../오목천/오목천 개발_2.png" alt="오목천 개발 계획도 2" class="w-full h-auto rounded-lg object-contain" onerror="this.src='오목천/오목천 개발_2.png'">
        </div>
      </div>
    </div>

    <!-- 마크다운 본문 -->
    <div id="content" class="prose max-w-none text-slate-800 leading-relaxed"></div>
  </div>

  <script>
    const md = {md_json_str};
    document.getElementById('content').innerHTML = marked.parse(md);
  </script>
</body>
</html>
"""

with open(out_file, "w", encoding="utf-8") as f:
    f.write(html)

print("[OK] Standalone report file generated at:", out_file)
