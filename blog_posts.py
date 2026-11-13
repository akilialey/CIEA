# Blog articles for the CIEA site. build.py turns each entry into its own page and adds it to blog.html.
# Every figure in an article must come from one of its listed sources. When a fact changes, update the
# text, the "updated" date and the source link together. No em dashes or en dashes anywhere.

def a(url, text):
    """External source link, opened in a new tab."""
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'

# Official sources used across the articles
UWI_FIN = "https://www.cavehill.uwi.edu/international/?p=278"
UWI_TRAVEL = "https://www.cavehill.uwi.edu/international/travelling-information/"
UWI_FAQ = "https://www.cavehill.uwi.edu/international/?p=294"
UWI_FEES = "https://www.cavehill.uwi.edu/wp-content/uploads/sites/95/Resources/Fees/2025-26-Financial-Information_International_Final.pdf"
UWI_GUIDE = "https://www.cavehill.uwi.edu/newstudents/wp-content/uploads/sites/94/Pre_arrival-Guide-July-2026.pdf"
BCC_FEES = "https://bcc.edu.bb/Admissions/Fees/"
CBB_PEG = "https://www.centralbank.org.bb/news/general-press-release/fixed-for-forty-one-years"
BRA_VAT = "https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates"
BRA_ZERO = "https://bra.gov.bb/News/Policy-Notes/Items-Zero-Rated-for-Value-Added-T"
IMM_STUDENT = "https://immigration.gov.bb/pages/StudentVisa.aspx"
IMM_WORK = "https://immigration.gov.bb/pages/WorkPermit.aspx"
GIS_PLASTICS = "https://gisbarbados.gov.bb/blog/reminder-of-ban-for-single-use-plastics/"
GIS_HURRICANE = "https://gisbarbados.gov.bb/blog/early-warning-action-can-save-lives"
VISIT_DRIVE = "https://www.visitbarbados.org/your-stay/get-around-the-island/vehicle-rentals"
NCF_CROPOVER = "https://ncf.bb/?p=1582"
BAC_SKILLS = "https://bac.gov.bb/?p=1177"
BAC_GUIDE = "https://bac.gov.bb/wp-content/uploads/2026/05/Certificate-of-Recognition-of-CARICOM-Skills-Qualification-Guidelines-Booklet-v15.4.pdf"

PUBLISHED = "2026-11-13"

