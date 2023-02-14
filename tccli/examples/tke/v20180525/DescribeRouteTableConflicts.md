**Example 1: 查询路由表冲突列表**



Input: 

```
tccli tke DescribeRouteTableConflicts --cli-unfold-argument  \
    --RouteTableCidrBlock 10.4.0.0/16 \
    --VpcId vpc-abcdefgh
```

Output: 
```
{
    "Response": {
        "HasConflict": false,
        "RouteTableConflictSet": [
            {
                "RouteTableType": "CcsCluster",
                "RouteTableCidrBlock": "172.20.0.0/16",
                "RouteTableName": "tke-test",
                "RouteTableId": "cls-abcdefgh"
            }
        ],
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

