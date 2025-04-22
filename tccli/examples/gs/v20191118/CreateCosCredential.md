**Example 1: 示例1添加创建 Cos 临时密钥请求**



Input: 

```
tccli gs CreateCosCredential --cli-unfold-argument  \
    --CosType Mobile
```

Output: 
```
{
    "Response": {
        "SecretID": "xx",
        "SecretKey": "xx",
        "SessionToken": "xx",
        "CosBucket": "xx",
        "CosRegion": "xx",
        "Path": "xx",
        "StartTime": 1500000,
        "ExpiredTime": 1500000,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

