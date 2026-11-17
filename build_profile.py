"""Build banner_{dark,light}.svg and toolkit_{dark,light}.svg.
Run: python3 -I build_profile.py   (needs Pillow not required). Edit TOOLKIT / TIMELINE below."""
from PIL import Image, ImageOps
from html import escape

W, H = 1000, 440
PITCH = 5            # halftone grid in px
CROP = (60, 0, 300, 300)
ARCH = dict(x=60, y=40, w=320, h=360)

THEMES = {
    "dark":  dict(bg="#0d1117", grid="#58a6ff", grid_o=".07", ink="#e6edf3", dim="#8b949e", accent="#d4a85f", dot="#e6edf3", line="#30363d"),
    "light": dict(bg="#fbfaf7", grid="#1f4e8c", grid_o=".07", ink="#1b1f24", dim="#6a7380", accent="#9a6b1c", dot="#1b1f24", line="#d6d2c8"),
}
SERIF = "Georgia,'Times New Roman',serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

TIMELINE = [("2018", "B.Tech, Civil Engineering"), ("2023", "Masters, Public Admin."), ("2025", "Full-stack products")]
TOOLKIT = [
    ("LANGUAGES", ["TypeScript", "JavaScript", "Java", "Python", "SQL"]),
    ("FRONTEND", ["React", "Next.js", "Vite", "Tailwind", "Redux Toolkit", "TanStack Query"]),
    ("MOBILE", ["React Native", "Expo"]),
    ("BACKEND", ["Node.js", "Express", "NestJS", "Spring Boot", "JWT"]),
    ("DATA", ["MongoDB", "PostgreSQL", "MySQL", "Prisma"]),
    ("PAYMENTS", ["Razorpay", "Stripe", "UPI"]),
    ("SHIP", ["Git", "Docker", "Vercel", "AWS", "CI/CD"]),
]


def hero(name):
    c = THEMES[name]
    HH, x0, y0 = 300, 60, 200
    tl = []
    for i, (yr, label) in enumerate(TIMELINE):
        cx = x0 + 8 + i * 250
        d = 1.2 + i * .3
        tl.append(f'<circle cx="{cx}" cy="{y0}" r="5" fill="{c["bg"]}" stroke="{c["accent"]}" stroke-width="1.6" class="fade" style="animation-delay:{d}s"/>'
                  f'<text x="{cx - 5}" y="{y0 + 26}" font-family="{MONO}" font-size="12" fill="{c["accent"]}" class="fade" style="animation-delay:{d}s">{yr}</text>'
                  f'<text x="{cx - 5}" y="{y0 + 46}" font-family="{SERIF}" font-size="14" fill="{c["dim"]}" class="fade" style="animation-delay:{d + .1}s">{escape(label)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{HH}" viewBox="0 0 {W} {HH}" role="img" aria-label="Ishan Tripathi, full-stack developer in Lucknow. Software, built like structures.">
<style>
.fade{{opacity:0;animation:f .9s ease forwards}}
.draw{{stroke-dasharray:1200;stroke-dashoffset:1200;animation:d 2.2s ease forwards}}
@keyframes f{{to{{opacity:1}}}}
@keyframes d{{to{{stroke-dashoffset:0}}}}
@media (prefers-reduced-motion:reduce){{.fade{{opacity:1;animation:none}}.draw{{stroke-dashoffset:0;animation:none}}}}
</style>
<rect width="{W}" height="{HH}" rx="14" fill="{c["bg"]}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{HH - 1}" rx="14" fill="none" stroke="{c["line"]}"/>
<text x="60" y="62" font-family="{MONO}" font-size="12" letter-spacing="4" fill="{c["accent"]}" class="fade" style="animation-delay:.2s">FULL-STACK DEVELOPER · LUCKNOW</text>
<text x="58" y="124" font-family="{SERIF}" font-size="64" fill="{c["ink"]}" class="fade" style="animation-delay:.4s">Ishan Tripathi</text>
<text x="60" y="160" font-family="{SERIF}" font-size="21" font-style="italic" fill="{c["dim"]}" class="fade" style="animation-delay:.7s">Software, built like structures: load-bearing, tested, made to last.</text>
<path d="M68 {y0}H{x0 + 8 + 2 * 250}" stroke="{c["line"]}" stroke-width="1.5" class="draw" style="animation-delay:1s"/>
{"".join(tl)}
</svg>'''


def toolkit(name):
    c = THEMES[name]
    rows, y = [], 34
    for label, items in TOOLKIT:
        x = 170
        rows.append(f'<text x="30" y="{y + 4}" font-family="{MONO}" font-size="11" letter-spacing="3" fill="{c["accent"]}">{label}</text>')
        for it in items:
            w = 14 + len(it) * 7.4
            rows.append(f'<rect x="{x:.0f}" y="{y - 14}" width="{w:.0f}" height="26" rx="13" fill="none" stroke="{c["line"]}"/>'
                        f'<text x="{x + w / 2:.0f}" y="{y + 4}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{c["ink"]}">{escape(it)}</text>')
            x += w + 10
        y += 44
    h = y - 8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="Toolkit: {escape(", ".join(i for _, l in TOOLKIT for i in l))}">'
            f'<rect width="{W}" height="{h}" rx="14" fill="{c["bg"]}"/><rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="14" fill="none" stroke="{c["line"]}"/>'
            + "".join(rows) + "</svg>")


if __name__ == "__main__":
    for n in THEMES:
        open(f"banner_{n}.svg", "w").write(hero(n))
        open(f"toolkit_{n}.svg", "w").write(toolkit(n))
    print("ok")
