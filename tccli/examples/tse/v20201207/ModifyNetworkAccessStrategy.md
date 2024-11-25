**Example 1: 修改云原生API网关实例Kong访问策略**



Input: 

```
tccli tse ModifyNetworkAccessStrategy --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7 \
    --NetworkType Open \
    --Vip 152.47.137.12 \
    --AccessControl.Mode Whitelist \
    --AccessControl.CidrWhiteList 0.0.0.0/0 \
    --AccessControl.CidrBlackList 0.0.0.0/0
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

