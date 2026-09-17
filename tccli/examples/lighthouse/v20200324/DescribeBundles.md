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
                        "OriginalBundlePrice": 60,
                        "OriginalPrice": 60,
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

**Example 2: 查询套餐时指定镜像**

查询套餐时指定镜像

Input: 

```
tccli lighthouse DescribeBundles --cli-unfold-argument  \
    --BundleIds bundle_starter_mc_med2_01 \
    --BlueprintId lhbp-etg1zbmm
```

Output: 
```
{
    "Response": {
        "BundleSet": [
            {
                "BundleDisplayLabel": "NORMAL",
                "BundleId": "bundle_starter_mc_med2_01",
                "BundleSalesState": "SOLD_OUT",
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "CPU": 2,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "InternetMaxBandwidthOut": 3,
                "Memory": 2,
                "MonthlyTraffic": 200,
                "Price": {
                    "InstancePrice": {
                        "Currency": "CNY",
                        "Discount": 100,
                        "DiscountPrice": 40,
                        "OriginalBundlePrice": 40,
                        "OriginalPrice": 40
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "SystemDiskSize": 40,
                "SystemDiskType": "CLOUD_SSD",
                "TrafficUnlimited": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "34069df6-5f6c-4a7e-9895-6bd266d67e7d"
    }
}
```

