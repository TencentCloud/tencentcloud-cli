**Example 1: 查询可用的计算资源计费项规格**



Input: 

```
tccli tione DescribeBillingSpecs --cli-unfold-argument  \
    --ChargeType POSTPAID_BY_HOUR \
    --ResourceType GPU
```

Output: 
```
{
    "Response": {
        "Specs": [
            {
                "Available": true,
                "AvailableRegion": [],
                "CategoryId": "1024552",
                "GpuType": "T4",
                "SpecAlias": "8C32GB GPU(T4)*1",
                "SpecFeatures": [
                    "TurboCFS"
                ],
                "SpecId": "sv_tio_platform_cloud_post_gpu_8c32g_1t4",
                "SpecName": "TI.GN7.2XLARGE32.POST",
                "SpecType": "GPU"
            }
        ],
        "RequestId": "41cf032e-3bcd-4e60-8c97-98cb0812b505"
    }
}
```

