**Example 1: GetBillingSpecs**



Input: 

```
tccli wedata GetBillingSpecs --cli-unfold-argument  \
    --ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "Data": {
            "SpecInfos": [
                {
                    "Available": true,
                    "AvailableRegion": [],
                    "CategoryId": "1024552",
                    "GpuType": "T4",
                    "SpecAlias": "8C32G T4*1",
                    "SpecFeatures": [
                        "TurboCFS",
                        "VpcENI",
                        "EMR",
                        "COS",
                        "CBS",
                        "CFS"
                    ],
                    "SpecId": "sv_tio_platform_cloud_post_gpu_8c32g_1t4",
                    "SpecName": "TI.GN7.2XLARGE32.POST",
                    "SpecType": "GPU"
                }
            ]
        },
        "RequestId": "8e967e6a-9927-4caf-a98a-b76c560e541c"
    }
}
```