POSTS = [
# ------------------------------------------------------------------ 1. COST OF LIVING
{
"slug": "cost-of-living-in-barbados-for-students.html",
"title": "What It Costs to Study and Live in Barbados",
"seo_title": "Cost of Living in Barbados for International Students (2026 Guide) | CIEA",
"desc": "Rent, food, transport, tuition and visa costs for international students in Barbados, with figures from UWI Cave Hill, BCC and the Barbados government.",
"lede": "A clear, sourced look at rent, food, transport, tuition and the one-off costs to plan for before you arrive.",
"photo": ("family-planning", "A family planning together at a laptop"),
"read": 7,
"body": f'''
<p>One of the first questions families ask me is simple: what will this really cost? It is the right question to start with. A year in Barbados is very achievable when you plan for it, and the best plans are built on real numbers. Here are the figures the schools and the Government of Barbados publish themselves, so you can build your own budget with confidence.</p>

<h2 id="currency">First, the Barbados dollar</h2>
<p>Prices on the island are in Barbados dollars (BBD, often written BDS$). The Barbados dollar has been fixed to the US dollar at <strong>US$1 to BBD$2</strong> since 5 July 1975, according to the {a(CBB_PEG, "Central Bank of Barbados")}. That makes the maths easy: halve a Barbados price to get the US dollar amount. A BBD$3.50 bus fare is US$1.75.</p>

<h2 id="monthly">A monthly budget from UWI Cave Hill</h2>
<p>The International Office at The University of the West Indies, Cave Hill Campus publishes {a(UWI_FIN, "estimated living costs for international students")}. These are their figures, in US dollars:</p>
<div class="table-wrap"><table>
<caption>Estimated monthly living costs, UWI Cave Hill (US$)</caption>
<thead><tr><th scope="col">Item</th><th scope="col">Estimate per month</th></tr></thead>
<tbody>
<tr><th scope="row">Accommodation (shared)</th><td>$300 to $400</td></tr>
<tr><th scope="row">Meals ($15 to $30 a day)</th><td>$450 to $900</td></tr>
<tr><th scope="row">Daily transportation</th><td>$100 to $200</td></tr>
<tr><th scope="row">Incidentals</th><td>$200</td></tr>
</tbody></table></div>
<p>Added together, those ranges come to roughly <strong>US$1,050 to US$1,700 a month</strong>. That total is my own sum of UWI's figures, not a number the university publishes. UWI also notes that a room costs more, about US$500, if you would rather not share, that a homestay with meals is approximately US$50 a day, and that transport costs can be reduced significantly by using the campus shuttle.</p>

<h2 id="housing">Living on campus or off campus</h2>
<p>UWI Cave Hill has three Halls of Residence, offered on a first come, first served basis. Rooms are furnished single bedrooms with a shared kitchen, bathroom and living area, and you bring your own linen and kitchen things ({a(UWI_TRAVEL, "UWI Travelling Information")}).</p>
<p>In the university's {a(UWI_FEES, "2025/2026 Financial Information for International Students")}, a single room for Semester 1 was listed at US$1,512.50 in Frank Worrell Hall or Sherlock Hall, and US$2,722.50 in Keith Hunte Hall. There is also a US$150 advance deposit, which comes off your semester fees, and a US$100 security deposit. The same document lists off-campus options at about US$350 to US$450 a month. UWI's {a(UWI_GUIDE, "July 2026 pre-arrival guide")} says the 2026/2027 fees will be published shortly, so always check the latest figures before you commit.</p>
<p>If you live off campus, UWI keeps a list of approved accommodation and its Accommodations Assistant can help you search, but the agreement is between you and the landlord.</p>

<h2 id="tuition">Tuition</h2>
<p>Tuition depends on the school and the program. As two examples from the schools' own fee pages:</p>
<ul>
<li><strong>UWI Cave Hill (2025/2026, international students):</strong> most full-time undergraduate degrees in Humanities and Education, Social Sciences, and Science and Technology were US$18,650 a year. Law (LLB) was US$27,000, and the MBBS medical degree was US$32,500 a year for the pre-clinical years ({a(UWI_FEES, "UWI fee schedule")}).</li>
<li><strong>Barbados Community College:</strong> the yearly total for extra-regional students is listed at BBD$8,925 (about US$4,463). That covers BBD$8,000 tuition, BBD$295 registration, BBD$330 medical insurance and the BBD$300 visa fee. Regional students pay a total of BBD$4,925. Some bachelor's programs cost more ({a(BCC_FEES, "BCC Fees")}).</li>
</ul>
<p>Looking for a specific course? Our <a href="course-finder.html">Program Finder</a> lists programs across UWI Cave Hill, BCC, Codrington College and SJPI.</p>

<h2 id="one-off">One-off costs to plan for</h2>
<ul>
<li><strong>Student visa:</strong> the application fee is BBD$300, paid when you apply ({a(IMM_STUDENT, "Barbados Immigration Department")}).</li>
<li><strong>Getting from the airport:</strong> UWI's {a(UWI_GUIDE, "pre-arrival guide")} estimates a taxi from Grantley Adams International Airport to the Cave Hill campus at US$47, with extra charges for additional luggage.</li>
<li><strong>Setting up your room:</strong> halls do not supply linen or kitchen utensils, so budget for these in your first week.</li>
</ul>

<h2 id="everyday">Everyday costs worth knowing</h2>
<ul>
<li><strong>Buses:</strong> a one-way trip is BBD$3.50, however far you travel ({a(UWI_GUIDE, "UWI pre-arrival guide")}).</li>
<li><strong>Tax on purchases:</strong> the standard rate of VAT is 17.5%, and telecommunications services are taxed at 22% ({a(BRA_VAT, "Barbados Revenue Authority")}). The Revenue Authority also keeps a {a(BRA_ZERO, "list of zero-rated items")}.</li>
<li><strong>Health cover:</strong> fully registered UWI students are automatically enrolled in the Campus Medical Assistance Programme. It covers serious illness and accidents, but not dental, vision or preventative care, and it only applies within the Caribbean ({a(UWI_TRAVEL, "UWI Travelling Information")}). BCC includes a BBD$330 medical insurance charge in its fees.</li>
</ul>

<h2 id="proof-of-funds">Why your budget matters for your visa</h2>
<p>Your budget is not only for peace of mind. When you apply for a student visa, the Immigration Department asks for proof of financial support covering your school, living and medical expenses ({a(IMM_STUDENT, "Student Visa requirements")}). International students also cannot rely on a part-time job, which I explain in <a href="working-in-barbados-as-an-international-student.html">Can International Students Work in Barbados?</a> So the numbers above are worth getting right before you apply.</p>

<h2 id="next">Building your plan</h2>
<p>Every student's budget is different. It depends on the school, the program, how you like to live and how often you want to travel home. If you would like help putting real numbers together for your family, <a href="contact.html">book a free consultation</a> and we will work through it with you. And when you are ready for the practical side of daily life, read <a href="barbados-student-life-shopping-and-things-to-know.html">Shopping, Getting Around and Things to Know</a>.</p>
''',
"sources": [
    (CBB_PEG, "Central Bank of Barbados, Fixed for Forty One Years"),
    (UWI_FIN, "UWI Cave Hill International Office, Financial Information"),
    (UWI_FEES, "UWI Cave Hill, 2025/2026 Financial Information for International Students (PDF)"),
    (UWI_TRAVEL, "UWI Cave Hill International Office, Travelling Information"),
    (UWI_GUIDE, "UWI Cave Hill, Pre-arrival Guide, July 2026 (PDF)"),
    (BCC_FEES, "Barbados Community College, Fees"),
    (IMM_STUDENT, "Barbados Immigration Department, Student Visa"),
    (BRA_VAT, "Barbados Revenue Authority, VAT Rates"),
    (BRA_ZERO, "Barbados Revenue Authority, Items Zero Rated for VAT"),
],
},
# ------------------------------------------------------------------ 2. THINGS TO KNOW
{
"slug": "barbados-student-life-shopping-and-things-to-know.html",
"title": "Student Life in Barbados: Shopping, Getting Around and Things to Know",
"seo_title": "Student Life in Barbados: Shopping, Transport and Practical Tips | CIEA",
"desc": "Banking, groceries, buses, weather, plugs, customs and culture: practical, sourced tips for international students moving to Barbados.",
"lede": "Banking, groceries, buses, the weather and the little things that make your first weeks on the island easier.",
"photo": ("chattel-house", "A colourful Barbadian chattel house"),
"read": 7,
"body": f'''
<p>The first few weeks in a new country are full of small questions. Where do I buy groceries? How do the buses work? Will my laptop charger work? I have helped many students settle in, and the ones who arrive knowing the basics relax into island life much faster. Here is what to know, with links to where each fact comes from.</p>

<h2 id="arriving">Arriving</h2>
<ul>
<li><strong>Apply for your student visa early.</strong> Every non-immigrant student needs a student visa before entering Barbados ({a(IMM_STUDENT, "Immigration Department")}). UWI asks students to get applications to Immigration at least three months before the program starts ({a(UWI_TRAVEL, "UWI Travelling Information")}).</li>
<li><strong>Keep key papers in your hand luggage:</strong> your passport, letter of offer, proof of your campus address, original or certified documents and evidence of funds. UWI also advises booking a return ticket rather than one way ({a(UWI_GUIDE, "UWI pre-arrival guide")}).</li>
<li><strong>Bring paperwork for any medicine</strong> and keep it in its original packaging. Without proof of what it is, medication may be confiscated. Luggage can be searched by Customs on arrival, and penalties for illegal drugs, including marijuana, are heavy (same guide).</li>
</ul>

<h2 id="money">Money and banking</h2>
<p>The Barbados dollar is fixed at BBD$2 to US$1 ({a(CBB_PEG, "Central Bank of Barbados")}). UWI recommends opening a local bank account and lists RBC, CIBC, Republic Bank, Scotiabank, First Citizens and Sagicor among the banks on the island. If your home bank has no branch in Barbados, you will usually need a reference letter from your bank, proof of your Barbados address and your student ID. UWI students can request a supporting letter from the university's Customer Service Centre ({a(UWI_GUIDE, "UWI pre-arrival guide")}).</p>

<h2 id="shopping">Shopping and groceries</h2>
<ul>
<li><strong>On campus:</strong> UWI Cave Hill has a cafeteria, a Campus Mart and approved food concessions. There are no meal plans, so most students mix campus food, nearby restaurants and cooking for themselves ({a(UWI_GUIDE, "UWI pre-arrival guide")}, {a(UWI_FAQ, "UWI International Office FAQ")}).</li>
<li><strong>Supermarkets:</strong> UWI points new students to nearby supermarkets including Carlton in Black Rock and Massy in Warrens (pre-arrival guide).</li>
<li><strong>VAT:</strong> the standard rate is 17.5% ({a(BRA_VAT, "Barbados Revenue Authority")}), with a {a(BRA_ZERO, "list of zero-rated items")} that the Revenue Authority publishes.</li>
<li><strong>Bring a reusable kit.</strong> Under the Control of Disposable Plastics Act 2020, single-use straws, forks, knives, spoons, plates and stirrers made from petroleum-based plastic are banned ({a(GIS_PLASTICS, "Government Information Service")}). A reusable bottle, cup and cutlery set is handy.</li>
</ul>
<p>For what all of this adds up to each month, see <a href="cost-of-living-in-barbados-for-students.html">What It Costs to Study and Live in Barbados</a>.</p>

<h2 id="getting-around">Getting around</h2>
<ul>
<li><strong>Buses:</strong> government buses are blue with a yellow stripe, private minibuses are yellow with a blue stripe, and ZR route taxis are white with a maroon stripe. A one-way trip is BBD$3.50, whatever the distance ({a(UWI_GUIDE, "UWI pre-arrival guide")}).</li>
<li><strong>Campus shuttle:</strong> UWI's Office of Student Services and Development runs a shuttle during the semester, which you can follow on the Shuttle Tracker app (same guide).</li>
<li><strong>Driving:</strong> Barbados drives on the left. To drive here you need your valid licence plus a visitor's driving permit, which costs BBD$10 from car rental companies or the Barbados Licensing Authority ({a(VISIT_DRIVE, "Visit Barbados")}).</li>
</ul>

<h2 id="weather">Weather and hurricane season</h2>
<p>Days are usually 27 to 29&deg;C and nights around 23&deg;C. December to May are the driest months, and afternoon showers are common from June to November ({a(UWI_GUIDE, "UWI pre-arrival guide")}). The Atlantic hurricane season runs from 1 June to 30 November ({a(GIS_HURRICANE, "Government Information Service")}). During those months, follow local news and the Department of Emergency Management's advice, and know your school's plan for storms.</p>
<p>Pack light clothes for the heat, plus at least one semi-formal outfit and one set of business clothes for presentations and events (pre-arrival guide).</p>

<h2 id="power">Power and plugs</h2>
<p>Electricity is 110 volts at 50 cycles, and sockets take flat-blade plugs, with or without a grounding pin ({a(UWI_GUIDE, "UWI pre-arrival guide")}). If you are coming from the UK, Africa or Europe, bring adapters, and check the label on your chargers before plugging them in.</p>

<h2 id="health">Health</h2>
<p>Fully registered UWI students are automatically enrolled in the Campus Medical Assistance Programme, which covers serious illness and accidents within the Caribbean but not dental, vision or preventative care ({a(UWI_TRAVEL, "UWI Travelling Information")}). UWI also strongly advises vaccination against varicella, hepatitis B and COVID-19 ({a(UWI_GUIDE, "pre-arrival guide")}). If you have insurance at home, ask whether it can be extended to cover your time in Barbados.</p>

<h2 id="culture">Enjoying the island</h2>
<p>This is the part students remember most. The UWI Cave Hill campus is less than a ten minute walk from the beach ({a(UWI_FAQ, "UWI International Office")}). In summer, Crop Over, a uniquely Barbadian festival of music, arts and food, builds over about three months to Grand Kadooment, the big carnival parade in August ({a(NCF_CROPOVER, "National Cultural Foundation")}). Say yes to invitations, try the food and join a club. That is how Barbados starts to feel like home.</p>

<h2 id="next">We are here to help</h2>
<p>If you have a question this guide does not answer, <a href="contact.html">get in touch</a>. Helping students and parents prepare for life on the island is a big part of what we do. You can also read about <a href="study-in-barbados.html">why students choose Barbados</a> and <a href="working-in-barbados-as-an-international-student.html">the rules on working while you study</a>.</p>
''',
"sources": [
    (IMM_STUDENT, "Barbados Immigration Department, Student Visa"),
    (UWI_TRAVEL, "UWI Cave Hill International Office, Travelling Information"),
    (UWI_GUIDE, "UWI Cave Hill, Pre-arrival Guide, July 2026 (PDF)"),
    (UWI_FAQ, "UWI Cave Hill International Office, FAQ"),
    (CBB_PEG, "Central Bank of Barbados, Fixed for Forty One Years"),
    (BRA_VAT, "Barbados Revenue Authority, VAT Rates"),
    (BRA_ZERO, "Barbados Revenue Authority, Items Zero Rated for VAT"),
    (GIS_PLASTICS, "Government Information Service, Reminder of Ban for Single-Use Plastics"),
    (VISIT_DRIVE, "Visit Barbados, Vehicle Rentals"),
    (GIS_HURRICANE, "Government Information Service, Early Warning Action Can Save Lives"),
    (NCF_CROPOVER, "National Cultural Foundation, The Barbados Crop Over Festival"),
],
},
# ------------------------------------------------------------------ 3. WORK
{
"slug": "working-in-barbados-as-an-international-student.html",
"title": "Can International Students Work in Barbados?",
"seo_title": "Can International Students Work in Barbados? Rules and Options | CIEA",
"desc": "What the law says about working on a Barbados student visa, on-campus work, internships, work permits and the CARICOM Skills Certificate after you graduate.",
"lede": "What the rules say about working on a student visa, and the real options during and after your studies.",
"photo": ("advisor-meeting", "An advisor talking with a student at a table by a sunny window"),
"read": 6,
"body": f'''
<p>Many students hope to pay part of their way with a part-time job, the way students often do in Canada, the UK or the US. Barbados works differently, and it is much better to know that before you arrive than after. Here is what the rules actually say, and what your options look like.</p>

<h2 id="short-answer">The short answer</h2>
<p>In most cases, no. UWI Cave Hill's International Office puts it plainly: <q>International students are not permitted to work in Barbados, except for limited hours on campus</q> ({a(UWI_TRAVEL, "UWI Travelling Information")}).</p>

<h2 id="the-law">What the law says</h2>
<p>The Barbados Immigration Department states that all non-nationals who want to work in Barbados must register with Immigration before they start any job, under Section 17 of the Immigration Act, CAP. 190 ({a(IMM_WORK, "Immigration Department, Work Permits")}). A student visa lets you live in Barbados to study. The {a(IMM_STUDENT, "student visa page")} does not give any right to work.</p>
<p>Work permits are applied for by the employer, not the student. A short-term permit lasts up to eleven months and a long-term permit up to three years. For a long-term permit, the employer has to show that no Barbadian or resident is capable and willing to do the job. The application fee is BBD$300, with a further fee once a permit is granted ({a(IMM_WORK, "Work Permits")}).</p>

<h2 id="plan-funds">Plan your finances without a job</h2>
<p>Because a part-time job is not an option for most international students, the student visa application asks for proof of financial support for your school, living and medical expenses ({a(IMM_STUDENT, "Student Visa requirements")}). Plan for the full cost of your studies up front. Our guide to <a href="cost-of-living-in-barbados-for-students.html">what it costs to study and live in Barbados</a> walks through the numbers.</p>

<h2 id="on-campus">On-campus work</h2>
<p>UWI allows limited hours of work on campus. The details, such as which roles are open and how many hours you can do, are set by your school, so ask the International Office before you accept anything. You can reach UWI Cave Hill's International Office on (246) 417-4972 ({a(UWI_TRAVEL, "UWI Travelling Information")}). If you are at another school, speak to its student services team first.</p>

<h2 id="internships">Internships and placements</h2>
<p>If your program includes a placement with an organisation in Barbados, talk to your school early. Immigration's work permit page lists training attachments under short-term permits, with the same documents required but no final fee ({a(IMM_WORK, "Work Permits")}). Your school will know how this applies to your course.</p>

<h2 id="caricom">If you are a CARICOM national</h2>
<p>Students from CARICOM member states have an important extra route after graduation. Under the free movement of skills, a CARICOM national with a recognised qualification can work in other member states without a work permit by holding a Certificate of Recognition of CARICOM Skills Qualification ({a(BAC_SKILLS, "Barbados Accreditation Council")}).</p>
<ul>
<li><strong>Who qualifies:</strong> the eligible groups include graduates with at least a bachelor's degree from a recognised university, and holders of associate degrees and comparable qualifications, along with nurses, teachers, artisans and others ({a(BAC_GUIDE, "BAC guidelines booklet")}).</li>
<li><strong>Where to apply in Barbados:</strong> the Barbados Accreditation Council issues the certificate. You apply in person, with documents including your birth certificate, passport copy, photos, qualifications and two professional references. There is a $100 application fee, and processing takes at least seven working days ({a(BAC_SKILLS, "BAC, CARICOM Skills Certificate")}).</li>
<li><strong>Then Immigration:</strong> once you have the certificate, you return to the Immigration Department to be granted indefinite entry ({a(BAC_GUIDE, "BAC guidelines booklet")}).</li>
</ul>
<p>Note that this right is tied to working. The Accreditation Council is clear that there is currently no free movement right purely to live in another member state.</p>

<h2 id="after">After you graduate, if you are not from CARICOM</h2>
<p>If you are not a CARICOM national and want to work in Barbados after your studies, you will need an employer to apply for a work permit for you, under the rules above. Rules can change, so always check the latest position with the {a(IMM_WORK, "Immigration Department")} and your school.</p>

<h2 id="make-it-count">Making the most of your time</h2>
<p>Not being able to take a part-time job does not mean you cannot build your future while you study. Many students use the time to focus fully on their grades, join clubs, and build the relationships with lecturers and classmates that lead to references and opportunities later. If you would like to talk through your plans, including your options after graduation, <a href="contact.html">book a free consultation</a>. You can also explore programs in our <a href="course-finder.html">Program Finder</a> or read our <a href="barbados-student-life-shopping-and-things-to-know.html">practical guide to student life</a>.</p>
<p class="note">This article is general information, not legal or immigration advice. Always confirm your own situation with the Barbados Immigration Department and your school.</p>
''',
"sources": [
    (UWI_TRAVEL, "UWI Cave Hill International Office, Travelling Information"),
    (IMM_WORK, "Barbados Immigration Department, Work Permits"),
    (IMM_STUDENT, "Barbados Immigration Department, Student Visa"),
    (BAC_SKILLS, "Barbados Accreditation Council, CARICOM Skills Certificate"),
    (BAC_GUIDE, "Barbados Accreditation Council, Certificate of Recognition of CARICOM Skills Qualification Guidelines (PDF)"),
],
},
]
