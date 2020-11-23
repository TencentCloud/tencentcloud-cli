**Example 1: 删除路由规则**



Input: 

```
tccli ecm DeleteRoutes --cli-unfold-argument  \
    --RouteTableId rtb-12345678 \
    --Routes.0.RouteId 678
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

