---
name: Clear Estate Brief
colors:
  surface: '#f8f9ff'
  surface-dim: '#d1dbed'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dfe9fb'
  surface-container-highest: '#d9e3f5'
  on-surface: '#121c29'
  on-surface-variant: '#414755'
  inverse-surface: '#27313f'
  inverse-on-surface: '#eaf1ff'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005ac3'
  primary: '#0058be'
  on-primary: '#ffffff'
  primary-container: '#006fee'
  on-primary-container: '#fefcff'
  inverse-primary: '#aec6ff'
  secondary: '#535f72'
  on-secondary: '#ffffff'
  secondary-container: '#d4e0f7'
  on-secondary-container: '#576377'
  tertiary: '#006a3c'
  on-tertiary: '#ffffff'
  tertiary-container: '#00864e'
  on-tertiary-container: '#f6fff5'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#aec6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#d7e3fa'
  secondary-fixed-dim: '#bbc7dd'
  on-secondary-fixed: '#101c2c'
  on-secondary-fixed-variant: '#3b475a'
  tertiary-fixed: '#76fcac'
  tertiary-fixed-dim: '#57df92'
  on-tertiary-fixed: '#00210f'
  on-tertiary-fixed-variant: '#00522d'
  background: '#f8f9ff'
  on-background: '#121c29'
  surface-variant: '#d9e3f5'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 30px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 22px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-desktop: 2.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.875rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system delivers a restrained, high-conviction analytics and briefing environment for localized real estate auctions. The brand personality balances institutional precision with approachable clarity: pragmatic, lucid, confident, and meticulously organized. 

Targeted at real estate investors, property evaluators, and legal analysts navigating municipal court listings, the UI evokes stability, legal assurance, and operational momentum. By pairing pure structural minimalism with deliberate data density, interfaces prioritize rapid scanning of valuation differentials, bid timelines, and encumbrance assessments without visual noise. High trust is established through crisp geometric boundaries, unembellished typography, and high-contrast analytical indicators.

## Colors

The palette establishes an air of analytical certainty through clear chromatic separation:

- **Primary (`#0078ff`)**: Dedicated to definitive actions, selected data states, active chart indices, and primary verification touchpoints.
- **Canvas Base (`#ffffff`)**: Pure white foundation providing maximum contrast for complex analytical figures and ledger lines.
- **Secondary / Primary Text (`#354153`)**: A deep, desaturated slate navy engineered for sustained reading comfort across auction item descriptions, appraisal breakdowns, and numerical values.
- **Muted Text (`#697383`)**: A disciplined secondary grey for metadata, labels, table headers, and subsidiary timestamps.
- **Borders & Dividers (`#e5e8ef`)**: Structural hairline boundaries designed to contain dense modular metrics without segmenting visual flow.
- **Surfaces & Input Fill (`#f2f3f8`)**: Neutral blue-grey fills providing subtle separation for inputs, inactive tags, and secondary metric badges.
- **Tertiary / Success (`#25b870`)**: Reserved for positive bid margins, clear title indicators, and profitable valuation deltas.

## Typography

Typography prioritizes systematic Korean and Latin clarity using tight grotesque letterforms (implemented via Pretendard/Inter). Heading scales are strictly capped for dense data dashboards:

- **H1 (`26px/700`)**: Case summaries, auction property identifiers, and aggregate valuation headers.
- **H2 (`22px/700`)**: Section groupings, modal title bars, and financial ledger headlines.
- **H3 (`16px/600`)**: Card headers, metric block labels, and breakdown categories.
- **Data Numerics**: Numbers representing currency (KRW), land area (㎡/pyeong), and probability scores must utilize tabular lining figures (`font-variant-numeric: tabular-nums`) with `-0.01em` tracking to guarantee vertical alignment in lists and briefing summaries.
- **Labeling**: Labels below 13px employ medium-to-semibold weights to ensure legibility against subtle surface fills.

