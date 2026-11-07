# -*- coding: utf-8 -*-
"""Build the static study site (index.html) for 電子學作業 II."""
import figures as F

CSS = """
:root{
  --ink:#1e242a; --ink2:#3b444c; --mut:#7c868f; --line:#e2ddd3;
  --paper:#fffefb; --bg:#efece6; --acc:#2b6b7f; --acc-soft:#eef4f5;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:"Inter","Segoe UI","Microsoft JhengHei","PingFang TC",system-ui,sans-serif;
  font-size:15.5px; line-height:1.85; letter-spacing:.01em;
}
.page{max-width:880px;margin:0 auto;background:var(--paper);
  border-left:1px solid var(--line);border-right:1px solid var(--line);
  padding:64px 72px 88px}
@media(max-width:780px){
  .page{padding:36px 22px 64px;border:0}
  h1{font-size:25px;margin-top:12px}
  .sub{font-size:12.5px;line-height:1.7}
  .chap-head{flex-wrap:wrap;gap:6px 12px}
  .chap-head .no{white-space:nowrap}
  .chap-head h2{font-size:16px}
  .chap-head .en{display:none}
  .chapter{margin-top:46px}
  .prob{margin-top:34px}
  .prob-head{flex-wrap:wrap;gap:6px 10px}
  .prob-head .tag{margin-left:0}
  .eq{font-size:15px}
  .src{font-size:14px}
  .steps>li{padding-left:30px}
  .ans p{font-size:15px}
  table{font-size:12.5px}
  th,td{padding:7px 6px}
}

/* ---------- masthead ---------- */
.kicker{font-family:ui-monospace,"SFMono-Regular",Consolas,monospace;
  font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--acc)}
h1{font-size:31px;line-height:1.35;margin:14px 0 6px;font-weight:600;letter-spacing:.01em}
.sub{margin:0;color:var(--mut);font-size:13.5px}
.chips{margin:20px 0 0;display:flex;gap:8px;flex-wrap:wrap}
.chip{font-family:ui-monospace,monospace;font-size:11.5px;color:var(--ink2);
  border:1px solid var(--line);border-radius:999px;padding:3px 11px;background:#fff}
.rule{height:1px;background:var(--line);margin:28px 0 0}
.conv{margin:18px 0 0;font-size:12.5px;color:var(--mut)}

/* ---------- chapters ---------- */
.chapter{margin-top:64px}
.chap-head{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--ink);padding-bottom:10px}
.chap-head .no{font-family:ui-monospace,monospace;font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--acc)}
.chap-head h2{font-size:17px;margin:0;font-weight:600;letter-spacing:.02em}
.chap-head .en{margin-left:auto;font-size:12px;color:var(--mut);letter-spacing:.04em}

/* ---------- problems ---------- */
.prob{margin:44px 0 0;break-inside:avoid;page-break-inside:avoid}
.prob-head{display:flex;gap:10px;align-items:baseline}
.pnum{font-family:ui-monospace,monospace;font-size:12px;font-weight:600;color:#fff;
  background:var(--ink);border-radius:3px;padding:2px 7px;letter-spacing:.06em}
.prob-head h3{font-size:16.5px;margin:0;font-weight:600}
.prob-head .tag{margin-left:auto;font-size:11.5px;color:var(--mut);font-family:ui-monospace,monospace}
.src{margin:12px 0 0;font-family:Georgia,"Times New Roman",serif;font-size:15px;
  color:var(--ink2);line-height:1.75}
.src .zh{display:block;font-family:inherit;font-size:13.5px;color:var(--mut);margin-top:6px}
figure{margin:22px 0 0;padding:0;text-align:center}
figure svg{max-width:100%;height:auto}
figcaption{margin-top:10px;font-size:11.5px;color:var(--mut);line-height:1.6}

/* ---------- steps ---------- */
.steps{list-style:none;counter-reset:s;margin:22px 0 0;padding:0}
.steps>li{counter-increment:s;position:relative;padding-left:34px;margin:0 0 16px}
.steps>li::before{content:counter(s);position:absolute;left:0;top:3px;
  font-family:ui-monospace,monospace;font-size:11px;color:var(--acc);
  border:1px solid #cfdde0;border-radius:50%;width:20px;height:20px;
  display:flex;align-items:center;justify-content:center;background:#fff}
.lab{font-size:13px;color:var(--mut);margin:0 0 4px}
.eq{font-family:Georgia,"Times New Roman",serif;font-size:16px;margin:0;color:var(--ink);
  line-height:1.95;letter-spacing:.01em}
.eq+.eq{margin-top:2px}
.eq em{font-style:italic}
.eq b{font-weight:600;color:var(--acc)}

/* ---------- answer ---------- */
.ans{margin:20px 0 0;background:var(--acc-soft);border-left:2px solid var(--acc);
  border-radius:0 4px 4px 0;padding:13px 18px;break-inside:avoid}
.ans .h{font-family:ui-monospace,monospace;font-size:10.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--acc);display:block;margin-bottom:2px}
.ans p{margin:0;font-family:Georgia,serif;font-size:16px}
.note{margin:12px 0 0;font-size:12.5px;color:var(--mut);padding-left:2px}

/* ---------- summary ---------- */
.summary{margin-top:72px;border-top:1px solid var(--ink);padding-top:20px}
.summary h2{font-size:16px;margin:0 0 14px;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:13.5px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:ui-monospace,monospace;font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--mut);font-weight:500}
td.q{font-family:ui-monospace,monospace;font-size:12.5px;color:var(--acc);white-space:nowrap}
td.r{font-family:Georgia,serif;font-size:14px}
footer{margin-top:56px;color:var(--mut);font-size:11.5px;letter-spacing:.03em}

@media print{
  body{background:#fff;font-size:11.5pt}
  .page{max-width:none;border:0;padding:0}
  .prob{margin-top:26px}
  .chapter{margin-top:34px}
  a{color:inherit;text-decoration:none}
  @page{size:A4;margin:16mm 15mm}
}
"""


