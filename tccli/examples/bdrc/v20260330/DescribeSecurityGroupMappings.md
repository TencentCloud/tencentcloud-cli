**Example 1: 查询安全组映射**



Input: 

```
tccli bdrc DescribeSecurityGroupMappings --cli-unfold-argument  \
    --SitePairId sitepair-0wxbktxr
```

Output: 
```
{
    "Response": {
        "SecurityGroupMappingSet": [
            {
                "LifeState": "NORMAL",
                "SecurityGroupMappingId": "sgmap-88ylio5h",
                "SitePairId": "sitepair-0wxbktxr",
                "SourceSecurityGroupId": "sg-h8pnwgld",
                "TargetSecurityGroupId": "sg-h8pnwgld"
            }
        ],
        "TotalCount": 1,
        "RequestId": "9c40a9f1-fbb2-4f7f-87a7-58a30d6232d2"
    }
}
```

