**Example 1: 查询路由策略冲突列表**



Input: 

```
tccli ecm DescribeRouteConflicts --cli-unfold-argument  \
    --RouteTableId rtb-q8o2z892 \
    --DestinationCidrBlocks 10.11.0.0/24
```

Output: 
```
{
    "Response": {
        "RouteConflictSet": [],
        "RequestId": "cf11a8a4-e7c6-42cf-a35a-649c1789868b"
    }
}
```

