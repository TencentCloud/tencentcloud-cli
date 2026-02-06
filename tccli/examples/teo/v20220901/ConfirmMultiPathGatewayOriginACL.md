**Example 1: 确认已更新至最新的回源 IP 网段**

确认 ZoneId 为 'zone-27q0p0bal192' ，GatewayId 为 'mpgw-lbxuhk1oh' 的实例已将最新的回源 IP 网段更新至源站防火墙。

Input: 

```
tccli teo ConfirmMultiPathGatewayOriginACL --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --OriginACLVersion 1
```

Output: 
```
{
    "Response": {
        "RequestId": "af0a2b4f-df6d-4d2a-ac39-1706cbf8a868"
    }
}
```

