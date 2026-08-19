**Example 1: 示例**



Input: 

```
tccli csip DescribeEdrLogCollectPaths --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Paths": [
            {
                "CreateTime": "2026-03-22 18:32:47",
                "Id": 1,
                "LogTag": "user_tag_msg",
                "ModifyTime": "2026-03-22 18:32:47",
                "Path": "/var/log/messages"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5faef0f0-9353-4c15-9323-3b3f3c793ebb"
    }
}
```

