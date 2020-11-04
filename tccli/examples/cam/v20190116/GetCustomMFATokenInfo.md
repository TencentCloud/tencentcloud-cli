**Example 1: 获取自定义多因子Token关联信息**



Input: 

```
tccli cam GetCustomMFATokenInfo --cli-unfold-argument  \
    --MFAToken abc123
```

Output: 
```
{
    "Response": {
        "Uin": 12345678,
        "RequestId": "f8914327-5a9f-4016-8b2e-00f8b8901121"
    }
}
```

