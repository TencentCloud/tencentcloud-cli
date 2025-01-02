**Example 1: 查询个人版命名空间信息**



Input: 

```
tccli tcr DescribeNamespacePersonal --cli-unfold-argument  \
    --Namespace nicokang \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "NamespaceCount": 1,
            "NamespaceInfo": [
                {
                    "CreationTime": "2024-06-22 10:37:26",
                    "Namespace": "nicokang",
                    "RepoCount": 10
                }
            ]
        },
        "RequestId": "94a1d32a-4f73-4214-8864-6bafdda6b5f6"
    }
}
```

