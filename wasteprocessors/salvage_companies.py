# copy and pasted from city of seattle website
# http://your.kingcounty.gov/solidwaste/wdidw/category.asp?CatID=17%20%20
# click through to individual provider detail pages. this is easier than
# scraping for this site because of asp.net weirdness

company = """Benchmark Recycling, Inc.

Services
Benchmark Recycling provides drop boxes for hauling recyclable materials to the proper recycling facility. Benchmark Recycling also provides site clean-up services and foreclosure clean up.

Contact Information
Address: 3024 S Mullen St. (external map/directions)
Suite E Tacoma, WA 98409
Telephone: 253-565-1565
Fax: 253-565-1576
Email: info@benchmarkrecycling.com
Web: http://www.benchmarkrecycling.com/ (external)
Hours: Mon-Fri 7:30am - 4pm
Materials Handled
Carpet
 - Carpet
 - Carpet Padding
Construction and Demolition Debris
 - Acoustic Ceiling Tile
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Fiberglass
 - Plaster
 - Porcelain
 - Reusable Building Materials
 - Wood
Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
Metal
 - Ferrous Metals
 - Nonferrous Metals
Pallets
 - Pallets
Paper
 - Cardboard
Vehicles, Vehicle-related Items
 - Vehicles and Major Vehicle Parts
Selected Material(s)
Reusable Building Materials
Description: Accepts miscellaneous reusable building materials including cabinets, doors, fencing, floor coverings, and fixtures, etc.

Minimum volume: 3 tons

Maximum volume: unlimited

Restrictions: Do not accept: household trash, garbage, suspect asbestos containing material, fluorescent light tubes, other mercury containing devices, light ballast that may contain PCB’s, other potential PCB sources, electronics equipment, clothing, grass and yard clippings, contaminated soil, and containers with flammable liquid.

Pick-up only.

Serves businesses and residents."""

# a list for storing all companies -- use to update database
all_companies = []

# extract relevant values from string and store in a dict. this will be moved
# to a function, or perhaps a model method

c_dict = {}
c_list = company.split('\n')

c_dict['company'] = c_list[0]
for i in c_list:
    # figure out how to add both services and description to description value
    if i.startswith('Address:'):
        c_dict['address'] = i.replace('Address: ', '')
    if i.startswith('Telephone:'):
        c_dict['phone'] = i.replace('Telephone: ', '')
    if i.startswith('Email:'):
        c_dict['email'] = i.replace('Email: ', '')
    if i.startswith('Web:'):
        website = i.replace('Web: ', '')
        c_dict['website'] = website.replace(' (external)', '')
# get building materials accepted by company
m_index = c_list.index('Materials Handled')
for i in c_list:
    if i.startswith('Description:'):
        d_index = c_list.index(i)
m_list = c_list[m_index+1:d_index]
materials_accepted = []
for i in m_list:
    material = i.replace('-', '').strip()
    materials_accepted.append(material)
c_dict['materials_accepted'] = materials_accepted








