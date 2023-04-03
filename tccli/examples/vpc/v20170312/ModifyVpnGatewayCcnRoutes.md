**Example 1: 修改VPN网关云联网路由**

修改VPN网关云联网路由

Input: 

```
tccli vpc ModifyVpnGatewayCcnRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-qol17bjo \
    --Routes.0.RouteId dcr-7t3tknmp \
    --Routes.0.Status ENABLE \
    --Routes.0.DestinationCidrBlock 172.2.9.3/32
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

