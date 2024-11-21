**Example 1: 查询网络域**



Input: 

```
tccli dasb DescribeDomains --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Status \
    --Filters.0.Values 0 \
    --Filters.1.Name Ip \
    --Filters.1.Values 127.9.9.1
```

Output: 
```
{
    "Response": {
        "DomainSet": [
            {
                "Id": 7,
                "DomainId": "net-vvr396q5",
                "DomainName": "domain-9990",
                "Enabled": 1,
                "Status": 0,
                "ResourceId": "bh-saas-jtvukub4",
                "CreateTime": "2024-04-19T11:11:55+08:00",
                "Default": 0,
                "WhiteIpSet": [
                    "127.9.9.1",
                    "171.0.0.1"
                ]
            }
        ],
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af",
        "TotalCount": 1
    }
}
```

