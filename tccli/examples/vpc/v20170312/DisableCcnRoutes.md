**Example 1: 禁用多条路由策略**

禁用多条路由策略

Input: 

```
tccli vpc DisableCcnRoutes --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --RouteIds ccnr-bvipc87w ccnr-oc61so0o
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

