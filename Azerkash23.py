{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
import sys\
import time\
import socket\
import requests\
import re\
import phonenumbers\
from phonenumbers import geocoder, carrier, timezone, number_type\
import dns.resolver\
from datetime import datetime\
from colorama import init\
import hashlib\
import random\
from bs4 import BeautifulSoup\
import warnings\
\
warnings.filterwarnings('ignore')\
init(autoreset=True)\
\
CONFIG = \{\
"version": "3.5",\
"author": "@azerkash",\
"dev": "HS777",\
"timeout": 10,\
"user_agents": [\
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",\
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"\
]\
\}\
\
def print_banner():\
    os.system('clear' if os.name != 'nt' else 'cls')\
    colors = ['\\033[38;5;88m', '\\033[38;5;124m', '\\033[38;5;160m', '\\033[38;5;196m', '\\033[91m', '\\033[38;5;196m']\
    banner_lines = [\
        "  _____  _______________________________ ____  __.  _____    _________ ___ ___         ___________________   ________  .____       _________   ______________ ",\
        " /  _  \\\\ \\\\____    /\\\\_   _____/\\\\______   \\\\    |/ _| /  _  \\\\  /   _____//   |   \\\\        \\\\__    ___/\\\\_____  \\\\  \\\\_____  \\\\ |    |     /   _____/  /  |  \\\\______  \\\\",\
        "/  /_\\\\  \\\\  /     /  |    __)_  |       _/      <  /  /_\\\\  \\\\ \\\\_____  \\\\/    ~    \\\\  ______ |    |    /   |   \\\\  /   |   \\\\|    |     \\\\_____  \\\\  /   |  |_  /    /",\
        "/    |    \\\\/     /_  |        \\\\ |    |   \\\\    |  \\\\/    |    \\\\/        \\\\    Y    \\\\ /_____/ |    |   /    |    \\\\/    |    \\\\    |___  /        \\\\/    ^   / /    / ",\
        "\\\\____|__  /_______ \\\\/_______  / |____|_  /____|__ \\\\____|__  /_______  /\\\\___|_  /          |____|   \\\\_______  /\\\\_______  /_______ \\\\/_______  /\\\\____   | /____/  ",\
        "        \\\\/        \\\\/        \\\\/         \\\\/        \\\\/       \\\\/        \\\\/       \\\\/                            \\\\/         \\\\/        \\\\/        \\\\/      |__|          "\
    ]\
\
    for i, line in enumerate(banner_lines):\
        color = colors[min(i, len(colors)-1)]\
        print(f"\{color\}\{line\}\\033[0m")\
\
    print(f"\\n\\033[38;5;196m                          made by \{CONFIG['author']\} | developers: \{CONFIG['dev']\}\\033[0m")\
    print(f"\\033[38;5;160m    [ OSINT FRAMEWORK v\{CONFIG['version']\} | EDUCATIONAL USE ONLY ]\\033[0m\\n")\
\
def loading_animation(text, duration=2):\
    chars = "\'e2\'a0\uc0\u139 \'e2\'a0\u153 \'e2\'a0\'b9\'e2\'a0\'b8\'e2\'a0\'bc\'e2\'a0\'b4\'e2\'a0\'a6\'e2\'a0\'a7\'e2\'a0\u135 \'e2\'a0\u143 "\
    end_time = time.time() + duration\
    i = 0\
    while time.time() < end_time:\
        print(f"\\r\\033[38;5;160m[\{chars[i % len(chars)]\}]\\033[0m \{text\}", end="", flush=True)\
        time.sleep(0.1)\
        i += 1\
    print(f"\\r\\033[38;5;196m[\'e2\uc0\u156 \u147 ]\\033[0m \{text\}\{' ' * 20\}")\
\
def section_header(title):\
    print(f"\\n\\033[38;5;196m\{'\'e2\uc0\u149 \u144 ' * 70\}\\033[0m")\
    print(f"\\033[38;5;160m[ \{title\} ]\\033[0m")\
    print(f"\\033[38;5;196m\{'\'e2\uc0\u149 \u144 ' * 70\}\\033[0m")\
\
def error_msg(msg):\
    print(f"\\033[38;5;196m[!] \{msg\}\\033[0m")\
\
def get_random_ua():\
    return random.choice(CONFIG["user_agents"])\
\
def make_request(url, headers=None, timeout=10):\
    if headers is None:\
        headers = \{"User-Agent": get_random_ua()\}\
    try:\
        return requests.get(url, headers=headers, timeout=timeout)\
    except:\
        return None\
\
def phone_lookup():\
    section_header("01 - PHONE NUMBER LOOKUP")\
    phone = input("\\033[38;5;160m[?] Enter phone number (with country code): \\033[0m").strip()\
    if not phone:\
        return\
\
    try:\
        parsed = phonenumbers.parse(phone)\
        if not phonenumbers.is_valid_number(parsed):\
            error_msg("Invalid phone number")\
            return\
        \
        loading_animation("Querying phone databases", 2)\
        \
        print(f"\\n\\033[38;5;196m[+] PHONE INFORMATION\\033[0m")\
        print(f"    International:    \{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)\}")\
        print(f"    National:         \{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)\}")\
        print(f"    E.164:            \{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)\}")\
        print(f"    Country Code:     +\{parsed.country_code\}")\
        print(f"    National Number:  \{parsed.national_number\}")\
        \
        # Location\
        location = geocoder.description_for_number(parsed, "en")\
        print(f"\\n\\033[38;5;196m[+] LOCATION DATA\\033[0m")\
        print(f"    Region:           \{location\}")\
        \
        # Carrier\
        service = carrier.name_for_number(parsed, "en")\
        if service:\
            print(f"    Carrier:          \{service\}")\
        \
        # Timezone\
        timezones = timezone.time_zones_for_number(parsed)\
        if timezones:\
            print(f"    Timezone:         \{', '.join(timezones)\}")\
        \
        # Number type\
        num_type = number_type(parsed)\
        type_map = \{0: "FIXED_LINE", 1: "MOBILE", 2: "FIXED_LINE_OR_MOBILE", \
                   3: "TOLL_FREE", 4: "PREMIUM_RATE", 6: "VOIP", 10: "UNKNOWN"\}\
        print(f"    Number Type:      \{type_map.get(num_type, 'UNKNOWN')\}")\
        \
        # Online presence\
        national = str(parsed.national_number)\
        cc = str(parsed.country_code)\
        print(f"\\n\\033[38;5;196m[+] ONLINE PRESENCE\\033[0m")\
        print(f"    WhatsApp:         https://wa.me/\{cc\}\{national\}")\
        print(f"    Telegram:         https://t.me/+\{cc\}\{national\}")\
        print(f"    Viber:            https://viber.me/+\{cc\}\{national\}")\
        \
        # Country-specific\
        if parsed.country_code == 33:\
            print(f"\\n\\033[38;5;196m[+] FRENCH NUMBER INTELLIGENCE\\033[0m")\
            if national.startswith('6') or national.startswith('7'):\
                print(f"    Type:             Mobile")\
                if national.startswith(('60', '61')):\
                    print(f"    Operator:         Free Mobile")\
                elif national.startswith(('62', '63')):\
                    print(f"    Operator:         Orange")\
                elif national.startswith(('64', '65')):\
                    print(f"    Operator:         SFR")\
                elif national.startswith(('66', '67')):\
                    print(f"    Operator:         Bouygues")\
        \
        # Additional lookups\
        print(f"\\n\\033[38;5;196m[+] ADDITIONAL RESOURCES\\033[0m")\
        print(f"    Truecaller:       https://www.truecaller.com/search/\{cc\}/\{national\}")\
        print(f"    Whitepages:       https://www.whitepages.com/phone/\{cc\}-\{national\}")\
        \
    except Exception as e:\
        error_msg(str(e))\
\
def email_lookup():\
    section_header("02 - EMAIL LOOKUP")\
    email = input("\\033[38;5;160m[?] Enter email address: \\033[0m").strip().lower()\
    if not re.match(r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$', email):\
        error_msg("Invalid email format")\
        return\
\
    loading_animation("Analyzing email", 1)\
\
    local_part = email.split('@')[0]\
    domain = email.split('@')[1]\
\
    print(f"\\n\\033[38;5;196m[+] EMAIL ANALYSIS\\033[0m")\
    print(f"    Email:            \{email\}")\
    print(f"    Local Part:       \{local_part\}")\
    print(f"    Domain:           \{domain\}")\
    print(f"    MD5 Hash:         \{hashlib.md5(email.encode()).hexdigest()\}")\
\
    # MX Records\
    loading_animation("Querying DNS records", 2)\
    try:\
        mx_records = dns.resolver.resolve(domain, 'MX')\
        print(f"\\n\\033[38;5;196m[+] MAIL SERVER RECORDS\\033[0m")\
        for mx in mx_records:\
            print(f"    Priority \{mx.preference\}: \{mx.exchange\}")\
    except:\
        error_msg("No MX records found")\
\
    # Additional records\
    try:\
        spf = dns.resolver.resolve(domain, 'TXT')\
        for record in spf:\
            if 'v=spf' in str(record):\
                print(f"\\n\\033[38;5;196m[+] SPF RECORD\\033[0m")\
                print(f"    \{record\}")\
    except:\
        pass\
\
    # Profile discovery\
    print(f"\\n\\033[38;5;196m[+] PROFILE DISCOVERY\\033[0m")\
    platforms = \{\
        "GitHub": f"https://github.com/\{local_part\}",\
        "Twitter": f"https://twitter.com/\{local_part\}",\
        "Instagram": f"https://instagram.com/\{local_part\}",\
        "LinkedIn": f"https://linkedin.com/in/\{local_part\}",\
        "Reddit": f"https://reddit.com/user/\{local_part\}",\
        "TikTok": f"https://tiktok.com/@\{local_part\}",\
        "Telegram": f"https://t.me/\{local_part\}",\
        "Steam": f"https://steamcommunity.com/id/\{local_part\}",\
        "Spotify": f"https://open.spotify.com/user/\{local_part\}"\
    \}\
\
    for platform, url in platforms.items():\
        print(f"    \{platform:15\} \{url\}")\
\
    # Pattern variations\
    print(f"\\n\\033[38;5;196m[+] EMAIL VARIATIONS\\033[0m")\
    variations = [\
        f"\{local_part\}@gmail.com",\
        f"\{local_part\}@yahoo.com",\
        f"\{local_part\}@hotmail.com",\
        f"\{local_part\}@outlook.com",\
        f"\{local_part\}@protonmail.com"\
    ]\
    for var in variations:\
        print(f"    \{var\}")\
\
def domain_lookup():\
    section_header("10 - DOMAIN INTELLIGENCE")\
    domain = input("\\033[38;5;160m[?] Enter domain: \\033[0m").strip()\
    domain = domain.replace('http://', '').replace('https://', '').split('/')[0]\
\
    loading_animation("Resolving domain", 1)\
\
    # DNS Resolution\
    try:\
        ip = socket.gethostbyname(domain)\
        print(f"\\n\\033[38;5;196m[+] DNS RESOLUTION\\033[0m")\
        print(f"    Domain:           \{domain\}")\
        print(f"    IP Address:       \{ip\}")\
        \
        # Reverse DNS\
        try:\
            reverse = socket.gethostbyaddr(ip)\
            print(f"    Reverse DNS:      \{reverse[0]\}")\
        except:\
            pass\
    except:\
        error_msg("Domain resolution failed")\
        return\
\
    # WHOIS\
    loading_animation("Querying WHOIS", 2)\
    try:\
        import whois\
        w = whois.whois(domain)\
        \
        print(f"\\n\\033[38;5;196m[+] WHOIS DATA\\033[0m")\
        if w.creation_date:\
            date = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date\
            print(f"    Creation Date:    \{date\}")\
        if w.expiration_date:\
            date = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date\
            print(f"    Expiration:       \{date\}")\
        if w.registrar:\
            print(f"    Registrar:        \{w.registrar\}")\
        if w.name_servers:\
            ns = w.name_servers[0] if isinstance(w.name_servers, list) else w.name_servers\
            print(f"    Nameserver:       \{ns\}")\
        if w.org:\
            print(f"    Organization:     \{w.org\}")\
        if w.country:\
            print(f"    Country:          \{w.country\}")\
    except Exception as e:\
        error_msg(f"WHOIS failed: \{str(e)\}")\
\
    # DNS Records\
    loading_animation("Enumerating DNS", 1)\
    print(f"\\n\\033[38;5;196m[+] DNS RECORDS\\033[0m")\
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']\
    for rtype in record_types:\
        try:\
            answers = dns.resolver.resolve(domain, rtype)\
            values = [str(r) for r in answers][:2]\
            print(f"    \{rtype:6\}           \{', '.join(values)\}")\
        except:\
            pass\
\
    # Subdomain enumeration\
    loading_animation("Testing subdomains", 2)\
    subs = ['www', 'mail', 'ftp', 'admin', 'api', 'blog', 'shop', 'cdn', 'dev']\
    found = []\
    for sub in subs:\
        try:\
            full = f"\{sub\}.\{domain\}"\
            sub_ip = socket.gethostbyname(full)\
            found.append((full, sub_ip))\
        except:\
            pass\
\
    if found:\
        print(f"\\n\\033[38;5;196m[+] DISCOVERED SUBDOMAINS\\033[0m")\
        for sub, ip in found:\
            print(f"    \{sub:20\} \{ip\}")\
\
def ip_lookup():\
    section_header("11 - IP INTELLIGENCE")\
    ip = input("\\033[38;5;160m[?] Enter IP address: \\033[0m").strip()\
\
    try:\
        socket.inet_aton(ip)\
    except:\
        error_msg("Invalid IP address")\
        return\
\
    loading_animation("Querying geolocation", 2)\
\
    # IP-API lookup\
    try:\
        response = requests.get(f"http://ip-api.com/json/\{ip\}", timeout=5)\
        data = response.json()\
        \
        if data.get('status') == 'success':\
            print(f"\\n\\033[38;5;196m[+] GEOLOCATION DATA\\033[0m")\
            print(f"    IP:               \{data.get('query')\}")\
            print(f"    Country:          \{data.get('country')\} (\{data.get('countryCode')\})")\
            print(f"    Region:           \{data.get('regionName')\}")\
            print(f"    City:             \{data.get('city')\}")\
            print(f"    ZIP:              \{data.get('zip')\}")\
            print(f"    Coordinates:      \{data.get('lat')\}, \{data.get('lon')\}")\
            print(f"    Timezone:         \{data.get('timezone')\}")\
            print(f"    ISP:              \{data.get('isp')\}")\
            print(f"    Organization:     \{data.get('org')\}")\
            print(f"    AS:               \{data.get('as')\}")\
            \
            print(f"\\n\\033[38;5;196m[+] MAP LINKS\\033[0m")\
            print(f"    Google Maps:      https://www.google.com/maps?q=\{data.get('lat')\},\{data.get('lon')\}")\
            print(f"    OpenStreetMap:    https://www.openstreetmap.org/?mlat=\{data.get('lat')\}&mlon=\{data.get('lon')\}")\
    except:\
        error_msg("Geolocation lookup failed")\
\
    # Reverse DNS\
    try:\
        hostname = socket.gethostbyaddr(ip)[0]\
        print(f"\\n\\033[38;5;196m[+] REVERSE DNS\\033[0m")\
        print(f"    Hostname:         \{hostname\}")\
    except:\
        pass\
\
    # Port scan\
    loading_animation("Scanning common ports", 3)\
    ports = \{21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS', \
             80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 3306: 'MySQL', \
             3389: 'RDP', 8080: 'HTTP-Alt'\}\
\
    open_ports = []\
    for port, service in ports.items():\
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\
        sock.settimeout(0.3)\
        if sock.connect_ex((ip, port)) == 0:\
            open_ports.append((port, service))\
        sock.close()\
\
    if open_ports:\
        print(f"\\n\\033[38;5;196m[+] OPEN PORTS\\033[0m")\
        for port, service in open_ports:\
            print(f"    Port \{port:5\}/tcp     \{service\} - OPEN")\
\
def username_lookup():\
    section_header("20 - USERNAME INTELLIGENCE")\
    username = input("\\033[38;5;160m[?] Enter username: \\033[0m").strip()\
\
    loading_animation("Searching platforms", 2)\
\
    print(f"\\n\\033[38;5;196m[+] SOCIAL MEDIA PRESENCE\\033[0m")\
\
    sites = [\
        ("Twitter/X", f"https://twitter.com/\{username\}"),\
        ("Instagram", f"https://instagram.com/\{username\}"),\
        ("Facebook", f"https://facebook.com/\{username\}"),\
        ("GitHub", f"https://github.com/\{username\}"),\
        ("LinkedIn", f"https://linkedin.com/in/\{username\}"),\
        ("Reddit", f"https://reddit.com/user/\{username\}"),\
        ("TikTok", f"https://tiktok.com/@\{username\}"),\
        ("YouTube", f"https://youtube.com/@\{username\}"),\
        ("Pinterest", f"https://pinterest.com/\{username\}"),\
        ("Twitch", f"https://twitch.tv/\{username\}"),\
        ("Snapchat", f"https://snapchat.com/add/\{username\}"),\
        ("Telegram", f"https://t.me/\{username\}"),\
        ("Medium", f"https://medium.com/@\{username\}"),\
        ("Steam", f"https://steamcommunity.com/id/\{username\}"),\
        ("Spotify", f"https://open.spotify.com/user/\{username\}"),\
        ("Gravatar", f"https://en.gravatar.com/\{username\}"),\
        ("Keybase", f"https://keybase.io/\{username\}"),\
        ("GitLab", f"https://gitlab.com/\{username\}")\
    ]\
\
    for site, url in sites:\
        print(f"    \{site:18\} \{url\}")\
\
    print(f"\\n\\033[38;5;196m[+] LIKELY EMAILS\\033[0m")\
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'protonmail.com']\
    for domain in domains:\
        print(f"    \{username\}@\{domain\}")\