def eq(s):
    return f'<p class="eq">{s}</p>'


def problem(p):
    out = [f'<article class="prob" id="{p["id"]}">']
    head = f'<div class="prob-head"><span class="pnum">{p["num"]}</span><h3>{p["title"]}</h3>'
    if p.get("tag"):
        head += f'<span class="tag">{p["tag"]}</span>'
    head += '</div>'
    out.append(head)
    src = f'<p class="src">{p["en"]}'
    if p.get("zh"):
        src += f'<span class="zh">{p["zh"]}</span>'
    out.append(src + '</p>')
    if p.get("fig"):
        svg, cap = p["fig"]
        out.append(f'<figure>{svg}<figcaption>{cap}</figcaption></figure>')
    out.append('<ol class="steps">')
    for st in p["steps"]:
        out.append('<li>')
        if st.get("t"):
            out.append(f'<p class="lab">{st["t"]}</p>')
        for line in st["e"]:
            out.append(eq(line))
        out.append('</li>')
    out.append('</ol>')
    if p.get("ans"):
        out.append(f'<div class="ans"><span class="h">答案</span><p>{p["ans"]}</p></div>')
    if p.get("note"):
        out.append(f'<p class="note">{p["note"]}</p>')
    out.append('</article>')
    return "".join(out)


CH3 = [
    dict(
        id="p3-9", num="P9", title="由射極電流回推 I<sub>C</sub>、I<sub>B</sub>", tag="3.3",
        en="If the emitter current of a transistor is 8 mA and I<sub>B</sub> is 1/100 of I<sub>C</sub>, determine the levels of I<sub>C</sub> and I<sub>B</sub>.",
        zh="已知射極電流 8 mA，且基極電流是集極電流的 1/100，求 I<sub>C</sub> 與 I<sub>B</sub>。",
        steps=[
            dict(t="三電流關係，把 I<sub>B</sub> = I<sub>C</sub>/100 代入",
                 e=["I<sub>E</sub> = I<sub>C</sub> + I<sub>B</sub> = I<sub>C</sub>(1 + 1/100) = 1.01 I<sub>C</sub>"]),
            dict(t="解出集極電流", e=["I<sub>C</sub> = I<sub>E</sub>/1.01 = 8 mA/1.01 = <b>7.92 mA</b>"]),
            dict(t="再代回求基極電流", e=["I<sub>B</sub> = I<sub>C</sub>/100 = 79.2 µA"]),
            dict(t="驗算（直流 α）", e=["α<sub>dc</sub> = I<sub>C</sub>/I<sub>E</sub> = 7.92/8 = 0.990 ✓"]),
        ],
        ans="I<sub>C</sub> = 7.92 mA　；　I<sub>B</sub> = 79.2 µA（α<sub>dc</sub> = 0.990）",
    ),
    dict(
        id="p3-21", num="P21", title="由特性曲線讀 β<sub>dc</sub>、α、I<sub>CEO</sub>、I<sub>CBO</sub>", tag="3.6",
        en="For the common-emitter characteristics of Fig. 3.14: (a) find the dc beta at an operating point of V<sub>CE</sub> = +8 V and I<sub>C</sub> = 2 mA. (b) Find the value of α corresponding to this operating point. (c) At V<sub>CE</sub> = +8 V, find the corresponding value of I<sub>CEO</sub>. (d) Calculate the approximate value of I<sub>CBO</sub> using the dc beta value obtained in (a).",
        zh="在圖 3.14 的共射極特性曲線上：求 (a) 工作點 V<sub>CE</sub> = 8 V、I<sub>C</sub> = 2 mA 的直流 β (b) 該點的 α (c) V<sub>CE</sub> = 8 V 時的 I<sub>CEO</sub> (d) 用 (a) 的 β 求 I<sub>CBO</sub>。",
        fig=(F.fig_characteristics(),
             "圖 3.14　共射極輸出特性（依原題重繪；曲線每 10 µA 一條）。<br>I<sub>B</sub> = 0 的那條曲線，在 V<sub>CE</sub> = 8 V 處的 I<sub>C</sub> 就是 I<sub>CEO</sub>。"),
        steps=[
            dict(t="(a) 在圖上找 V<sub>CE</sub> = 8 V 與 I<sub>C</sub> = 2 mA 的交點 Q，讀出它對應的 I<sub>B</sub>；該點落在 10 µA 與 20 µA 之間，約 18 µA",
                 e=["β<sub>dc</sub> = I<sub>C</sub>/I<sub>B</sub> = 2 mA/18 µA = <b>111</b>"]),
            dict(t="(b) β 與 α 的轉換", e=["α<sub>dc</sub> = β/(β + 1) = 111/112 = 0.991"]),
            dict(t="(c) I<sub>CEO</sub> 是 I<sub>B</sub> = 0 那條曲線的 I<sub>C</sub> 值（V<sub>CE</sub> = 8 V）",
                 e=["I<sub>CEO</sub> ≈ 0.3 mA"]),
            dict(t="(d) 由 I<sub>CBO</sub> = (1 − α)I<sub>CEO</sub>",
                 e=["I<sub>CBO</sub> = (1 − 0.991)(0.3 mA) = 2.7 µA"]),
        ],
        ans="β<sub>dc</sub> ≈ 111　；　α = 0.991　；　I<sub>CEO</sub> ≈ 0.3 mA　；　I<sub>CBO</sub> ≈ 2.7 µA",
        note="讀圖值會隨刻度略有差異（例如讀成 I<sub>B</sub> = 20 µA 就得到 β = 100）；考卷上把「讀到的 I<sub>B</sub>」寫出來，過程就完整。",
    ),
]

