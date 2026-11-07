"""Business details and shared settings. Change things here, then run:  python3 build/build.py  (from the project folder)

Everything on the website that mentions the phone number, email, areas or opening
hours reads it from this file, so a change here updates every page at once.
"""

BUSINESS = {
    "name": "Elite Drainage Services",
    "url": "https://elitedrainage.uk",
    # Most-used number on the old site (every Call Now button). The old About page text
    # showed 0330 633 6033 instead. Confirm which is right and change both lines if needed.
    "phone_display": "0330 633 0336",
    "phone_tel": "+443306330336",
    "email": "elitedrainageservices@gmail.com",
    "town": "Waterlooville",
    "county": "Hampshire",
    # Leave street/postcode blank to keep the address private (service-area business).
    "street": "",
    "postcode": "",
    "lat": 50.890312,   # from the old site's page code (Waterlooville)
    "lng": -1.028751,
    "hours_text": "Available 24 hours a day, 7 days a week for emergencies",
    "open_24_7": True,
    "founded_text": "over 30 years' experience",
}

# Towns covered. Remove any you do not want to be found for, or add more.
AREAS = [
    {"name": "Waterlooville", "postcodes": "PO7 and PO8",
     "text": "Our home town. We cover the whole of Waterlooville, including the town centre, Wecock Farm, Hart Plain, Crookhorn and Widley."},
    {"name": "Cowplain", "postcodes": "PO8",
     "text": "Cowplain and the roads either side of the A3 London Road, a few minutes north of Waterlooville town centre."},
    {"name": "Purbrook", "postcodes": "PO7",
     "text": "Purbrook, Stakes and Purbrook Heath. Where a property has older clay pipework we carry out a CCTV survey before quoting for repairs, so you only pay for work that is needed."},
    {"name": "Denmead", "postcodes": "PO7",
     "text": "Denmead village and the surrounding rural roads. For properties that are not on mains drainage we also service septic tanks, sewage treatment plants and pump stations."},
    {"name": "Horndean", "postcodes": "PO8",
     "text": "Horndean, Catherington, Clanfield and Lovedean, from blocked toilets and outside gullies to new drainage runs for extensions."},
    {"name": "Havant", "postcodes": "PO9",
     "text": "Havant, Bedhampton, Leigh Park and Rowlands Castle, for homeowners, landlords, letting agents and commercial premises."},
    {"name": "Portsmouth", "postcodes": "PO1 to PO6",
     "text": "Portsmouth, Southsea, Cosham, Drayton and Farlington. In terraced streets several houses often share one drain run, so a single blockage can affect neighbours. A CCTV survey shows exactly where the problem is."},
]

NAV = [
    ("Home", "/"),
    ("Services", "/services/"),
    ("Areas", "/areas/"),
    ("About", "/about/"),
    ("Blog", "/blog/"),
    ("Contact", "/contact/"),
]