\
def social_analyzer():\
    section_header("21 - SOCIAL ANALYZER")\
    print("\\033[38;5;160m[!] Enter profile URLs to analyze\\033[0m")\
    url = input("\\033[38;5;160m[?] Profile URL: \\033[0m").strip()\
\
    loading_animation("Fetching profile data", 2)\
\
    try:\
        headers = \{"User-Agent": get_random_ua()\}\
        response = requests.get(url, headers=headers, timeout=5)\
        \
        print(f"\\n\\033[38;5;196m[+] PROFILE DATA\\033[0m")\
        print(f"    URL:              \{url\}")\
        print(f"    Status:           \{response.status_code\}")\
        print(f"    Content-Type:     \{response.headers.get('Content-Type', 'Unknown')\}")\
        print(f"    Server:           \{response.headers.get('Server', 'Unknown')\}")\
        \
        # Parse with BeautifulSoup\
        soup = BeautifulSoup(response.text, 'html.parser')\
        \
        # Extract title\
        title = soup.find('title')\
        if title:\
            print(f"    Page Title:       \{title.string[:50] if title.string else 'N/A'\}")\
        \
        # Extract meta description\
        desc = soup.find('meta', attrs=\{'name': 'description'\})\
        if desc:\
            print(f"    Description:      \{desc.get('content', 'N/A')[:60]\}...")\
        \
        # Extract images\
        images = soup.find_all('img')\
        print(f"\\n\\033[38;5;196m[+] MEDIA FOUND\\033[0m")\
        print(f"    Images:           \{len(images)\}")\
        \
        # Extract links\
        links = soup.find_all('a', href=True)\
        external = [l['href'] for l in links if l['href'].startswith('http')]\
        print(f"    External Links:   \{len(external)\}")\
        \
        if external[:5]:\
            print(f"\\n    Sample links:")\
            for link in external[:3]:\
                print(f"      \'e2\uc0\u134 \u146  \{link[:60]\}...")\
                \
    except Exception as e:\
        error_msg(str(e))\
