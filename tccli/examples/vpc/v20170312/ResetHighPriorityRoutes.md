**Example 1: 重置高优路由表条目**

重置高优路由表条目

Input: 

```
tccli vpc ResetHighPriorityRoutes --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --Name demo \
    --HighPriorityRoutes.0.DestinationCidrBlock 172.20.0.0/18 \
    --HighPriorityRoutes.0.GatewayType NORMAL_CVM \
    --HighPriorityRoutes.0.GatewayId 172.16.0.11 \
    --HighPriorityRoutes.0.Description demo
```

Output: 
```
{
    "Response": {
        "RequestId": "461358ec-f329-4273-b5f0-e87730703e6d"
    }
}
```

