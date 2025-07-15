**Example 1: 查询多通道安全加速网关的直连线路**

查询站点（ZoneId 为 zone-27q0p0bal192）下，网关 Id（GatewayId 为 mpgw-lbxuhk1oh），线路类型（LineId 为 line-0）的详细信息。

Input: 

```
tccli teo DescribeMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-0
```

Output: 
```
{
    "Response": {
        "Line": {
            "LineId": "line-0",
            "LineType": "direct",
            "LineAddress": "159.21.35.91:8080"
        },
        "RequestId": "9153aae4-26b1-4580-adc3-fa7cd4d32bf5"
    }
}
```

**Example 2: 查询多通道安全加速网关的代理线路**

查询站点（ZoneId 为 zone-27q0p0bal192）下，网关 Id（GatewayId 为 mpgw-lbxuhk1oh），线路类型（LineId 为 line-1）的详细信息。

Input: 

```
tccli teo DescribeMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-1
```

Output: 
```
{
    "Response": {
        "Line": {
            "LineType": "proxy",
            "LineAddress": "120.12.31.91:8080",
            "LineId": "line-1",
            "ProxyId": "sid-2gpv1z8cx8y2",
            "RuleId": "rule-33ik84rw3nuu"
        },
        "RequestId": "9153aae4-26b1-4580-adc3-fa7cd4d32bf5"
    }
}
```

**Example 3: 查询多通道安全加速网关的自定义接入线路**

查询站点（ZoneId 为 zone-27q0p0bal192）下，网关 Id（GatewayId 为 mpgw-lbxuhk1oh），线路类型（LineId 为 line-2）的详细信息。

Input: 

```
tccli teo DescribeMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-2
```

Output: 
```
{
    "Response": {
        "Line": {
            "LineId": "line-2",
            "LineType": "custom",
            "LineAddress": "120.12.31.91:8080"
        },
        "RequestId": "9153aae4-26b1-4580-adc3-fa7cd4d32bf5"
    }
}
```