\
def crypto_tracker():\
    section_header("30 - CRYPTOCURRENCY TRACKER")\
    addr = input("\\033[38;5;160m[?] Enter crypto address: \\033[0m").strip()\
\
    loading_animation("Analyzing blockchain", 2)\
\
    # Detect type\
    if addr.startswith(('1', '3', 'bc1')):\
        coin = "Bitcoin (BTC)"\
        explorer = f"https://www.blockchain.com/btc/address/\{addr\}"\
    elif addr.startswith('0x'):\
        coin = "Ethereum (ETH)"\
        explorer = f"https://etherscan.io/address/\{addr\}"\
    elif addr.startswith(('L', 'M', 'ltc1')):\
        coin = "Litecoin (LTC)"\
        explorer = f"https://blockchair.com/litecoin/address/\{addr\}"\
    elif addr.startswith(('X', '7')):\
        coin = "Dash (DASH)"\
        explorer = f"https://blockchair.com/dash/address/\{addr\}"\
    elif addr.startswith('r'):\
        coin = "Ripple (XRP)"\
        explorer = f"https://bithomp.com/explorer/\{addr\}"\
    else:\
        coin = "Unknown"\
        explorer = "N/A"\
\
    print(f"\\n\\033[38;5;196m[+] BLOCKCHAIN ANALYSIS\\033[0m")\
    print(f"    Address:          \{addr\}")\
    print(f"    Detected:         \{coin\}")\
    print(f"    Explorer:         \{explorer\}")\
