import argparse
from .domain_sentry_core import process_domains

def main():
    parser = argparse.ArgumentParser(description="DomainSentry - Ultimate WHOIS Extractor for Threat Analysts")
    parser.add_argument("input_file", help="Input file containing domains or URLs")
    parser.add_argument("-o", "--output", choices=["terminal", "csv"], default="terminal", help="Output format (default: terminal)")
    parser.add_argument("-f", "--file", help="Output CSV file name (required if output is csv)")
    args = parser.parse_args()

    if args.output == "csv" and not args.file:
        parser.error("--file is required when output is csv")

    with open(args.input_file, 'r') as infile:
        urls = infile.readlines()

    process_domains(urls, args.output, args.file)

if __name__ == "__main__":
    main()