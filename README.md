# Elite Drainage Services website (elitedrainage.uk)

A rebuild of elitedrainage.uk, replacing the UENI site. It keeps the original wording and photos and fixes the problems listed in the SEO audit.

- **`public/`** is the finished website. This folder is what goes online.
- **`build/`** holds the content and the script that generates `public/`.
- **`DEPLOY.md`** has step-by-step instructions for putting the site live.

## What changed compared with the old site

| Audit finding | What the new site does |
|---|---|
| The same title tag on every page | Every page has its own title and description, with the service and town in them |
| Services, About and Contact had no H1 | Every page has exactly one H1. The home page H1 is "Blocked Drains and Drainage Services in Waterlooville" and the slogan sits underneath it |
| Phone number not visible as text | The number is in the header, the top bar, the footer, every page banner and a call bar fixed to the bottom of the screen on phones |
| Two different phone numbers | One number everywhere: 0330 633 0336 (see "Things you need to confirm") |
| No structured data (schema) | LocalBusiness markup on every page, plus Service, FAQ, Breadcrumb and BlogPosting markup |
| Pinch-to-zoom disabled on mobile | Zoom works |
| Thin service pages (about 110 words) | Each service page now has roughly 400 to 700 words: the original text, warning signs, how the job is done, areas covered, FAQs and photos |
| No area pages | New "Areas we cover" page with a section for each town and its postcodes |
| Leftover "Custom code - 4" heading | Removed |
| Service links pointing to ueniweb.com | Every link points to elitedrainage.uk |
| No homebuyer survey page | New page for the £299 homebuyer drain survey |
| No privacy policy for the contact form | A privacy policy has been added |
| Old page addresses | Every old UENI address permanently redirects (301) to its new page, so existing Google listings and links still work |

Other improvements:
- Pages load fast: plain HTML with no page builder, compressed WebP images in three sizes, and no tracking scripts.
- The photos have descriptive file names and alt text.
- The contact form works through Netlify and emails each enquiry to you.
- There is a sitemap (`sitemap.xml`) and a `robots.txt` for Google.

## Things you need to confirm or supply

These could not be checked from the old site. Each one affects either rankings or trust.

1. **Phone number.** The Call Now buttons on the old site used **0330 633 0336**. The old About page text said **0330 633 6033**. The new site uses 0330 633 0336. If that is wrong, change it in `build/business.py`.
2. **24/7.** The site says you are available 24/7, as the old site did. Only keep this if you really answer the phone at night. To change it, edit `hours_text` and `open_24_7` in `build/business.py`.
3. **Areas.** The site lists Waterlooville, Cowplain, Purbrook, Denmead, Horndean, Havant and Portsmouth. Remove any you don't cover. The old site also mentioned Reading. I left Reading out because it is about 60 miles away and dilutes your local relevance. Add it back if you work there regularly.
4. **Senior discount.** The audit flagged that this had no terms. It now says "Ask for details when you call". Add the actual discount (for example "10% for over-65s") if you have one.
5. **Business name.** The logo says "Elite Drainage Services Ltd", the site says "Elite Drainage Services" and MyJobQuote says "Elite Drainage Services Limited". Pick one and use it on Google, directories and invoices. If you are a registered limited company, add the company number to the Legal page.
6. **Address.** The site shows the town only. If you are happy to show a street address, add it in `build/business.py`.
7. **Names and accreditations.** Add the two founders' names, any trade memberships and your insurance details to the About page. This helps both trust and Google.
8. **Reviews.** The site shows no reviews because none could be checked. Once you have Google reviews, add a few with the customer's first name and area.
9. **Photos.** A few of the reused photos look like stock images (for example the engineer at a front door, the burst pipe and the trench at sunset). Replace them with your own job photos when you can, because real photos rank and convert better.
10. **Email.** The site uses the Gmail address from the old site. An address on your own domain (for example info@elitedrainage.uk) looks more established.

## How to change text and rebuild

You only need this if you are editing the site yourself or asking someone to do it.

1. Business details, areas and phone number are in `build/business.py`.
2. Service page text is in `build/services.py`.
3. Home, About, Contact and the other pages are in `build/build.py`.
4. To rebuild the site after a change, run this from the project folder:
   ```
   python3 build/build.py
   ```
5. Commit and push the changes. Netlify publishes them automatically within about a minute.

The original photos are converted with `python3 build/images.py <folder-of-originals>`. You only need to run this again when you add new photos.
