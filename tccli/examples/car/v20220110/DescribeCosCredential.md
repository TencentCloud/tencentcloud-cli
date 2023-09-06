**Example 1: 添加查询 COS 密钥信息请求**



Input: 

```
tccli car DescribeCosCredential --cli-unfold-argument  \
    --ApplicationId app-fcegkdfa \
    --ApplicationFileName xxx.rar
```

Output: 
```
{
    "Response": {
        "SecretID": "xxx",
        "SecretKey": "xxx",
        "SessionToken": "xxx",
        "CosBucket": "examplebucket-1250000000",
        "CosRegion": "ap-guangzhou",
        "Path": "103121832/app-fcegkdfa/ver-xxx/app-fcegkdfa.rar",
        "StartTime": 1500000,
        "ExpiredTime": 1000000,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

