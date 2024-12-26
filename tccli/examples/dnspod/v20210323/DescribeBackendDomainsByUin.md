**Example 1: 根据UIN查询域名列表信息**

根据UIN查询域名列表信息

Input: 

```
tccli dnspod DescribeBackendDomainsByUin --cli-unfold-argument  \
    --OwnerUin 100000014880 \
    --DNSStatus no \
    --DomainStatus enable \
    --Length 5 \
    --LastDomainId 0
```

Output: 
```
{
    "Response": {
        "DomainList": [
            {
                "DNSStatus": "no",
                "Domain": "tao9.xyz",
                "DomainId": 12611936,
                "DomainStatus": "enable"
            },
            {
                "DNSStatus": "no",
                "Domain": "taopao.wang",
                "DomainId": 12613585,
                "DomainStatus": "enable"
            },
            {
                "DNSStatus": "no",
                "Domain": "sina.cn",
                "DomainId": 12613586,
                "DomainStatus": "enable"
            },
            {
                "DNSStatus": "no",
                "Domain": "bb.com",
                "DomainId": 12613588,
                "DomainStatus": "enable"
            },
            {
                "DNSStatus": "no",
                "Domain": "aaaa.cn",
                "DomainId": 12613589,
                "DomainStatus": "enable"
            }
        ],
        "DomainTotal": 27,
        "BigCustomer": true,
        "RequestId": "0bcd9764-6846-4058-b378-3c65a7149dac"
    }
}
```

