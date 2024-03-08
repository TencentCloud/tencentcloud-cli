**Example 1: 获取自定义多因子Token关联信息**



Input: 

```
tccli cam GetCustomMFATokenInfo --cli-unfold-argument  \
    --MFAToken mfa_idc-100033287777-d70986da-24c7-1d5f-b6bd-0d2f94a571d0
```

Output: 
```
{
    "Response": {
        "Uin": 100033287777,
        "RequestId": "f8914327-5a9f-4016-8b2e-00f8b8901121"
    }
}
```

