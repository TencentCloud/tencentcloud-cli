**Example 1: DescribeReplayDetails示例**



Input: 

```
tccli rum DescribeReplayDetails --cli-unfold-argument  \
    --AppId 146662 \
    --SessionId e6f1ecbeb640423496f11bf1bfa1501a \
    --ReplayId rep_7e9d242b7cde49ac65e7f680c40d8aeb \
    --Categories all \
    --Limit 3 \
    --Cursor 3 \
    --StartOffsetMs 20 \
    --EndOffsetMs 50
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InternalError\",\"Message\":\"查询失败\"}",
        "RequestId": "99490db4-46de-4b15-89d1-09ab1fda7922"
    }
}
```

