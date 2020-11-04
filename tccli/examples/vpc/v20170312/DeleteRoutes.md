**Example 1: 删除路由规则**



Input: 

```
tccli vpc DeleteRoutes --cli-unfold-argument  \
    --Version 2017-03-12\
    --RouteTableId rtb-n0yejvje\
    --Routes.0.RouteId 16644
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

