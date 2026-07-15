**Example 1: 正常响应**



Input: 

```
tccli tokenhub DescribeEndpoint --cli-unfold-argument  \
    --EndpointId ep-uikic4v5
```

Output: 
```
{
    "Response": {
        "Endpoint": {
            "ChargeDetail": "{\"FreeQuota\":{\"TotalQuota\":200,\"UsedQuota\":0,\"UsagePercent\":0,\"ExpireTime\":\"2026-09-21T17:39:22.10566639+08:00\"}}",
            "ChargeType": "FREE",
            "EndpointId": "ep-test",
            "EndpointName": "测试服务",
            "ModelId": "deepseek-v3.2",
            "ModelName": "deepseek-v3.2",
            "PaymentEnabled": false,
            "ServiceType": "TEXT_GENERATION",
            "Status": "ACTIVE"
        },
        "RequestId": "6903b78b-a277-46c7-9bb6-805da0ec6a57"
    }
}
```

