**Example 1: 修改云原生API网关实例Kong访问策略**



Input: 

```
tccli tse ModifyNetworkAccessStrategy --cli-unfold-argument  \
    --GatewayId gateway-xxxxx \
    --GroupId group-xxxxxx \
    --NetworkType abc \
    --Vip abc \
    --AccessControl.Mode abc \
    --AccessControl.CidrWhiteList abc \
    --AccessControl.CidrBlackList abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