## Layout & Spacing

The layout operates on a fluid grid designed for rapid transition between field assessments on mobile devices and multi-pane analytical reviews on desktop screens:

- **Mobile (< 768px)**: Single column stream with `1rem` outer margin and `0.75rem` vertical separation between briefing modules. Sticky critical metrics bar (Current Minimum Bid & Auction Date) anchored to viewport base.
- **Desktop (>= 768px)**: 12-column layout with a fixed max-width container of `1280px`. Left analytical column (7 cols) displays auction dossier, photos, and tenant rights; right sticky rail (5 cols) handles financial projections, bidding calculators, and precedent metrics.
- **Padding Hierarchy**: Form items and metric cells rely uniformly on `space-md` (14px) and `space-lg` (20px) to balance information density without clutter.

## Elevation & Depth

This system intentionally avoids deep, blurred drop shadows in favor of flat structural clarity and crisp architectural layering:

- **Surface Tiers**: Hierarchy is established horizontally through surface coloring rather than simulated physical distance. Default canvases use pure white (`#ffffff`), while data groupings and input frames sit directly upon it via the cool `#f2f3f8` fill.
- **Borders over Shadows**: Card enclosures, table wrappers, and interactive panels employ single-pixel solid borders (`1px solid #e5e8ef`). 
- **Active Elevation**: Floating action sheets, property address autocomplete dropdowns, and context tooltips employ a single utilitarian shadow: `0 4px 16px rgba(53, 65, 83, 0.08)`.
- **Modals & Overlays**: Light backdrop veil (`rgba(53, 65, 83, 0.4)`) paired with unblurred containment borders ensures attention remains focused on legal disclosures and bid forms.

## Shapes

The design system employs a refined, moderate radius scale calibrated to soften data-heavy tabular layouts while maintaining architectural rigor:

- **Standard Components (12px)**: Inputs, buttons, secondary badges, and mini analytical cards.
- **Intermediate Panels (14px)**: Nested container blocks, map overlays, image preview viewports, and tab groups.
- **Structural Containers (16px)**: Primary briefing cards, floating side rails, bottom sheets, and modal frames.
- **Status Pills (Full Radius)**: Reserved strictly for legal status tags (e.g., "Auction Postponed", "Appraisal Confirmed", "Successful Bid").

## Components

### Buttons
- **Primary**: Solid `#0078ff` background, white text, 12px radius, `h-11` (44px) on mobile for reliable touch targeting. Active press state shifts to `#0063d1`.
- **Secondary**: Clean `#f2f3f8` surface fill with `#354153` text, no border.
- **Outline**: 1px `#e5e8ef` border, pure white background, `#354153` text. Hover state introduces `#f2f3f8`.

### Input Fields & Controls
- **Inputs**: Background fill `#f2f3f8`, 12px radius, zero border in resting state. Transition to pure white background with `1.5px solid #0078ff` on focus. Placeholder text in `#697383`.
- **Checkboxes & Radios**: 18px squircle/circle, resting state `#e5e8ef` outline. Selected state fills with `#0078ff` displaying a crisp white indicator.

### Cards & Dossier Modules
- Background `#ffffff`, border `1px solid #e5e8ef`, 16px radius.
- Padding set to 20px (`space-lg`). Header bars within cards use a bottom divider of `1px solid #e5e8ef` with a 14px padding rhythm.

### Badges & Status Chips
- Height 26px, padding horizontal 8px, font size 12px weight 600.
- Neutral variant: `#f2f3f8` background with `#697383` text.
- Highlight variant: Tinted blue background (`rgba(0, 120, 255, 0.08)`) with `#0078ff` text.

### Auction Data Tables
- Header row: `#f2f3f8` background, `#697383` uppercase/medium weight 12px text, 36px height.
- Rows: White background, 48px standard row height, bottom border `1px solid #e5e8ef`. Numerical data right-aligned using tabular figures.