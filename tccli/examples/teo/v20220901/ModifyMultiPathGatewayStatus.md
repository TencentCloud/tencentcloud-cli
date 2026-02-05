**Example 1: 更新多通道安全网关状态**

更新 ZoneId 为 'zone-27q0p0bal192' ，GatewayId 为 'eo-gw-lb-uhk1oh 的多通道安全网关状态。

Input: 

```
tccli teo ModifyMultiPathGatewayStatus --cli-unfold-argument  \
    --GatewayId eo-gw-lb-uhk1oh \
    --GatewayStatus offline \
    --ZoneId zone-27q0p0bal192
```

Output: 
```
{
    "Response": {
        "RequestId": "a03c3e4d-3a8c-4ef1-924c-81b33df6453a"
    }
}
```

