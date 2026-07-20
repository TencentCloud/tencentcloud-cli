**Example 1: 删除Nat防火墙Dnat规则**

删除Nat防火墙Dnat规则

Input: 

```
tccli cfw DeleteNatFwDnatRule --cli-unfold-argument  \
    --Mode 1 \
    --CfwInstance cfw-dsad \
    --DnatRules.0.IpProtocol tcp \
    --DnatRules.0.PublicIpAddress 1.10.101.1 \
    --DnatRules.0.PublicPort 0 \
    --DnatRules.0.PrivateIpAddress 1.1.1.1 \
    --DnatRules.0.PrivatePort 0 \
    --DnatRules.0.Description sadabc
```

Output: 
```
{
    "Response": {
        "RequestId": "dsadsaabc"
    }
}
```