CH4 = [
    dict(
        id="p4-3", num="P3", title="固定偏壓：求 I<sub>C</sub>、V<sub>CC</sub>、β、R<sub>B</sub>", tag="4.3",
        en="Given the information appearing in Fig. 4.110, determine: a. I<sub>C</sub>. b. V<sub>CC</sub>. c. β. d. R<sub>B</sub>.",
        zh="圖 4.110 為固定偏壓電路，已知 R<sub>C</sub> = 2.2 kΩ、I<sub>B</sub> = 20 µA、V<sub>CE</sub> = 7.2 V、I<sub>E</sub> = 4 mA。",
        fig=(F.fig_4110(), "圖 4.110　固定偏壓電路（依原題重繪）"),
        steps=[
            dict(t="a. 由節點電流求集極電流", e=["I<sub>C</sub> = I<sub>E</sub> − I<sub>B</sub> = 4 mA − 0.02 mA = 3.98 mA ≈ 4 mA"]),
            dict(t="b. 由輸出迴路：V<sub>CC</sub> = I<sub>C</sub>R<sub>C</sub> + V<sub>CE</sub>",
                 e=["V<sub>CC</sub> = (3.98 mA)(2.2 kΩ) + 7.2 V = 8.76 + 7.2 = 15.96 V ≈ 16 V"]),
            dict(t="c. 直流電流增益", e=["β<sub>dc</sub> = I<sub>C</sub>/I<sub>B</sub> = 3.98 mA/20 µA = 199 ≈ 200"]),
            dict(t="d. 基極迴路：R<sub>B</sub> = (V<sub>CC</sub> − V<sub>BE</sub>)/I<sub>B</sub>",
                 e=["R<sub>B</sub> = (15.96 − 0.7)/20 µA = 763 kΩ"]),
        ],
        ans="I<sub>C</sub> = 3.98 mA　；　V<sub>CC</sub> = 15.96 V　；　β = 199　；　R<sub>B</sub> = 763 kΩ",
    ),
    dict(
        id="p4-7", num="P7", title="射極偏壓：求 R<sub>C</sub>、R<sub>E</sub>、R<sub>B</sub>、V<sub>CE</sub>、V<sub>B</sub>", tag="4.4",
        en="Given the information provided in Fig. 4.113, determine: a. R<sub>C</sub>. b. R<sub>E</sub>. c. R<sub>B</sub>. d. V<sub>CE</sub>. e. V<sub>B</sub>.",
        zh="圖 4.113 為射極穩定偏壓電路，已知 V<sub>CC</sub> = 12 V、I<sub>C</sub> = 2 mA、V<sub>C</sub> = 7.6 V、V<sub>E</sub> = 2.4 V、β = 80。",
        fig=(F.fig_4113(), "圖 4.113　射極偏壓電路（依原題重繪）"),
        steps=[
            dict(t="a. R<sub>C</sub> 上的電壓除以電流", e=["R<sub>C</sub> = (V<sub>CC</sub> − V<sub>C</sub>)/I<sub>C</sub> = (12 − 7.6)/2 mA = 2.2 kΩ"]),
            dict(t="b. I<sub>E</sub> ≈ I<sub>C</sub>", e=["R<sub>E</sub> = V<sub>E</sub>/I<sub>E</sub> = 2.4 V/2 mA = 1.2 kΩ"]),
            dict(t="c. 先求 V<sub>B</sub> 與 I<sub>B</sub>",
                 e=["V<sub>B</sub> = V<sub>E</sub> + 0.7 = 3.1 V　；　I<sub>B</sub> = I<sub>C</sub>/β = 2 mA/80 = 25 µA",
                    "R<sub>B</sub> = (V<sub>CC</sub> − V<sub>B</sub>)/I<sub>B</sub> = (12 − 3.1)/25 µA = 356 kΩ"]),
            dict(t="d、e. 兩端電壓相減即 V<sub>CE</sub>", e=["V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 7.6 − 2.4 = 5.2 V　；　V<sub>B</sub> = 3.1 V"]),
        ],
        ans="R<sub>C</sub> = 2.2 kΩ　；　R<sub>E</sub> = 1.2 kΩ　；　R<sub>B</sub> = 356 kΩ　；　V<sub>CE</sub> = 5.2 V　；　V<sub>B</sub> = 3.1 V",
    ),
    dict(
        id="p4-13", num="P13", title="分壓偏壓：求 I<sub>C</sub>、V<sub>E</sub>、V<sub>B</sub>、R<sub>1</sub>", tag="4.5",
        en="Given the information provided in Fig. 4.116, determine: a. I<sub>C</sub>. b. V<sub>E</sub>. c. V<sub>B</sub>. d. R<sub>1</sub>.",
        zh="圖 4.116 為分壓偏壓電路，已知 V<sub>CC</sub> = 18 V、R<sub>C</sub> = 4.7 kΩ、V<sub>C</sub> = 12 V、R<sub>2</sub> = 5.6 kΩ、R<sub>E</sub> = 1.2 kΩ。",
        fig=(F.fig_4116(), "圖 4.116　分壓偏壓電路（依原題重繪）"),
        steps=[
            dict(t="a. R<sub>C</sub> 上 18 − 12 = 6 V", e=["I<sub>C</sub> = (V<sub>CC</sub> − V<sub>C</sub>)/R<sub>C</sub> = 6 V/4.7 kΩ = 1.28 mA"]),
            dict(t="b. I<sub>E</sub> ≈ I<sub>C</sub>", e=["V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> = (1.28 mA)(1.2 kΩ) = 1.54 V"]),
            dict(t="c. 基極比射極高 0.7 V", e=["V<sub>B</sub> = V<sub>E</sub> + V<sub>BE</sub> = 1.54 + 0.7 = 2.24 V"]),
            dict(t="d. 先算 R<sub>2</sub> 的電流；因 I<sub>B</sub> 遠小於分壓器電流，取 I<sub>R1</sub> ≈ I<sub>R2</sub>",
                 e=["I<sub>R2</sub> = V<sub>B</sub>/R<sub>2</sub> = 2.24/5.6 kΩ = 0.4 mA",
                    "R<sub>1</sub> = (V<sub>CC</sub> − V<sub>B</sub>)/I<sub>R1</sub> = (18 − 2.24)/0.4 mA = 39.4 kΩ"]),
        ],
        ans="I<sub>C</sub> = 1.28 mA　；　V<sub>E</sub> = 1.54 V　；　V<sub>B</sub> = 2.24 V　；　R<sub>1</sub> = 39.4 kΩ（取 39 kΩ 標準值）",
        note="此題未給 β，故 R<sub>1</sub> 採分壓器近似（I<sub>B</sub> 忽略）；若要精確解，需先知道 β 才能定出 I<sub>B</sub>。",
    ),
    dict(
        id="p4-19", num="P19", title="分壓偏壓設計：由 Q 點反推 R<sub>C</sub>、R<sub>E</sub>、R<sub>2</sub>", tag="4.5",
        en="a. Using the characteristics of Fig. 4.111, determine R<sub>C</sub> and R<sub>E</sub> for a voltage-divider network having a Q-point of I<sub>CQ</sub> = 5 mA and V<sub>CEQ</sub> = 8 V. Use V<sub>CC</sub> = 24 V and R<sub>C</sub> = 3R<sub>E</sub>. b. Find V<sub>E</sub>. c. Determine V<sub>B</sub>. d. Find R<sub>2</sub> if R<sub>1</sub> = 24 kΩ assuming βR<sub>E</sub> &gt; 10R<sub>2</sub>. e. Calculate β at the Q-point. f. Test Eq. (4.33), and note whether the assumption of part (d) is correct.",
        zh="設計一個分壓偏壓網路：Q 點 I<sub>CQ</sub> = 5 mA、V<sub>CEQ</sub> = 8 V，V<sub>CC</sub> = 24 V，且 R<sub>C</sub> = 3R<sub>E</sub>。",
        fig=(F.fig_design(), "設計完成的分壓偏壓網路（依求得值重繪；Q 點 5 mA / 8 V）"),
        steps=[
            dict(t="a. 直流負載線：R<sub>C</sub> + R<sub>E</sub> = 4R<sub>E</sub>",
                 e=["V<sub>CC</sub> = I<sub>C</sub>(R<sub>C</sub> + R<sub>E</sub>) + V<sub>CE</sub>",
                    "24 = (5 mA)(4R<sub>E</sub>) + 8　→　R<sub>E</sub> = 16 V/20 mA = 0.8 kΩ　；　R<sub>C</sub> = 3R<sub>E</sub> = 2.4 kΩ"]),
            dict(t="b. 射極電壓", e=["V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> ≈ (5 mA)(0.8 kΩ) = 4 V"]),
            dict(t="c. 基極電壓", e=["V<sub>B</sub> = V<sub>E</sub> + 0.7 = 4.7 V"]),
            dict(t="d. 近似分壓公式（因假設 βR<sub>E</sub> &gt; 10R<sub>2</sub>，I<sub>B</sub> 可忽略）",
                 e=["V<sub>B</sub> = R<sub>2</sub>V<sub>CC</sub>/(R<sub>1</sub> + R<sub>2</sub>)　→　4.7 = 24R<sub>2</sub>/(24 k + R<sub>2</sub>)",
                    "R<sub>2</sub> = 5.84 kΩ（取 5.6 kΩ 標準值）"]),
            dict(t="e. 由圖 4.111 在 Q(5 mA, 8 V) 讀出 I<sub>B</sub> ≈ 38.5 µA",
                 e=["β = I<sub>C</sub>/I<sub>B</sub> = 5 mA/38.5 µA = 129.8 ≈ 130"]),
            dict(t="f. 檢驗 Eq. (4.33)：βR<sub>E</sub> &gt; 10R<sub>2</sub> ?",
                 e=["(129.8)(0.8 kΩ) = 103.8 kΩ　&gt;　10(5.84 kΩ) = 58.4 kΩ ✓　假設成立"]),
        ],
        ans="R<sub>E</sub> = 0.8 kΩ　；　R<sub>C</sub> = 2.4 kΩ　；　V<sub>E</sub> = 4 V　；　V<sub>B</sub> = 4.7 V　；　R<sub>2</sub> = 5.84 kΩ　；　β ≈ 130（假設成立）",
    ),
]

