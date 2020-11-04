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
                        "OriginalBundlePrice": 60.0,
                        "OriginalPrice": 60.0,
                        "Discount": 65,
                        "DiscountPrice": 39.0
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": false,
                "BundleSalesState": "AVAILABLE",
                "BundleType": "GENERAL_BUNDLE"
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
                        "OriginalBundlePrice": 90.0,
                        "OriginalPrice": 90.0,
                        "Discount": 65,
                        "DiscountPrice": 58.5
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleSalesState": "AVAILABLE",
                "BundleType": "GENERAL_BUNDLE"
            }
        ],
        "TotalCount": 2,
        "RequestId": "4f05e47f-9d54-49a9-8d03-bca50b32dbc5"
    }
}
```

