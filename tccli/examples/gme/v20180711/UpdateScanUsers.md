**Example 1: 更新用户自定义送检用户号**



Input: 

```
tccli gme UpdateScanUsers --cli-unfold-argument  \
    --UserIdRegex xx \
    --UserIdString xx \
    --BizId 1
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "xx"
    }
}
```

