**Example 1: 赎回请求**

赎回请求

Input: 

```
tccli domain CreateDomainRedemption --cli-unfold-argument  \
    --DomainId domain-dsaklnkl
```

Output: 
```
{
    "Response": {
        "RequestId": "dwdw-dwewe-*****"
    }
}
```

**Example 2: 权限不足**

当前账号未有权限创建赎回订单，需要联系产品

Input: 

```
tccli domain CreateDomainRedemption --cli-unfold-argument  \
    --DomainId domain-dwesqweq
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.PermissionDenied.",
            "Message": "权限不足"
        },
        "RequestId": "dwdw-dwewe-*****"
    }
}
```

