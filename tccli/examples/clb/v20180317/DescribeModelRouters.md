**Example 1: 查询模型路由实例**



Input: 

```
tccli clb DescribeModelRouters --cli-unfold-argument  \
    --ModelRouterIds cmr-rc1mry4d \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "ModelRouterSet": [
            {
                "CreatedTime": "2026-03-27T14:10:08+08:00",
                "Domain": "",
                "ModelRouterId": "cmr-rc1mry4d",
                "ModelRouterName": "test-enterprise-tgw-polaris",
                "ModelRouterType": "Enterprise",
                "BudgetId": "budget-1a2b3c4d",
                "BudgetName": "production-budget",
                "CreditUsageSet": [
                    {
                        "BudgetDuration": "1d",
                        "Limit": 100,
                        "Used": 12.34,
                        "BudgetResetAt": "2026-04-17T00:00:00+08:00"
                    },
                    {
                        "BudgetDuration": "30d",
                        "Limit": 1000,
                        "Used": 123.45,
                        "BudgetResetAt": "2026-05-01T00:00:00+08:00"
                    }
                ],
                "ModifiedTime": "2026-03-27T22:10:36+08:00",
                "NetworkType": "Intranet",
                "SecurityStatus": "Normal",
                "Status": "Active",
                "Tags": [],
                "TradeStatus": "Normal",
                "Vip": "172.16.0.28",
                "VpcId": "vpc-fc7eyow9"
            }
        ],
        "TotalCount": 1,
        "RequestId": "f6abe033-5e38-4637-a372-9cb5b2d85c9b"
    }
}
```