CH5 = [
    dict(
        id="p5-5", num="P5", title="共基極：Z<sub>i</sub>、V<sub>o</sub>、A<sub>v</sub>、Z<sub>o</sub>、A<sub>i</sub>、I<sub>b</sub>", tag="5.4",
        en="For the common-base configuration of Fig. 5.18, an ac signal of 10 mV is applied, resulting in an ac emitter current of 0.5 mA. If α = 0.980, determine: a. Z<sub>i</sub>. b. V<sub>o</sub> if R<sub>L</sub> = 1.2 kΩ. c. A<sub>v</sub> = V<sub>o</sub>/V<sub>i</sub>. d. Z<sub>o</sub> with r<sub>o</sub> = ∞ Ω. e. A<sub>i</sub> = I<sub>o</sub>/I<sub>i</sub>. f. I<sub>b</sub>.",
        zh="共基極組態：V<sub>i</sub> = 10 mV，交流射極電流 0.5 mA，α = 0.98，R<sub>L</sub> = 1.2 kΩ。本題直接由定義求解，不需先做直流分析。",
        fig=(F.fig_cb_model(), "共基極交流等效電路：輸入看進去就是 r<sub>e</sub>（依原題重繪）"),
        steps=[
            dict(t="a. 輸入阻抗＝輸入電壓除以輸入電流", e=["Z<sub>i</sub> = V<sub>i</sub>/I<sub>i</sub> = 10 mV/0.5 mA = 20 Ω　（即 r<sub>e</sub>）"]),
            dict(t="b. 集極電流 = αI<sub>e</sub>，再乘上負載",
                 e=["I<sub>c</sub> = αI<sub>e</sub> = 0.98 × 0.5 mA = 0.49 mA",
                    "V<sub>o</sub> = I<sub>c</sub>R<sub>L</sub> = (0.49 mA)(1.2 kΩ) = 0.588 V"]),
            dict(t="c. 電壓增益", e=["A<sub>v</sub> = V<sub>o</sub>/V<sub>i</sub> = 0.588 V/10 mV = 58.8　（= αR<sub>L</sub>/r<sub>e</sub>）"]),
            dict(t="d. 輸出端沒有 R<sub>C</sub>、r<sub>o</sub> 又視為無限大", e=["Z<sub>o</sub> = ∞ Ω"]),
            dict(t="e. 電流增益", e=["A<sub>i</sub> = I<sub>o</sub>/I<sub>i</sub> = α = 0.98"]),
            dict(t="f. 基極電流＝射極電流扣掉集極電流", e=["I<sub>b</sub> = I<sub>e</sub> − I<sub>c</sub> = 0.5 − 0.49 = 0.01 mA = 10 µA"]),
        ],
        ans="Z<sub>i</sub> = 20 Ω　；　V<sub>o</sub> = 0.588 V　；　A<sub>v</sub> = 58.8　；　Z<sub>o</sub> = ∞　；　A<sub>i</sub> = 0.98　；　I<sub>b</sub> = 10 µA",
    ),
    dict(
        id="p5-9", num="P9", title="固定偏壓 CE：Z<sub>i</sub>、Z<sub>o</sub>、A<sub>v</sub>（含 r<sub>o</sub>）", tag="5.5",
        en="For the network of Fig. 5.150: a. Determine Z<sub>i</sub> and Z<sub>o</sub>. b. Find A<sub>v</sub>. c. Repeat part (a) with r<sub>o</sub> = 20 kΩ. d. Repeat part (b) with r<sub>o</sub> = 20 kΩ.",
        zh="圖 5.150：V<sub>CC</sub> = 12 V、R<sub>B</sub> = 220 kΩ、R<sub>C</sub> = 2.2 kΩ、β = 60、r<sub>o</sub> = 40 kΩ。",
        fig=(F.fig_5150(), "圖 5.150　固定偏壓共射極放大器（依原題重繪）"),
        steps=[
            dict(t="1. 直流分析（耦合電容視為開路）",
                 e=["I<sub>B</sub> = (V<sub>CC</sub> − V<sub>BE</sub>)/R<sub>B</sub> = (12 − 0.7)/220 kΩ = 51.4 µA",
                    "I<sub>E</sub> = (β + 1)I<sub>B</sub> = 61 × 51.4 µA = 3.13 mA"]),
            dict(t="2. 交流射極電阻", e=["r<sub>e</sub> = 26 mV/I<sub>E</sub> = 26 mV/3.13 mA = 8.30 Ω"]),
            dict(t="3. a. 輸入阻抗＝R<sub>B</sub> 並聯 βr<sub>e</sub>",
                 e=["Z<sub>i</sub> = R<sub>B</sub> ∥ βr<sub>e</sub> = 220 kΩ ∥ (60 × 8.30 = 498 Ω) = 497 Ω"]),
            dict(t="4. a. 輸出阻抗：r<sub>o</sub> = 40 kΩ ≥ 10R<sub>C</sub> = 22 kΩ，可忽略 r<sub>o</sub>",
                 e=["Z<sub>o</sub> ≈ R<sub>C</sub> = 2.2 kΩ"]),
            dict(t="5. b. 電壓增益（射極接地，無 R<sub>E</sub> 分壓）",
                 e=["A<sub>v</sub> = −R<sub>C</sub>/r<sub>e</sub> = −2.2 kΩ/8.30 Ω = −265"]),
            dict(t="6. c、d. r<sub>o</sub> = 20 kΩ &lt; 22 kΩ，必須計入",
                 e=["Z<sub>o</sub> = R<sub>C</sub> ∥ r<sub>o</sub> = 2.2 k ∥ 20 k = 1.98 kΩ",
                    "A<sub>v</sub> = −(R<sub>C</sub> ∥ r<sub>o</sub>)/r<sub>e</sub> = −1.98 kΩ/8.30 Ω = −239"]),
        ],
        ans="Z<sub>i</sub> = 497 Ω　；　Z<sub>o</sub> = 2.2 kΩ　；　A<sub>v</sub> = −265　；　(r<sub>o</sub> = 20 kΩ) Z<sub>o</sub> = 1.98 kΩ、A<sub>v</sub> = −239",
        note="判準：r<sub>o</sub> ≥ 10R<sub>C</sub> 時輸出端可把 r<sub>o</sub> 當開路，否則要與 R<sub>C</sub> 並聯。",
    ),
    dict(
        id="p5-11", num="P11", title="固定偏壓 CE：I<sub>B</sub>、I<sub>C</sub>、r<sub>e</sub>、Z<sub>i</sub>、Z<sub>o</sub>、A<sub>v</sub>", tag="5.5",
        en="For the network of Fig. 5.152: a. Calculate I<sub>B</sub>, I<sub>C</sub>, and r<sub>e</sub>. b. Determine Z<sub>i</sub> and Z<sub>o</sub>. c. Calculate A<sub>v</sub>. d. Determine the effect of r<sub>o</sub> = 30 kΩ on A<sub>v</sub>.",
        zh="圖 5.152：V<sub>CC</sub> = 10 V、R<sub>C</sub> = 4.3 kΩ、R<sub>B</sub> = 390 kΩ、β = 100、r<sub>o</sub> = 60 kΩ。",
        fig=(F.fig_5152(), "圖 5.152　固定偏壓共射極放大器（依原題重繪）"),
        steps=[
            dict(t="a. 基極迴路", e=["I<sub>B</sub> = (10 − 0.7)/390 kΩ = 23.8 µA"]),
            dict(t="a. 電流與 r<sub>e</sub>",
                 e=["I<sub>C</sub> = βI<sub>B</sub> = 100 × 23.8 µA = 2.38 mA　；　I<sub>E</sub> = 101I<sub>B</sub> = 2.41 mA",
                    "r<sub>e</sub> = 26 mV/2.41 mA = 10.8 Ω"]),
            dict(t="b. 輸入阻抗", e=["Z<sub>i</sub> = R<sub>B</sub> ∥ βr<sub>e</sub> = 390 kΩ ∥ 1.08 kΩ = 1.08 kΩ"]),
            dict(t="b. 輸出阻抗：r<sub>o</sub> = 60 kΩ ≥ 10R<sub>C</sub> = 43 kΩ",
                 e=["Z<sub>o</sub> ≈ R<sub>C</sub> = 4.3 kΩ"]),
            dict(t="c. 電壓增益", e=["A<sub>v</sub> = −R<sub>C</sub>/r<sub>e</sub> = −4.3 kΩ/10.8 Ω = −398"]),
            dict(t="d. r<sub>o</sub> = 30 kΩ &lt; 43 kΩ，改與 R<sub>C</sub> 並聯",
                 e=["R<sub>C</sub> ∥ r<sub>o</sub> = 4.3 k ∥ 30 k = 3.76 kΩ",
                    "A<sub>v</sub> = −3.76 kΩ/10.8 Ω = −348（增益下降約 13%）"]),
        ],
        ans="I<sub>B</sub> = 23.8 µA　；　I<sub>C</sub> = 2.38 mA　；　r<sub>e</sub> = 10.8 Ω　；　Z<sub>i</sub> = 1.08 kΩ　；　Z<sub>o</sub> = 4.3 kΩ　；　A<sub>v</sub> = −398（r<sub>o</sub> = 30 kΩ 時 −348）",
    ),
    dict(
        id="p5-13", num="P13", title="分壓偏壓 CE：由 A<sub>v</sub> 反求 V<sub>CC</sub>", tag="5.6",
        en="Determine V<sub>CC</sub> for the network of Fig. 5.154 if A<sub>v</sub> = −160 and r<sub>o</sub> = 100 kΩ.",
        zh="圖 5.154：R<sub>1</sub> = 82 kΩ、R<sub>2</sub> = 5.6 kΩ、R<sub>C</sub> = 3.3 kΩ、R<sub>E</sub> = 1 kΩ（C<sub>E</sub> 旁路）、β = 100。已知 A<sub>v</sub> = −160、r<sub>o</sub> = 100 kΩ，反求 V<sub>CC</sub>。",
        fig=(F.fig_5154(), "圖 5.154　分壓偏壓放大器（R<sub>E</sub> 被 C<sub>E</sub> 旁路，交流上射極接地）"),
        steps=[
            dict(t="1. 先檢驗 r<sub>o</sub> 是否可忽略：r<sub>o</sub> = 100 kΩ ≥ 10R<sub>C</sub> = 33 kΩ ✓",
                 e=["A<sub>v</sub> = −R<sub>C</sub>/r<sub>e</sub>（r<sub>o</sub> 不計）"]),
            dict(t="2. 由增益反推 r<sub>e</sub>", e=["r<sub>e</sub> = R<sub>C</sub>/|A<sub>v</sub>| = 3.3 kΩ/160 = 20.63 Ω"]),
            dict(t="3. 由 r<sub>e</sub> 反推射極電流與電壓",
                 e=["I<sub>E</sub> = 26 mV/r<sub>e</sub> = 26 mV/20.63 Ω = 1.261 mA",
                    "V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> = (1.261 mA)(1 kΩ) = 1.261 V"]),
            dict(t="4. 基極電壓", e=["V<sub>B</sub> = V<sub>E</sub> + 0.7 = 1.961 V"]),
            dict(t="5. 分壓公式（檢查 βR<sub>E</sub> = 100 kΩ &gt; 10R<sub>2</sub> = 56 kΩ，近似法可用）",
                 e=["V<sub>B</sub> = [R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>)]V<sub>CC</sub>",
                    "1.961 = [5.6 k/87.6 k]V<sub>CC</sub>　→　V<sub>CC</sub> = 30.7 V"]),
        ],
        ans="V<sub>CC</sub> ≈ 30.7 V（≈ 31 V）",
        note="若把 r<sub>o</sub> 也算進去（A<sub>v</sub> = −(R<sub>C</sub>∥r<sub>o</sub>)/r<sub>e</sub>），答案會是 31.3 V；因 100 kΩ ≥ 10R<sub>C</sub>，課本標準解法忽略 r<sub>o</sub>。",
    ),
]

