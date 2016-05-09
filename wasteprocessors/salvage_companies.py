# copy and pasted from city of seattle website
# http://your.kingcounty.gov/solidwaste/wdidw/category.asp?CatID=17%20%20
# click through forms to individual provider detail pages. this is easier than
# scraping for this site because of complex html structure and asp.net weirdness

companies = [
"""Benchmark Recycling, Inc.

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

Serves businesses and residents.""",
"""Ballard Reuse

Services
Ballard Reuse is a used and salvaged building materials super store. Our mission is to keep as much out of the landfill as possible while sharing creative reuse ideas and having fun. We have the full range of used building materials as well as odd finds and some just plain cool stuff. Stop in to check out all the great material we have in our store. Ballard Reuse is a qualified verifying agent for deconstruction and architectural salvage assessments. Ballard Reuse prides ourselves on taking the widest variety of materials possible and continually pushing the limits of materials reuse. If you have something you think we might like please call or send us a picture.

Contact Information
Address: 1440 NW 52nd St (external map/directions)
Seattle, WA 98107
Telephone: 206-297-9119
Fax: 206-297-7260
Email: store@ballardreuse.com
Web: http://ballardreuse.com/ (external)
Hours: Mon-Sat: 9am - 6pm Sun:10am - 5pm
Materials Handled
Construction and Demolition Debris
 - Brick
 - Porcelain
 - Reusable Building Materials
 - Wood
Furniture
 - Household Furniture
 - Office Furniture
Selected Material(s)
Reusable Building Materials
Wood
Description: Ballard Reuse prides ourselves on taking the widest variety of materials possible and continually pushing the limits of materials reuse. If you have something you think we might like please call or send us a picture.

Restrictions: Call first to confirm that your materials are acceptable.

Drop-off and Pick-up.

Fees: In most cases we can offer a tax deduction for the donation of the materials, give a store credit, or we can pay cash for the salvage rights to the job.

Serves businesses and residents.""",
"""IMEX - Industrial Materials Exchange

Services
IMEX is a free service designed to help businesses find markets for industrial by-products, surplus materials and wastes. Through IMEX, waste generators can be matched with businesses and individuals that can use them. Businesses, offices, schools, and individuals can "advertise" their surplus/unwanted materials or can request the materials they need. The goal of IMEX is to conserve energy, resources and landfill space by helping businesses and organizations find alternatives to the disposal of valuable materials or wastes.

Contact Information
Address: Call for locations
 
Telephone: 206-263-8465 or 888-879-4639
Fax: 206-263-3997
Email: imex@kingcounty.gov
Web: http://www.lhwmp.org/home/IMEX/index.aspx (external)
Hours: Always available on-line.
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
 - Wood
Drums and Barrels
 - Barrels and Drums
Electronics
 - Computers, Laptops, Tablets
 - Monitors
Glass
 - Mixed Glass
 - Separated Glass
 - Window Glass
Metal
 - Ferrous Metals
 - Nonferrous Metals
Paint
 - Paint
Pallets
 - Pallets
Paper
 - Cardboard
 - Newspaper
Plastic
 - Agricultural Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Packing Peanuts and Foam Blocks
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
 - Plastic Office Supplies
Textiles
 - Clothing, Shoes, and Fabrics
Vehicles, Vehicle-related Items
 - Motor Oil and Automotive Fluids
Selected Material(s)
Reusable Building Materials
Wood
Description: IMEX, the Industrial Materials Exchange, is a classifieds listing for business industrial waste, matching waste generators with waste users. Submit a listing to the IMEX Web Site.

Restrictions: Must follow Listing Policy.

Fees: Free Service.

Serves businesses only.""",
"""Re-Use Consulting

Services
Consultants working in Western Washington to help building owners, architects and contractors to find sustainable alternatives to demolition and to sell/buy reusable building materials. Perform jobsite assessments and then find buyers and create markets for materials to be diverted from the landfill. RE-USE Consulting provides on-site step-by-step assistance to disassemble buildings. Options might include tax deductions for donating building materials. Visit http://www.reuseconsulting.com for available reusable building materials, intact structures to be moved, and plants and landscaping materials.

Contact Information
Address: Pick-up service only
 
Telephone: 360-201-6977
Email: re-use@comcast.net
Web: http://www.reuseconsulting.com (external)
Hours: Mon-Fri: 8am-6pm. Weekends by appointment.
Materials Handled
Appliances
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Carpet
 - Carpet
Construction and Demolition Debris
 - Brick
 - Porcelain
 - Reusable Building Materials
 - Wood
Furniture
 - Office Furniture
Landscaping, Landclearing
 - Rock
Selected Material(s)
Reusable Building Materials
Wood
Description: Provides assistance in finding companies to provide deconstruction/salvage services and helps find buyers for salvaged materials. Conditionally accepts wood in good condition for reuse.

Restrictions: Call for details.

Pick-up only.

Fees: Call for details.

Serves businesses and residents.""",
"""Republic Services - Third & Lander Recycling & Transfer Station

Services
The Republic Services (formerly Allied Waste) Recycling Center & Transfer Station is located 1 mile south of downtown Seattle. For materials accepted and current rates visit the 3rd & Lander Recycling & Transfer Station Web site. The facility incorporates curbside commingled recyclables processing technologies, construction and demolition processing and recycling, compostibles transfer services, contaminated media (soil) transfer services, and rail intermodal services.

Contact Information
Address: 2733 3rd Ave. S (external map/directions)
Seattle, WA 98134
Telephone: 206-332-7700
Web: http://www.Rabanco.com (external)
Hours: Mon-Fri: 7am - 5:30pm; Sat-Sun: 8am - 5pm 
Materials Handled
Asbestos
 - Asbestos-Containing Waste
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
Drums and Barrels
 - Barrels and Drums
Electronics
 - Monitors
 - TVs
Food
 - Food Scraps
Glass
 - Mixed Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Contaminated Sand
 - Contaminated Soil
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Shredded Paper
Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Packing Peanuts and Foam Blocks
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
Tires
 - Passenger, Truck, Motorcycle Tires
Selected Material(s)
Wood
Description: For drop off information call 206-623-4080. Hauling services available.

Restrictions: Wood waste must be free of contamination.

Drop-off only.

Fees: Call for details.

Serves businesses and residents.
Reusable Building Materials
Drop-off only.

Serves businesses only.""",
"""Resource Woodworks Inc.

Contact Information
Address: 627 E 60th St (external map/directions)
Tacoma, WA 98404
Telephone: 253-474-3757
Fax: 253-474-1139
Email: rwtimber@aol.com
Web: http://www.rwtimber.com (external)
Hours: Mon-Fri: 8am - 4:30pm
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
 - Wood
Selected Material(s)
Reusable Building Materials
Description: Remills salvaged wood for reuse.

Restrictions: Strictly wood products; no treated materials.

Drop-off only.

Fees: Call for information.

Serves businesses and residents.""",
"""Second Use Building Materials, Inc.

Services
Recovers usable building materials in good condition including: cabinetry, doors, windows, plumbing fixtures, lighting, lumber, trim, flooring, hardware, appliances, and brick/masonry. Salvaged materials for sale to the general public 7 days a week

Contact Information
Address: 3223 6th Ave. S. (external map/directions)
Seattle, WA 98134
Telephone: 206-763-6929
Fax: 206-763-6021
Email: seattle@seconduse.com
Web: http://www.seconduse.com (external)
Hours: Mon-Sun: 9am - 6pm
Materials Handled
Appliances
 - Microwaves
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Construction and Demolition Debris
 - Brick
 - Reusable Building Materials
 - Wood
Furniture
 - Office Furniture
Selected Material(s)
Reusable Building Materials
Description: Accepts all types of reusable building materials in good condition including: cabinetry, doors, windows, plumbing fixtures, lighting, lumber, trim, flooring, hardware, appliances, brick/masonry and more. Material drop-off/pick-up/strip-out services are available. Call for acceptance policies. Accepts tax-deductible donations for local affiliates of Habitat for Humanity. Used building materials in good condition including: cabinetry, doors, lumber, trim, and flooring. Call for more details.

Restrictions: Salvage services available. Limited pickup.

Drop-off and Pick-up.

Fees: Call for information.

Serves businesses and residents.""",
"""United Recycling & Container

Services
United Recycling is a full service state of the art recycling facility. We accept all types of recyclable material from wood, cardboard and plastic - to construction and demolition debris. We are the recycler - no middle man. Container services are available to all surrounding areas.

Contact Information
Address: 18827 Yew Way (external map/directions)
Snohomish, WA 98296
Telephone: 360-668-4300
Email: info@unitedrecyclingco.com
Web: http://www.unitedrecyclingco.com (external)
Hours: Mon-Fri: 7am - 5pm Sat: 8am - 4pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Reusable Building Materials
 - Wood
Drums and Barrels
 - Barrels and Drums
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
Plastic
 - Agricultural Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
Selected Material(s)
Reusable Building Materials
Drop-off and Pick-up.

Serves businesses and residents.""",
"""Waste Management - Cascade Recycling Center

Services
Recycling facility accepting construction, demolition and landclearing debris from commercial customers. All material must be in trucks equipped with electrical or hydraulic offloading capabilities. No pickup loads.

Contact Information
Address: 14020 NE 190th St. (external map/directions)
Woodinville, WA 98072
Telephone: 425-951-8311 or 425-951-8305
Fax: 425-482-9681
Email: pnwbccmservices@wm.com
Web: http://www.wmnorthwest.com/cascaderecycling/ (external)
Hours: Mon-Fri: 5am - 5pm; Saturdays by appointment only
Materials Handled
Carpet
 - Carpet
 - Carpet Padding
Construction and Demolition Debris
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Drywall
 - Reusable Building Materials
 - Wood
Metal
 - Ferrous Metals
 - Nonferrous Metals
Pallets
 - Pallets
Paper
 - Cardboard
Selected Material(s)
Wood
Description: Accepts wood from commercial customers.

Restrictions: Materials must be brought in trucks equipped with electrical or hydraulic offloading capabilities. Call for more information. 

Drop-off only.

Fees: Call for more information.

Serves businesses only.""",
"""All Wood Recycling

Services
Accepts asphalt, brick, concrete, landclearing, pallets and wood for recycling. Offers containers, pick up, or drop off.

Contact Information
Address: 8504 192nd Ave. NE (external map/directions)
Redmond, WA 98053
Telephone: 206-682-5735
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Porcelain
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
Pallets
 - Pallets
Selected Material(s)
Wood
Restrictions: No pressure treated wood. No wood with lead-based paint.

Drop-off and Pick-up.

Serves businesses and residents.""",
"""Services
CDL Recycle (part of Drywall Recycling Services Inc. (DRS)) receives and processes construction, demolition, and woody land clearing debris in two locations: Seattle (Georgetown) and Woodinville. DRS accepts co-mingled loads of recyclable waste materials from construction projects and sorting those loads into re-usable and recyclable commodities. Drywall and wood are accepted only in Woodinville.

Contact Information
Address: 7201 E Marginal Way S (external map/directions)
Seattle, WA 98108
Telephone: 425-245-8015
Fax: 425-245-8013
Web: http://www.cdlrecycle.com (external)
Hours: Mon-Fri: 5am – 7pm Sat: 7am - 2pm and by appointment
Materials Handled
Appliances
 - Other Major Appliances
 - Refrigerators, Freezers
Construction and Demolition Debris
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Plaster
 - Wood
Furniture
 - Mattresses
Metal
 - Ferrous Metals
 - Nonferrous Metals
Pallets
 - Pallets
Paper
 - Cardboard
Plastic
 - Mixed Plastics and Other Types of Plastics
 - Plastic Film and Grocery Bags
Tires
 - Passenger, Truck, Motorcycle Tires
Selected Material(s)
Wood
Description: Accepts wood for recycling.

Restrictions: No painted, old, rotted, molded, treated or creosote wood is accepted. Longer lengths and larger dimensional pieces may be accepted for salvage/ reuse. Call recycling center to confirm prior to sending. Railroad ties, utility or telephone poles not accepted.

Drop-off only.

Fees: $115/ton - call to confirm


Serves businesses only.""",
"""Bobby Wolford Trucking & Demolition

Services
Offers hauling services, drop box services, and drop off site for asphalt, brick, ceramic tile, concrete, rock, dirt, clean waste wood, pallets, land clearing debris, site-sorted demolition, downed limbs, landscape trimmings (no grass). Sells recycled crushed concrete and hog fuel.

Contact Information
Address: 22014 W Bostian Rd (external map/directions)
Woodinville, WA 98072
Telephone: 425-481-1800 or 425-827-7530
Fax: 425-486-6613
Email: info@wolfordtrucking.com
Web: http://wolfordtrucking.com/ (external)
Hours: Mon-Sat: 7am - 6pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Porcelain
 - Wood
Landscaping, Landclearing
 - Rock
Pallets
 - Pallets
Selected Material(s)
Wood
Description: Accepts and recycles clean wood including pallets, lumber, scraps, stumps, land clearing debris.

Restrictions: Pickup done at jobsites. Please call for more information.

Drop-off and Pick-up.

Fees: Call for rates.

Serves businesses and residents.""",
"""Bow Lake Recycling & Transfer Station

Services
King County Transfer Station.
Note: transfer station recycling bins have limited capacity. Excess materials cannot be stored outside of bins. Call the Solid Waste Information Line: 206-296-4466 for assistance with unusually large quantities.

Contact Information
Address: 18800 Orillia Rd S (external map/directions)
Tukwila, WA 98188
Telephone: 206-477-4466 or 800-325-6165 x74466
Fax: 206-296-0197
Hours: Station hours (different from recycle area hours listed below): Mon-Thurs: 24 hours a day Fri: 12 a.m. – 11:30 p.m. Sat and Sun: 8:30 a.m. – 5:30 p.m. Recycle area hours (different from station hours listed above): Mon-Fri 6:00 a.m. – 8:00 p.m. Sat and Sun: 8:30 a.m. – 5:30 p.m. The following materials are accepted only during Recycle area hours:

Commingled recyclable materials
Appliances
Mercury-containing light bulbs and tubes
Textiles
Yard waste
For more information, see Recycling services.

This facility is closed on Thanksgiving, Christmas, and New Year’s Day
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
 - Other Major Appliances
 - Refrigerators, Freezers
Construction and Demolition Debris
 - Wood
Fluorescent Lights
 - Fluorescent Light Bulbs
 - Fluorescent Light Tubes
Glass
 - Mixed Glass
Landscaping, Landclearing
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Misc Household Items
 - Bicycles and Bicycle Parts
Pallets
 - Pallets
Paper
 - Books
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
 - Shredded Paper
Plastic
 - Bottles, Jugs and Tubs
Sharps
 - Medical Sharps
Textiles
 - Clothing, Shoes, and Fabrics
Selected Material(s)
Wood
Description: Accepts clean wood including branches less than 8 feet long, stumps (no dirt), pallets, cedar shingles (no tarpaper), lath (no plaster), untreated and unpainted decking, fencing, plywood, OSB, and construction lumber. Nails and staples in the wood are acceptable. Place clean wood in the recycle area.

Restrictions: All wood must be free of paint, preservatives, metals, concrete, etc., be less than 8 feet in length and less than 2 feet in diameter. Clean wood must be separated from garbage for recycling.

Drop-off only.

Fees: $75 per ton with a minimum fee of $12 per entry. The entry fee covers the first 320 pounds.

Serves businesses and residents.""",
"""Cedar Grove Composting - Everett

Services
Accepts clean greens: grass, leaves, stumps, branches and shrubs. Provides composting services. Sells finished compost and topsoils.

Contact Information
Address: 3620 36th Pl NE (external map/directions)
Everett, WA 98205
Telephone: 877-764-5748 or 425-212-2515
Fax: 425-212-2512
Email: info@cgcompost.com
Web: http://www.cgcompost.com (external)
Hours: Mon - Fri: 7am - 4:30pm Sat: 8am - 4pm (Mar-Oct) Mon - Fri: 8am - 4pm (Nov-Feb)
Materials Handled
Construction and Demolition Debris
 - Wood
Food
 - Food Scraps
Landscaping, Landclearing
 - Brush, Woody Waste
 - Yard Waste
Selected Material(s)
Wood
Description: Accepts wood crates, clean lumber, stumps and other wood. See list of acceptable materials at: http://www.cgcompost.com/organics/recyclables/default.htm

Restrictions: No manure, foodwaste, concrete or dirt.

Drop-off only.

Fees: Call or email info@cgcompost.com for rates.

Serves businesses and residents.""",
"""Concrete Recyclers, Inc.

Services
Concrete and asphalt breaking, removal, disposal and recycling. We can provide portable on-site concrete and asphalt crushing and screening. We also offer asbestos inspection and removal.

Contact Information
Address: 2935 Black Lake Blvd. SW (external map/directions)
Olympia, WA 98512
Telephone: 360-570-1562 or 360-951-0999
Fax: 360-866-9665
Email: crushit@comcast.net
Web: http://www.concreterecyclersolympia.com (external)
Hours: Mon-Fri: 7:30am - 4:30pm Sat: 8am - 3:30pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Wood
Glass
 - Mixed Glass
Landscaping, Landclearing
 - Yard Waste
Selected Material(s)
Wood
Restrictions: Non-painted, untreated.

Drop-off and Pick-up.

Fees: Call for information.

Serves businesses only.""",
"""Construction Waste Management

Services
Provides onsite containers and hauling services for construction and demolition materials for recycling.

Contact Information
Address: 11110 Mukilteo Spdwy, Ste 202 (external map/directions)
Mukilteo, WA 98275
Telephone: 425-402-1972 or 206-707-2666
Fax: 425-493-6809
Email: constructionwastemonica@gmail.com
Hours: Mon-Fri: 7:30am - 4:30pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
Selected Material(s)
Wood
Description: Provides multiple sizes of containers for recycling all types of wood waste and other construction materials.

Minimum volume: None

Maximum volume: Our Largest Container is 52 cubic yards

Restrictions: Recyclable wood waste includes: All types of dimesional lumber, plywood, posts, beams logs, brush, stumps, old cabinets and doors, etc.

Pick-up only.

Fees: Please Call - Pricing is based on your specific job-site location and the total volume of material to be removed

Serves businesses and residents.""",
"""Dirt Exchange

Services
We accept yard waste, scrapings, soil, sod, clean wood, rock, concrete, asphalt and brick for recycling.

Contact Information
Address: 1521 NW 50th St. (external map/directions)
Seattle, WA 98107
Telephone: 206-599-3478
Email: dirtexchange@gmail.com
Web: http://dirtexchange.us/ (external)
Hours: Mon-Fri: 7am - 5pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Sand
 - Clean Soil
 - Rock
 - Yard Waste
Pallets
 - Pallets
Selected Material(s)
Wood
Description: Clean wood, fencing ok (see restrictions)

Restrictions: No paint, no pressure treated, minimal nails. Call for details. Can not take any contaminated material and all loads are subject to review.

Drop-off and Pick-up.

Fees: $23.00 per cubic yard

Serves businesses and residents.""",
"""Earthwise Building Salvage

Services
Earthwise salvages and sells to the public primarily vintage fixtures and building materials.

Contact Information
Address: 3447 4th Ave. S (external map/directions)
Seattle, WA 98134
Telephone: 206-624-4510
Fax: 206-223-0990
Email: earthwise.salvage@gmail.com
Web: http://www.earthwise-salvage.com (external)
Hours: Mon - Sun: 9:30am - 5:30pm 
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
Selected Material(s)
Reusable Building Materials
Description: Licensed and bonded to perform salvages, demolitions, and strip-outs. Acceptance of materials based on current inventory. All items must be approved by Earthwise buyer - E-mail photos to confirm that materials are acceptable. Pick-up available for some items. Call with questions.

Restrictions: Drop-off accepted during store hours. Not accepted: items that contain hazardous materials, railroad ties, and chemicals (paints, glue, caulk, etc.).

Drop-off and Pick-up.

Fees: No fees.

Serves businesses and residents.""",
"""Grayhawk Construction

Services
Will provide 15-, 20-, 25-, 30-, or 40-yard rolloff containers and hauling for all construction recycled materials. No drop-offs accepted.

Contact Information
Address: 9606 NE 180th St. (external map/directions)
Bothell, WA 98011
Telephone: 425-402-4122 or 206-391-1324
Fax: 425-402-4132
Email: davis.kerr@grayhawkconst.com
Web: http://grayhawkrecyclingservices.com/home.html (external)
Hours: 24 hours
Materials Handled
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
 - Wood
Drums and Barrels
 - Barrels and Drums
Glass
 - Mixed Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
Selected Material(s)
Wood
Description: Will provide 15-, 20-, 30-, or 40-yard rolloff containers and hauling for all construction recycled materials. Please call for more information.

Minimum volume: 15 cubic yards

Maximum volume: None

Restrictions: No food, garbage, hazardous waste, paint, chemicals, TVs, or computer monitors.

Pick-up only.

Fees: Call for more information.

Serves businesses and residents.""",
"""Habitat for Humanity Seattle/South King County Home Improvement Outlet

Services
We accept donations of new and gently used furniture, building materials, appliances and hardware that are clean and in 100% working condition. If you have overstock, seasonal items, inventory close outs, be sure to give us a call. By donating materials to a Habitat Store (Bellevue and Seattle), you will enjoy a tax deduction, help provide our community with a source of low-cost materials, and reduce materials going to landfills. Note the Seattle store is closed while moving to a new location and reopening in November 2015.

Contact Information
Address: 13500 Bel Red Rd (external map/directions)
Bellevue, WA 98005
Telephone: 206-957-6914
Email: outlet@seattle-habitat.org
Web: http://www.habitatskc.org/store (external)
Hours: Please call to make arrangements.
Materials Handled
Appliances
 - Other Major Appliances
 - Refrigerators, Freezers
Construction and Demolition Debris
 - Reusable Building Materials
Furniture
 - Household Furniture
Selected Material(s)
Reusable Building Materials
Description: Accepts new and used building materials such as: lumber, cabinets, countertops, paint, doors, plumbing, electrical, roofing, flooring, windows, hardware, wall board and lighting.

Restrictions: Please call first to confirm that your materials are acceptable. Does not provide salvage service.

Drop-off and Pick-up.

Fees: Donation only.

Serves businesses and residents.""",
"""Lloyd Enterprises, Inc.

Services
Accepts concrete, asphalt, dirt, brush, stumps, demolition debris, and construction debris.

Contact Information
Address: 80 5th Ave. (external map/directions)
Milton, WA 98354
Telephone: 253-874-6692 or 253-927-0416
Fax: 253-838-0103
Email: sales@lloydenterprisesinc.com
Web: http://www.lloydenterprise.com (external)
Hours: Mon-Fri: 7am - 5pm Sat: 8am - 12pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Drywall
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Sand
 - Clean Soil
 - Rock
Selected Material(s)
Wood
Description: Accepts brush, landclearing wood waste and stumps. Hauling services available.

Restrictions: No dimensional lumber accepted.

Drop-off and Pick-up.

Fees: Price structured according to amounts--call for prices.

Serves businesses and residents.""",
"""Nickel Bros. House Moving

Services
Nickel Bros. House Moving rescues houses from demolition by working with developers and homeowners who plan to demolish a house in order to build another larger house or a development. These houses are then resold.

Contact Information
Address: 625 Riverside Rd (external map/directions)
Everett, WA 98201
Telephone: 425-257-2067
Fax: 425-257-2069
Email: washington@nickelbrosusa.com
Web: http://www.nickelbros.com/ (external)
Hours: Mon - Fri: 8am - 5pm
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
Selected Material(s)
Reusable Building Materials
Description: Recovers houses before demolition to be resold.

Fees: Call for details.

Serves businesses and residents.""",
"""Pacific Topsoils, Inc. - North Seattle

Services
Pacific Topsoils serves homeowners and landscape contractors with topsoil products, mulches, and tools with locations in Bellevue, Everett, Issaquah, Kenmore, Maltby, Marysville, Redmond, Seattle, and Tukwila. Contact Sales at sales@pacifictopsoils.com, or visit our website at www.pacifictopsoils.com.

Contact Information
Address: 1212 N 107th St. (external map/directions)
Seattle, WA 98133
Telephone: 800-884-7645 or 425-337-2700
Email: sales@pacifictopsoils.com
Web: http://www.pacifictopsoils.com (external)
Hours: Varies with season - 7 days a week
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Concrete
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Yard Waste
Pallets
 - Pallets
Selected Material(s)
Wood
Description: Accepts small stumps, lumber, pallets, and wood chips (with or without staples or nails).

Restrictions: Untreated materials only. No paint or stains. Also takes railroad ties.

Drop-off and Pick-up.

Fees: Call for pricing, email us at sales@pacifictopsoils.com, or see our website at www.pacifictopsoils.com for more information.

Serves businesses and residents.""",
"""R. W. Rhine, Inc.

Services
Commercial demolition and salvage contractor for wood products and metal.

Contact Information
Address: 1313 112th St E (external map/directions)
Tacoma, WA 98445
Telephone: 253-537-5852
Email: info@rwrhine.com
Web: http://www.rwrhine.com (external)
Hours: Mon-Fri: 8am - 5pm
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
Selected Material(s)
Reusable Building Materials
Description: Commercial demolition and salvage contractor for wood products and metal. Call to find out about other materials that may be accepted. Materials processed from site.

Restrictions: Accepts select building materials at yard location. Timbers must be in reusable condition. Treated or painted wood is acceptable if reusable. Pick up for large quantities only, call first.

Drop-off and Pick-up.

Fees: Call for information.

Serves businesses and residents.""",
"""Seattle Building Salvage

Contact Information
Address: Call for location
 
Telephone: 425-374-2550
Email: Seattlebuildingsalvage@gmail.com
Web: http://www.seattlebuildingsalvage.com (external)
Materials Handled
Construction and Demolition Debris
 - Reusable Building Materials
Misc Household Items
 - General
Selected Material(s)
Reusable Building Materials
Description: Accepts pre-1940 construction salvage items such as light fixtures, other types of fixtures, doors, bath tubs, and any reusable building materials.

Drop-off and Pick-up.

Fees: Call for more information.

Serves businesses and residents.""",
"""Waste Management - Commercial Recycling Collection Services

Services
Provides commercial garbage and recycling collection for businesses in King County. Outdoor containers available. Will visit site.

Contact Information
Address: Pick-up service only
 
Telephone: 800-592-9995
Fax: 800-284-1337
Email: commercialinfo@wmnorthwest.com
Web: http://www.wmnorthwest.com (external)
Hours: Mon.-Fri: 7am-5pm
Materials Handled
Animal Waste
 - Animal Manure, Excrement
Construction and Demolition Debris
 - Asphalt Roofing
 - Concrete
 - Wood
Food
 - Food Scraps
Glass
 - Separated Glass
Landscaping, Landclearing
 - Brush, Woody Waste
Metal
 - Aluminum Cans
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Plastic Film and Grocery Bags
Selected Material(s)
Wood
Description: Permitted construction waste disposal facility. Accepts clean wood, dirty wood, painted or treated wood.

Restrictions: Call for more information.

Pick-up only.

Fees: Reduced tipping fee for recyclable material.

Serves businesses only.""",
"""Alternative Concepts

Services
Alternative Concepts deconstructs buildings, salvaging and reclaiming materials that would end up in the landfill. We recycle and reuse as much material as possible. We accept left-over building supplies as well as material you don't know what to do with and would like to keep out of the landfill.

Contact Information
Address: Pick-up service only
 
Telephone: 206-734-6317
Email: thehoogenconnection@gmail.com
Hours: By appointment only.
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Reusable Building Materials
 - Wood
Metal
 - Ferrous Metals
 - Nonferrous Metals
Selected Material(s)
Reusable Building Materials
Description: Deconstructs old buildings and rebuilds new buildings out of reusable materials such as asphalt, lumber, concrete, metal, and brick. Also offers pick-up service for some recyclable materials. Call for details.

Restrictions: No hazardous waste. Call for specific questions.

Pick-up only.

Fees: Call for fee info.

Serves businesses and residents.
Wood
Description: Deconstructs old buildings and rebuilds new buildings out of reusable materials such as asphalt, lumber, concrete, metal, and brick. Also offers pick-up service for some recyclable materials. Call for details.

Restrictions: No hazardous waste. Call for specific questions.

Pick-up only.

Fees: Call for fee info.

Serves businesses and residents.""",
"""Angel's Junk Removal

Services
Angel's is a pick up and removal service, accepting everything from appliances to yard waste debris. Materials are taken to a recycling center or are properly disposed of. We serve King, Snohomish and Pierce Counties. Call 877-744-5865 or visit our website for a complete list of services.

Contact Information
Address: Pick-up service only
 
Telephone: 877-744-5865
Email: patm@angelsjunkremoval.com
Web: http://www.angelsjunkremoval.com (external)
Hours: Mon-Fri: 8am - 6pm
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
 - Microwaves
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Batteries
 - Alkaline Batteries
 - Button Batteries
 - Motor Vehicle Batteries
 - Rechargeable Batteries
 - Uninterruptible Power Supply (UPS) Batteries
Carpet
 - Carpet
 - Carpet Padding
Cleaning Products
 - Cleaning Products
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
 - Rigid Foam Insulation Board
 - Vermiculite Attic Insulation
 - Wood
Drums and Barrels
 - Barrels and Drums
Electronics
 - Audio Video and Camera equipment
 - Cell Phones, Smart Phones, Mobile Devices
 - Computers, Laptops, Tablets
 - Gaming Devices
 - Monitors
 - Printers, Copiers, Fax Machines, Peripherals
 - TVs
Fluorescent Lights
 - Fluorescent Light Ballasts
 - Fluorescent Light Bulbs
 - Fluorescent Light Tubes
Furniture
 - Foam Padding
 - Household Furniture
 - Office Furniture
Glass
 - Mixed Glass
 - Separated Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Sand
 - Clean Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Misc Household Items
 - Baby Supplies
 - Bicycles and Bicycle Parts
 - General
 - Smoke Detectors
Paint
 - Paint
Pallets
 - Pallets
Paper
 - Books
 - Cardboard
 - Confidential Documents
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
 - Pulltabs
 - Shredded Paper
Plastic
 - Agricultural Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Packing Peanuts and Foam Blocks
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
 - Plastic Office Supplies
Printer Cartridges
 - Inkjet Cartridges
 - Ribbon Cartridges
 - Toner Cartridges
Textiles
 - Clothing, Shoes, and Fabrics
 - Flags
Tires
 - Passenger, Truck, Motorcycle Tires
Selected Material(s)
Reusable Building Materials
Description: Angel’s removes construction and demolition debris. Items are separated for reuse and recycling.

Restrictions: We do not accept hazardous materials except ewaste and fluorescent lighting.

Pick-up only.

Serves businesses and residents.""",
"""Busby Junk Removal LLC

Services
Authorized E-Cycle Washington Collector. Commercial and residential debris removal service, provides pick-up service in King, Pierce and Snohomish Counties. Fees for pick-up, additional fees may be charged for recycling electronic products. Free junk removal consultation.

Contact Information
Address: Pick-up service only
 
Telephone: 877-404-5865
Fax: 425-605-9452
Email: sales@buzz-bee.net
Web: http://www.buzz-bee.net (external)
Hours: Mon-Sun: 8am - 5pm
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
 - Microwaves
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Batteries
 - Uninterruptible Power Supply (UPS) Batteries
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
 - Rigid Foam Insulation Board
 - Wood
Electronics
 - Audio Video and Camera equipment
 - Cell Phones, Smart Phones, Mobile Devices
 - Computers, Laptops, Tablets
 - Gaming Devices
 - Monitors
 - Printers, Copiers, Fax Machines, Peripherals
 - TVs
Glass
 - Mixed Glass
 - Separated Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Sand
 - Clean Soil
 - Contaminated Sand
 - Contaminated Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Misc Household Items
 - Baby Supplies
 - Bicycles and Bicycle Parts
 - Eyeglasses
 - General
Paint
 - Paint
Pallets
 - Pallets
Paper
 - Books
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
 - Pulltabs
 - Shredded Paper
Plastic
 - Agricultural Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Packing Peanuts and Foam Blocks
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
 - Plastic Office Supplies
Printer Cartridges
 - Inkjet Cartridges
 - Ribbon Cartridges
 - Toner Cartridges
Textiles
 - Clothing, Shoes, and Fabrics
 - Flags
Tires
 - Passenger, Truck, Motorcycle Tires
Vehicles, Vehicle-related Items
 - Oversized Items
 - Vehicles and Major Vehicle Parts
Selected Material(s)
Wood
Description: A junk removal service that provides recycling for metal, wood, appliances, ewaste, fluorescent bulbs and tubes, yard waste, concrete, paper and printer cartridges. See more information about recyclable materials.

Restrictions: Does not accept hazardous materials except ewaste and fluorescent bulbs and tubes.

Pick-up only.

Fees: See Busby pricing fees.

Serves businesses and residents.""",
"""E.I.R. Enterprise

Services
Provides 18- and 25-yard roll-off containers for the hauling of non-hazardous materials: source separated recyclables such as wood, metal (stoves, water heaters, fridges), cardboard, newspaper, books, high grade paper, most electronics (TVs, computers, etc.), concrete and asphalt (under 8,000 lbs per load). Targets commercial centers and malls between Highway 520 and I-90 east of Lake Washington.

Contact Information
Address: Pick-up service only
 
Telephone: 206-339-9166
Email: pixibob69@yahoo.com
Hours: Provides pick up services only - No staffed commercial drop locations.
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
 - Microwaves
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Carpet
 - Carpet
 - Carpet Padding
Construction and Demolition Debris
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
Drums and Barrels
 - Barrels and Drums
Electronics
 - Audio Video and Camera equipment
 - Computers, Laptops, Tablets
 - Monitors
 - Printers, Copiers, Fax Machines, Peripherals
 - TVs
Glass
 - Mixed Glass
 - Separated Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Paper
 - Books
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Pulltabs
Propane Tanks
 - Propane Tanks
Selected Material(s)
Wood
Description: We haul wood in source separated loads. Small quantities in mixed loads. Volume and weight limits apply on this type of material. Call for details on your specific job.

Maximum volume: 8,000 lb load limit per haul.

Restrictions: 8,000 lb load limit per haul. No hazardous wastes. Collection only available within a 20 mile radius of their headquarters in Redmond.

Pick-up only.

Fees: Call for rates.

Serves businesses only.""",
"""Hungry Buzzard Recovery, LLC

Services
Drop container hauling service of recyclable materials for the construction industry and residential customers. Service area includes all of King County and all of Snohomish County.

Contact Information
Address: Pick-up service only
 
Telephone: 425-489-9235 or 866-489-9235
Fax: 425-489-9245
Email: dispatch@hungrybuzzard.com
Web: http://www.hungrybuzzard.com (external)
Hours: Mon-Fri: 7am - 5pm
Materials Handled
Appliances
 - Other Major Appliances
Construction and Demolition Debris
 - Acoustic Ceiling Tile
 - Asphalt
 - Asphalt Roofing
 - Brick
 - Concrete
 - Drywall
 - Plaster
 - Porcelain
 - Reusable Building Materials
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Rock
 - Yard Waste
Metal
 - Ferrous Metals
Selected Material(s)
Reusable Building Materials
Description: Will drop off and pick up steel containers to job sites and private residences to capture all the "recyclable" building materials. Will pick up construction, demolition, & land clearing debris including: roofing (shake, composite, tile), co-mingled construction material, wood, concrete, masonry, metals (stoves, washers, dryers, ducting, hot water heaters, piping).

Restrictions: Does not pick up the following (non-recyclables): Household garbage, TV's, computers, monitors, oils, solvents, paints, asbestos containing materials, treated wood, fluorescent tubes, car batteries, tires.

Pick-up only.

Fees: Call for details.

Serves businesses and residents.""",
"""KT Recycling (formerly Kendall Trucking and Recycling)

Services
On-site container hauling service for general demolition and construction recycling.

Contact Information
Address: Pick-up service only
 
Telephone: 206-545-6950
Fax: 206-324-6273
Email: ktrecyclingwa@gmail.com
Web: http://ktrecyclingwa.com (external)
Hours: Mon-Fri: 7am - 6pm and Sat: 8am - 4pm. Night service available.
Materials Handled
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
 - Vermiculite Attic Insulation
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Contaminated Soil
 - Rock
 - Yard Waste
Metal
 - Ferrous Metals
 - Nonferrous Metals
Paper
 - Cardboard
 - Confidential Documents
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
 - Pulltabs
 - Shredded Paper
Selected Material(s)
Reusable Building Materials
Pick-up only.

Serves businesses and residents.
Wood
Pick-up only.

Serves businesses and residents.""",
"""Republic Services - Commercial Services & Sales

Services
Republic Services (formerly Allied Waste) provides hauling services for businesses, offering commercial carts, front-load (dumpster), roll-off drop boxes and intermodal container services for garbage, recycling, construction demolition debris, and yard/landscape debris. For more information please visit www.rabanco.com or call 206-332-7700.

Contact Information
Address: Pick-up service only
 
Telephone: 206-332-7777
Fax: 206-764-1234
Web: http://www.disposal.com (external)
Hours: Mon - Fri: 8am - 5pm
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
Asbestos
 - Asbestos-Containing Waste
Carpet
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
 - Vermiculite Attic Insulation
 - Wood
Food
 - Food Scraps
Glass
 - Mixed Glass
 - Separated Glass
 - Window Glass
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Contaminated Sand
 - Contaminated Soil
 - Rock
 - Yard Waste
Metal
 - Aluminum Cans
 - Ferrous Metals
 - Nonferrous Metals
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Packing Peanuts and Foam Blocks
 - Plastic Film and Grocery Bags
Selected Material(s)
Wood
Description: Provides hauling services for wood, garbage, recycling, construction debris and many other materials.

Minimum volume: Any

Maximum volume: Any

Pick-up only.

Fees: For commercial rates please call 206-332-7700. For current residential rates select your city or service area on our Web site or call us at 206-332-7700.

Serves businesses and residents.""",
"""Big Haul Junk Removal

Services
Our company is a pick up and removal service. We accept everything from appliances to yard waste debris. Materials are taken to a recycling center or are properly disposed of. We provide pick up service to King, and parts of Snohomish and Pierce Counties. Please check out our website or call us for a complete list of services.

Contact Information
Address: Pick-up service only (external map/directions)
P.O. Box 50331 Bellevue, WA 98015
Telephone: 877-770-4285 or 877-937-2444
Email: info@bighaul.net
Web: http://www.bighaul.com (external)
Hours: Mon-Sun: 7am - 7pm
Materials Handled
Appliances
 - Air Conditioners, Heat Pumps
 - Microwaves
 - Other Major Appliances
 - Refrigerators, Freezers
 - Small Household Appliances
Construction and Demolition Debris
 - Acoustic Ceiling Tile
 - Brick
 - Concrete
 - Drywall
 - Fiberglass
 - Plaster
 - Porcelain
 - Rigid Foam Insulation Board
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Rock
 - Yard Waste
Selected Material(s)
Wood
Description: Licensed, Bonded and Insured Junk Removal Company providing recycling for Appliances, Metal, Furniture, Wood, Ewaste, Yard Waste, TV's, Monitors, Ewaste, Paper, Concrete, Dirt,

Restrictions: Does not accept hazardous waste

Pick-up only.

Fees: See Big Haul pricing fees

Serves businesses and residents.""",
"""CWRR - Commercial Waste Reduction and Recycling

Services
Provides commercial recycling collection services. Indoor and outdoor containers provided. No drop-off facility.

Contact Information
Address: Pick-up service only
 
Telephone: 206-772-4745
Email: dave@cwrrecycling.com
Web: http://www.cwrrecycling.com (external)
Hours: Mon-Sat: 8am-5pm
Materials Handled
Construction and Demolition Debris
 - Asphalt
 - Brick
 - Concrete
 - Wood
Electronics
 - Computers, Laptops, Tablets
 - Monitors
 - Printers, Copiers, Fax Machines, Peripherals
 - TVs
Food
 - Fats, Oil and Grease
 - Food Scraps
Glass
 - Mixed Glass
 - Separated Glass
Landscaping, Landclearing
 - Yard Waste
Metal
 - Aluminum Cans
 - Steel, Tin Cans
 - Steel, Tin Cans
Pallets
 - Pallets
Paper
 - Books
 - Cardboard
 - Mixed Paper
 - Newspaper
 - Office Paper
 - Phone Books
 - Polycoated Cardboard
 - Pulltabs
 - Shredded Paper
Plastic
 - Agricultural Plastic
 - Bottles, Jugs and Tubs
 - Mixed Plastics and Other Types of Plastics
 - Plastic Film and Grocery Bags
 - Plastic Nursery Pots
Selected Material(s)
Wood
Description: Accepts CDL for recycling.

Restrictions: Call for details.

Pick-up only.

Serves businesses only.""",
"""ReNu Recycling Services

Services
ReNu Recycling Services, part of Nuprecon, a C&D hauler, offers a menu of services that include the collection of both source separated (single stream) and commingled materials, wherein you can put most C&D waste products in the same box. Additionally, we will work with you to manage and mitigate site waste and costs and even provide recycling and diversion reporting on a regular basis at no extra charge.

Contact Information
Address: Pick-up service only
 
Telephone: 877-444-7368 or 425-881-0623
Fax: 425-881-5935
Email: renu@nuprecon.com
Web: http://www.nuprecon.com (external)
Hours: Mon-Fri: 7am - 5pm
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
 - Wood
Landscaping, Landclearing
 - Brush, Woody Waste
 - Clean Soil
 - Rock
 - Yard Waste
Paper
 - Cardboard
Selected Material(s)
Wood
Description: Onsite drop box and hauling services for all types of construction and demolition materials (concrete, asphalt, brick, drywall, wood, etc.) for recycling. Accepts co-mingled CDL loads; night service available

Restrictions: Pick-up services only. No garbage, liquids, or hazardous wastes.

Pick-up only.

Fees: Call for price quote. Flat rate depending on box size, material type, and location.

Serves businesses and residents.""",

]

