# -*- coding: utf-8 -*-
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "index.html")
DOMAIN = "https://peterilles.info"

LANG_ORDER = ["de", "en", "fr", "it", "es", "pt", "hu"]

PATHS = {
    "de": "/",
    "en": "/en/",
    "fr": "/fr/",
    "it": "/it/",
    "es": "/es/",
    "pt": "/pt/",
    "hu": "/hu/",
}

LABELS = {
    "de": "Deutsch", "en": "English", "fr": "Français", "it": "Italiano",
    "es": "Español", "pt": "Português", "hu": "Magyar",
}

HELLO = {
    "de": "Grüezi", "en": "Hello", "fr": "Bonjour", "it": "Buongiorno",
    "es": "Hola", "pt": "Olá", "hu": "Üdv",
}

OG_LOCALE = {
    "de": "de_CH", "en": "en_US", "fr": "fr_FR", "it": "it_IT",
    "es": "es_ES", "pt": "pt_PT", "hu": "hu_HU",
}

SEO = {
    "de": {
        "title": "Dr. med. Peter Illes – Psychiater Zürich | Psychiatrie & Psychotherapie",
        "description": "Dr. med. Peter Illes, Facharzt FMH für Psychiatrie und Psychotherapie in Zürich. Sprechstunde vor Ort oder online, in sieben Sprachen.",
        "og_title": "Dr. med. Peter Illes – Psychiater Zürich",
        "og_description": "Psychiatrie & Psychotherapie in 7 Sprachen. General Wille-Strasse 21, 8002 Zürich.",
    },
    "en": {
        "title": "Dr. med. Peter Illes – Psychiatrist in Zurich | Psychiatry & Psychotherapy",
        "description": "Dr. med. Peter Illes, board-certified psychiatrist (FMH) in Zurich. In-person or online consultations, in seven languages.",
        "og_title": "Dr. med. Peter Illes – Psychiatrist in Zurich",
        "og_description": "Psychiatry & psychotherapy in 7 languages. General Wille-Strasse 21, 8002 Zurich.",
    },
    "fr": {
        "title": "Dr. med. Peter Illes – Psychiatre à Zurich | Psychiatrie & Psychothérapie",
        "description": "Dr. med. Peter Illes, médecin spécialiste FMH en psychiatrie et psychothérapie à Zurich. Consultations sur place ou en ligne, en sept langues.",
        "og_title": "Dr. med. Peter Illes – Psychiatre à Zurich",
        "og_description": "Psychiatrie et psychothérapie en 7 langues. General Wille-Strasse 21, 8002 Zurich.",
    },
    "it": {
        "title": "Dr. med. Peter Illes – Psichiatra a Zurigo | Psichiatria & Psicoterapia",
        "description": "Dr. med. Peter Illes, medico specialista FMH in psichiatria e psicoterapia a Zurigo. Consulenze in studio o online, in sette lingue.",
        "og_title": "Dr. med. Peter Illes – Psichiatra a Zurigo",
        "og_description": "Psichiatria e psicoterapia in 7 lingue. General Wille-Strasse 21, 8002 Zurigo.",
    },
    "es": {
        "title": "Dr. med. Peter Illes – Psiquiatra en Zúrich | Psiquiatría y Psicoterapia",
        "description": "Dr. med. Peter Illes, médico especialista FMH en psiquiatría y psicoterapia en Zúrich. Consultas presenciales u online, en siete idiomas.",
        "og_title": "Dr. med. Peter Illes – Psiquiatra en Zúrich",
        "og_description": "Psiquiatría y psicoterapia en 7 idiomas. General Wille-Strasse 21, 8002 Zúrich.",
    },
    "pt": {
        "title": "Dr. med. Peter Illes – Psiquiatra em Zurique | Psiquiatria e Psicoterapia",
        "description": "Dr. med. Peter Illes, médico especialista FMH em psiquiatria e psicoterapia em Zurique. Consultas presenciais ou online, em sete idiomas.",
        "og_title": "Dr. med. Peter Illes – Psiquiatra em Zurique",
        "og_description": "Psiquiatria e psicoterapia em 7 idiomas. General Wille-Strasse 21, 8002 Zurique.",
    },
    "hu": {
        "title": "Dr. med. Peter Illes – Pszichiáter Zürichben | Pszichiátria és Pszichoterápia",
        "description": "Dr. med. Peter Illes, FMH szakorvos pszichiátria és pszichoterápia területén, Zürichben. Személyes vagy online konzultáció, hét nyelven.",
        "og_title": "Dr. med. Peter Illes – Pszichiáter Zürichben",
        "og_description": "Pszichiátria és pszichoterápia 7 nyelven. General Wille-Strasse 21, 8002 Zürich.",
    },
}