SUMMARY = [
    ("Ch3 P9", "I<sub>C</sub> = 7.92 mA，I<sub>B</sub> = 79.2 µA"),
    ("Ch3 P21", "β = 111，α = 0.991，I<sub>CEO</sub> = 0.3 mA，I<sub>CBO</sub> = 2.7 µA"),
    ("Ch4 P3", "I<sub>C</sub> = 3.98 mA，V<sub>CC</sub> = 15.96 V，β = 199，R<sub>B</sub> = 763 kΩ"),
    ("Ch4 P7", "R<sub>C</sub> = 2.2 kΩ，R<sub>E</sub> = 1.2 kΩ，R<sub>B</sub> = 356 kΩ，V<sub>CE</sub> = 5.2 V，V<sub>B</sub> = 3.1 V"),
    ("Ch4 P13", "I<sub>C</sub> = 1.28 mA，V<sub>E</sub> = 1.54 V，V<sub>B</sub> = 2.24 V，R<sub>1</sub> = 39.4 kΩ"),
    ("Ch4 P19", "R<sub>C</sub> = 2.4 kΩ，R<sub>E</sub> = 0.8 kΩ，V<sub>E</sub> = 4 V，V<sub>B</sub> = 4.7 V，R<sub>2</sub> = 5.84 kΩ，β = 130"),
    ("Ch5 P5", "Z<sub>i</sub> = 20 Ω，V<sub>o</sub> = 0.588 V，A<sub>v</sub> = 58.8，Z<sub>o</sub> = ∞，A<sub>i</sub> = 0.98，I<sub>b</sub> = 10 µA"),
    ("Ch5 P9", "Z<sub>i</sub> = 497 Ω，Z<sub>o</sub> = 2.2 kΩ，A<sub>v</sub> = −265；r<sub>o</sub> = 20 kΩ：Z<sub>o</sub> = 1.98 kΩ，A<sub>v</sub> = −239"),
    ("Ch5 P11", "I<sub>B</sub> = 23.8 µA，I<sub>C</sub> = 2.38 mA，r<sub>e</sub> = 10.8 Ω，Z<sub>i</sub> = 1.08 kΩ，Z<sub>o</sub> = 4.3 kΩ，A<sub>v</sub> = −398（−348）"),
    ("Ch5 P13", "V<sub>CC</sub> = 30.7 V"),
]


