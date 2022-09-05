**Example 1: 查询当前账户可用套餐信息列表**



Input: 

```
tccli teo DescribeAvailablePlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e9fa0c8b-3c73-9ec2-cb5c-faa4725e0e07",
        "PlanInfoList": [
            {
                "Currency": "CNY",
                "Flux": 3000000000000,
                "Frequency": "m",
                "PlanType": "sta",
                "Price": 450000,
                "Request": 50000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 3000000000000,
                "Frequency": "m",
                "PlanType": "sta_with_bot",
                "Price": 1262500,
                "Request": 50000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 3000000000000,
                "Frequency": "m",
                "PlanType": "sta_cm",
                "Price": 380000,
                "Request": 50000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 3000000000000,
                "Frequency": "m",
                "PlanType": "sta_cm_with_bot",
                "Price": 1192500,
                "Request": 50000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 10000000000000,
                "Frequency": "m",
                "PlanType": "ent",
                "Price": 10228400,
                "Request": 80000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 10000000000000,
                "Frequency": "m",
                "PlanType": "ent_with_bot",
                "Price": 11216400,
                "Request": 80000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 10000000000000,
                "Frequency": "m",
                "PlanType": "ent_cm",
                "Price": 8637300,
                "Request": 80000000,
                "SiteNumber": 1
            },
            {
                "Currency": "CNY",
                "Flux": 10000000000000,
                "Frequency": "m",
                "PlanType": "ent_cm_with_bot",
                "Price": 9625300,
                "Request": 80000000,
                "SiteNumber": 1
            }
        ]
    }
}
```

