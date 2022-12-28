**Example 1: 添加域名**

 

Input: 

```
tccli dnspod CreateDomain --cli-unfold-argument  \
    --Domain dnspod.com \
    --IsMark no \
    --GroupId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DomainInfo": {
            "Id": 62,
            "Punycode": "dnspod.com",
            "Domain": "dnspod.com",
            "GradeNsList": [
                "source.dnspod.net",
                "low.dnspod.net"
            ]
        }
    }
}
```

**Example 2: CreateDomain_success**

 

Input: 

```
tccli dnspod CreateDomain --cli-unfold-argument  \
    --Domain iceice.club
```

Output: 
```
{
    "Response": {
        "RequestId": "674a208e-4829-4c2d-a519-a85f2f9bb223",
        "DomainInfo": {
            "GradeNsList": [
                "eunice.dnspod.net",
                "country.dnspod.net"
            ],
            "Id": 15,
            "Punycode": "iceice.club",
            "Domain": "iceice.club"
        }
    }
}
```

