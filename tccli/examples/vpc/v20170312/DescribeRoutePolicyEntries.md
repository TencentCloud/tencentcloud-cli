**Example 1: 查询路由策略规则列表**

查询路由策略规则列表。

Input: 

```
tccli vpc DescribeRoutePolicyEntries --cli-unfold-argument  \
    --Filters.0.Name route-policy-id \
    --Filters.0.Values rrp-fcrulzf8 \
    --Offset 1 \
    --Limit 1 \
    --OrderField abc \
    --OrderDirection abc
```

Output: 
```
{
    "Response": {
        "RoutePolicyEntrySet": [
            {
                "RoutePolicyEntryId": "rrpi-5j5wut37",
                "Description": "",
                "GatewayType": "PVGW",
                "GatewayId": "172.16.16.37",
                "Priority": 1113,
                "Action": "DROP",
                "RouteType": "ANY",
                "CidrBlock": "10.0.0.0/16",
                "CreatedTime": "2021-09-08 15:20:14",
                "Region": "ap-guangtzhou"
            }
        ],
        "TotalCount": 1,
        "RequestId": "2cd67e99-9376-421d-a5bb-044a10c9d744"
    }
}
```

