**Example 1: 查询实时任务日志接口**



Input: 

```
tccli wedata TaskLog --cli-unfold-argument  \
    --ProjectId ** \
    --StartTime 1659258887409 \
    --EndTime 1659345287409 \
    --Limit 100 \
    --OrderType desc \
    --TaskId a9d94710bfa8f80437a217 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "LogContentList": [
            {
                "Time": 1,
                "PkgId": "a2b142c",
                "Log": "test log content "
            }
        ],
        "RequestId": "bd947vbf-a8fer80-4u782-17"
    }
}
```

