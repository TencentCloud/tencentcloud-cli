**Example 1: 查询套餐时指定镜像**

查询套餐时指定镜像

Input: 

```
tccli lighthouse DescribeBundleConfigs --cli-unfold-argument  \
    --BundleIds bundle_starter_mc_med2_01 \
    --BlueprintId lhbp-etg1zbmm
```

Output: 
```
{
    "Response": {
        "BundleConfigSet": [
            {
                "BandwidthType": "BANDWIDTH",
                "BundleDisplayLabel": "NORMAL",
                "BundleId": "bundle_starter_mc_med2_01",
                "BundleSalesState": "SOLD_OUT",
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 20,
                "CPU": 2,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "InternetMaxBandwidthOut": 3,
                "Memory": 2,
                "MonthlyTraffic": 200,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "SystemDiskSize": 40,
                "SystemDiskType": "CLOUD_SSD",
                "TrafficUnlimited": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "066f45e2-89eb-4d4a-b438-1f8e34c014a8"
    }
}
```

**Example 2: 查询套餐配置**

查询套餐配置

Input: 

```
tccli lighthouse DescribeBundleConfigs --cli-unfold-argument  \
    --BundleIds bundle_ntp_small1_500 bundle_bw_small1_1 \
    --Offset 0 \
    --Limit 20 \
    --Zones ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "BundleConfigSet": [
            {
                "BundleId": "bundle_starter_mc_med8_02",
                "CPU": 2,
                "Memory": 8,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 100,
                "InternetMaxBandwidthOut": 8,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 1000,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 1,
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            },
            {
                "BundleId": "bundle_starter_mc_med8_01",
                "CPU": 2,
                "Memory": 8,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 80,
                "InternetMaxBandwidthOut": 7,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 800,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 1,
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            },
            {
                "BundleId": "bundle_starter_mc_lg4_02",
                "CPU": 4,
                "Memory": 4,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 70,
                "InternetMaxBandwidthOut": 6,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 600,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 1,
                "BundleSalesState": "SOLD_OUT",
                "BundleDisplayLabel": "ACTIVITY"
            },
            {
                "BundleId": "bundle_starter_mc_med4_02",
                "CPU": 2,
                "Memory": 4,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 70,
                "InternetMaxBandwidthOut": 6,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 600,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 1,
                "BundleSalesState": "AVAILABLE",
                "BundleDisplayLabel": "NORMAL"
            },
            {
                "BundleId": "bundle_starter_mc_lg4_01",
                "CPU": 4,
                "Memory": 4,
                "SystemDiskType": "CLOUD_SSD",
                "SystemDiskSize": 60,
                "InternetMaxBandwidthOut": 5,
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "MonthlyTraffic": 500,
                "SupportLinuxUnixPlatform": true,
                "SupportWindowsPlatform": true,
                "BundleType": "STARTER_BUNDLE",
                "BundleTypeDescription": "入门型",
                "BundleTypePriority": 1,
                "BundleSalesState": "SOLD_OUT",
                "BundleDisplayLabel": "ACTIVITY"
            }
        ],
        "TotalCount": 4,
        "RequestId": "ec60eb8d-057d-4e34-8a1b-1e8c1d5cea19"
    }
}
```

