**Example 1: Modifying VPN gateway-based CCN routes**



Input: 

```
tccli vpc ModifyVpnGatewayCcnRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-qol17bjx\
    --Routes.0.RouteId xxx-xxxxxxxx\
    --Routes.0.DestinationCidrBlock 10.2.2.0/24\
    --Routes.0.Status ENABLE\
    --Routes.1.RouteId xxx-xxxxxxxx\
    --Routes.1.DestinationCidrBlock 10.2.3.0/24\
    --Routes.1.Status DISABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

