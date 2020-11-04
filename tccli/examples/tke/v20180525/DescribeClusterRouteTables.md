**Example 1: 查询集群路由表**



Input: 

```
tccli tke DescribeClusterRouteTables --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-xxx",
                "RouteTableCidrBlock": "10.4.0.0/16",
                "RouteTableName": "MANAGED_CLUSTER"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

