**Example 1: 创建VPN网关目的路由**

创建路由型VPN网关的目的路由

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
                "RouteId": "vpnr-xxxxxxxx",
                "DestinationCidrBlock": "10.0.0.0/24",
                "InstanceType": "VPNCONN",
                "InstanceId": "vpnx-xxxxxxxx",
                "Priority": 0,
                "Status": "ENABLE",
                "Type": "Static",
                "CreateTime": "2020-09-22 00:00:00",
                "UpdateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "a713021b-1942-4569-aa08-d8ad1867c2ad"
    }
}
```

**Example 2: 创建VPN网关路由示例**

创建路由型VPN网关的目的路由

Input: 

```
tccli vpc CreateVpnGatewayRoutes --cli-unfold-argument  \
    --Routes.0.Status ENABLE \
    --Routes.0.Priority 0 \
    --Routes.0.InstanceId vpnx-f99clft2 \
    --Routes.0.InstanceType VPNCONN \
    --Routes.0.DestinationCidrBlock 172.0.0.0/16 \
    --VpnGatewayId vpngw-7lhl5331
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "RouteId": "vpnr-85lq3m31",
                "DestinationCidrBlock": "172.0.0.0/16",
                "Status": "ENABLE",
                "InstanceId": "vpnx-f99clft2",
                "InstanceType": "VPNCONN",
                "Priority": 0,
                "Type": "Static",
                "CreateTime": "0000-00-00 00:00:00",
                "UpdateTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "a713021b-1942-4569-aa08-d8ad1867c2ad"
    }
}
```

