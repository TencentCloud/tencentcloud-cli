**Example 1: 禁用VPN网关路由**

禁用某条VPN网关路由

Input: 

```
tccli vpc ModifyVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-ngenl4az \
    --Routes.0.RouteId vpnr-7t3tknmg \
    --Routes.0.Status DISABLE
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "RouteId": "vpnr-7t3tknmg",
                "DestinationCidrBlock": "10.11.0.0/16",
                "Status": "DISABLE",
                "InstanceId": "vpnx-ng2asdew",
                "InstanceType": "VPNCONN",
                "Priority": 0,
                "Type": "Static",
                "CreateTime": "2023-03-21 07:08:13",
                "UpdateTime": "2023-04-28 17:02:43"
            }
        ],
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

