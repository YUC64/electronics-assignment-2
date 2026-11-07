# -*- coding: utf-8 -*-
"""Generate SVG circuit figures for the electronics homework site."""
import re

INK = "#232a31"
MUT = "#79838d"
ACC = "#2b6b7f"

DEFS = (
    '<defs>'
    '<marker id="ar" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5.4" markerHeight="5.4" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
    '<marker id="arr" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5.4" markerHeight="5.4" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker>'
    '</defs>'
)


def svg(w, h, inner):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" role="img">'
            + DEFS + inner + '</svg>')


def W(*pts, w=1.6, color=INK):
    d = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    return f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def L(x1, y1, x2, y2, w=1.6, color=INK, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{da}/>'


def _rich(s, size):
    """<sub>/<sup> -> SVG tspans (HTML tags inside <svg> break the HTML parser)."""
    def sub(m):
        return (f'<tspan dy="{size*0.30:.1f}" font-size="{size*0.72:.1f}">{m.group(1)}</tspan>'
                f'<tspan dy="{-size*0.30:.1f}">')
    def sup(m):
        return (f'<tspan dy="{-size*0.34:.1f}" font-size="{size*0.72:.1f}">{m.group(1)}</tspan>'
                f'<tspan dy="{size*0.34:.1f}">')
    s = re.sub(r'<sub>(.*?)</sub>', sub, s)
    s = re.sub(r'<sup>(.*?)</sup>', sup, s)
    return s


def T(x, y, s, size=11, anchor="start", color=INK, weight=400, style="normal", rotate=None):
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
            f'font-weight="{weight}" font-style="{style}"{tr}>{_rich(s, size)}</text>')


def res_v(x, y1, y2, label=None, lx=None, anchor="start", color=INK, size=11):
    Lz = y2 - y1
    a, b = y1 + min(9, Lz * 0.18), y2 - min(9, Lz * 0.18)
    n, amp = 6, 4.6
    pts = [(x, y1), (x, a)]
    seg = (b - a) / n
    for i in range(1, n):
        pts.append((x + (amp if i % 2 else -amp), a + seg * i))
    pts.append((x, b))
    pts.append((x, y2))
    out = W(*pts, color=color)
    if label:
        out += T(lx if lx is not None else x + 9, (y1 + y2) / 2 + 4, label, size, anchor, color)
    return out


def cap_v(x, y, gap=8, pl=16, label=None, lx=None, anchor="start", color=INK, size=11):
    """Capacitor in a VERTICAL wire (plates horizontal), top plate at y."""
    out = L(x - pl / 2, y, x + pl / 2, y, 2.6, color)
    out += L(x - pl / 2, y + gap, x + pl / 2, y + gap, 2.6, color)
    if label:
        out += T(lx if lx is not None else x + 14, y + gap / 2 + 4, label, size, anchor, color)
    return out


def cap_h(x, y, gap=8, pl=16, label=None, lx=None, anchor="start", color=INK, size=11):
    """Capacitor in a HORIZONTAL wire (plates vertical), left plate at x."""
    out = L(x, y - pl / 2, x, y + pl / 2, 2.6, color)
    out += L(x + gap, y - pl / 2, x + gap, y + pl / 2, 2.6, color)
    if label:
        out += T(lx if lx is not None else x + gap / 2, y - 16, label, size, anchor, color)
    return out


def gnd(x, y, color=INK):
    out = L(x - 12, y, x + 12, y, 1.7, color)
    out += L(x - 7.5, y + 5, x + 7.5, y + 5, 1.7, color)
    out += L(x - 3, y + 10, x + 3, y + 10, 1.7, color)
    return out


def node(x, y, color=INK, r=2.6):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


def term(x, y, label=None, lx=None, ly=None, anchor="middle", color=INK, size=11):
    out = f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" stroke="{color}" stroke-width="1.6"/>'
    if label:
        out += T(lx if lx is not None else x, ly if ly is not None else y - 12, label, size, anchor, color)
    return out


def arrow(x1, y1, x2, y2, color=INK, w=1.5, mk="ar"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" '
            f'marker-end="url(#{mk})" stroke-linecap="round"/>')


def badge(x, y, lines, size=10, color=MUT, fill="#f5f7f8"):
    wmax = max(len(re.sub(r'<[^>]+>', '', s)) for s in lines)
    w = max(54, wmax * 6.0 + 16)
    h = 14 * len(lines) + 8
    out = (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" rx="3" fill="{fill}" '
           f'stroke="#e0e5e8" stroke-width="1"/>')
    for i, s in enumerate(lines):
        out += T(x + w / 2, y + 15 + i * 14, s, size, "middle", color)
    return out