print("Script scaffold written OK")

T = {
  "pt": {
    "kicker": "Psiquiatria & Psicoterapia · Zurique",
    "heroLead": "Terapia na sua língua materna",
    "langsBody": "As consultas são possíveis nas seguintes línguas:",
    "approachTitle": "A minha abordagem",
    "approachBody": "O meu consultório é um lugar de calma. É recebido com abertura e sem preconceitos. Juntos procuramos o caminho que corresponde às suas necessidades.",
    "offerTitle": "O que ofereço",
    "offerBody": "Psicoterapia médica e farmacoterapia – <strong>presencialmente ou online</strong>",
    "methodsTitle": "Métodos",
    "methodsPrimary": ["Terapia cognitivo-comportamental (TCC)", "Terapia de orientação psicanalítica"],
    "methods": ["Métodos imaginativos", "Psicodrama", "Técnicas de relaxamento"],
    "focusTitle": "Áreas de foco",
    "focus": ["PHDA e perturbações neuropsiquiátricas relacionadas", "Perturbações de ansiedade", "Perturbações de personalidade incluindo perturbação borderline", "Depressão", "Perturbações de adaptação", "Perturbações relacionadas com trauma", "Psicoses"],
    "practicalTitle": "Informações práticas",
    "hoursLabel": "Horário de consulta", "hoursValue": "Mediante marcação<br>segunda a sexta-feira<br>presencialmente ou online",
    "feesLabel": "Honorários", "feesValue": "Segundo a tarifa suíça TARDOC",
    "insuranceLabel": "Seguro de saúde", "insuranceValue": "Reconhecido pelo seguro básico suíço (LAMal/KVG)",
    "accessLabel": "Como chegar", "accessValue": "Localização central, perto da estação de Enge e do Museu FIFA",
    "addressLabel": "Endereço", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Inscrição",
    "contactBody": "Partilhe comigo a sua situação e responderei pessoalmente.",
    "telLabel": "Telefone", "emailLabel": "E-mail",
    "fName": "O seu nome", "fEmail": "E-mail", "fPhone": "Telefone", "fConcern": "O que o traz aqui?",
    "fSubmit": "Enviar pedido", "fThanks": "Obrigado! Responderei pessoalmente em breve.",
  },
  "es": {
    "kicker": "Psiquiatría & Psicoterapia · Zúrich",
    "heroLead": "Terapia en su lengua materna",
    "langsBody": "Las consultas son posibles en los siguientes idiomas:",
    "approachTitle": "Mi enfoque",
    "approachBody": "Mi consulta es un lugar de calma. Es recibido con apertura y sin prejuicios. Juntos buscamos el camino que corresponde a sus necesidades.",
    "offerTitle": "Lo que ofrezco",
    "offerBody": "Psicoterapia médica y farmacoterapia – <strong>en consulta o en línea</strong>",
    "methodsTitle": "Métodos",
    "methodsPrimary": ["Terapia cognitivo-conductual (TCC)", "Terapia de orientación psicoanalítica"],
    "methods": ["Métodos imaginativos", "Psicodrama", "Técnicas de relajación"],
    "focusTitle": "Áreas de enfoque",
    "focus": ["TDAH y trastornos neuropsiquiátricos relacionados", "Trastornos de ansiedad", "Trastornos de personalidad incluido el trastorno límite", "Depresión", "Trastornos adaptativos", "Trastornos relacionados con el trauma", "Psicosis"],
    "practicalTitle": "Información práctica",
    "hoursLabel": "Horario de consulta", "hoursValue": "Con cita previa<br>lunes a viernes<br>en consulta o en línea",
    "feesLabel": "Honorarios", "feesValue": "Según la tarifa suiza TARDOC",
    "insuranceLabel": "Seguro médico", "insuranceValue": "Reconocido por el seguro básico suizo (LAMal/KVG)",
    "accessLabel": "Cómo llegar", "accessValue": "Ubicación céntrica, cerca de la estación de Enge y del Museo FIFA",
    "addressLabel": "Dirección", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Inscripción",
    "contactBody": "Comparta conmigo su consulta y le responderé personalmente.",
    "telLabel": "Teléfono", "emailLabel": "Correo electrónico",
    "fName": "Tu nombre", "fEmail": "Correo electrónico", "fPhone": "Teléfono", "fConcern": "¿Qué le trae aquí?",
    "fSubmit": "Enviar solicitud", "fThanks": "¡Gracias! Le responderé personalmente en breve.",
  },
  "fr": {
    "kicker": "Psychiatrie & Psychothérapie · Zurich",
    "heroLead": "Une thérapie dans votre langue maternelle",
    "langsBody": "Les consultations sont possibles dans les langues suivantes :",
    "approachTitle": "Mon approche",
    "approachBody": "Mon cabinet est un lieu de calme. Vous êtes accueilli avec ouverture et sans préjugés. Ensemble, nous cherchons le chemin qui correspond à vos besoins.",
    "offerTitle": "Ce que je propose",
    "offerBody": "Psychothérapie médicale et pharmacothérapie – <strong>en cabinet ou en ligne</strong>",
    "methodsTitle": "Méthodes",
    "methodsPrimary": ["Thérapie cognitivo-comportementale (TCC)", "Thérapie d'orientation psychanalytique"],
    "methods": ["Méthodes imaginatives", "Psychodrame", "Techniques de relaxation"],
    "focusTitle": "Domaines de spécialité",
    "focus": ["TDAH et troubles neuropsychiatriques associés", "Troubles anxieux", "Troubles de la personnalité dont trouble borderline", "Dépression", "Troubles de l'adaptation", "Troubles liés au trauma", "Psychoses"],
    "practicalTitle": "Informations pratiques",
    "hoursLabel": "Heures de consultation", "hoursValue": "Sur rendez-vous<br>du lundi au vendredi<br>en cabinet ou en ligne",
    "feesLabel": "Honoraires", "feesValue": "Selon le tarif suisse TARDOC",
    "insuranceLabel": "Assurance maladie", "insuranceValue": "Reconnu par l'assurance de base suisse (LAMal/KVG)",
    "accessLabel": "Accès", "accessValue": "Situation centrale, à proximité de la gare d'Enge et du Musée FIFA",
    "addressLabel": "Adresse", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Inscription",
    "contactBody": "Faites-moi part de votre demande et je vous répondrai personnellement.",
    "telLabel": "Téléphone", "emailLabel": "E-mail",
    "fName": "Votre nom", "fEmail": "E-mail", "fPhone": "Téléphone", "fConcern": "Qu'est-ce qui vous amène ?",
    "fSubmit": "Envoyer la demande", "fThanks": "Merci ! Je vous répondrai personnellement dans les meilleurs délais.",
  },
  "it": {
    "kicker": "Psichiatria & Psicoterapia · Zurigo",
    "heroLead": "Una terapia nella sua lingua madre",
    "langsBody": "Le consultazioni sono possibili nelle seguenti lingue:",
    "approachTitle": "Il mio approccio",
    "approachBody": "Il mio studio è un luogo di calma. Viene accolto con apertura e senza pregiudizi. Insieme cerchiamo il percorso che corrisponde alle sue esigenze.",
    "offerTitle": "Cosa offro",
    "offerBody": "Psicoterapia medica e farmacoterapia – <strong>in studio o online</strong>",
    "methodsTitle": "Metodi",
    "methodsPrimary": ["Terapia cognitivo-comportamentale (TCC)", "Terapia a orientamento psicoanalitico"],
    "methods": ["Metodi immaginativi", "Psicodramma", "Tecniche di rilassamento"],
    "focusTitle": "Aree di specializzazione",
    "focus": ["ADHD e disturbi neuropsichiatrici correlati", "Disturbi d'ansia", "Disturbi di personalità incluso il disturbo borderline", "Depressione", "Disturbi dell'adattamento", "Disturbi correlati al trauma", "Psicosi"],
    "practicalTitle": "Informazioni pratiche",
    "hoursLabel": "Orari di consultazione", "hoursValue": "Su appuntamento<br>dal lunedì al venerdì<br>in studio o online",
    "feesLabel": "Onorari", "feesValue": "Secondo la tariffa svizzera TARDOC",
    "insuranceLabel": "Assicurazione", "insuranceValue": "Riconosciuto dall'assicurazione di base svizzera (LAMal/KVG)",
    "accessLabel": "Come arrivare", "accessValue": "Posizione centrale, vicino alla stazione di Enge e al Museo FIFA",
    "addressLabel": "Indirizzo", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Iscrizione",
    "contactBody": "Mi comunichi la sua richiesta e le risponderò personalmente.",
    "telLabel": "Telefono", "emailLabel": "E-mail",
    "fName": "Il tuo nome", "fEmail": "E-mail", "fPhone": "Telefono", "fConcern": "Cosa la porta qui?",
    "fSubmit": "Invia richiesta", "fThanks": "Grazie! Le risponderò personalmente a breve.",
  },
  "de": {
    "kicker": "Psychiatrie & Psychotherapie · Zürich",
    "heroLead": "Therapie in Ihrer Muttersprache",
    "langsBody": "Konsultationen sind in folgenden Sprachen möglich:",
    "approachTitle": "Meine Haltung",
    "approachBody": "Meine Praxis ist ein Ort der Ruhe. Sie werden mit Offenheit und ohne Vorurteil empfangen. Gemeinsam suchen wir den Weg, der Ihren Bedürfnissen entspricht.",
    "offerTitle": "Mein Angebot",
    "offerBody": "Ärztliche Psycho- und Pharmakotherapie – <strong>vor Ort oder Online</strong>",
    "methodsTitle": "Methoden",
    "methodsPrimary": ["Kognitive Verhaltenstherapie (KVT)", "Psychoanalytisch-orientierte Therapie"],
    "methods": ["Imaginative Verfahren", "Psychodrama", "Entspannungsverfahren"],
    "focusTitle": "Schwerpunkte",
    "focus": ["ADHS und verwandte neuropsychiatrische Störungen", "Angststörungen", "Persönlichkeitsstörungen einschliesslich Borderline-Störung", "Depressionen", "Anpassungsstörungen", "Traumafolgestörungen", "Psychosen"],
    "practicalTitle": "Praktische Informationen",
    "hoursLabel": "Sprechzeiten", "hoursValue": "Nach Vereinbarung<br>Montag bis Freitag<br>Vor Ort oder Online",
    "feesLabel": "Honorar", "feesValue": "Nach schweizerischem TARDOC-Tarif",
    "insuranceLabel": "Krankenversicherung", "insuranceValue": "Anerkannt durch die schweizerische Grundversicherung (KVG)",
    "accessLabel": "Anfahrt", "accessValue": "Zentral gelegen, unweit des Bahnhofs Enge und des FIFA-Museums",
    "addressLabel": "Adresse", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Anmeldung",
    "contactBody": "Teilen Sie mir Ihr Anliegen, und ich melde mich persönlich bei Ihnen.",
    "telLabel": "Telefon", "emailLabel": "E-Mail",
    "fName": "Ihr Name", "fEmail": "E-Mail", "fPhone": "Telefon", "fConcern": "Was führt Sie zu mir?",
    "fSubmit": "Anfrage senden", "fThanks": "Danke! Ich melde mich zeitnah bei Ihnen.",
  },
  "en": {
    "kicker": "Psychiatry & Psychotherapy · Zurich",
    "heroLead": "Therapy in your mother tongue",
    "langsBody": "Consultations are possible in the following languages:",
    "approachTitle": "My approach",
    "approachBody": "My office is a place of calm. You will be received with openness and without prejudice. Together we define the methods that best correspond to your needs.",
    "offerTitle": "What I offer",
    "offerBody": "Medical psycho- and pharmacotherapy – <strong>in person or online</strong>",
    "methodsTitle": "Methods",
    "methodsPrimary": ["Cognitive behavioural therapy (CBT)", "Psychoanalytically oriented therapy"],
    "methods": ["Imaginative methods", "Psychodrama", "Relaxation techniques"],
    "focusTitle": "Areas of focus",
    "focus": ["ADHD and related neuropsychiatric disorders", "Anxiety disorders", "Personality disorders including borderline disorder", "Depression", "Adjustment disorders", "Trauma-related disorders", "Psychoses"],
    "practicalTitle": "Practical information",
    "hoursLabel": "Consultation hours", "hoursValue": "By appointment<br>Monday to Friday<br>in person or online",
    "feesLabel": "Fees", "feesValue": "According to the Swiss TARDOC tariff",
    "insuranceLabel": "Health insurance", "insuranceValue": "Recognised by Swiss basic insurance (KVG)",
    "accessLabel": "Getting here", "accessValue": "Centrally located, close to Enge station and the FIFA Museum",
    "addressLabel": "Address", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Registration",
    "contactBody": "Share your concern with me and I will get back to you personally.",
    "telLabel": "Phone", "emailLabel": "Email",
    "fName": "Your name", "fEmail": "Email", "fPhone": "Phone", "fConcern": "What brings you here?",
    "fSubmit": "Send request", "fThanks": "Thank you! I will get back to you personally shortly.",
  },
  "hu": {
    "kicker": "Pszichiátria & Pszichoterápia · Zürich",
    "heroLead": "Terápia az anyanyelvén",
    "langsBody": "A konzultációk az alábbi nyelveken lehetségesek:",
    "approachTitle": "A szemléletem",
    "approachBody": "A rendelőm a nyugalom helye. Nyitottsággal és előítéletek nélkül fogadom. Együtt keressük az Ön igényeinek megfelelő utat.",
    "offerTitle": "Amit nyújtok",
    "offerBody": "Orvosi pszicho- és farmakoterápia – <strong>személyesen vagy online</strong>",
    "methodsTitle": "Módszerek",
    "methodsPrimary": ["Kognitív viselkedésterápia (KVT)", "Pszichoanalitikusan orientált terápia"],
    "methods": ["Imaginatív eljárások", "Pszichodráma", "Relaxációs technikák"],
    "focusTitle": "Fő területek",
    "focus": ["ADHD és kapcsolódó neuropszichiátriai zavarok", "Szorongásos zavarok", "Személyiségzavarok, beleértve a borderline zavart", "Depresszió", "Alkalmazkodási zavarok", "Traumával összefüggő zavarok", "Pszichózisok"],
    "practicalTitle": "Gyakorlati tudnivalók",
    "hoursLabel": "Rendelési idő", "hoursValue": "Előzetes egyeztetés alapján<br>hétfőtől péntekig<br>személyesen vagy online",
    "feesLabel": "Honorárium", "feesValue": "A svájci TARDOC tarifa szerint",
    "insuranceLabel": "Egészségbiztosítás", "insuranceValue": "A svájci alapbiztosítás (KVG) által elismert",
    "accessLabel": "Megközelítés", "accessValue": "Központi elhelyezkedés, az Enge állomás és a FIFA Múzeum közelében",
    "addressLabel": "Cím", "addressValue": "General Wille-Strasse 21, 8002 Zürich",
    "contactTitle": "Bejelentkezés",
    "contactBody": "Ossza meg velem az ügyét, és személyesen válaszolok.",
    "telLabel": "Telefon", "emailLabel": "E-mail",
    "fName": "Az Ön neve", "fEmail": "E-mail", "fPhone": "Telefon", "fConcern": "Mi hozta ide?",
    "fSubmit": "Kérés elküldése", "fThanks": "Köszönöm! Hamarosan személyesen jelentkezem.",
  },
}

