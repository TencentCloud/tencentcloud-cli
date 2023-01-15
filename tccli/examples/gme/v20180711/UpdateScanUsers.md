**Example 1: 更新用户自定义送检用户号**

更新用户自定义送检用户号

Input: 

```
tccli gme UpdateScanUsers --cli-unfold-argument  \
    --UserIdRegex ^[0-9]*$ \
    --UserIdString 0001,0002,0003 \
    --BizId 1400000000
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "454859b0-5e53-491d-814c-ac40faaca5f7"
    }
}
```

