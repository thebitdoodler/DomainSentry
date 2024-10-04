import whois
import tldextract
import csv
from urllib.parse import urlparse
from datetime import datetime
import textwrap
from colorama import init, Fore, Style

init(autoreset=True)

def extract_domain(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            'Domain Name': domain,
            'Registrar': w.registrar,
            'Date Created': w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date,
            'Date Expires': w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date,
            'Owner Name': w.name,
            'Owner Address': ', '.join(w.address) if isinstance(w.address, list) else w.address,
            'Owner Email': w.email,
            'Owner Phone': w.phone,
            'Nameserver': ', '.join(w.name_servers) if w.name_servers else None
        }
    except Exception as e:
        print(f"Error processing {domain}: {str(e)}")
        return None

def format_value(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    elif value is None:
        return "N/A"
    return str(value)

def print_terminal_output(results):
    for result in results:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{'=' * 60}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}Domain: {result['Domain Name']}")
        print(f"{Fore.CYAN}{Style.BRIGHT}{'-' * 60}")
        
        for key, value in result.items():
            if key != 'Domain Name':
                formatted_value = format_value(value)
                wrapped_value = textwrap.fill(formatted_value, width=50, subsequent_indent=' ' * 20)
                print(f"{Fore.GREEN}{key:18}: {Fore.WHITE}{wrapped_value}")
        
        print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 60}")

def process_domains(urls, output_format='terminal', output_file=None):
    results = []
    for url in urls:
        domain = extract_domain(url.strip())
        print(f"Processing: {domain}")
        info = get_whois_info(domain)
        if info:
            results.append(info)
    
    if output_format == 'terminal':
        print_terminal_output(results)
    elif output_format == 'csv':
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Domain Name', 'Registrar', 'Date Created', 'Date Expires', 'Owner Name', 'Owner Address', 'Owner Email', 'Owner Phone', 'Nameserver']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        print(f"WHOIS information has been saved to {output_file}")
    
    return results

# Make sure to export the process_domains function
__all__ = ['process_domains']