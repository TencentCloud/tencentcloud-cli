**Example 1: 资源包绑定策略查询**

无

Input: 

```
tccli billing DescribeMeasureBoundPackageList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProductCode p_bsp \
    --SubscriptionId bsp100570
```

Output: 
```
{
    "Response": {
        "Data": {
            "BindPackages": [
                {
                    "BindProperties": [],
                    "EffectiveTime": "2025-02-28 11:29:33",
                    "InvalidTime": "9999-99-99 99:99:99",
                    "ResourceId": "bsp-jlj000eALGlLEc5"
                },
                {
                    "BindProperties": [
                        {
                            "PropertyKey": "regionId",
                            "PropertyValue": "47"
                        }
                    ],
                    "EffectiveTime": "2025-03-04 15:15:07",
                    "InvalidTime": "9999-99-99 99:99:99",
                    "ResourceId": "bsp-jln000eAMm5Odlo"
                },
                {
                    "BindProperties": [
                        {
                            "PropertyKey": "regionId",
                            "PropertyValue": "47"
                        }
                    ],
                    "EffectiveTime": "2025-03-04 15:17:04",
                    "InvalidTime": "9999-99-99 99:99:99",
                    "ResourceId": "bsp-jln000eAMlZAb44"
                },
                {
                    "BindProperties": [],
                    "EffectiveTime": "2025-03-04 16:43:24",
                    "InvalidTime": "9999-99-99 99:99:99",
                    "ResourceId": "bsp-jln000eAMmNWl47"
                }
            ]
        },
        "RequestId": "67838c79-2980-41cc-bae5-5fd5c7c4ab25"
    }
}
```

