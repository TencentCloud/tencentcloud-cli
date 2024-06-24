**Example 1: 查询实例可修改套餐列表**

查询实例可修改套餐列表

Input: 

```
tccli lighthouse DescribeModifyInstanceBundles --cli-unfold-argument  \
    --InstanceId lhins-p6xbekdt
```

Output: 
```
{
    "Response": {
        "ModifyBundleSet": [
            {
                "Bundle": {
                    "BundleDisplayLabel": "NORMAL",
                    "BundleId": "bundle_gen_mc_med2_02",
                    "BundleSalesState": "AVAILABLE",
                    "BundleType": "GENERAL_BUNDLE",
                    "BundleTypeDescription": "通用型",
                    "CPU": 2,
                    "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 5,
                    "Memory": 2,
                    "MonthlyTraffic": 500,
                    "Price": {
                        "InstancePrice": {
                            "Currency": "CNY",
                            "Discount": 100,
                            "DiscountPrice": 65,
                            "OriginalBundlePrice": 65,
                            "OriginalPrice": 65
                        }
                    },
                    "SupportLinuxUnixPlatform": true,
                    "SupportWindowsPlatform": true,
                    "SystemDiskSize": 70,
                    "SystemDiskType": "CLOUD_PREMIUM"
                },
                "ModifyBundleState": "AVAILABLE",
                "ModifyPrice": {
                    "InstancePrice": {
                        "Currency": "CNY",
                        "Discount": 100,
                        "DiscountPrice": 10,
                        "OriginalBundlePrice": 65,
                        "OriginalPrice": 10
                    }
                },
                "NotSupportModifyMessage": ""
            }
        ],
        "RequestId": "651060b7-b781-4ed9-898c-a06b8c5c51dc",
        "TotalCount": 1
    }
}
```

