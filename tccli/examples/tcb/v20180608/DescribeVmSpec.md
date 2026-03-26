**Example 1: 查询LightHouse规格**



Input: 

```
tccli tcb DescribeVmSpec --cli-unfold-argument  \
    --Type LightHouse
```

Output: 
```
{
    "Response": {
        "SpecList": [
            {
                "LightHouseSpec": {
                    "BundleConfig": "{\"BundleId\":\"bundle_starter_mc_med2_01\",\"Memory\":2,\"SystemDiskType\":\"CLOUD_SSD\",\"SystemDiskSize\":40,\"MonthlyTraffic\":200,\"SupportLinuxUnixPlatform\":true,\"SupportWindowsPlatform\":true,\"Price\":{\"InstancePrice\":{\"OriginalBundlePrice\":40,\"OriginalPrice\":40,\"Discount\":100,\"DiscountPrice\":40,\"Currency\":\"CNY\"}},\"CPU\":2,\"InternetMaxBandwidthOut\":3,\"InternetChargeType\":\"TRAFFIC_POSTPAID_BY_HOUR\",\"BundleSalesState\":\"AVAILABLE\",\"BundleType\":\"STARTER_BUNDLE\",\"BundleTypeDescription\":\"入门型\",\"BundleTypePriority\":20,\"BundleDisplayLabel\":\"NORMAL\",\"TrafficUnlimited\":false,\"BandwidthType\":\"BANDWIDTH\"}",
                    "BundleId": "bundle_starter_mc_med2_01"
                },
                "Price": {
                    "Currency": "CNY",
                    "Discount": 100,
                    "DiscountCredits": 1333.3334,
                    "DiscountPrice": 40,
                    "OriginalCredits": 1333.3334,
                    "OriginalPrice": 40
                },
                "Type": "LightHouse"
            }
        ],
        "RequestId": "435b540b-3677-4960-9f5c-3960f0d837c5"
    }
}
```

