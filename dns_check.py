import dns.resolver

def query_record(domain, record_type):
    try:
        response = dns.resolver.resolve(domain, record_type, raise_on_no_answer=False)

        # If the DNS server returned an answer
        if response.rrset:
            print(f"\n[{record_type}]")
            print(response.rrset)

    except dns.resolver.NXDOMAIN:
        print(f"[ERROR] The domain {domain} does not exist.")
    except dns.resolver.NoAnswer:
        print(f"[NO ANSWER] The DNS server returned no data for {record_type}.")
    except dns.resolver.Timeout:
        print("[ERROR] The DNS server took too long to respond.")
    except Exception as e:
        print(f"[UNKNOWN ERROR] Type: {record_type} | Details: {e}")

def main():
    domain = input("TARGET: ")

    records = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]

    print("\n=== STARTING DNS ENUMERATION ===")

    for record in records:
        query_record(domain, record)

    print("\n=== DNS ENUMERATION FINISHED ===")

if __name__ == "__main__":
    main()