def npn(cx, cy, r=19, color=INK):
    bar_x = cx - 7
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="1.5"/>'
    out += L(bar_x, cy - 13, bar_x, cy + 13, 2.8, color)
    out += L(cx - 34, cy, bar_x, cy, 1.6, color)
    out += L(bar_x, cy - 8, cx + 11, cy - 18, 1.6, color)
    out += L(cx + 11, cy - 18, cx + 11, cy - 30, 1.6, color)
    out += L(bar_x, cy + 8, cx + 11, cy + 18, 1.6, color)
    out += L(cx + 11, cy + 18, cx + 11, cy + 30, 1.6, color)
    out += (f'<line x1="{bar_x + 3}" y1="{cy + 9.5}" x2="{cx + 7}" y2="{cy + 16}" stroke="{color}" '
            f'stroke-width="1.4" marker-end="url(#ar)" stroke-linecap="round"/>')
    return out, (cx - 34, cy), (cx + 11, cy - 30), (cx + 11, cy + 30)


def ac_source(x, y, label="V<sub>i</sub>", color=INK):
    out = f'<circle cx="{x}" cy="{y}" r="13" fill="#fff" stroke="{color}" stroke-width="1.6"/>'
    out += (f'<path d="M{x-7},{y} q3.5,-6.5 7,0 q3.5,6.5 7,0" fill="none" stroke="{color}" stroke-width="1.4"/>')
    out += T(x - 21, y + 4, label, 11, "end", color)
    return out


def input_net(cy, base_x, src_x=54, cap_x=94, lab_below=False):
    """AC source + series coupling capacitor feeding the node at (base_x, cy)."""
    out = ac_source(src_x, cy + 34)
    out += W((src_x, cy + 21), (src_x, cy), (cap_x, cy))
    out += cap_h(cap_x, cy, 8, 16)
    out += T(cap_x + 4, cy + (18 if lab_below else -14), "C<sub>c</sub>", 9.5, "middle", MUT)
    out += W((cap_x + 8, cy), (base_x, cy))
    out += W((src_x, cy + 47), (src_x, cy + 62))
    out += gnd(src_x, cy + 62)
    return out


# ---------------------------------------------------------------- FIG 3.14 characteristics
def fig_characteristics():
    x0, x1 = 88, 392
    y0, y1 = 268, 66
    out = L(x0, y0, x1, y0, 1.5) + L(x0, y0, x0, y1, 1.5)
    for v in range(0, 13, 2):
        px = x0 + (v / 12) * (x1 - x0)
        out += L(px, y0, px, y0 + 5, 1.2)
        col = ACC if v == 8 else MUT
        out += T(px, y0 + 18, str(v), 10, "middle", col, 600 if v == 8 else 400)
    for m in range(0, 7):
        py = y0 - (m / 6) * (y0 - y1)
        out += L(x0 - 5, py, x0, py, 1.2)
        col = ACC if m == 2 else MUT
        out += T(x0 - 9, py + 3.5, str(m), 10, "end", col, 600 if m == 2 else 400)
    out += T((x0 + x1) / 2, y0 + 38, "V<sub>CE</sub> (V)", 11, "middle", INK)
    out += T(28, (y0 + y1) / 2, "I<sub>C</sub> (mA)", 11, "middle", INK, rotate=-90)

    px = lambda v: x0 + (v / 12) * (x1 - x0)
    py = lambda i: y0 - (i / 6) * (y0 - y1)
    curves = [(0.30, "0"), (1.35, "10 µA"), (2.40, "20 µA"), (3.25, "30 µA"),
              (4.10, "40 µA"), (4.60, "50 µA"), (5.25, "60 µA")]
    for ic, lab in curves:
        pts = [(px(0.02), py(0.0)), (px(0.16), py(ic * 0.55)), (px(0.35), py(ic * 0.90)),
               (px(0.9), py(ic * 0.98)), (px(12), py(ic * 1.02))]
        d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
        for i in range(1, len(pts)):
            xa, ya = pts[i - 1]
            xb, yb = pts[i]
            dx = (xb - xa) * 0.5
            d += f' C{xa+dx:.1f},{ya:.1f} {xa+dx:.1f},{yb:.1f} {xb:.1f},{yb:.1f}'
        out += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.25"/>'
        out += T(x1 + 8, py(ic * 1.02) + 3.5, lab, 9.5, "start", MUT)

    qx, qy = px(8), py(2)
    out += L(qx, y0, qx, qy, 1.2, ACC, "3 3")
    out += L(x0, qy, qx, qy, 1.2, ACC, "3 3")
    out += f'<circle cx="{qx}" cy="{qy}" r="4.2" fill="{ACC}"/>'
    out += L(qx + 30, y0 - 22, qx + 3, qy + 7, 1.2, ACC, "3 3")
    out += T(qx + 34, y0 - 20, "Q (8 V, 2 mA)", 10, "start", ACC, 600)
    return svg(522, 332, out)


