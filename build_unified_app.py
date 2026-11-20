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

print("Properties processed successfully.")
