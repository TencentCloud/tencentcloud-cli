**Example 1: 查询域名列表**



Input: 

```
tccli lighthouse DescribeDomains --cli-unfold-argument  \
    --DomainIds lhdo-3ob8xfu
```

Output: 
```
{
    "Response": {
        "RequestId": "37b3c92f-4b1d-4889-a46f-8dc7d61d76e1",
        "TotalCount": 1,
        "DomainSet": [
            {
                "DomainId": "lhdo-3ob8xfuu",
                "DomainName": "lhsday.com",
                "PurchaseState": "",
                "DNSState": "UNUSE_DNSPOD",
                "RegisterTime": "",
                "ExpireTime": "",
                "EffectiveDNS": [
                    "t8j7g.dnspod.net",
                    "u6n7d.dnspod.net"
                ],
                "CreatedTime": "2022-09-27T03:12:43Z",
                "UpdatedTime": "2022-09-27T03:12:43Z"
            }
        ]
    }
}
```

