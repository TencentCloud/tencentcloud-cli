**Example 1: 验证拨测结果示例1**



Input: 

```
tccli cat VerifyResult --cli-unfold-argument  \
    --ResultId 38
```

Output: 
```
{
    "Response": {
        "ResultCode": 10000,
        "ErrorReason": "DNS解析失败",
        "RequestId": "b4c35d62-7407-46db-a064-ad600970cd87"
    }
}
```

**Example 2: 验证拨测结果示例2**



Input: 

```
tccli cat VerifyResult --cli-unfold-argument  \
    --ResultId 1446
```

Output: 
```
{
    "Response": {
        "ResultCode": -2,
        "ErrorReason": "连接失败",
        "RequestId": "ce6599b6-fe65-46b5-9b19-e9eada64aa97"
    }
}
```

