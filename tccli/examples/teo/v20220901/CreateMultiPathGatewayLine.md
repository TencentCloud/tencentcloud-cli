**Example 1: 创建 EdgeOne 四层代理线路**

为指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，网关 ID 为 mpgw-lbxuhk1oh 的多通道安全加速网关创建 EdgeOne 四层代理线路。

Input: 

```
tccli teo CreateMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineType proxy \
    --LineAddress 101.23.573.10:8989 \
    --ProxyId sid-2gpv1z8cx8y2 \
    --RuleId rule-33ik84rw3nuu
```

Output: 
```
{
    "Response": {
        "LineId": "line-1",
        "RequestId": "34b734a7-71de-4ffc-a59d-eeac9d171da2"
    }
}
```

**Example 2: 创建自定义线路**

为指定站点（ ZoneId 为 zone-27q0p0bal192 ）下，网关 ID 为 mpgw-lbxuhk1oh 的多通道安全加速网关创建自定义线路。

Input: 

```
tccli teo CreateMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineType custom \
    --LineAddress 120.62.91.54:8080
```

Output: 
```
{
    "Response": {
        "LineId": "line-2",
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0"
    }
}
```

