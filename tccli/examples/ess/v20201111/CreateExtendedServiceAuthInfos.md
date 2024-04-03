**Example 1: 创建企业扩展服务授权-主代子**

集团主企业代子企业操作

Input: 

```
tccli ess CreateExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDxlzUxxxxxxxxxxxxxxxxPNG1SC2 \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --Agent.ProxyOrganizationId yDxlzUxxxxxxxxxxxxxxxxskenibR \
    --UserIds yDxlzUxxxxxxxxxxxxxxxxPNG1SC2
```

Output: 
```
{
    "Response": {
        "RequestId": "s169xxxxxxxx6107"
    }
}
```

**Example 2: 创建企业扩展服务授权-自动签**

创建企业扩展服务授权


Input: 

```
tccli ess CreateExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDxlzUxxxxxxxxxxxxxxxxPNG1SC2 \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --UserIds yDxlzUxxxxxxxxxxxxxxxxPNG1SC2
```

Output: 
```
{
    "Response": {
        "RequestId": "s169xxxxxxxx6107"
    }
}
```

**Example 3: 创建企业自动签授权-类型错误**



Input: 

```
tccli ess CreateExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDxlzUxxxxxxxxxxxxxxxxPNG1SC2 \
    --ExtendServiceType  \
    --UserIds yDxlzUxxxxxxxxxxxxxxxxPNG1SC2
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

**Example 4: 创建企业扩展服务授权- 批量签署**



Input: 

```
tccli ess CreateExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDxlzUxxxxxxxxxxxxxxxxPNG1SC2 \
    --ExtendServiceType BATCH_SIGN \
    --UserIds yDxlzUxxxxxxxxxxxxxxxxPNG1SC2
```

Output: 
```
{
    "Response": {
        "RequestId": "s169xxxxxxxx6107"
    }
}
```

