from argparse import ArgumentParser
import sys
from Levenshtein import distance
import re

MIN_CHARS = 6

def validate_domain(ref_domains, test_domains, min_chars=MIN_CHARS, verbose=False):

    if isinstance(ref_domains, str):
        ref_domains = [ref_domains]
    if isinstance(test_domains, str):
        test_domains = [test_domains]

    results = []

    for x in test_domains:
        # literal match
        if x in ref_domains:
            if verbose:
                results.append('{},{},literal_match'.format(x, x))
            else:
                results.append(x)

        # Levenshtein
        else:
            # short domains are problematic :(
            r = re.compile(r'^(\w){{{},}}'.format(min_chars))
            if re.search(r, x):
                for y in ref_domains:
                    if distance(str(y), str(x)) == 1:
                        if verbose:
                            results.append('{},{},levenshtein'.format(x, y))
                        else:
                            results.append(y)

    return results

def main():

    p = ArgumentParser()
    p.add_argument('-v','--verbose', help="verbose output", action="store_true")
    p.add_argument('-f','--file', help="file of domains to validate")
    p.add_argument('-d','--domain', help="domain to test")
    p.add_argument('-r','--ref-file', help="path to reference file of domains")
    p.add_argument('-s', '--min-size', help="minimum domain length for levenshtein tests (default: 6)", default=6)

    args = p.parse_args()

    if len(sys.argv) == 1:
        p.print_usage()
        raise SystemExit

    verbose = False
    if args.verbose:
        verbose = True

    if not args.ref_file:
        raise SystemExit('must specify a reference file')

    with open(args.ref_file) as f:
        ref_file = set([l.rstrip('\n') for l in f])

    if verbose:
        print('test_domain,actual_domain,method')

    if args.file:
        with open(args.file) as f:
            test_file = set([l.rstrip('\n') for l in f])

        for r in validate_domain(ref_domains=ref_file, test_domains=test_file, min_chars=args.min_size, verbose=verbose):
            print(r)

    if args.domain:
        for r in validate_domain(ref_domains=ref_file, test_domains=args.domain, min_chars=args.min_size, verbose=verbose):
            print(r)

if __name__ == "__main__":
    main()