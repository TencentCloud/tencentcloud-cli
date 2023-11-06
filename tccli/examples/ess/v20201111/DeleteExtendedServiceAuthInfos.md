**Example 1: 删除企业自动签授权-扩展类型错误**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId abc \
    --ExtendServiceType  \
    --UserIds abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "不支持的扩展类型"
        },
        "RequestId": "s1697xxxxxxxxx107"
    }
}
```

**Example 2: 删除企业扩展服务授权- 批量签署**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId abc \
    --ExtendServiceType BATCH_SIGN \
    --UserIds abc
```

Output: 
```
{
    "Response": {
        "RequestId": "s1697xxxxxxxxx107"
    }
}
```

**Example 3: 删除企业扩展服务授权- 自动签**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId abc \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --UserIds abc
```

Output: 
```
{
    "Response": {
        "RequestId": "s1697xxxxxxxxx107"
    }
}
```