\
    print(f"\\n\\033[38;5;196m[+] ADDITIONAL RESOURCES\\033[0m")\
    print(f"    BlockChair:       https://blockchair.com/")\
    print(f"    WalletExplorer:   https://www.walletexplorer.com/")\
    print(f"    Chainalysis:      https://www.chainalysis.com/")\
\
def breach_checker():\
    section_header("31 - BREACH CHECKER")\
    email = input("\\033[38;5;160m[?] Enter email to check: \\033[0m").strip()\
\
    loading_animation("Querying breach databases", 2)\
\
    print(f"\\n\\033[38;5;196m[+] BREACH ANALYSIS\\033[0m")\
    print(f"    Target:           \{email\}")\
    print(f"    Hash (SHA256):    \{hashlib.sha256(email.encode()).hexdigest()[:32]\}...")\
\
    print(f"\\n\\033[38;5;196m[+] CHECK RESOURCES\\033[0m")\
    print(f"    HaveIBeenPwned:   https://haveibeenpwned.com/")\
    print(f"    DeHashed:         https://www.dehashed.com/")\
    print(f"    IntelligenceX:    https://intelx.io/")\
    print(f"    LeakCheck:        https://leakcheck.io/")\
\
    print(f"\\n\\033[38;5;160m[i] Note: Use APIs for actual breach data\\033[0m")\