def chapter(no, title, en, problems):
    out = [f'<section class="chapter" id="ch{no}">',
           f'<div class="chap-head"><span class="no">Chapter {no}</span>'
           f'<h2>{title}</h2><span class="en">{en}</span></div>']
    out += [problem(p) for p in problems]
    out.append('</section>')
    return "".join(out)


rows = "".join(f'<tr><td class="q">{q}</td><td class="r">{r}</td></tr>' for q, r in SUMMARY)

html = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>電子學 作業 II 全解 — Ch3 / Ch4 / Ch5</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">

  <div class="kicker">Electronic Devices &amp; Circuit Theory · Assignment II</div>
  <h1>電子學作業 II　全解</h1>
  <p class="sub">Ch 3 P9、P21　·　Ch 4 P3、P7、P13、P19　·　Ch 5 P5、P9、P11、P13</p>
  <div class="chips">
    <span class="chip">11 題</span>
    <span class="chip">DC → r<sub>e</sub> → Z<sub>i</sub> / Z<sub>o</sub> / A<sub>v</sub></span>
    <span class="chip">電路圖依原題重繪</span>
  </div>
  <div class="rule"></div>
  <p class="conv">全篇採矽 BJT：V<sub>BE</sub> = 0.7 V；r<sub>e</sub> = 26 mV / I<sub>E</sub>(dc)；未特別註明時視 β ≫ 1、I<sub>E</sub> ≈ I<sub>C</sub>，且耦合／旁路電容在直流下視為開路、交流下視為短路。</p>

  {chapter("3", "Bipolar Junction Transistors", "直流電流關係與特性曲線", CH3)}
  {chapter("4", "DC Biasing — BJTs", "偏壓電路的直流分析與設計", CH4)}
  {chapter("5", "BJT AC Analysis", "小訊號 r<sub>e</sub> 模型", CH5)}

  <section class="summary">
    <h2>答案總表</h2>
    <table>
      <thead><tr><th>題號</th><th>答案</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </section>

  <footer>依 Boylestad &amp; Nashelsky《Electronic Devices and Circuit Theory》題號整理；數值以課本解答為準（四捨五入至 3 位有效數字）。</footer>
</div>
</body>
</html>
"""
open("index.html", "w", encoding="utf-8").write(html)
print("index.html written", len(html), "bytes")
