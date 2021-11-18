**Example 1: 敏感邮箱域名信息列表**



Input: 

```
tccli bsca DescribeSensitiveEmailDomainList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SensitiveDomainSet": [
            {
                "RootDomain": "here.my.org",
                "Count": 3
            }
        ],
        "TotalCount": 2,
        "FieldValuesSet": [
            {
                "Field": "RootDomain",
                "Values": [
                    "my.org",
                    "one.org",
                    "two.org",
                    "four.org",
                    "here.my.org",
                    "sendmail.org",
                    "three.org",
                    "integral.org",
                    "thyrsus.com",
                    "clear.net.nz",
                    "bigfoot.de",
                    "lemburg.com",
                    "python.org",
                    "sweetapp.com",
                    "nightmare.com",
                    "gmail.com",
                    "benfinney.id.au",
                    "python.net",
                    "lists.sourceforge.net",
                    "example.com",
                    "cs.su.oz.au",
                    "brown.edu",
                    "mrbook.org",
                    "openssl.org",
                    "nightshade.la.mastaler.com",
                    "zesty.ca",
                    "isi.edu",
                    "pythonware.com",
                    "pearwood.inf",
                    "groups.google.com",
                    "ms.com",
                    "gol.com",
                    "nl.linux.org",
                    "lysator.liu.se",
                    "ionrock.org",
                    "users.sourceforge.net",
                    "gnu.org",
                    "egenix.com",
                    "gustaebel.de",
                    "skippinet.com.au",
                    "aon.at",
                    "krypto.org",
                    "cmu.edu",
                    "wbond.net",
                    "lfw.org",
                    "shore.net",
                    "shazow.net",
                    "bzip.org",
                    "debian.org",
                    "osu.edu",
                    "abo.fi",
                    "u.washington.edu",
                    "isg.de",
                    "interlink.com.au",
                    "kreativkombinat.de",
                    "kennethreitz.org",
                    "llnl.gov",
                    "samba.org",
                    "sprymix.com",
                    "zooko.com",
                    "fastmail.fm",
                    "cs.uni-sb.de",
                    "jaraco.com",
                    "alum.mit.edu",
                    "magnet.com",
                    "ski.org",
                    "example.net",
                    "redivi.com",
                    "nextday.fi",
                    "red-dove.com"
                ]
            }
        ],
        "RequestId": "f968723d-3438-431f-93ed-27405990f1c2"
    }
}
```

