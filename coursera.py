data = [{'week 1': [{'module 1': {'description': '', 'total_videos': 3, 'total_quizzes': 0, 'total_duration': 1715000, 'total_lecture_duration': 1115000, 'total_readings': 1, 'other_details': [{'id': 'XMN6o', 'duration': 70000, 'name': 'Welcome to Advanced Python for Cybersecurity', 'typeName': 'lecture', 'slug': 'welcome-to-advanced-python-for-cybersecurity', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'xOdb1', 'duration': 416000, 'name': 'Introduction to Python', 'typeName': 'lecture', 'slug': 'introduction-to-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'Z00bu', 'duration': 600000, 'name': 'Advanced Python for Cybersecurity Handout', 'typeName': 'supplement', 'slug': 'advanced-python-for-cybersecurity-handout', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'fEF11', 'duration': 629000, 'name': 'Introduction to MITRE ATT&CK and SHIELD', 'typeName': 'lecture', 'slug': 'introduction-to-mitre-att-ck-and-shield', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}]}}]}, {'week 2': [{'module 1': {'description': '', 'total_videos': 6, 'total_quizzes': 0, 'total_duration': 5218000, 'total_lecture_duration': 5218000, 'total_readings': 0, 'other_details': [{'id': '28GEP', 'duration': 804000, 'name': 'Introduction to Reconnaissance', 'typeName': 'lecture', 'slug': 'introduction-to-reconnaissance', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'U3p5a', 'duration': 863000, 'name': 'Querying Shodan with Python', 'typeName': 'lecture', 'slug': 'querying-shodan-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'dmYgQ', 'duration': 863000, 'name': 'DNS Queries with Python', 'typeName': 'lecture', 'slug': 'dns-queries-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'N67Q2', 'duration': 1002000, 'name': 'Network Scanning with Scapy', 'typeName': 'lecture', 'slug': 'network-scanning-with-scapy', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'l063g', 'duration': 1283000, 'name': 'Service Detection with Python', 'typeName': 'lecture', 'slug': 'service-detection-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'd0VBy', 'duration': 403000, 'name': 'CVE Lookups with Python', 'typeName': 'lecture', 'slug': 'cve-lookups-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}]}}]}, {'week 3': [{'module 1': {'description': '', 'total_videos': 4, 'total_quizzes': 1, 'total_duration': 4719000, 'total_lecture_duration': 2919000, 'total_readings': 0, 'other_details': [{'id': 'nVG5d', 'duration': 787000, 'name': 'Introduction to Initial Access', 'typeName': 'lecture', 'slug': 'introduction-to-initial-access', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'WjNy6', 'duration': 820000, 'name': 'Generating Password Variations with Python', 'typeName': 'lecture', 'slug': 'generating-password-variations-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'DnQzx', 'duration': 619000, 'name': 'Generating Three Random Words with Python', 'typeName': 'lecture', 'slug': 'generating-three-random-words-with-python', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'OdToQ', 'duration': 693000, 'name': 'Automating Brute Force', 'typeName': 'lecture', 'slug': 'automating-brute-force', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}, {'id': 'rPXDn', 'duration': 1800000, 'name': 'Advanced Python - Reconnaissance', 'typeName': 'exam', 'slug': 'advanced-python-reconnaissance', '__typename': 'XdpV1_org_coursera_xdp_common_XDPModuleItem'}]}}]}, {'detail_url': 'https://www.coursera.org/learn/python-in-recon'}]
count = 1
for i in data:
    if i.get("week " + str(count)) is not None:
        print("present")
        count += 1
    else:
        print("absent")

while count <= 7:
    key = "week " + str(count)
    data.append({key: None})
    count += 1

for i in data:
    print(i)