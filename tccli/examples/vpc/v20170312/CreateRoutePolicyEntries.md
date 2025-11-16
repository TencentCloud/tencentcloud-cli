**Example 1: 创建路由接收策略条目。**

创建路由接收策略条目。

Input: 

```
tccli vpc CreateRoutePolicyEntries --cli-unfold-argument  \
    --RoutePolicyId rrp-azd4dt1c \
    --RoutePolicyEntrySet.0.CidrBlock 192.168.0.0/16 \
    --RoutePolicyEntrySet.0.GatewayType CVM \
    --RoutePolicyEntrySet.0.GatewayId 172.16.16.37 \
    --RoutePolicyEntrySet.0.Priority 100 \
    --RoutePolicyEntrySet.0.Action ACCEPT \
    --RoutePolicyEntrySet.0.RouteType USER
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

