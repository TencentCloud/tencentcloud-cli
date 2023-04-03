**Example 1: 删除指定VPN网关路由**

本接口（DeleteVpnGatewayRoutes）用于删除VPN网关路由

Input: 

```
tccli vpc DeleteVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-12345678 \
    --RouteIds vpnr-00wv1z75 vpnr-19oqx1ab
```

Output: 
```
{
    "Response": {
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