print("T dict OK, langs:", list(T.keys()))

def flag_svg(code):
    a = 'width="20" height="13" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"'
    def v3(c1,c2,c3): return f'<svg {a} viewBox="0 0 3 2"><rect x="0" width="1" height="2" fill="{c1}"/><rect x="1" width="1" height="2" fill="{c2}"/><rect x="2" width="1" height="2" fill="{c3}"/></svg>'
    def hz3(c1,c2,c3): return f'<svg {a} viewBox="0 0 3 2"><rect y="0" width="3" height="0.667" fill="{c1}"/><rect y="0.667" width="3" height="0.667" fill="{c2}"/><rect y="1.333" width="3" height="0.667" fill="{c3}"/></svg>'
    if code == "fr": return v3("#0055A4","#FFFFFF","#EF4135")
    if code == "it": return v3("#008C45","#F4F5F0","#CD212A")
    if code == "de": return hz3("#000000","#DD0000","#FFCE00")
    if code == "hu": return hz3("#CD2A3E","#FFFFFF","#436F4D")
    if code == "es": return f'<svg {a} viewBox="0 0 3 2"><rect width="3" height="2" fill="#AA151B"/><rect y="0.5" width="3" height="1" fill="#F1BF00"/></svg>'
    if code == "pt": return f'<svg {a} viewBox="0 0 60 40"><rect width="60" height="40" fill="#046A38"/><rect x="24" width="36" height="40" fill="#DA291C"/><circle cx="24" cy="20" r="7" fill="#FFD100"/><circle cx="24" cy="20" r="3.2" fill="#DA291C"/></svg>'
    if code == "en": return f'<svg {a} viewBox="0 0 60 30"><rect width="60" height="30" fill="#012169"/><path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/><path d="M0,0 L60,30 M60,0 L0,30" stroke="#C8102E" stroke-width="2"/><path d="M30,0 V30 M0,15 H60" stroke="#fff" stroke-width="10"/><path d="M30,0 V30 M0,15 H60" stroke="#C8102E" stroke-width="6"/></svg>'
    return ""

