**Example 1: 重置数据库账户密码**



Input: 

```
tccli postgres ResetInstancePassword --cli-unfold-argument  \
    --UserResourceId postgres-r95q23pn \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount root \
    --Password 1357Wer= \
    --PasswordEncrypt False
```

Output: 
```
{
    "Response": {
        "RequestId": "6f3d27d1-1462-4287-87a4-2b1cccb51681",
        "TimeCost": 3000,
        "ResetTimestamp": 1760346593000
    }
}
```

