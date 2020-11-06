**Example 1: 查询路由表冲突列表**



Input: 

```
tccli tke DescribeRouteTableConflicts --cli-unfold-argument  \
    --RouteTableCidrBlock 10.4.0.0/16 \
    --VpcId vpc-xxx
```

Output: 
```
{
    "Response": {
        "HasConflict": false,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

