**Example 1: 查询VPN网关目的路由**

查询VPN网关目的路由

Input: 

```
tccli vpc DescribeVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-7lhl5331 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "RouteId": "vpnr-h53fo5tv",
                "DestinationCidrBlock": "10.0.0.0/16",
                "Status": "ENABLE",
                "InstanceId": "vpnx-f99clft2",
                "InstanceType": "VPNCONN",
                "Priority": 0,
                "Type": "Static",
                "CreateTime": "2022-12-05 11:02:44",
                "UpdateTime": "2022-12-05 11:02:44"
            }
        ],
        "TotalCount": 1,
        "RequestId": "cf5ec1b0-ec85-4e28-bc05-763c617b57a0"
    }
}
```

