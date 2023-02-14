**Example 1: 检测域名是否可注册**

检测域名是否可注册

Input: 

```
tccli domain CheckDomain --cli-unfold-argument  \
    --DomainName 字符串
```

Output: 
```
{
    "Response": {
        "Available": true,
        "Premium": false,
        "RecordSupport": true,
        "DomainName": "的国防生的国防生.show",
        "FeeTransfer": 0,
        "Describe": "",
        "FeeRestore": 0,
        "Period": 1,
        "Reason": "",
        "RequestId": "cc5af1aa-544c-11ea-9bcb-525400f1e866",
        "RealPrice": 10,
        "BlackWord": false,
        "Price": 35,
        "FeeRenew": 0
    }
}
```

