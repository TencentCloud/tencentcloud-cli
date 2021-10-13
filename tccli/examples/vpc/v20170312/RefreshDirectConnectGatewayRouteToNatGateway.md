**Example 1: 路由预刷新**

预刷新路由，只展示IDC网段信息

Input: 

```
tccli vpc RefreshDirectConnectGatewayRouteToNatGateway --cli-unfold-argument  \
    --VpcId vpc-3m6kvgrx \
    --NatGatewayId nat-2jd1e1rm \
    --DryRun True
```

Output: 
```
{
    "Response": {
        "RequestId": "928d1513-d3fa-4c4e-b8fd-077cebbc3118",
        "DirectConnectSubnetSet": [
            {
                "DirectConnectGatewayId": "dcg-71awizmv",
                "CidrBlock": "99.99.99.77/32"
            }
        ]
    }
}
```

**Example 2: 刷新路由**

正式刷新路由，执行刷新操作

Input: 

```
tccli vpc RefreshDirectConnectGatewayRouteToNatGateway --cli-unfold-argument  \
    --VpcId vpc-3m6kvgrx \
    --NatGatewayId nat-2jd1e1rm \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "RequestId": "b2b08cbc-c0dc-4346-bc55-a9b17a7a2a03",
        "DirectConnectSubnetSet": [
            {
                "DirectConnectGatewayId": "dcg-71awizmv",
                "CidrBlock": "99.99.99.77/32"
            }
        ]
    }
}
```

