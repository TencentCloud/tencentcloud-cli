**Example 1: 查询镜像实例**

查询镜像实例

Input: 

```
tccli lighthouse DescribeBlueprintBundles --cli-unfold-argument  \
    --BlueprintId lhbp-5e886mc4
```

Output: 
```
{
    "Response": {
        "BlueprintBundleSet": [
            {
                "BundleId": "bundle_game_mc_gen_03",
                "CPU": 2,
                "Memory": 8,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 50,
                "InternetMaxBandwidthOut": 6,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 500,
                "Price": {
                    "InstancePrice": {
                        "Currency": "CNY",
                        "OriginalBundlePrice": 80,
                        "OriginalPrice": 80,
                        "Discount": 100,
                        "DiscountPrice": 80
                    }
                },
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "GAME_PORTAL_BUNDLE",
                "BundleTypeDescription": "游戏专区",
                "BundleTypePriority": 110,
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL",
                "SupportSlot": 4
            }
        ],
        "TotalCount": 1,
        "RequestId": "a04dba8e-efb7-4c9b-ac19-2b5b779b3e1b"
    }
}
```

