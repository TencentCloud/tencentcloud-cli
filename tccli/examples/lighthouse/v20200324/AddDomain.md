**Example 1: 添加域名**



Input: 

```
tccli lighthouse AddDomain --cli-unfold-argument  \
    --DomainName lhsday.com
```

Output: 
```
{
    "Response": {
        "RequestId": "456b895b-6bd8-4d86-83cd-98298712b2e9",
        "DomainId": "lhdo-qpnq8qzk",
        "DNSState": "UNUSE_DNSPOD",
        "EffectiveDNS": [
            "t8j7g.dnspod.net",
            "u6n7d.dnspod.net"
        ]
    }
}
```

