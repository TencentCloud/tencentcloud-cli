**Example 1: 查询自定义DNS Host列表**



Input: 

```
tccli domain DescribeCustomDnsHostSet --cli-unfold-argument  \
    --DomainId domain-esysdasdgq \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "bd4fc5332-23a2-49bd-8cab-48cfe5963651",
        "DnsHostSet": [
            {
                "IpSet": [
                    "2.2.2.2"
                ],
                "DnsName": "bbbb"
            },
            {
                "IpSet": [
                    "8.8.9.9",
                    "3.3.3.3"
                ],
                "DnsName": "aaa"
            }
        ]
    }
}
```

