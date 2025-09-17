**Example 1: 设置实例密码**



Input: 

```
tccli mongodb ResetInstancePassword --cli-unfold-argument  \
    --UserResourceId cmgo-js2qrgp5 \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test1 \
    --Password abcde
```

Output: 
```
{
    "Response": {
        "RequestId": "9ab09c94-b2fc-4053-9115-ccc178e56000",
        "TimeCost": 10,
        "ResetTimestamp": 12345
    }
}
```

