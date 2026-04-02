**Example 1: 查询共享CNAME列表**

查询共享CNAME列表

Input: 

```
tccli teo DescribeSharedCNAME --cli-unfold-argument  \
    --Direction desc \
    --ZoneId zone-20hyebgyfsko \
    --Limit 10 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values qq.com \
    --Filters.0.Name shared-cname \
    --Offset 0 \
    --Order create-time \
    --Match all
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "SharedCNAMEInfo": [
            {
                "SharedCNAME": "qq.com.share.eo.dnse5.com",
                "Description": "用于业务A场景",
                "BindDomainCount": 3
            }
        ]
    }
}
```

