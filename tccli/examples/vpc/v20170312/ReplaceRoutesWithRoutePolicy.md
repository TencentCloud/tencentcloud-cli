**Example 1: 匹配路由接收策略**

匹配路由接收策略

Input: 

```
tccli vpc ReplaceRoutesWithRoutePolicy --cli-unfold-argument  \
    --RouteTableId rtb-65ckdx3a \
    --Routes.0.RouteItemId rti-g8jl2vll \
    --Routes.0.ForceMatchPolicy True
```

Output: 
```
{
    "Response": {
        "RequestId": "93512103-76f6-4780-a146-73380b1ab748"
    }
}
```

