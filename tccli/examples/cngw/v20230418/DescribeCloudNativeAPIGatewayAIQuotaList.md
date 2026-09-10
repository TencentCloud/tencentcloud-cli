**Example 1: 根据消费者Id过滤配额规则**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayAIQuotaList --cli-unfold-argument  \
    --GatewayId gateway-b6ec1f87 \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name cg-xxx \
    --Filters.0.Values cg-xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CreateTime": "2026-06-15 19:58:50",
                    "Enabled": true,
                    "Id": "701ece40-76a6-43ab-9477-888ab248c1f5",
                    "ModifyTime": "2026-06-15 20:11:02",
                    "PeriodUnit": "Month",
                    "QuotaLimit": 8000000,
                    "QuotaType": "TotalToken",
                    "ResourceId": "08727499-7d9d-41bd-86d1-9a9305ed1fc6",
                    "ResourceName": "even-2",
                    "ResourceType": "Consumer",
                    "Source": "Manual"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "6e8f07de-b0e4-45c3-9cd8-63887c310e35"
    }
}
```

