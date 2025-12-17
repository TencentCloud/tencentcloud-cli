**Example 1: 查询路由接收策略实例ID列表**

查询路由接收策略实例ID列表。

Input: 

```
tccli vpc DescribeRoutePolicies --cli-unfold-argument  \
    --RoutePolicyIds rrp-r70ctaia
```

Output: 
```
{
    "Response": {
        "RoutePolicySet": [
            {
                "RoutePolicyId": "rrp-r70ctaia",
                "RoutePolicyDescription": "TEST",
                "RoutePolicyName": "TEST",
                "CreatedTime": "2023-05-20 15:21:54",
                "RoutePolicyEntrySet": [
                    {
                        "RoutePolicyEntryId": "rrpi-aoh9t21x",
                        "Description": "",
                        "GatewayType": "CVM",
                        "GatewayId": "172.16.16.37",
                        "Priority": 10,
                        "Action": "ACCEPT",
                        "RouteType": "ANY",
                        "CidrBlock": "192.168.0.0/16",
                        "CreatedTime": "2023-05-12 10:00:00",
                        "Region": "ap-guangzhou"
                    }
                ],
                "RoutePolicyAssociationSet": [
                    {
                        "RoutePolicyId": "rrp-r70ctaia",
                        "RouteTableId": "rtb-qk8eyn9g",
                        "Priority": 600
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "037e2d12-aea5-48f1-b8db-db1c08722102"
    }
}
```