def build_pills(current):
    out = []
    for code in LANG_ORDER:
        active = " active" if code == current else ""
        out.append(f'<a class="pill{active}" href="{PATHS[code]}" aria-label="{LABELS[code]}">{flag_svg(code)} {LABELS[code]}</a>')
    return "".join(out)

def build_cards(current):
    out = []
    for code in LANG_ORDER:
        active = " active" if code == current else ""
        out.append(f'<a class="lang-card{active}" href="{PATHS[code]}" aria-label="{LABELS[code]}"><span class="lang-card-hello">{HELLO[code]}</span><span class="lang-card-label">{LABELS[code]}</span></a>')
    return "".join(out)

def build_methods(tr):
    primary = "".join(f'<span class="method-tag-primary">{m}</span>' for m in tr.get("methodsPrimary", []))
    secondary = "".join(f'<span class="method-tag">{m}</span>' for m in tr.get("methods", []))
    return f'<div class="methods-primary-row">{primary}</div><div class="methods-secondary-row">{secondary}</div>'

def build_focus(tr):
    return "".join(f'<span class="focus-tag">{f}</span>' for f in tr["focus"])

def build_hreflang(self_code=None):
    lines = []
    for code in LANG_ORDER:
        lines.append(f'  <link rel="alternate" hreflang="{code}" href="{DOMAIN}{PATHS[code]}">')
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{DOMAIN}/">')
    return "\n".join(lines)