\
def metadata_extractor():\
    section_header("32 - METADATA EXTRACTOR")\
    filepath = input("\\033[38;5;160m[?] Enter file path: \\033[0m").strip()\
\
    if not os.path.exists(filepath):\
        error_msg("File not found")\
        return\
\
    loading_animation("Analyzing file", 1)\
\
    print(f"\\n\\033[38;5;196m[+] FILE INFORMATION\\033[0m")\
    print(f"    Name:             \{os.path.basename(filepath)\}")\
    print(f"    Path:             \{os.path.abspath(filepath)\}")\
    print(f"    Size:             \{os.path.getsize(filepath):,\} bytes")\
    print(f"    Modified:         \{datetime.fromtimestamp(os.path.getmtime(filepath))\}")\
\
    # Hashes\
    with open(filepath, 'rb') as f:\
        content = f.read()\
        print(f"\\n\\033[38;5;196m[+] FILE HASHES\\033[0m")\
        print(f"    MD5:              \{hashlib.md5(content).hexdigest()\}")\
        print(f"    SHA1:             \{hashlib.sha1(content).hexdigest()\}")\
        print(f"    SHA256:           \{hashlib.sha256(content).hexdigest()\}")\
\
    # Image EXIF\
    ext = os.path.splitext(filepath)[1].lower()\
    if ext in ['.jpg', '.jpeg', '.png', '.tiff']:\
        try:\
            from PIL import Image\
            from PIL.ExifTags import TAGS\
            \
            loading_animation("Extracting EXIF", 1)\
            img = Image.open(filepath)\
            \
            print(f"\\n\\033[38;5;196m[+] IMAGE DATA\\033[0m")\
            print(f"    Format:           \{img.format\}")\
            print(f"    Mode:             \{img.mode\}")\
            print(f"    Size:             \{img.size[0]\}x\{img.size[1]\} pixels")\
            \
            exif = img._getexif()\
            if exif:\
                print(f"\\n\\033[38;5;196m[+] EXIF METADATA\\033[0m")\
                for tag_id, value in exif.items():\
                    tag = TAGS.get(tag_id, tag_id)\
                    if 'GPS' not in tag and len(str(value)) < 50:\
                        print(f"    \{tag:20\} \{value\}")\
                \
                # GPS extraction\
                if 'GPSInfo' in exif:\
                    print(f"\\n\\033[38;5;196m[!] GPS COORDINATES FOUND\\033[0m")\
                    print(f"    Maps:             Check EXIF for lat/lon")\
        except:\
            pass\
