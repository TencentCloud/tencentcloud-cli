**Example 1: 查询授权的自定义分组**



Input: 

```
tccli ioa DescribeResourceGrantedVirtualGroups --cli-unfold-argument  \
    --ResourceId 7 \
    --ResourceType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountCount": 0,
                    "Description": "",
                    "ExpireTime": 0,
                    "Name": "正编",
                    "RelationId": 27,
                    "VirtualGroupId": 126
                }
            ]
        },
        "RequestId": "cde84834-df28-4aac-9251-9f1941a730c5"
    }
}
```

