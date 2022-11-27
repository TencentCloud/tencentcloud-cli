**Example 1: 查询实例可修改套餐列表**



Input: 

```
tccli lighthouse DescribeModifyInstanceBundles --cli-unfold-argument  \
    --InstanceId lhins-f4s3n38h
```

Output: 
```
{
    "Response": {
        "ModifyBundleSet": [
            {
                "Bundle": {
                    "BundleDisplayLabel": "NORMAL",
                    "BundleId": "bundle_ntp_small2_500",
                    "BundleSalesState": "AVAILABLE",
                    "BundleType": "GENERAL_BUNDLE",
                    "CPU": 1,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 3,
                    "Memory": 2,
                    "MonthlyTraffic": 500,
                    "Price": {
                        "InstancePrice": {
                            "Discount": 100,
                            "DiscountPrice": 90,
                            "OriginalBundlePrice": 90,
                            "OriginalPrice": 90
                        }
                    },
                    "SupportLinuxUnixPlatform": true,
                    "SupportWindowsPlatform": true,
                    "SystemDiskSize": 40,
                    "SystemDiskType": "CLOUD_SSD"
                },
                "ModifyBundleState": "UNAVAILABLE",
                "NotSupportModifyMessage": "",
                "ModifyPrice": {
                    "InstancePrice": {
                        "Discount": 100,
                        "DiscountPrice": 19.73,
                        "OriginalBundlePrice": 90,
                        "OriginalPrice": 19.73
                    }
                }
            },
            {
                "Bundle": {
                    "BundleDisplayLabel": "NORMAL",
                    "BundleId": "bundle_ntp_small1_500",
                    "BundleSalesState": "AVAILABLE",
                    "BundleType": "GENERAL_BUNDLE",
                    "CPU": 1,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 3,
                    "Memory": 1,
                    "MonthlyTraffic": 500,
                    "Price": {
                        "InstancePrice": {
                            "Discount": 100,
                            "DiscountPrice": 90,
                            "OriginalBundlePrice": 90,
                            "OriginalPrice": 90
                        }
                    },
                    "SupportLinuxUnixPlatform": true,
                    "SupportWindowsPlatform": true,
                    "SystemDiskSize": 40,
                    "SystemDiskType": "CLOUD_SSD"
                },
                "ModifyBundleState": "UNAVAILABLE",
                "NotSupportModifyMessage": "",
                "ModifyPrice": {
                    "InstancePrice": {
                        "Discount": 100,
                        "DiscountPrice": 19.73,
                        "OriginalBundlePrice": 90,
                        "OriginalPrice": 19.73
                    }
                }
            },
            {
                "Bundle": {
                    "BundleDisplayLabel": "NORMAL",
                    "BundleId": "bundle_ntp_small2_1000",
                    "BundleSalesState": "AVAILABLE",
                    "BundleType": "GENERAL_BUNDLE",
                    "CPU": 1,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "Memory": 2,
                    "MonthlyTraffic": 1000,
                    "Price": {
                        "InstancePrice": {
                            "Discount": 100,
                            "DiscountPrice": 140,
                            "OriginalBundlePrice": 140,
                            "OriginalPrice": 140
                        }
                    },
                    "SupportLinuxUnixPlatform": true,
                    "SupportWindowsPlatform": true,
                    "SystemDiskSize": 40,
                    "SystemDiskType": "CLOUD_SSD"
                },
                "ModifyBundleState": "UNAVAILABLE",
                "NotSupportModifyMessage": "",
                "ModifyPrice": {
                    "InstancePrice": {
                        "Discount": 100,
                        "DiscountPrice": 52.6,
                        "OriginalBundlePrice": 140,
                        "OriginalPrice": 52.6
                    }
                }
            }
        ],
        "RequestId": "f1bb6c99-e704-441e-a405-a594cb55c989",
        "TotalCount": 3
    }
}
```

