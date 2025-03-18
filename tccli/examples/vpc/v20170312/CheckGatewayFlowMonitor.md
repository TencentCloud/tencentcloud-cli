**Example 1: 示例1 查询VPN网关是否开启了网关流控**



Input: 

```
tccli vpc CheckGatewayFlowMonitor --cli-unfold-argument  \
    --GatewayId vpngw-4je9dgin
```

Output: 
```
{
    "Response": {
        "Enabled": true,
        "Bandwidth": 5,
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

