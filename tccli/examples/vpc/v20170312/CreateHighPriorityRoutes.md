**Example 1: 创建高优路由表条目**

创建高优路由表条目

Input: 

```
tccli vpc CreateHighPriorityRoutes --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --HighPriorityRoutes.0.DestinationCidrBlock 192.168.0.0/24 \
    --HighPriorityRoutes.0.GatewayType NORMAL_CVM \
    --HighPriorityRoutes.0.GatewayId 172.16.0.11 \
    --HighPriorityRoutes.0.Description ivan_test
```

Output: 
```
{
    "Response": {
        "HighPriorityRouteSet": [
            {
                "CreatedTime": "0000-00-00 00:00:00",
                "Description": "ivan_test",
                "DestinationCidrBlock": "192.168.0.0/24",
                "GatewayId": "172.16.0.11",
                "GatewayType": "NORMAL_CVM",
                "HighPriorityRouteId": "hprti-0sb1mbut",
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg",
                "SubnetRouteAlgorithm": "ECMP_QUINTUPLE_HASH"
            }
        ],
        "RequestId": "2af8e306-ffc0-4f18-a927-9f1ee04f0788"
    }
}
```

