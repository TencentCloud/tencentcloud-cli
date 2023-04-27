**Example 1: 查询套餐-成功返回**

查询套餐-成功返回

Input: 

```
tccli lighthouse DescribeBundles --cli-unfold-argument  \
    --BundleIds bundle_ntp_small1_500 bundle_bw_small1_1
```

Output: 
```
{
    "Response": {
        "BundleSet": [
            {
                "BundleId": "bundle2022_gen_02",
                "CPU": 2,
                "Memory": 2,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 50,
                "InternetMaxBandwidthOut": 5,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 500,
                "Price": {
                    "InstancePrice": {
                        "Currency": "CNY",
                        "OriginalBundlePrice": 60.0,
                        "OriginalPrice": 60.0,
                        "Discount": 66.229933,
                        "DiscountPrice": 39.74
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "GENERAL_BUNDLE",
                "BundleTypeDescription": "通用型",
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b2563b1d-e93f-4e05-9c6f-096e0c403add"
    }
}
```

