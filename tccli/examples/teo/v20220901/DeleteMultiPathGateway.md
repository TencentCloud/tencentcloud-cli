**Example 1: 删除多通道安全加速网关**

删除指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，网关 ID 为 mpgw-lbxuhk1oh 的多通道安全加速网关。

Input: 

```
tccli teo DeleteMultiPathGateway --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh
```

Output: 
```
{
    "Response": {
        "RequestId": "7ad406fd-0e19-4bb4-af86-4ec580f89901"
    }
}
```

