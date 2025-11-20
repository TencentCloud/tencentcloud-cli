**Example 1: 获取用户同步状态**



Input: 

```
tccli bh DescribeUserSyncStatus --cli-unfold-argument  \
    --UserKind 1
```

Output: 
```
{
    "Response": {
        "RequestId": "dfac445370-8b23-499e-83b2-a50e3ca059af",
        "Status": {
            "LastStatus": 1,
            "LastTime": "2025-04-22T15:04:05Z07:00",
            "InProcess": true
        }
    }
}
```

