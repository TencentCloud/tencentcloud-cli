**Example 1: 开启 WAF 防护**

开启 WAF 防护

Input: 

```
tccli tse OpenWafProtection --cli-unfold-argument  \
    --GatewayId gateway-0f7c158e \
    --Type Global
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

