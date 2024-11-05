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
                "DomainId": "dm-00ye8ek7",
                "FullDomain": "gd-qbsrvjtf.gaapqcloud.com.cn",
                "Alias": "abc",
                "Type": "IP",
                "Status": 0,
                "ProjectId": 0,
                "DefaultValue": "192.168.1.2",
                "ProxyCount": 1,
                "CreateTime": 1662216195,
                "UpdateTime": 1662216195,
                "TagSet": [
                    {
                        "TagKey": "project",
                        "TagValue": "abc"
                    }
                ],
                "BanStatus": "RECOVER"
            }
        ],
        "TotalCount": 1,
        "RequestId": "90955c1c-ef70-40b4-bf3f-74409cf24d60"
    }
}
```

