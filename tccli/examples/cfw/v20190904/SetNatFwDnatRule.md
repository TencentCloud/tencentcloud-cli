**Example 1: 配置防火墙Dnat规则**



Input: 

```
tccli cfw SetNatFwDnatRule --cli-unfold-argument  \
    --Mode 1 \
    --CfwInstance cfwnat-d2afc817 \
    --OperationType add \
    --AddOrDelDnatRules.0.IpProtocol TCP \
    --AddOrDelDnatRules.0.PublicIpAddress 119.45.163.54 \
    --AddOrDelDnatRules.0.PublicPort 80 \
    --AddOrDelDnatRules.0.PrivateIpAddress 10.206.22.4 \
    --AddOrDelDnatRules.0.PrivatePort 80 \
    --AddOrDelDnatRules.0.Description 
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