# a list for storing all companies -- use to update database
all_companies = []

# extract relevant values from string and store in a dict. this will be moved
# to a function, or perhaps a model method

for company in companies:
    c_dict = {}

    c_list = company.split('\n')

    c_dict['company'] = c_list[0]

    for i in c_list:
        if i.startswith('Address:'):
            c_dict['address'] = i.replace('Address: ', '')
        if i.startswith('Telephone:'):
            c_dict['phone'] = i.replace('Telephone: ', '')
        if i.startswith('Email:'):
            c_dict['email'] = i.replace('Email: ', '')
        if i.startswith('Hours:'):
            c_dict['business_hours'] = i.replace('Hours: ', '')
        if i.startswith('Web:'):
            website = i.replace('Web: ', '')
            c_dict['website'] = website.replace(' (external)', '')

    # get building materials accepted by company
    m_index = c_list.index('Materials Handled')
    for i in c_list:
        if i.startswith('Description:'):
            d_index = c_list.index(i)
    m_list = c_list[m_index+1:d_index]
    materials_accepted = set()
    for i in m_list:
        material = i.replace('-', '').strip()
        materials_accepted.add(material)
    c_dict['materials_accepted'] = materials_accepted
    if 'Selected Material(s)' in c_dict['materials_accepted']:
        c_dict['materials_accepted'].remove('Selected Material(s)')

    # add services to description value
    c_dict['description'] = ''
    for index, item in enumerate(c_list):
        if item =='Services':
            c_dict['description'] = c_list[index+1]

    # add description to description value
    for i in c_list[d_index:]:
        if i.startswith('Description:'):
            c_dict['description'] += '\n'
            c_dict['description'] += i.replace('Description: ', '')
        elif i:
            c_dict['description'] += '\n'
            c_dict['description'] += i
    all_companies.append(c_dict)








