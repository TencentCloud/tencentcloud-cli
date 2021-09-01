**Example 1: 禁用子网路由**



Input: 

```
tccli vpc DisableRoutes --cli-unfold-argument  \
    --RouteTableId rtb-9wzwlnhc \
    --RouteIds 18292 18293
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

**Example 2: 根据唯一ID禁用子网路由**



Input: 

```
tccli vpc DisableRoutes --cli-unfold-argument  \
    --RouteTableId rtb-12345678 \
    --RouteItemIds rti-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

