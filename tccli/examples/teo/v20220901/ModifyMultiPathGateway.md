**Example 1: 修改多通道安全加速网关信息**

修改指定站点下 ZoneId 为 zone-27q0p0bal192，网关 GatewayId 为 mpgw-lbxuhk1oh 的多通道安全加速网关的网关名、 IP  和端口信息。

Input: 

```
tccli teo ModifyMultiPathGateway --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --GatewayName eomp \
    --GatewayIP 101.31.33.19 \
    --GatewayPort 8080
```

Output: 
```
{
    "Response": {
        "RequestId": "175a5e55-a849-41f1-93d2-c9741859fedd"
    }
}
```

