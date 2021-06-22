**Example 1: 删除指定VPN网关路由**



Input: 

```
tccli vpc DeleteVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-12345678 \
    --RouteIds xxx-xxxx xxx-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

