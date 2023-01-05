**Example 1: 查询计费项列表 示例**

查询计费项列表

Input: 

```
tccli tione DescribeBillingSpecs --cli-unfold-argument  \
    --ChargeType PREPAID \
    --TaskType TRAIN
```

Output: 
```
{
    "Response": {
        "RequestId": "9f91ba5c-03bb-4c02-b9cc-d2740821112f",
        "Specs": [
            {
                "SpecName": "TI.GN10.2XLARGE40.POST",
                "SpecAlias": "8核40GB V100*1",
                "SpecId": "sv_tio_platform_cloud_post_gpu_8c40g_1v100",
                "Available": false,
                "AvailableRegion": [
                    "ap-guangzhou",
                    "ap-beijing"
                ]
            }
        ]
    }
}
```

