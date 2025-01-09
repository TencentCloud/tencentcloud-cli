**Example 1: 删除企业扩展服务授权- 自动签**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --UserIds yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E
```

Output: 
```
{
    "Response": {
        "RequestId": "s1697xxxxxxxxx107"
    }
}
```

**Example 2: 删除企业扩展服务授权- 批量签署**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E \
    --ExtendServiceType BATCH_SIGN \
    --UserIds yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E
```

Output: 
```
{
    "Response": {
        "RequestId": "s1697xxxxxxxxx107"
    }
}
```

**Example 3: 删除企业自动签授权-扩展类型错误**



Input: 

```
tccli ess DeleteExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E \
    --ExtendServiceType  \
    --UserIds yDwcCUUgyg3tgmwcUEVzyNaupO7DiB3E
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

