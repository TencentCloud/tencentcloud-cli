**Example 1: 删除路由key**



Input: 

```
tccli vpc DeleteRouteKeyInternal --cli-unfold-argument  \
    --DelRouteKeySet.0.Vip 10.6.2.3 \
    --DelRouteKeySet.0.VpcId 1 \
    --DelRouteKeySet.0.Protocol tcp \
    --DelRouteKeySet.0.VirtualPort 8181
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

