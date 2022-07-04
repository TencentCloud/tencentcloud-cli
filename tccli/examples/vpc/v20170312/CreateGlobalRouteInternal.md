**Example 1: 添加全局路由**



Input: 

```
tccli vpc CreateGlobalRouteInternal --cli-unfold-argument  \
    --GlobalRouteRequestSet.0.VpcId 1 \
    --GlobalRouteRequestSet.0.Subnet 10.0.0.0 \
    --GlobalRouteRequestSet.0.IntMask 16 \
    --GlobalRouteRequestSet.0.Remote 172.16.0.18 \
    --GlobalRouteRequestSet.0.Type 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

