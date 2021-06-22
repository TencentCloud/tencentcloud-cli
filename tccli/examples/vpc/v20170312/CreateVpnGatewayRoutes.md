**Example 1: 创建VPN网关目的路由**



Input: 

```
tccli vpc CreateVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpn-ngenl4az \
    --Routes.0.DestinationCidrBlock 192.241.0.0/24 \
    --Routes.0.Status ENABLE \
    --Routes.0.InstanceType VPNCONN \
    --Routes.0.InstanceId vpnx-ng2asdew \
    --Routes.0.Priority 100
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