# ---------------------------------------------------------------- FIG 4.110 (Ch4 P3)
def fig_4110():
    out = ""
    rail_y, cy = 46, 200
    rb_x, rc_x = 108, 250
    out += L(rb_x, rail_y, rc_x, rail_y, 1.6)
    out += term(179, rail_y, "V<sub>CC</sub>", 179, rail_y - 12)
    out += res_v(rb_x, rail_y, 158, "R<sub>B</sub>", rb_x - 9, "end")
    out += W((rb_x, 158), (rb_x, cy), (216, cy))
    out += node(rb_x, cy)
    out += arrow(124, cy, 152, cy, ACC, 1.4, "arr")
    out += T(138, cy - 10, "I<sub>B</sub> = 20 µA", 10, "middle", ACC)
    out += res_v(rc_x, rail_y, 148, "2.2 kΩ", rc_x + 9, "start")
    out += arrow(rc_x - 17, 78, rc_x - 17, 104, INK)
    out += T(rc_x - 23, 96, "I<sub>C</sub>", 10, "end")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 148), (c[0], 148), c)
    out += W(e, (e[0], 252))
    out += gnd(e[0], 252)
    out += arrow(e[0] + 40, 220, e[0] + 40, 246, INK)
    out += T(e[0] + 48, 240, "I<sub>E</sub> = 4 mA", 10, "start")
    out += T(c[0] + 16, c[1] + 10, "+", 12, "start", MUT)
    out += T(e[0] + 16, e[1] - 2, "−", 12, "start", MUT)
    out += T(c[0] + 26, cy + 22, "V<sub>CE</sub> = 7.2 V", 10.5, "start")
    out += badge(176, 226, ["β"])
    return svg(460, 300, out)


# ---------------------------------------------------------------- FIG 4.113 (Ch4 P7)
def fig_4113():
    out = ""
    rail_y, cy = 46, 200
    rb_x, rc_x = 108, 250
    out += L(rb_x, rail_y, rc_x, rail_y, 1.6)
    out += term(179, rail_y, "12 V", 179, rail_y - 12)
    out += res_v(rb_x, rail_y, 158, "R<sub>B</sub>", rb_x - 9, "end")
    out += W((rb_x, 158), (rb_x, cy), (216, cy))
    out += node(rb_x, cy)
    out += res_v(rc_x, rail_y, 148, "R<sub>C</sub>", rc_x + 9, "start")
    out += arrow(rc_x - 17, 74, rc_x - 17, 100, INK)
    out += T(rc_x - 23, 92, "2 mA", 10, "end")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 148), (c[0], 148), c)
    out += W(e, (e[0], 254))
    out += res_v(e[0], 254, 300, "R<sub>E</sub>", e[0] + 9, "start")
    out += gnd(e[0], 310)
    out += node(e[0], 252)
    out += T(e[0] + 60, 258, "V<sub>E</sub> = 2.4 V", 10.5, "start")
    out += T(c[0] + 16, 168, "V<sub>C</sub> = 7.6 V", 10.5, "start")
    out += badge(178, 226, ["β = 80"])
    return svg(460, 330, out)


# ---------------------------------------------------------------- FIG 4.116 (Ch4 P13)
def fig_4116():
    out = ""
    rail_y, cy = 44, 196
    r1_x, rc_x = 106, 254
    out += L(r1_x, rail_y, rc_x, rail_y, 1.6)
    out += term(180, rail_y, "18 V", 180, rail_y - 12)
    out += res_v(r1_x, rail_y, 152, "R<sub>1</sub>", r1_x - 9, "end")
    out += W((r1_x, 152), (r1_x, cy), (218, cy))
    out += node(r1_x, cy)
    out += T(r1_x - 12, cy - 9, "V<sub>B</sub>", 10.5, "end")
    out += res_v(r1_x, cy, 292, "5.6 kΩ", r1_x - 9, "end")
    out += gnd(r1_x, 300)
    out += res_v(rc_x, rail_y, 144, "4.7 kΩ", rc_x + 9, "start")
    out += arrow(rc_x - 17, 74, rc_x - 17, 100, INK)
    out += T(rc_x - 23, 92, "I<sub>C</sub>", 10, "end")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 144), (c[0], 144), c)
    out += W(e, (e[0], 250))
    out += res_v(e[0], 250, 292, "1.2 kΩ", e[0] + 9, "start")
    out += gnd(e[0], 300)
    out += node(e[0], 248)
    out += T(e[0] + 60, 254, "V<sub>E</sub>", 10.5, "start")
    out += T(c[0] + 16, 162, "V<sub>C</sub> = 12 V", 10.5, "start")
    out += badge(182, 222, ["β"])
    return svg(460, 316, out)


