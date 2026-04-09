**Example 1: 创建Nat防火墙Dnat规则**

创建Nat防火墙Dnat规则

Input: 

```
tccli cfw CreateNatFwDnatRule --cli-unfold-argument  \
    --Mode 1 \
    --CfwInstance abc \
    --DnatRules.0.IpProtocol abc \
    --DnatRules.0.PublicIpAddress abc \
    --DnatRules.0.PublicPort 0 \
    --DnatRules.0.PrivateIpAddress abc \
    --DnatRules.0.PrivatePort 0 \
    --DnatRules.0.Description abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

