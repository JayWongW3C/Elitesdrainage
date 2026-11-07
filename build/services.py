"""Service page content.

Each service has:
  intro     – the wording from the old site (kept), lightly edited
  sections  – extra content added for SEO (what the problem looks like, how it is fixed)
  faqs      – questions and answers (also sent to Google as FAQ structured data)
  images    – photo names from public/img (without the -480/-960 size ending)

Text is plain HTML. Keep claims factual: only promise what you actually do.
"""

SERVICES = [
    # ------------------------------------------------------------------ BLOCKED DRAINS
    {
        "slug": "blocked-drain-clearing",
        "group": "Drain Maintenance",
        "name": "Blocked Drain Clearing",
        "card": "Grease, wipes, roots and debris cleared fast with rods and high-pressure jetting, day or night.",
        "title": "Blocked Drains Waterlooville | 24/7 Drain Unblocking",
        "meta": "Blocked drain in Waterlooville, Havant or Portsmouth? Elite Drainage Services clears sinks, toilets, gullies and main drains 24/7. Free estimates. Call 0330 633 0336.",
        "h1": "Blocked Drain Clearing in Waterlooville",
        "images": ["drain-jetting-machine-blocked-drain-patio", "jetting-hose-in-inspection-chamber", "open-sewer-chamber-before-clearing"],
        "old": ["/services/drain-maintenance/blocked-drain-clearing-150626624"],
        "intro": [
            "Imagine coming home after a long day only to be greeted by a flooded kitchen. It is a nightmare scenario, but one Elite Drainage Services is equipped to handle swiftly. Our blocked drain clearing service is the first line of defence against unexpected water issues. From minor grease build-up to entrenched debris, we use proven methods and modern equipment to restore proper flow efficiently.",
            "Our team is available 24/7 to respond to emergencies, so your home or business returns to normal with minimal disruption.",
        ],
        "sections": [
            ("Signs your drain is blocked", """
<ul class="ticks">
<li>Sinks, showers or baths draining slowly or not at all</li>
<li>Toilets filling up higher than normal when flushed, or not clearing</li>
<li>Gurgling noises from plugholes or the toilet</li>
<li>Bad smells from drains, gullies or manhole covers</li>
<li>Water pooling around an outside gully or a manhole cover lifting</li>
</ul>
<p>If more than one fitting in the house is affected, the blockage is usually further down the main drain rather than in a single pipe. That is a job for drain rods or a jetter, not a plunger.</p>"""),
            ("How we clear a blocked drain", """
<ol class="steps">
<li><strong>Find the blockage.</strong> We lift the inspection chambers to see where the water stops flowing, so we work on the right section first time.</li>
<li><strong>Clear it.</strong> Depending on the cause we use drain rods or high-pressure water jetting, which cuts through grease, scale, wet wipes and silt and flushes the pipe clean.</li>
<li><strong>Check it.</strong> We run water through to confirm everything flows. If a drain keeps blocking, we recommend a <a href="/services/cctv-drain-inspection/">CCTV drain survey</a> to find out why, such as a cracked pipe, root ingress or a sunken section.</li>
<li><strong>Leave it clean.</strong> We tidy the work area and explain what caused the blockage and how to stop it happening again.</li>
</ol>"""),
            ("What causes most blockages", """
<p>Most blocked drains are caused by fat, oil and grease poured down the kitchen sink, wet wipes and sanitary products flushed down the toilet, and tree roots getting into older clay pipes through cracked joints. Leaves and silt also build up in outside gullies, especially after autumn and heavy rain.</p>
<p>A blockage inside your property boundary that only serves your home is usually your responsibility. If the blocked pipe is shared with neighbours or is beyond your boundary, it is usually the responsibility of the water company (Southern Water in most of this area). We can tell you which applies when we inspect it.</p>"""),
        ],
        "faqs": [
            ("Do you offer an emergency blocked drain service?", "Yes. We provide round-the-clock cover for emergency drainage problems, day or night. Call 0330 633 0336 and tell us what is happening."),
            ("How much does it cost to unblock a drain?", "It depends on where the blockage is and what is causing it. We give a free, upfront estimate before starting, so you know the price before any work begins."),
            ("Can you stop my drain blocking again?", "If a drain blocks repeatedly there is usually an underlying cause, such as a damaged or sunken pipe or root ingress. A CCTV survey shows the cause so it can be repaired rather than just cleared."),
            ("Do you clear blocked toilets, sinks and outside gullies?", "Yes. We clear blockages in toilets, sinks, showers, baths, outside gullies, inspection chambers and main drain runs for homes and businesses."),
        ],
    },
    # ------------------------------------------------------------------ DRAIN REPAIR
    {
        "slug": "drain-repair",
        "group": "Drain Maintenance",
        "name": "Drain Repair",
        "card": "Cracked, leaking or collapsed drains fixed with no-dig relining, patch repairs or excavation.",
        "title": "Drain Repair Waterlooville | No-Dig Relining & Patch Repairs",
        "meta": "Cracked, leaking or collapsed drain? Elite Drainage Services repairs drains in Waterlooville and Hampshire with no-dig relining, patch repairs or excavation. Free estimates.",
        "h1": "Drain Repair in Waterlooville and Hampshire",
        "images": ["no-dig-patch-liner-drain-repair", "excavated-drain-trench-repair", "digging-out-damaged-drain-pipe"],
        "old": ["/services/drain-maintenance/drain-repair-150626638"],
        "intro": [
            "A crack or leak in a drainage system can quickly escalate from a nuisance to serious property damage if left unresolved. Elite Drainage Services provides comprehensive drain repair solutions that address current problems while strengthening the overall integrity of the system.",
            "Our expertise ranges from non-intrusive pipe relining to complete drain replacement, all carried out with precision and care. Minor leaks are assessed thoroughly to prevent future failures, ensuring long-term drainage performance.",
        ],
        "sections": [
            ("Signs a drain needs repairing", """
<ul class="ticks">
<li>Drains that keep blocking even after being cleared</li>
<li>Damp patches on walls or floors near drain runs</li>
<li>Sunken paving, subsidence or a dip in the lawn above a drain</li>
<li>Persistent sewage smells outside the property</li>
<li>Rats or other pests around the property (they can enter through broken drains)</li>
</ul>"""),
            ("Our drain repair methods", """
<p>We start with a <a href="/services/cctv-drain-inspection/">CCTV drain survey</a> so the repair is based on what is actually wrong, not guesswork. Then we recommend the least disruptive fix that will last.</p>
<h3>Patch repairs (no dig)</h3>
<p>For a single crack, open joint or small hole, a resin-soaked liner is pushed into position on an inflatable packer and pressed against the pipe wall. Once the resin cures it forms a sealed, structural repair. This is often completed in a few hours with no digging.</p>
<h3>CiPP relining (no dig)</h3>
<p>Where a longer section of pipe is cracked or has root ingress, a cured-in-place pipe (CiPP) liner creates a new seamless pipe inside the old one. Driveways, patios and gardens stay intact.</p>
<h3>Excavation and replacement</h3>
<p>If a pipe has collapsed or is badly misaligned, the damaged section needs to be dug out and replaced. We keep the excavation as small as possible and reinstate the area afterwards.</p>
<p>Read more in our article on <a href="/blog/no-dig-drain-repairs-faster-fixes-with-less-disruption/">no-dig drain repairs</a>.</p>"""),
            ("Is a drain repair covered by insurance?", """
<p>Many home insurance policies cover accidental damage to underground pipes. Insurers usually ask for evidence, such as CCTV footage and a written report showing the damage. Our survey reports give you that evidence. Check your policy wording or call your insurer before work starts.</p>"""),
        ],
        "faqs": [
            ("Do you need to dig up my garden or driveway to repair a drain?", "Not always. Many cracks, open joints and root problems can be repaired from inside the pipe using patch repairs or CiPP relining, with no digging. Excavation is only needed where a pipe has collapsed or is badly displaced."),
            ("How long does a no-dig drain repair last?", "A correctly installed liner or patch repair forms a structural, sealed pipe that is designed to last for many years. We will explain the expected lifespan for your specific repair."),
            ("Will you show me the damage before repairing it?", "Yes. We use CCTV to inspect the pipe first, so you can see the problem and we can agree the right repair and price with you before starting."),
        ],
    },
    # ------------------------------------------------------------------ CCTV
    {
        "slug": "cctv-drain-inspection",
        "group": "Drainage Solutions",
        "name": "CCTV Drain Inspection & Maintenance",
        "short": "CCTV Drain Inspection",
        "card": "High-definition CCTV drain surveys with written reports, plus planned maintenance to prevent blockages.",
        "title": "CCTV Drain Survey Waterlooville | Inspection & Reports",
        "meta": "CCTV drain surveys in Waterlooville, Havant and Portsmouth. Full HD camera inspection, written condition report and maintenance plans. Call Elite Drainage Services.",
        "h1": "CCTV Drain Inspection and Maintenance",
        "images": ["cctv-drain-survey-monitor-at-manhole", "cctv-drain-camera-screen-pipe-view", "cctv-drain-camera-reel-unit"],
        "old": ["/services/drainage-solutions/drain-inspection-and-maintenance-150626637"],
        "intro": [
            "Drainage issues do not need to come as a surprise. Our drain inspection and maintenance services help turn drainage performance into something predictable and manageable. With detailed CCTV drain surveys, we provide a clear internal view of your drains without invasive digging.",
            "Preventative maintenance plans help stop blockages before they develop, saving time, stress and unnecessary costs. Comprehensive assessments and written reports keep you informed about the condition of your drainage system, highlighting potential issues and clear next steps.",
        ],
        "sections": [
            ("How a CCTV drain survey works", """
<p>A waterproof camera on a flexible push rod is fed into the drain through an inspection chamber. Live high-resolution footage is shown on a monitor, and the distance travelled is recorded, so any fault can be located precisely from above ground.</p>
<p>The survey shows problems that cannot be seen any other way, including:</p>
<ul class="ticks">
<li>Cracks, fractures and holes</li>
<li>Root ingress through joints</li>
<li>Displaced or open joints</li>
<li>Sunken sections (dips that hold water and debris)</li>
<li>Build-up of scale, grease or silt</li>
<li>Collapsed pipes</li>
</ul>"""),
            ("When you need a CCTV drain survey", """
<ul class="ticks">
<li><strong>Buying a home.</strong> See our <a href="/services/homebuyer-drain-survey/">homebuyer drain survey</a> for £299.</li>
<li><strong>Recurring blockages</strong>, to find the cause instead of clearing the same drain again and again.</li>
<li><strong>Insurance claims</strong>, where your insurer needs evidence of damage.</li>
<li><strong>Before an extension or building work</strong>, to confirm where drains run and their condition.</li>
<li><strong>Commercial properties</strong>, as part of a planned maintenance schedule to avoid downtime.</li>
</ul>"""),
            ("What you receive", """
<p>After the survey you get a written condition report with still images from the footage, the location and depth of any defects, and our recommendations for repair or maintenance. The report is yours to keep and can be shared with your insurer, solicitor, landlord or builder.</p>
<p>Find out more in our article on <a href="/blog/how-cctv-drain-inspections-prevent-costly-repairs/">how CCTV drain inspections prevent costly repairs</a>.</p>"""),
        ],
        "faqs": [
            ("How long does a CCTV drain survey take?", "Most surveys of a standard house take one to two hours on site, depending on the length of the drain runs and how many inspection chambers there are."),
            ("Do I need to be at home for the survey?", "We need access to the inspection chambers (manholes) and usually to the inside of the property to run water through the fittings, so someone should be available to let us in."),
            ("Can you do planned drain maintenance for my business?", "Yes. We offer preventative maintenance, including scheduled CCTV inspections and cleaning, to help keep commercial drainage running without unexpected shutdowns."),
        ],
    },
    # ------------------------------------------------------------------ HOMEBUYER
    {
        "slug": "homebuyer-drain-survey",
        "group": "Drainage Solutions",
        "name": "Homebuyer Drain Survey",
        "card": "A full HD CCTV survey of the drains before you buy, for £299. Avoid expensive surprises after you move in.",
        "title": "Homebuyer Drain Survey £299 | Pre-Purchase CCTV Survey Hampshire",
        "meta": "Buying a house in Waterlooville, Havant or Portsmouth? Our £299 homebuyer CCTV drain survey checks the whole drainage system before you commit. Call 0330 633 0336.",
        "h1": "Homebuyer Drain Survey: £299",
        "images": ["cctv-drain-camera-homebuyer-survey", "cctv-drain-camera-screen-pipe-view"],
        "old": [],
        "intro": [
            "Are you moving home? Do not take the risk of investing in your biggest life purchase without inspecting under the ground. Who knows what surprises you will find once you move in. For just £299 you could save yourself thousands of pounds and hours of distress.",
            "We use top-of-the-range full HD inspection cameras and many years of knowledge to inspect and survey the whole drainage system. Call us for total peace of mind when buying your new home.",
        ],
        "sections": [
            ("Why a standard house survey is not enough", """
<p>A RICS HomeBuyer Report or building survey looks at the parts of a property that can be seen. Surveyors generally lift manhole covers at most; they do not put a camera inside the drains. Damaged drains can be expensive to repair, and once you have completed the purchase the cost is yours.</p>
<p>A drain survey before exchange of contracts gives you the facts while you can still act on them.</p>"""),
            ("What the survey includes", """
<ul class="ticks">
<li>Full HD CCTV inspection of the accessible drain runs</li>
<li>Check of inspection chambers, gullies and connections</li>
<li>Location of any defects such as cracks, roots, displaced joints or collapses</li>
<li>Written report with images and our recommendations</li>
<li>An estimate for any repairs needed</li>
</ul>"""),
            ("How the report helps you", """
<p>If the survey finds a problem you can ask the seller to repair it before completion, negotiate a reduction in the price to cover the work, or decide not to proceed. If the drains are in good condition, you can buy with confidence.</p>"""),
        ],
        "faqs": [
            ("How much is a homebuyer drain survey?", "Our homebuyer drain survey costs £299."),
            ("When should I book the survey?", "After your offer has been accepted and before you exchange contracts, so there is still time to negotiate or ask the seller to fix any problems. You will need the seller's or estate agent's permission to access the property."),
            ("Do you cover properties outside Waterlooville?", "Yes. We carry out homebuyer drain surveys across Waterlooville, Havant, Portsmouth and the surrounding areas. See our areas page or call to check."),
        ],
    },
    # ------------------------------------------------------------------ DRAIN CLEANING
    {
        "slug": "drain-cleaning",
        "group": "Drainage Solutions",
        "name": "Drain Cleaning",
        "card": "High-pressure jetting, root cutting and pipe descaling to restore full flow and extend pipe life.",
        "title": "Drain Cleaning & Jetting Waterlooville | Root Removal",
        "meta": "Professional drain cleaning in Waterlooville and Hampshire. High-pressure water jetting, root removal and pipe descaling for homes and businesses. Free estimates.",
        "h1": "Drain Cleaning and High-Pressure Jetting",
        "images": ["drain-cleaning-jetter-garden-manhole", "high-pressure-jetter-on-driveway", "inspection-chamber-drain-clearing"],
        "old": ["/services/drainage-solutions/drain-cleaning-150626636"],
        "intro": [
            "Say goodbye to persistent clogs and slow drains with our professional drain cleaning services. Elite Drainage Services uses powerful high-pressure cleaning techniques to tackle even the toughest build-up, including invasive tree roots and stubborn grease deposits.",
            "Our hydro jetting and root removal solutions ensure every part of your drainage system is thoroughly cleared, supporting long-lasting performance. Where mineral build-up and corrosion restrict water flow, our pipe descaling service helps extend pipe lifespan significantly.",
        ],
        "sections": [
            ("Our drain cleaning services", """
<h3>High-pressure water jetting</h3>
<p>A jetting nozzle fires water at high pressure through the pipe, scouring grease, silt, scale and debris from the pipe walls and flushing it away. It restores the full bore of the pipe rather than just making a hole through the blockage.</p>
<h3>Root cutting and removal</h3>
<p>Tree roots get into drains through small cracks and joints and grow into dense masses that trap waste. We cut them out with specialist cutting heads, then recommend a repair to seal the entry point so they do not grow back.</p>
<h3>Descaling</h3>
<p>Hard water and old cast-iron pipes can build up scale and corrosion that narrows the pipe. Descaling removes this build-up and restores flow.</p>"""),
            ("Who we clean drains for", """
<p>We clean drains for homeowners, landlords, letting agents, restaurants and takeaways (where grease build-up is common), schools, offices and commercial premises across Waterlooville and the surrounding area.</p>"""),
        ],
        "faqs": [
            ("How often should drains be cleaned?", "Most household drains only need attention when there is a problem. Commercial kitchens and properties with large trees nearby benefit from cleaning on a regular schedule. We can advise on the right interval after an inspection."),
            ("Is high-pressure jetting safe for old pipes?", "Yes, when done by a trained operator. We adjust the pressure and nozzle for the type and condition of the pipe. If a pipe is badly damaged, we will tell you before jetting."),
            ("Do you remove tree roots from drains?", "Yes. We cut roots out of drains using root-cutting heads and can then reline or patch the pipe to stop them coming back."),
        ],
    },
    # ------------------------------------------------------------------ INSTALLATION
    {
        "slug": "drainage-installation",
        "group": "Drainage Solutions",
        "name": "Drainage Installation",
        "card": "New drain runs, sewer connections, soakaways and French drains, designed for your site.",
        "title": "Drainage Installation Waterlooville | New Drains & French Drains",
        "meta": "New drainage installation in Waterlooville and Hampshire: drain runs, sewer pipes, soakaways and French drains for homes, extensions and businesses. Free estimates.",
        "h1": "Drainage Installation in Waterlooville",
        "images": ["laying-new-drainage-pipe-in-trench", "mini-digger-drainage-installation-garden", "new-drain-run-in-trench"],
        "old": ["/services/drainage-solutions/drainage-installation-150626639"],
        "intro": [
            "Make sure your property is prepared for all weather conditions with our professional drainage installation services. Whether installing new sewer pipes or designing stormwater drainage systems to reduce flooding risk, each solution is tailored to the specific site.",
            "We combine extensive experience with modern methods to protect your property effectively. French drain installations can also improve the health of your garden by directing water away from vulnerable areas. Well-designed drainage systems provide long-term protection.",
        ],
        "sections": [
            ("What we install", """
<ul class="ticks">
<li>New foul drain runs and connections for extensions, kitchens and bathrooms</li>
<li>Replacement drain runs where old pipework has failed</li>
<li>Inspection chambers and access points</li>
<li>French drains to clear waterlogged gardens and protect foundations</li>
<li>Soakaways and surface water drainage</li>
<li>Channel drains for driveways and patios</li>
</ul>"""),
            ("How an installation project runs", """
<ol class="steps">
<li><strong>Site visit.</strong> We look at the ground, levels and existing drains, and survey with CCTV where needed.</li>
<li><strong>Quote.</strong> You get a clear written price with no hidden costs.</li>
<li><strong>Installation.</strong> We excavate, lay pipework to the correct fall, bed and backfill it properly, and test it.</li>
<li><strong>Making good.</strong> We reinstate the ground and leave the site tidy.</li>
</ol>
<p>Building work that involves new drains usually needs Building Regulations approval, and connecting to or building over a public sewer needs the water company's agreement. We can explain what applies to your project.</p>"""),
        ],
        "faqs": [
            ("Do I need permission to install a new drain?", "New drainage that forms part of building work usually needs Building Regulations approval from your local council or an approved inspector. A new connection to a public sewer needs approval from the water company. We can advise on your project."),
            ("What is a French drain?", "A French drain is a trench filled with gravel around a perforated pipe. It collects groundwater and surface water and carries it away from areas that flood or stay waterlogged, such as lawns or the base of walls."),
            ("Can you install drainage for a new extension?", "Yes. We install new drain runs and connections for extensions, garden rooms, kitchens and bathrooms."),
        ],
    },
    # ------------------------------------------------------------------ SEWER
    {
        "slug": "sewer-line-services",
        "group": "Drainage Solutions",
        "name": "Sewer Line Services",
        "card": "Inspection, cleaning, repair and replacement of sewer pipes, including emergency call-outs.",
        "title": "Sewer Line Services Hampshire | Sewer Repair & Cleaning",
        "meta": "Sewer pipe inspection, cleaning, repair and replacement in Waterlooville, Havant and Portsmouth. Emergency and planned work by Elite Drainage Services.",
        "h1": "Sewer Line Services",
        "images": ["drainage-engineers-at-open-manhole", "open-sewer-chamber-before-clearing", "sewer-pipe-installation-trench"],
        "old": ["/services/drainage-solutions/sewer-line-services-150626640"],
        "intro": [
            "Managing sewer line issues can feel complex, but with Elite Drainage Services it does not have to be. Our sewer line services include detailed inspections using advanced video technology and thorough cleaning to remove stubborn blockages.",
            "Persistent odours or ageing sewer lines are addressed through targeted treatments or full replacements where required. Whether responding to an emergency repair or planning preventative upgrades, our solutions prioritise safety, comfort and long-term reliability.",
        ],
        "sections": [
            ("Common sewer line problems", """
<ul class="ticks">
<li>Sewage backing up into toilets, baths or the garden</li>
<li>Strong sewage smells inside or outside the property</li>
<li>Gurgling from several fittings at once</li>
<li>Wet, sunken patches of ground above the sewer line</li>
</ul>
<p>These usually mean the main pipe taking waste from the property is blocked, broken or partly collapsed. Sewage backing up is a health risk and should be dealt with straight away.</p>"""),
            ("Who is responsible for the sewer?", """
<p>In England, the pipe that carries waste from your property alone and sits within your boundary is normally your responsibility. Since 2011, pipes shared with neighbours or that run beyond your boundary are normally the responsibility of the local water company (Southern Water in most of this area). After a CCTV inspection we can tell you which section is affected, so you know who should pay for the work.</p>"""),
        ],
        "faqs": [
            ("What should I do if sewage is coming back up?", "Stop using water in the property (taps, toilets, washing machine), keep children and pets away from the affected area, and call us on 0330 633 0336."),
            ("Can a sewer pipe be repaired without digging?", "Often, yes. Many sewer defects can be repaired from inside using relining or patch repairs. Collapsed sections usually need excavating and replacing."),
        ],
    },
    # ------------------------------------------------------------------ STORMWATER
    {
        "slug": "stormwater-drainage",
        "group": "Drainage Solutions",
        "name": "Stormwater Drainage Solutions",
        "short": "Stormwater Drainage",
        "card": "Surface water management, channel drains, soakaways and gully maintenance to stop flooding.",
        "title": "Stormwater & Surface Water Drainage Waterlooville",
        "meta": "Stop flooding and standing water. Stormwater drainage design, installation, repair and maintenance in Waterlooville and Hampshire: channel drains, soakaways and gullies.",
        "h1": "Stormwater Drainage Solutions",
        "images": ["channel-drain-in-block-paving", "linear-channel-drain-grate", "stormwater-outfall-pipes"],
        "old": ["/services/drainage-solutions/stormwater-drainage-solutions-150626641"],
        "intro": [
            "Protect your property from excess water with our comprehensive stormwater drainage solutions. Elite Drainage Services provides expert maintenance, repair and surface water management to keep stormwater systems operating effectively throughout the year.",
            "Our assessments identify how runoff, pooling and erosion can be reduced, helping to protect both buildings and surrounding environments. From new installations to maintaining existing systems, proactive stormwater management is key to safeguarding your property against severe weather.",
        ],
        "sections": [
            ("Signs your surface water drainage is not coping", """
<ul class="ticks">
<li>Puddles that stay on driveways, patios or car parks after rain</li>
<li>Water running towards doors, garages or air bricks</li>
<li>Overflowing gullies and downpipes</li>
<li>Waterlogged lawns or soil washing away</li>
</ul>"""),
            ("Our stormwater services", """
<ul class="ticks">
<li><strong>Channel drains</strong> across driveways, patios and thresholds</li>
<li><strong>Soakaways</strong> and crate systems, where ground conditions allow</li>
<li><strong>Gully and downpipe clearing</strong>, including leaves and silt</li>
<li><strong>Repair of surface water pipes</strong> found damaged on CCTV</li>
<li><strong>Planned maintenance</strong> for commercial sites and car parks</li>
</ul>
<p>Since 2008, a new or replacement driveway in a front garden over 5 square metres generally needs planning permission unless it uses permeable surfacing or drains to a lawn or border. Good drainage design keeps you within the rules.</p>"""),
        ],
        "faqs": [
            ("Why does my driveway flood when it rains?", "Usually because water has nowhere to go: the surface falls the wrong way, the existing gullies are blocked, or there is no drainage at all. A channel drain or soakaway, sized for the area, normally solves it."),
            ("Can surface water go into the foul sewer?", "In general new surface water should not be connected to the foul sewer. It should go to a soakaway, a surface water sewer or a watercourse, in that order of preference. We can advise on the right option for your property."),
        ],
    },
    # ------------------------------------------------------------------ SPECIALIST
    {
        "slug": "specialist-drainage-systems",
        "group": "Drainage Solutions",
        "name": "Specialist Drainage Systems",
        "card": "Septic tanks, sewage treatment plants, mains-connected systems, pump stations and no-dig technology.",
        "title": "Septic Tanks & Specialist Drainage Systems Hampshire",
        "meta": "Specialist drainage in Hampshire: septic tanks, sewage treatment plants, mains-connected systems, pump stations and no-dig repairs. Elite Drainage Services, Waterlooville.",
        "h1": "Specialist Drainage Systems",
        "images": ["tanker-emptying-septic-tank", "soakaway-drainage-pipe-installation", "drainage-team-lifting-manhole-cover-tanker"],
        "old": ["/services/drainage-solutions/specialist-drainage-systems-150626695"],
        "intro": [
            "Elite Drainage Services delivers specialist drainage solutions for complex and technical systems. We work with septic systems, sewage treatment plants and mains-connected systems, providing expert inspection, maintenance and repair.",
            "Our experience also includes pump station works, ensuring critical infrastructure operates reliably. Where excavation is not suitable, no-dig technology allows issues to be resolved with minimal disruption. These specialist services are ideal for properties that require advanced drainage expertise beyond standard solutions.",
        ],
        "sections": [
            ("Systems we work on", """
<ul class="ticks">
<li><a href="/services/sewage-treatment-plant-works/">Sewage treatment plants</a>: servicing, repairs and upgrades</li>
<li>Septic tanks and soakaways (drainage fields): inspection, repair and replacement</li>
<li><a href="/services/pump-station-works/">Pump stations</a>: maintenance, pump replacement and alarms</li>
<li>Mains-connected systems: inspection, repair and new connections</li>
<li><a href="/services/drain-repair/">No-dig repairs</a>: patch repairs and CiPP relining</li>
</ul>"""),
            ("Septic tank rules in England", """
<p>Under the Environment Agency's General Binding Rules, a septic tank must not discharge directly into a river, stream, ditch or other surface water. Since 1 January 2020, tanks that did so had to be replaced or upgraded, for example to a sewage treatment plant or by connecting to a drainage field. If you are buying or selling a property with a septic tank, the system should be checked against these rules.</p>
<p>If you are not sure whether your system complies, we can inspect it and explain your options.</p>"""),
        ],
        "faqs": [
            ("What is the difference between a septic tank and a sewage treatment plant?", "A septic tank separates solids from liquid and lets the liquid soak into the ground through a drainage field. A sewage treatment plant uses a powered process to treat the wastewater to a higher standard, so it can be discharged to a drainage field or, with the right permissions, to a watercourse."),
            ("Do you work on off-mains properties?", "Yes. We work on rural and off-mains properties with septic tanks, treatment plants and pumped systems around Waterlooville, Denmead and the wider area."),
        ],
    },
    # ------------------------------------------------------------------ PUMP STATION
    {
        "slug": "pump-station-works",
        "group": "Drain Maintenance",
        "name": "Pump Station Works",
        "card": "Inspection, servicing and repair of foul and surface water pump stations.",
        "title": "Pump Station Maintenance & Repair Hampshire",
        "meta": "Pump station servicing, maintenance and repair for foul and surface water systems in Waterlooville and Hampshire. Elite Drainage Services. Call 0330 633 0336.",
        "h1": "Pump Station Works",
        "images": ["pump-pipework-pressure-testing", "drainage-engineers-at-open-manhole"],
        "old": ["/services/drain-maintenance/pump-station-works-150632009"],
        "intro": [
            "Pump station works involve the inspection, maintenance and repair of systems that move wastewater or surface water from lower to higher levels to keep drainage networks operating correctly. These systems are essential where gravity drainage alone is not sufficient, and problems can lead to blockages, slow drainage or an increased risk of flooding.",
            "Regular servicing and timely repairs help ensure consistent performance and protect surrounding pipework and property infrastructure. If your system is showing signs of reduced performance or needs scheduled maintenance, get in touch.",
        ],
        "sections": [
            ("What a pump station service covers", """
<ul class="ticks">
<li>Check of pumps, float switches and level controls</li>
<li>Test of high-level alarms</li>
<li>Inspection of non-return valves and rising main connections</li>
<li>Removal of rag, fat and debris from the chamber</li>
<li>Jetting of the chamber and incoming pipework where needed</li>
<li>Report of condition and any parts that need replacing</li>
</ul>"""),
            ("Signs of a pump station problem", """
<ul class="ticks">
<li>The high-level alarm sounding</li>
<li>The pump running constantly or cycling on and off</li>
<li>Slow drainage or waste backing up</li>
<li>Unusual noise or smells from the chamber</li>
</ul>
<p>Wet wipes and sanitary products are a common cause of pump failure, because they wrap around the impeller. Only toilet paper should be flushed on a pumped system.</p>"""),
        ],
        "faqs": [
            ("How often should a pump station be serviced?", "Most manufacturers recommend at least one service a year for domestic pump stations, and more often for commercial or high-use systems. Check your manufacturer's guidance."),
            ("My pump station alarm is going off. What should I do?", "Reduce water use straight away to stop the chamber overflowing, check the pump has power, and call us on 0330 633 0336."),
        ],
    },
    # ------------------------------------------------------------------ STP
    {
        "slug": "sewage-treatment-plant-works",
        "group": "Drain Maintenance",
        "name": "Sewage Treatment Plant Works",
        "card": "Servicing, repair and optimisation of on-site sewage treatment plants.",
        "title": "Sewage Treatment Plant Servicing & Repair Hampshire",
        "meta": "Sewage treatment plant servicing, repairs and upgrades in Waterlooville, Denmead and Hampshire. Prevent odours, blockages and environmental problems. Call 0330 633 0336.",
        "h1": "Sewage Treatment Plant Works",
        "images": ["tanker-emptying-septic-tank", "soil-pipe-connection-repair"],
        "old": ["/services/drain-maintenance/sewage-treatment-plant-works-150632018"],
        "intro": [
            "Sewage treatment plant works focus on maintaining, repairing or optimising on-site treatment systems so wastewater is processed effectively before discharge.",
            "Property owners may need this service when treatment efficiency declines, components wear out or routine servicing is needed to keep the system working within expected standards. Proper care helps prevent odours, blockages and environmental issues while supporting the long-term reliability of the installation.",
        ],
        "sections": [
            ("What we do", """
<ul class="ticks">
<li>Routine servicing to the manufacturer's schedule</li>
<li>Repair or replacement of air blowers, pumps and diffusers</li>
<li>Investigation of smells, poor discharge quality or alarms</li>
<li>Arranging desludging when the plant needs emptying</li>
<li>Upgrading old septic tanks to a treatment plant</li>
</ul>"""),
            ("Keeping your treatment plant healthy", """
<p>A treatment plant relies on bacteria to break down waste. Large amounts of bleach, disinfectant, fat or medicines can kill them off and reduce treatment quality. Keep the air blower running at all times, avoid flushing wipes and sanitary products, and have the plant serviced regularly.</p>
<p>The Environment Agency's General Binding Rules require small sewage discharges to be maintained by someone competent, following the manufacturer's instructions. Keep records of servicing and emptying.</p>"""),
        ],
        "faqs": [
            ("How often does a sewage treatment plant need emptying?", "It depends on the size of the plant and how many people use it. Many domestic plants need desludging about once a year. Your service engineer can check sludge levels and advise."),
            ("Why does my treatment plant smell?", "Common causes are a failed air blower, a blocked diffuser, too much sludge or chemicals killing the bacteria. We can find the cause and fix it."),
        ],
    },
]

# Order and grouping on the Services page
GROUPS = ["Drain Maintenance", "Drainage Solutions"]
FEATURED = ["blocked-drain-clearing", "cctv-drain-inspection", "drain-repair"]
