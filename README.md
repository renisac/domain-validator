
# domain_validator

Crude Python utility for validating domains against a reference list.

Leverages Levenshtein distance to match similar domains when the test set is dirty (such as in credential dumps).

## Install

```
git clone https://github.com/renisac/domain_validator.git

cd domain_validator/

python setup.py install

```

## CLI Usage

```
$ domain-validator -h
usage: domain-validator [-h] [-v] [-f FILE] [-d DOMAIN] [-r REF_FILE]
                        [-s MIN_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose output
  -f FILE, --file FILE  file of domains to validate
  -d DOMAIN, --domain DOMAIN
                        domain to test
  -r REF_FILE, --ref-file REF_FILE
                        path to reference file of domains
  -s MIN_SIZE, --min-size MIN_SIZE
                        minimum domain length for levenshtein tests (default:
                        6)
```

### Test an individual domain:
```
$ domain-validator -d foo.edu -r reference.txt
foo.edu
$
```
### Test a list of domains from a file:
```
$ domain-validator -f test.txt -r reference.txt
foobar.edu
barfoo.edu
$
```
### Test a list of domains from a file with verbose output:
```
$ domain-validator -f test.txt -r reference.txt -v
test_domain,actual_domain,method
foobar.edu,foobar.edu,literal_match
barfooz.edu,barfoo.edu,levenshtein
$
```
## Python 

```
from domain_validator import validate_domain

ref_domains = ['foobar.edu', 'barfoo.edu']
test_domains = ['foobar.edu', 'barfooz.edu']

validate_domain(ref_domains, test_domains)
['foobar.edu', 'barfoo.edu']

```