# ---------------------------------------------------------------- FIG 4.111 design (Ch4 P19)
def fig_design():
    out = ""
    rail_y, cy = 44, 196
    r1_x, rc_x = 106, 254
    out += L(r1_x, rail_y, rc_x, rail_y, 1.6)
    out += term(180, rail_y, "V<sub>CC</sub> = 24 V", 180, rail_y - 12)
    out += res_v(r1_x, rail_y, 150, "R<sub>1</sub> = 24 kΩ", r1_x - 9, "end")
    out += W((r1_x, 150), (r1_x, cy), (218, cy))
    out += node(r1_x, cy)
    out += T(r1_x - 12, cy - 9, "V<sub>B</sub> = 4.7 V", 10.5, "end")
    out += res_v(r1_x, cy, 288, "R<sub>2</sub> = 5.84 kΩ", r1_x - 9, "end")
    out += gnd(r1_x, 296)
    out += res_v(rc_x, rail_y, 144, "R<sub>C</sub> = 2.4 kΩ", rc_x + 9, "start")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 144), (c[0], 144), c)
    out += W(e, (e[0], 248))
    out += res_v(e[0], 248, 288, "R<sub>E</sub> = 0.8 kΩ", e[0] + 9, "start")
    out += gnd(e[0], 296)
    out += node(e[0], 246)
    out += T(e[0] + 60, 252, "V<sub>E</sub> = 4 V", 10.5, "start")
    out += T(c[0] + 16, 160, "V<sub>C</sub> = 12 V", 10, "start", MUT)
    out += badge(182, 220, ["Q: 5 mA, 8 V"], 9.8)
    return svg(470, 312, out)


# ---------------------------------------------------------------- FIG 5.18 (Ch5 P5) AC model
def fig_cb_model():
    out = ""
    y = 152
    ex, ox, cs_x = 150, 350, 260
    out += term(34, y, "I<sub>i</sub>", 34, y - 12)
    out += W((34, y), (ex, y))
    out += node(ex, y)
    out += arrow(56, y + 16, 86, y + 16, ACC, 1.4, "arr")
    out += T(71, y + 32, "I<sub>e</sub> = 0.5 mA", 9.5, "middle", ACC)
    out += res_v(ex, y, y + 84, "r<sub>e</sub> = 20 Ω", ex + 9, "start")
    out += gnd(ex, y + 84)
    out += L(ex, y, cs_x, y, 1.6)
    out += f'<circle cx="{cs_x}" cy="{y + 44}" r="20" fill="none" stroke="{INK}" stroke-width="1.5"/>'
    out += arrow(cs_x, y + 30, cs_x, y + 60, INK)
    out += T(cs_x + 26, y + 40, "αI<sub>e</sub>", 10, "start")
    out += W((cs_x, y), (cs_x, y + 24))
    out += W((cs_x, y + 64), (cs_x, y + 92), (ex, y + 92), (ex, y + 46))
    out += L(cs_x, y, ox, y, 1.6)
    out += node(ox, y)
    out += res_v(ox, y, y + 68, "R<sub>L</sub> = 1.2 kΩ", ox + 9, "start")
    out += gnd(ox, y + 68)
    out += L(ox, y, ox + 44, y, 1.6)
    out += term(ox + 44, y, "V<sub>o</sub>", ox + 44, y - 12)
    out += T(230, 42, "共基極交流等效電路（r<sub>e</sub> 模型）", 10.5, "middle", MUT)
    return svg(440, 290, out)


