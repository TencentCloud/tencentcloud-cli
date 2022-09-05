**Example 1: 查询域名列表**



Input: 

```
tccli gaap DescribeGlobalDomains --cli-unfold-argument  \
    --ProjectId 0 \
    --Limit 112 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "Status": 1,
                "FullDomain": "xx",
                "UpdateTime": 1,
                "DomainId": "xx",
                "BanStatus": "xx",
                "ProjectId": 0,
                "DefaultValue": "xx",
                "Alias": "xx",
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    },
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Type": "xx",
                "CreateTime": 1,
                "ProxyCount": 1
            },
            {
                "Status": 1,
                "FullDomain": "xx",
                "UpdateTime": 1,
                "DomainId": "xx",
                "BanStatus": "xx",
                "ProjectId": 0,
                "DefaultValue": "xx",
                "Alias": "xx",
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Type": "xx",
                "CreateTime": 1,
                "ProxyCount": 1
            },
            {
                "Status": 1,
                "FullDomain": "xx",
                "UpdateTime": 1,
                "DomainId": "xx",
                "BanStatus": "xx",
                "ProjectId": 0,
                "DefaultValue": "xx",
                "Alias": "xx",
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Type": "xx",
                "CreateTime": 1,
                "ProxyCount": 1
            },
            {
                "Status": 1,
                "FullDomain": "xx",
                "UpdateTime": 1,
                "DomainId": "xx",
                "BanStatus": "xx",
                "ProjectId": 0,
                "DefaultValue": "xx",
                "Alias": "xx",
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Type": "xx",
                "CreateTime": 1,
                "ProxyCount": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

