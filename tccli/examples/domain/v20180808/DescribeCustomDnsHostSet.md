**Example 1: 查询自定义DNS Host列表**



Input: 

```
tccli domain DescribeCustomDnsHostSet --cli-unfold-argument  \
    --DomainId domain-esysdasdgq \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "bd4fc5332-23a2-49bd-8cab-48cfe5963651",
        "DnsHostSet": [
            {
                "IpSet": [
                    "2.2.2.2"
                ],
                "DnsName": "a1.dns.dns"
            }
        ]
    }
}
```

