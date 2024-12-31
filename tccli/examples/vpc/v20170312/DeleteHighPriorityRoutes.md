**Example 1: 删除高优路由表条目**

删除高优路由表条目

Input: 

```
tccli vpc DeleteHighPriorityRoutes --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --HighPriorityRouteIds hprti-hd4tl8cr
```

Output: 
```
{
    "Response": {
        "HighPriorityRouteSet": [
            {
                "CreatedTime": "2024-07-11 17:07:03",
                "Description": "demo",
                "DestinationCidrBlock": "172.20.0.0/18",
                "GatewayId": "172.16.0.11",
                "GatewayType": "CVM",
                "HighPriorityRouteId": "hprti-hd4tl8cr",
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg"
            }
        ],
        "RequestId": "984c005d-e0d0-4d4a-98f5-b4b5c3af1e66"
    }
}
```

