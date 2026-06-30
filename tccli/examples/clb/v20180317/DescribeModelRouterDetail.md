**Example 1: 查询模型路由实例详情**



Input: 

```
tccli clb DescribeModelRouterDetail --cli-unfold-argument  \
    --ModelRouterId cmr-h2tdbhtz
```

Output: 
```
{
    "Response": {
        "ModelRouter": {
            "CreatedTime": "2026-04-07T11:06:48+08:00",
            "Domain": "lb-531cv26i-x07lj684b5nps1ko.clb.gz-tencentclb.com",
            "ModelRouterId": "cmr-h2tdbhtz",
            "ModelRouterName": "test-enterprise-tgw-polaris",
            "ModelRouterType": "Enterprise",
            "BudgetId": "budget-1a2b3c4d",
            "BudgetName": "production-budget",
            "CreditUsage": {
                "Limit": 100,
                "Used": 12.34,
                "BudgetResetAt": "2026-04-21T00:00:00+08:00"
            },
            "ModifiedTime": "2026-04-08T00:11:21+08:00",
            "NetworkType": "Internet",
            "RateLimitConfig": {
                "RPM": 60,
                "TPM": 100000
            },
            "RouterSetting": {
                "FallBack": null,
                "RoutingStrategy": "SimpleShuffle"
            },
            "SecurityStatus": "Normal",
            "ServiceEndPoints": [
                {
                    "CertId": "SCkPG15A",
                    "Port": 443,
                    "Schema": "HTTPS"
                }
            ],
            "Status": "Active",
            "SubnetId": "subnet-2cxt138a",
            "Tags": [
                {
                    "TagKey": "tes2t",
                    "TagValue": "2"
                }
            ],
            "TradeStatus": "Normal",
            "Vip": "43.136.247.59",
            "VpcId": "vpc-fc7eyow9"
        },
        "RequestId": "80171270-1687-4764-b352-9476750c2061"
    }
}
```

