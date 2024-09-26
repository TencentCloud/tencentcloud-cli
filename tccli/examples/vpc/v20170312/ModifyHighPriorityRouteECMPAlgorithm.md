**Example 1: 修改高优路由表 ECMP算法**

修改高优路由表 ECMP算法

Input: 

```
tccli vpc ModifyHighPriorityRouteECMPAlgorithm --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --RouteECMPAlgorithms.0.DestinationCidrBlock 172.20.0.0/19 \
    --RouteECMPAlgorithms.0.SubnetRouteAlgorithm ECMP_SOURCE_IP_HASH
```

Output: 
```
{
    "Response": {
        "RequestId": "89e403aa-b156-4d6d-9d41-3cd7cb995b65"
    }
}
```