def build_jsonld(lang, url):
    lang_names = {"de":"German","en":"English","fr":"French","it":"Italian","es":"Spanish","pt":"Portuguese","hu":"Hungarian"}
    data = {
        "@context": "https://schema.org",
        "@type": "Physician",
        "@id": f"{DOMAIN}/#physician",
        "name": "Dr. med. Peter Illes",
        "medicalSpecialty": "https://schema.org/Psychiatric",
        "url": url,
        "image": f"{DOMAIN}/dr-illes-portrait.webp",
        "telephone": "+41442116871",
        "email": "mailto:dr.peter.illes@hin.ch",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "General Wille-Strasse 21",
            "postalCode": "8002",
            "addressLocality": "Zürich",
            "addressCountry": "CH"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 47.36374597116766,
            "longitude": 8.529243776901244
        },
        "hasMap": "https://www.google.com/maps/search/?api=1&query=General+Wille-Strasse+21%2C+8002+Z%C3%BCrich",
        "availableLanguage": [lang_names[c] for c in LANG_ORDER]
    }
    return json.dumps(data, ensure_ascii=False, indent=2)

print("Helper functions OK")

with open(SRC, "r", encoding="utf-8") as f:
    template = f.read()

def render_page(lang):
    tr = T[lang]
    seo = SEO[lang]
    url = f"{DOMAIN}{PATHS[lang]}"
    html = template

    # --- HEAD ---
    html = html.replace('<html lang="pt">', f'<html lang="{lang}">')
    html = re.sub(r'<title>.*?</title>', f'<title>{seo["title"]}</title>', html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{seo["description"]}">', html, count=1, flags=re.S)
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">\n\n  <!-- hreflang alternates -->\n{build_hreflang()}', html, count=1, flags=re.S)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{seo["og_title"]}">', html, count=1, flags=re.S)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{seo["og_description"]}">', html, count=1, flags=re.S)
    html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">\n  <meta property="og:locale" content="{OG_LOCALE[lang]}">', html, count=1, flags=re.S)

    jsonld = f'\n  <script type="application/ld+json">\n{build_jsonld(lang, url)}\n  </script>\n</head>'
    html = html.replace("</head>", jsonld, 1)

    # --- IMAGE PATH (root-relative so it works from subfolders) ---
    html = html.replace('src="dr-illes-portrait.webp"', 'src="/dr-illes-portrait.webp"')

    # --- BODY: pre-render text so content matches URL language even without JS ---
    repl = {
        '<div id="hero-kicker"></div>': f'<div id="hero-kicker">{tr["kicker"]}</div>',
        '<h1 id="hero-lead"></h1>': f'<h1 id="hero-lead">{tr["heroLead"]}</h1>',
        '<a href="#contact" id="hero-cta"></a>': f'<a href="#contact" id="hero-cta">{tr["contactTitle"]} <span style="font-size:18px">→</span></a>',
        '<p id="langs-body"></p>': f'<p id="langs-body">{tr["langsBody"]}</p>',
        '<div id="lang-cards"></div>': f'<div id="lang-cards">{build_cards(lang)}</div>',
        '<h2 id="approach-kicker"></h2>': f'<h2 id="approach-kicker">{tr["approachTitle"]}</h2>',
        '<p id="approach-body"></p>': f'<p id="approach-body">{tr["approachBody"]}</p>',
        '<h2 id="offer-kicker"></h2>': f'<h2 id="offer-kicker">{tr["offerTitle"]}</h2>',
        '<p id="offer-body"></p>': f'<p id="offer-body">{tr["offerBody"]}</p>',
        '<div id="methods-title"></div>': f'<div id="methods-title">{tr["methodsTitle"]}</div>',
        '<div id="methods-list"></div>': f'<div id="methods-list">{build_methods(tr)}</div>',
        '<h2 id="focus-title"></h2>': f'<h2 id="focus-title">{tr["focusTitle"]}</h2>',
        '<div id="focus-list"></div>': f'<div id="focus-list">{build_focus(tr)}</div>',
        '<h2 id="practical-title"></h2>': f'<h2 id="practical-title">{tr["practicalTitle"]}</h2>',
        '<div class="info-label" id="hours-label"></div>': f'<div class="info-label" id="hours-label">{tr["hoursLabel"]}</div>',
        '<div class="info-value" id="hours-value"></div>': f'<div class="info-value" id="hours-value">{tr["hoursValue"]}</div>',
        '<div class="info-label" id="fees-label"></div>': f'<div class="info-label" id="fees-label">{tr["feesLabel"]}</div>',
        '<div class="info-value" id="fees-value"></div>': f'<div class="info-value" id="fees-value">{tr["feesValue"]}</div>',
        '<div class="info-label" id="insurance-label"></div>': f'<div class="info-label" id="insurance-label">{tr["insuranceLabel"]}</div>',
        '<div class="info-value" id="insurance-value"></div>': f'<div class="info-value" id="insurance-value">{tr["insuranceValue"]}</div>',
        '<div class="info-label" id="access-label"></div>': f'<div class="info-label" id="access-label">{tr["accessLabel"]}</div>',
        '<div class="info-value" id="access-value"></div>': f'<div class="info-value" id="access-value">{tr["accessValue"]}</div>',
        '<div class="info-label" id="address-label"></div>': f'<div class="info-label" id="address-label">{tr["addressLabel"]}</div>',
        '<div class="info-value" id="address-value"></div>': f'<div class="info-value" id="address-value">{tr["addressValue"]}</div>',
        '<div class="info-label" id="tel-label"></div>': f'<div class="info-label" id="tel-label">{tr["telLabel"]}</div>',
        '<div class="info-label" id="email-label"></div>': f'<div class="info-label" id="email-label">{tr["emailLabel"]}</div>',
        '<h2 id="contact-title"></h2>': f'<h2 id="contact-title">{tr["contactTitle"]}</h2>',
        '<p id="contact-body"></p>': f'<p id="contact-body">{tr["contactBody"]}</p>',
        '<input name="name" required id="f-name">': f'<input name="name" required id="f-name" placeholder="{tr["fName"]}">',
        '<input name="email" type="email" required id="f-email">': f'<input name="email" type="email" required id="f-email" placeholder="{tr["fEmail"]}">',
        '<input name="phone" id="f-phone">': f'<input name="phone" id="f-phone" placeholder="{tr["fPhone"]}">',
        '<textarea name="concern" rows="4" id="f-concern"></textarea>': f'<textarea name="concern" rows="4" id="f-concern" placeholder="{tr["fConcern"]}"></textarea>',
        '<button type="submit" id="f-submit"></button>': f'<button type="submit" id="f-submit">{tr["fSubmit"]}</button>',
        '<nav id="lang-pills" aria-label="language"></nav>': f'<nav id="lang-pills" aria-label="language">{build_pills(lang)}</nav>',
    }
    for old, new in repl.items():
        if old not in html:
            raise ValueError(f"Pattern not found for lang={lang}: {old[:60]}")
        html = html.replace(old, new, 1)

    # --- JS: fix initial language (no localStorage override -> always matches URL) ---
    html = html.replace(
        'let currentLang = "pt";\ntry { const s = localStorage.getItem("illes_lang"); if (s && t[s]) currentLang = s; } catch(e) {}',
        f'let currentLang = "{lang}";'
    )

    # add langUrls map right after the langs array definition
    langurls_js = "const langUrls = " + json.dumps(PATHS, ensure_ascii=False) + ";\n"
    html = html.replace("const t = {", langurls_js + "\nconst t = {", 1)

    # switch pill/card generation from buttons+onclick to real <a href> links
    html = html.replace(
        '''document.getElementById("lang-pills").innerHTML = langs.map(L =>
    `<button class="pill${L.code===lang?" active":""}" onclick="render('${L.code}')" aria-label="${L.label}">
      ${flagSVG(L.code)}${L.extraFlag ? ' '+flagSVG(L.extraFlag) : ''} ${L.label}
    </button>`
  ).join("");''',
        '''document.getElementById("lang-pills").innerHTML = langs.map(L =>
    `<a class="pill${L.code===lang?" active":""}" href="${langUrls[L.code]}" aria-label="${L.label}">
      ${flagSVG(L.code)}${L.extraFlag ? ' '+flagSVG(L.extraFlag) : ''} ${L.label}
    </a>`
  ).join("");'''
    )
    html = html.replace(
        '''document.getElementById("lang-cards").innerHTML = langs.map(L =>
    `<button class="lang-card${L.code===lang?" active":""}" onclick="render('${L.code}')" aria-label="${L.label}">
      <span class="lang-card-hello">${L.hello}</span>
      <span class="lang-card-label">${L.label}</span>
    </button>`
  ).join("");''',
        '''document.getElementById("lang-cards").innerHTML = langs.map(L =>
    `<a class="lang-card${L.code===lang?" active":""}" href="${langUrls[L.code]}" aria-label="${L.label}">
      <span class="lang-card-hello">${L.hello}</span>
      <span class="lang-card-label">${L.label}</span>
    </a>`
  ).join("");'''
    )

    return html

os.makedirs(os.path.join(BASE, "en"), exist_ok=True)
os.makedirs(os.path.join(BASE, "fr"), exist_ok=True)
os.makedirs(os.path.join(BASE, "it"), exist_ok=True)
os.makedirs(os.path.join(BASE, "es"), exist_ok=True)
os.makedirs(os.path.join(BASE, "pt"), exist_ok=True)
os.makedirs(os.path.join(BASE, "hu"), exist_ok=True)

OUT_PATHS = {
    "de": os.path.join(BASE, "index.html"),
    "en": os.path.join(BASE, "en", "index.html"),
    "fr": os.path.join(BASE, "fr", "index.html"),
    "it": os.path.join(BASE, "it", "index.html"),
    "es": os.path.join(BASE, "es", "index.html"),
    "pt": os.path.join(BASE, "pt", "index.html"),
    "hu": os.path.join(BASE, "hu", "index.html"),
}

for lang in LANG_ORDER:
    out = render_page(lang)
    with open(OUT_PATHS[lang], "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT_PATHS[lang]} ({len(out)} chars)")

print("ALL PAGES GENERATED OK")
