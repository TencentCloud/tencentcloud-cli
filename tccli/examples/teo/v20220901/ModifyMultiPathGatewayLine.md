**Example 1: 修改多通道安全加速网关的代理线路**

修改站点（ ZoneId 取值为 zone-27q0p0bal192 ）下，多通道安全加速网关 ID 为 mpgw-lbxuhk1oh 的 Edgeone 四层代理线路转发线路，将 LineAddress 修改为 101.23.573.10:8989，ProxyId 修改为 sid-2gpv1z8cx8y2，RuleId 修改为 rule-33ik84rw3nuu。

Input: 

```
tccli teo ModifyMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-1 \
    --LineType proxy \
    --LineAddress 101.23.573.10:8989 \
    --ProxyId sid-2gpv1z8cx8y2 \
    --RuleId rule-33ik84rw3nuu
```

Output: 
```
{
    "Response": {
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0"
    }
}
```

**Example 2: 修改多通道安全加速网关的自定义线路**

修改站点（ ZoneId 取值为 zone-27q0p0bal192 ）下，多通道安全加速网关 ID 为 mpgw-lbxuhk1oh 的自定义线路，将 LineAddress 修改为 120.91.82.74:8080。

Input: 

```
tccli teo ModifyMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-2 \
    --LineType custom \
    --LineAddress 120.91.82.74:8080
```

Output: 
```
{
    "Response": {
        "RequestId": "548b1b65-fcec-4095-8c7a-ec8afa862635"
    }
}
```