\
def settings_menu():\
    section_header("90 - SETTINGS")\
    print("    \\033[38;5;160m[1]\\033[0m Change Timeout")\
    print("    \\033[38;5;160m[2]\\033[0m Toggle User-Agent Rotation")\
    print("    \\033[38;5;160m[3]\\033[0m Clear Cache")\
    print("    \\033[38;5;160m[4]\\033[0m Export Configuration")\
    print("    \\033[38;5;160m[0]\\033[0m Back")\
\
def about():\
    section_header("99 - ABOUT")\
    print(f"\\n    \\033[38;5;196mGOLDEN EAGLE OSINT FRAMEWORK\\033[0m")\
    print(f"    Version:          \{CONFIG['version']\}")\
    print(f"    Author:           \{CONFIG['author']\}")\
    print(f"    Developer:        \{CONFIG['dev']\}")\
    print(f"    Python Version:   \{sys.version.split()[0]\}")\
    print(f"\\n    \\033[38;5;160mThis tool is for educational purposes only.\\033[0m")\
    print(f"    \\033[38;5;160mUse responsibly and legally.\\033[0m")\
\
def main():\
    print_banner()\
    while True:\
        print(f"\\n\\033[38;5;196m\{'\'e2\uc0\u148 \u128 ' * 70\}\\033[0m")\
        print(f"\\033[38;5;160m[ GOLDEN EAGLE v\{CONFIG['version']\} - MAIN MENU ]\\033[0m")\
        print(f"\\033[38;5;196m\{'\'e2\uc0\u148 \u128 ' * 70\}\\033[0m\\n")\
        \
        print("    \\033[38;5;196m[01-09] PHONE & EMAIL INTELLIGENCE\\033[0m")\
        print("    \\033[38;5;160m[01]\\033[0m Phone Lookup              \\033[38;5;160m[02]\\033[0m Email Lookup")\
        print("    \\033[38;5;160m[03]\\033[0m Phone Validator           \\033[38;5;160m[04]\\033[0m Email Pattern Generator")\
        \
        print(f"\\n    \\033[38;5;196m[10-19] DOMAIN & IP INTELLIGENCE\\033[0m")\
        print("    \\033[38;5;160m[10]\\033[0m Domain Lookup             \\033[38;5;160m[11]\\033[0m IP Geolocation")\
        print("    \\033[38;5;160m[12]\\033[0m Subdomain Scanner         \\033[38;5;160m[13]\\033[0m Port Scanner")\
        print("    \\033[38;5;160m[14]\\033[0m DNS Enumeration           \\033[38;5;160m[15]\\033[0m SSL Certificate Analysis")\
        \
        print(f"\\n    \\033[38;5;196m[20-29] USERNAME & SOCIAL INTELLIGENCE\\033[0m")\
        print("    \\033[38;5;160m[20]\\033[0m Username Lookup           \\033[38;5;160m[21]\\033[0m Social Analyzer")\
        print("    \\033[38;5;160m[22]\\033[0m Multi-Platform Search     \\033[38;5;160m[23]\\033[0m Profile Picture Analyzer")\
        \
        print(f"\\n    \\033[38;5;196m[30-39] ADVANCED OSINT\\033[0m")\
        print("    \\033[38;5;160m[30]\\033[0m Crypto Tracker            \\033[38;5;160m[31]\\033[0m Breach Checker")\
        print("    \\033[38;5;160m[32]\\033[0m Metadata Extractor        \\033[38;5;160m[33]\\033[0m Image Reverse Search")\
        print("    \\033[38;5;160m[34]\\033[0m Geolocation Tools         \\033[38;5;160m[35]\\033[0m Technology Detection")\
        print("    \\033[38;5;160m[36]\\033[0m People Search             \\033[38;5;160m[37]\\033[0m Vehicle Lookup")\
        \
        print(f"\\n    \\033[38;5;196m[90-99] SYSTEM\\033[0m")\
        print("    \\033[38;5;160m[90]\\033[0m Settings                  \\033[38;5;160m[99]\\033[0m About")\
        print("    \\033[38;5;160m[00]\\033[0m Exit")\
        \
        choice = input(f"\\n\\033[38;5;196m[?] Select option: \\033[0m").strip()\
        \
        actions = \{\
            "01": phone_lookup, "1": phone_lookup,\
            "02": email_lookup, "2": email_lookup,\
            "10": domain_lookup,\
            "11": ip_lookup,\
            "20": username_lookup,\
            "21": social_analyzer,\
            "30": crypto_tracker,\
            "31": breach_checker,\
            "32": metadata_extractor,\
            "90": settings_menu,\
            "99": about,\
            "00": lambda: sys.exit(0), "0": lambda: sys.exit(0)\
        \}\
        \
        if choice in actions:\
            try:\
                actions[choice]()\
            except KeyboardInterrupt:\
                print(f"\\n\\033[38;5;196m[!] Interrupted\\033[0m")\
            except Exception as e:\
                error_msg(f"Error: \{str(e)\}")\
        else:\
            error_msg("Invalid option")\
\
if __name__ == "__main__":\
    try:\
        main()\
    except KeyboardInterrupt:\
        print(f"\\n\\n\\033[38;5;196m[+] Exiting GOLDEN EAGLE\\033[0m")\
        sys.exit(0)}