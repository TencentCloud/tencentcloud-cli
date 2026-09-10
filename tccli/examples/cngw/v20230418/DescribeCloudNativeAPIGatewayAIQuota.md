**Example 1: 查询AI网关配额详情**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayAIQuota --cli-unfold-argument  \
    --GatewayId gateway-4a133c03 \
    --Id c4db7b5c-6de3-4597-a03f-b3ee9de5be2d
```

Output: 
```
{
    "Response": {
        "Result": {
            "CreateTime": "2026-05-13 15:49:29",
            "Enabled": true,
            "Id": "c4db7b5c-6de3-4597-a03f-b3ee9de5be2d",
            "ModifyTime": "2026-05-13 16:27:20",
            "PeriodUnit": "Day",
            "QuotaLimit": 10,
            "QuotaType": "RequestCount",
            "ResourceId": "71a775c5-e634-41ad-b329-15f6eac47f33",
            "ResourceName": "j********t",
            "ResourceType": "Consumer",
            "UsageRate": -1,
            "Used": -1
        },
        "RequestId": "2ffb26d8-409a-4651-8096-41092fc752ea"
    }
}
```

