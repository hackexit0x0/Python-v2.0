import re

# Define file paths
input_file = 'hsv.txt'
subdomains_file = 'subdomains.txt'
ips_file = 'ips.txt'
emails_file = 'emails.txt'

# Regular expressions for extraction
subdomain_pattern = re.compile(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b')
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}\b')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Initialize sets to avoid duplicates
subdomains = set()
ips = set()
emails = set()

# Read the input file and extract data
with open(input_file, 'r') as file:
    for line in file:
        subdomains.update(subdomain_pattern.findall(line))
        ips.update(ip_pattern.findall(line))
        emails.update(email_pattern.findall(line))

# Write extracted data to files
with open(subdomains_file, 'w') as file:
    for subdomain in sorted(subdomains):
        file.write(subdomain + '\n')

with open(ips_file, 'w') as file:
    for ip in sorted(ips):
        file.write(ip + '\n')

with open(emails_file, 'w') as file:
    for email in sorted(emails):
        file.write(email + '\n')

print(f"Extraction complete. Files saved:\n{subdomains_file}\n{ips_file}\n{emails_file}")
