**Example 1: 创建VPC路由接收策略。**

创建VPC路由接收策略。

Input: 

```
tccli vpc CreateRoutePolicy --cli-unfold-argument  \
    --RoutePolicyName TEST \
    --RoutePolicyDescription TEST \
    --RoutePolicyEntrySet.0.Description TEST \
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
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "RoutePolicy": {
            "RoutePolicyId": "rrp-azd4dt1c",
            "RoutePolicyName": "TEST",
            "RoutePolicyEntrySet": [
                {
                    "Description": "",
                    "CidrBlock": "192.168.0.0/16",
                    "GatewayType": "CVM",
                    "GatewayId": "172.16.16.37",
                    "Priority": 100,
                    "Action": "ACCEPT",
                    "RouteType": "USER"
                }
            ]
        }
    }
}
```

