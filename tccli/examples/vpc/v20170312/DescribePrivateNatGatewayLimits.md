**Example 1: 查询可创建的私网NAT网关配额数量**



Input: 

```
tccli vpc DescribePrivateNatGatewayLimits --cli-unfold-argument  \
    --Filters.0.Name VpcId \
    --Filters.0.Values vpc-12234568 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PrivateNatGatewayLimitSet": [
            {
                "UniqVpcId": "vpc-12234568",
                "TotalLimit": 1000,
                "Available": 998
            }
        ],
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

