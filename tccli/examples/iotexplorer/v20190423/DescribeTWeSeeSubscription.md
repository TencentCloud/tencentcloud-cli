**Example 1: 查询 TWeSee 视频理解订阅**



Input: 

```
tccli iotexplorer DescribeTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 69E4CNU1F0 \
    --DeviceName 10001 \
    --ServiceType VID_COMP
```

Output: 
```
{
    "Response": {
        "ComprehensionConfig": {
            "DetectTypes": [
                "person"
            ]
        },
        "CreditsQuota": 9000,
        "CreditsUsed": 23.5,
        "Enabled": true,
        "ExpireTime": 1793172443,
        "QuotaAdvanced": 9000,
        "QuotaRefreshTime": 1793172443,
        "QuotaUsedAdvanced": 23,
        "ResourceId": "twesee-753yd29zay9tzk8t140mner",
        "ServiceTier": "ADVANCED",
        "Status": "NORMAL",
        "RequestId": "3af64ac3-74d8-4435-b02a-1a0803427518"
    }
}
```

