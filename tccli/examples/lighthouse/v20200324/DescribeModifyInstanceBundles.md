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
        "TotalCount": 0,
        "ModifyBundleSet": [
            {
                "ModifyPrice": {
                    "InstancePrice": {
                        "OriginalBundlePrice": 0,
                        "OriginalPrice": 0,
                        "Discount": 0,
                        "DiscountPrice": 0,
                        "Currency": "abc"
                    }
                },
                "ModifyBundleState": "abc",
                "Bundle": {
                    "BundleId": "abc",
                    "Memory": 0,
                    "SystemDiskType": "abc",
                    "SystemDiskSize": 0,
                    "MonthlyTraffic": 0,
                    "SupportLinuxUnixPlatform": true,
                    "SupportWindowsPlatform": true,
                    "Price": {
                        "InstancePrice": {
                            "OriginalBundlePrice": 0,
                            "OriginalPrice": 0,
                            "Discount": 0,
                            "DiscountPrice": 0,
                            "Currency": "abc"
                        }
                    },
                    "CPU": 0,
                    "InternetMaxBandwidthOut": 1,
                    "InternetChargeType": "abc",
                    "BundleSalesState": "abc",
                    "BundleType": "abc",
                    "BundleTypeDescription": "abc",
                    "BundleDisplayLabel": "abc"
                },
                "NotSupportModifyMessage": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

