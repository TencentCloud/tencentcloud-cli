**Example 1: 查询自动删除策略列表**



Input: 

```
tccli cfs DescribeAutoDeletePolicies --cli-unfold-argument  \
    --FileSystemId cfs-4e5e7**** \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Policies": [
            {
                "CreateTime": "2026-**-** **:17:40",
                "ErrMsg": "",
                "FileSystemId": "cfs-4e5e7****",
                "Paths": [
                    "/cfs/*"
                ],
                "PolicyId": "adp-d774****",
                "PolicyName": "te***",
                "Region": "ap-guangzhou",
                "Status": "enabling",
                "UpdateTime": "2026-08-03 14:25:15"
            }
        ],
        "TotalCount": 1,
        "RequestId": "8d29b9df-293f-48d3-86dc-3e8e59269119"
    }
}
```

