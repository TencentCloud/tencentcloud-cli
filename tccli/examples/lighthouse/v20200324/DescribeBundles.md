**Example 1: 查询套餐-成功返回**



Input: 

```
tccli lighthouse DescribeBundles --cli-unfold-argument  \
    --BundleIds bundle_bw_small1_1 bundle_ntp_small1_500
```

Output: 
```
{
    "Response": {
        "BundleSet": [
            {
                "BundleId": "bundle_bw_small1_1",
                "CPU": 1,
                "Memory": 1,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 20,
                "InternetMaxBandwidthOut": 1,
                "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 1,
                "Price": {
                    "InstancePrice": {
                        "OriginalBundlePrice": 60,
                        "OriginalPrice": 60,
                        "Discount": 65,
                        "DiscountPrice": 39
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": false,
                "BundleType": "GENERAL_BUNDLE",
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            },
            {
                "BundleId": "bundle_ntp_small1_500",
                "CPU": 1,
                "Memory": 1,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 40,
                "InternetMaxBandwidthOut": 3,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 500,
                "Price": {
                    "InstancePrice": {
                        "OriginalBundlePrice": 90,
                        "OriginalPrice": 90,
                        "Discount": 65,
                        "DiscountPrice": 58.5
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "GENERAL_BUNDLE",
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6d4c966d-bc42-4425-8c98-a39f36c7ad1b"
    }
}
```

