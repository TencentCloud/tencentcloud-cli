**Example 1: 查询管控日志**



Input: 

```
tccli wedata TaskLog --cli-unfold-argument  \
    --ProjectId ** \
    --StartTime 1659258887409 \
    --EndTime 1659345287409 \
    --Limit 100 \
    --OrderType desc \
    --TaskId ** \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "LogContentList": [
            {
                "PkgId": "xx",
                "Log": "xx",
                "Time": 1
            },
            {
                "PkgId": "xx",
                "Log": "xx",
                "Time": 1
            },
            {
                "PkgId": "xx",
                "Log": "xx",
                "Time": 1
            }
        ]
    }
}
```

