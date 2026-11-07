"""Convert the original photos from the old UENI site into web-optimised WebP files.

Run:  python3 build/images.py <folder-with-original-images>
Output goes to public/img/. Each photo gets 3 widths (480, 960, 1600) for responsive loading.
"""
import sys, os
from PIL import Image, ImageOps

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'img')
os.makedirs(OUT, exist_ok=True)

# original file -> SEO-friendly name
PHOTOS = {
    '189b2516-44df-46dd-9f52-dc734ef703b7.jpg': 'drainage-team-lifting-manhole-cover-tanker',
    '290c8d60-d4dc-461f-903a-b776c6e5acf9.jpg': 'drain-jetting-machine-blocked-drain-patio',
    '01d0055ba4664d668f6f776bc3728d3a.jpg': 'jetting-hose-in-inspection-chamber',
    '322cf72e-5a76-4d70-8ad1-b951901eadf8.jpg': 'drain-cleaning-jetter-garden-manhole',
    '56947d232e264cbdb6125162dd82be7d.jpg': 'high-pressure-jetter-on-driveway',
    'c023885ab457468dabb4d56cea958203.jpg': 'open-sewer-chamber-before-clearing',
    '39580a07-2aab-4f71-bc9f-d77cfc7cdaca.jpg': 'cctv-drain-survey-monitor-at-manhole',
    '9a9c64e6-3b39-4f80-9435-7fc24ddf8b40.jpg': 'cctv-drain-camera-screen-pipe-view',
    'f471539b-196e-4277-a657-215fb91e8e07.jpg': 'cctv-drain-camera-reel-unit',
    '67bbaa89-4f75-4755-8178-7983c08c07eb.jpg': 'cctv-drain-camera-homebuyer-survey',
    '635157e9-9f92-4e6b-9694-59353cdf5cf9.jpg': 'no-dig-patch-liner-drain-repair',
    '5d2c3087-2cdb-4f04-adfc-545f56d38236.jpg': 'excavated-drain-trench-repair',
    '9a355ab0b1b3432a8abaaee518133059.jpg': 'drain-trench-cut-in-concrete',
    '71e28b8b-a180-44f5-8d81-845effc98c0a.jpg': 'leaking-pipe-joint-drain-repair',
    '3c918c74-2d20-40f4-8aac-3f9ffe27893d.jpg': 'laying-new-drainage-pipe-in-trench',
    '6bc5df7e-cb2e-4787-9409-c0d004890488.jpg': 'mini-digger-drainage-installation-garden',
    'af9bda2f22fe41ac89383f74c6c09168.jpg': 'new-drain-run-in-trench',
    'e30b39fe-7638-4ac6-a53b-1e09c1d41063.jpg': 'sewer-pipe-installation-trench',
    '00d96272-0fa7-4192-b17f-ce1dd0510bec.jpg': 'drainage-engineers-at-open-manhole',
    'c38ef00a-8b76-4161-809c-a1cb20c1989e.jpg': 'tanker-emptying-septic-tank',
    'a9f1f37c-eca8-4f45-ac28-6626b296a1e1.jpg': 'channel-drain-in-block-paving',
    '741c966a1cc04966b180437fadec3aa3.jpg': 'linear-channel-drain-grate',
    '5b24eb5a-404c-4b5c-8c87-5ebeb4a2d870.jpg': 'stormwater-outfall-pipes',
    '901bac6e04e2459fb7810518e5ffe7f1.jpg': 'pump-pipework-pressure-testing',
    'd8291fa4e22f4baf8b4b277c37e9e7ec.jpg': 'soil-pipe-connection-repair',
    'a76651ec-7dff-452c-a9da-3ba44c9cffa9.jpg': 'inspection-chamber-drain-clearing',
    '6f0002b6-17a1-4ef9-a519-e1c7ba40328d.jpg': 'soakaway-drainage-pipe-installation',
    '9da67214-b479-44c1-8737-fbf0ce9a0840.jpg': 'digging-out-damaged-drain-pipe',
    '18f8e76c-6ad4-484d-a008-ac4725717e6e.jpg': 'drainage-engineer-arriving-at-customer-home',
}
WIDTHS = [480, 960, 1600]

for src, name in PHOTOS.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src))).convert('RGB')
    w, h = im.size
    for tw in WIDTHS:
        if tw > w and tw != WIDTHS[0]:
            continue
        r = im if tw >= w else im.resize((tw, round(h * tw / w)), Image.LANCZOS)
        r.save(os.path.join(OUT, f'{name}-{tw}.webp'), 'WEBP', quality=72, method=6)
    # Open Graph / social share copy (JPEG, 1200 wide)
    if name == 'drainage-team-lifting-manhole-cover-tanker':
        og = im.resize((1200, round(h * 1200 / w)), Image.LANCZOS)
        og.save(os.path.join(OUT, 'og-elite-drainage-services.jpg'), 'JPEG', quality=80, optimize=True)
    print(name, im.size)

# Logo: trimmed, transparent
logo = Image.open(os.path.join(SRC, '2e8a61ecfb424ddd9121cd89cfd9c929.png')).convert('RGBA')
logo = logo.crop(logo.getbbox())
for h in (96, 192):
    lw = round(logo.width * h / logo.height)
    logo.resize((lw, h), Image.LANCZOS).save(os.path.join(OUT, f'elite-drainage-services-logo-{h}.webp'), 'WEBP', quality=90)
logo.resize((round(logo.width * 512 / logo.height), 512), Image.LANCZOS).save(os.path.join(OUT, 'elite-drainage-services-logo.png'), optimize=True)
# Favicon: square crop of the water-drop shield (top part of logo)
top = logo.crop((0, 0, logo.width, int(logo.height * 0.58)))
side = max(top.size)
sq = Image.new('RGBA', (side, side), (0, 0, 0, 0))
sq.paste(top, ((side - top.width) // 2, (side - top.height) // 2))
sq = sq.crop(sq.getbbox())
side = max(sq.size); sq2 = Image.new('RGBA', (side, side), (0, 0, 0, 0)); sq2.paste(sq, ((side - sq.width)//2, (side - sq.height)//2))
sq2.resize((180, 180), Image.LANCZOS).save(os.path.join(OUT, '..', 'apple-touch-icon.png'))
sq2.resize((32, 32), Image.LANCZOS).save(os.path.join(OUT, '..', 'favicon-32.png'))
sq2.save(os.path.join(OUT, '..', 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
print('logo', logo.size)
