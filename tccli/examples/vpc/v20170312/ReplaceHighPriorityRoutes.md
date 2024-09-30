**Example 1: 替换高优路由表条目信息**

替换高优路由表条目信息

Input: 

```
tccli vpc ReplaceHighPriorityRoutes --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --HighPriorityRoutes.0.HighPriorityRouteId hprti-0sb1mbut \
    --HighPriorityRoutes.0.DestinationCidrBlock 192.168.0.0/20 \
    --HighPriorityRoutes.0.GatewayType NORMAL_CVM \
    --HighPriorityRoutes.0.GatewayId 172.16.0.2 \
    --HighPriorityRoutes.0.Description ivan_test
```

Output: 
```
{
    "Response": {
        "NewHighPriorityRouteSet": [
            {
                "CreatedTime": "2024-07-11 17:34:48",
                "Description": "ivan_test",
                "DestinationCidrBlock": "192.168.0.0/20",
                "GatewayId": "172.16.0.2",
                "GatewayType": "NORMAL_CVM",
                "HighPriorityRouteId": "hprti-0sb1mbut",
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg"
            }
        ],
        "OldHighPriorityRouteSet": [
            {
                "CreatedTime": "2024-07-11 17:34:48",
                "Description": "ivan_test",
                "DestinationCidrBlock": "192.168.0.0/24",
                "GatewayId": "172.16.0.11",
                "GatewayType": "NORMAL_CVM",
                "HighPriorityRouteId": "hprti-0sb1mbut",
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg"
            }
        ],
        "RequestId": "c631a02c-052f-44b1-8807-f533cfa32406"
    }
}
```

