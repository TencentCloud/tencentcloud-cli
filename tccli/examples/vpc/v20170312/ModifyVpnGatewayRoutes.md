**Example 1: 禁用VPN网关路由**

禁用某条VPN网关路由

Input: 

```
tccli vpc ModifyVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpn-ngenl4az \
    --Routes.0.RouteId vpnr-7t3tknmg \
    --Routes.0.Status DISABLE
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "DestinationCidrBlock": "192.241.0.0/24",
                "Status": "ENABLE",
                "InstanceId": "vpnx-ng2asdew",
                "InstanceType": "VPNCONN",
                "Priority": 100
            }
        ],
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

