**Example 1: 创建Nat防火墙Dnat规则**

创建Nat防火墙Dnat规则

Input: 

```
tccli cfw CreateNatFwDnatRule --cli-unfold-argument  \
    --Mode 1 \
    --CfwInstance saabc \
    --DnatRules.0.IpProtocol dsabc \
    --DnatRules.0.PublicIpAddress sdsabc \
    --DnatRules.0.PublicPort 0 \
    --DnatRules.0.PrivateIpAddress sadsbc \
    --DnatRules.0.PrivatePort 0 \
    --DnatRules.0.Description sdsabc
```

Output: 
```
{
    "Response": {
        "RequestId": "sadabc"
    }
}
```

