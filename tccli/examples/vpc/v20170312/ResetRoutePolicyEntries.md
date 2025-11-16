**Example 1: 重置路由接收策略规则**

重置路由接收策略规则。

Input: 

```
tccli vpc ResetRoutePolicyEntries --cli-unfold-argument  \
    --RoutePolicyId rrp-azd4dt1c \
    --RoutePolicyDescription TEST \
    --RoutePolicyName TEST \
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