# ---------------------------------------------------------------- FIG 5.150 (Ch5 P9)
def fig_5150():
    out = ""
    rail_y, cy = 44, 200
    rb_x, rc_x = 108, 252
    out += L(rb_x, rail_y, rc_x, rail_y, 1.6)
    out += term(180, rail_y, "12 V", 180, rail_y - 12)
    out += res_v(rb_x, rail_y, 150, "220 kΩ", rb_x - 9, "end")
    out += W((rb_x, 150), (rb_x, cy), (218, cy))
    out += node(rb_x, cy)
    out += input_net(cy, rb_x)
    out += res_v(rc_x, rail_y, 146, "2.2 kΩ", rc_x + 9, "start")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 146), (c[0], 146), c)
    out += W(e, (e[0], 250))
    out += gnd(e[0], 250)
    out += badge(178, 226, ["β = 60", "r<sub>o</sub> = 40 kΩ"], 9.6)
    out += W((c[0], 164), (c[0] + 26, 164))
    out += cap_h(c[0] + 26, 164, 8, 16, "C<sub>c</sub>", c[0] + 30, "middle", MUT, 9.5)
    out += W((c[0] + 34, 164), (c[0] + 62, 164))
    out += term(c[0] + 62, 164, "V<sub>o</sub>", c[0] + 62, 152)
    return svg(450, 300, out)


# ---------------------------------------------------------------- FIG 5.152 (Ch5 P11)
def fig_5152():
    out = ""
    rail_y, cy = 44, 196
    rb_x, rc_x = 108, 250
    out += term(178, rail_y, "10 V", 178, rail_y - 12)
    out += L(rb_x, rail_y, rc_x, rail_y, 1.6)
    out += res_v(rc_x, rail_y, 144, "4.3 kΩ", rc_x + 9, "start")
    out += W((rb_x, rail_y), (rb_x, cy), (216, cy))
    out += node(rb_x, cy)
    out += res_v(rb_x, cy, 280, "390 kΩ", rb_x + 9, "start")
    out += term(rb_x, 288, "+10 V", rb_x, 306)
    out += input_net(cy, rb_x)
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 144), (c[0], 144), c)
    out += W(e, (e[0], 246))
    out += gnd(e[0], 246)
    out += badge(176, 248, ["β = 100", "r<sub>o</sub> = 60 kΩ"], 9.6)
    out += W((c[0], 160), (c[0] + 26, 160))
    out += cap_h(c[0] + 26, 160, 8, 16, "C<sub>c</sub>", c[0] + 30, "middle", MUT, 9.5)
    out += W((c[0] + 34, 160), (c[0] + 62, 160))
    out += term(c[0] + 62, 160, "V<sub>o</sub>", c[0] + 62, 148)
    return svg(450, 316, out)


# ---------------------------------------------------------------- FIG 5.154 (Ch5 P13)
def fig_5154():
    out = ""
    rail_y, cy = 44, 192
    r1_x, rc_x = 106, 250
    out += L(r1_x, rail_y, rc_x, rail_y, 1.6)
    out += term(178, rail_y, "V<sub>CC</sub> = ?", 178, rail_y - 12)
    out += res_v(r1_x, rail_y, 146, "82 kΩ", r1_x - 9, "end")
    out += W((r1_x, 146), (r1_x, cy), (216, cy))
    out += node(r1_x, cy)
    out += T(r1_x + 13, cy - 10, "V<sub>B</sub>", 10.5, "start")
    out += res_v(r1_x, cy, 284, "5.6 kΩ", r1_x + 9, "start")
    out += gnd(r1_x, 292)
    out += input_net(cy, r1_x, 46, 84, lab_below=True)
    out += res_v(rc_x, rail_y, 142, "3.3 kΩ", rc_x + 9, "start")
    tp, b, c, e = npn(rc_x, cy)
    out += tp
    out += W((rc_x, 142), (c[0], 142), c)
    out += W(e, (e[0], 236))
    out += node(e[0], 236)
    out += res_v(e[0], 236, 284, "1 kΩ", e[0] + 9, "start")
    out += gnd(e[0], 292)
    out += W((e[0], 236), (e[0] + 26, 236))
    out += cap_h(e[0] + 26, 236, 8, 16)
    out += T(e[0] + 30, 218, "C<sub>E</sub>", 9.5, "middle", MUT)
    out += W((e[0] + 34, 236), (e[0] + 42, 236), (e[0] + 42, 288), (e[0], 288))
    out += node(e[0], 288)
    out += badge(176, 244, ["β = 100"], 9.6)
    out += W((c[0], 156), (c[0] + 26, 156))
    out += cap_h(c[0] + 26, 156, 8, 16, "C<sub>c</sub>", c[0] + 30, "middle", MUT, 9.5)
    out += W((c[0] + 34, 156), (c[0] + 62, 156))
    out += term(c[0] + 62, 156, "V<sub>o</sub>", c[0] + 62, 144)
    return svg(460, 316, out)
