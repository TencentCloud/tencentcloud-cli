**Example 1: 查询资源组详情**



Input: 

```
tccli tione DescribeBillingResourceGroups --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --TagFilters.0.TagKey abc \
    --TagFilters.0.TagValues abc \
    --Offset 0 \
    --Limit 0 \
    --SearchWord abc \
    --DontShowInstanceSet True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ResourceGroupSet": [
            {
                "ResourceGroupId": "abc",
                "ResourceGroupName": "abc",
                "FreeInstance": 1,
                "TotalInstance": 1,
                "UsedResource": {
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "GpuDetailSet": [
                        {
                            "Name": "abc",
                            "Value": 1
                        }
                    ]
                },
                "TotalResource": {
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "GpuDetailSet": [
                        {
                            "Name": "abc",
                            "Value": 1
                        }
                    ]
                },
                "InstanceSet": [
                    {
                        "InstanceId": "abc",
                        "UsedResource": {
                            "Cpu": 1,
                            "Memory": 1,
                            "Gpu": 1,
                            "GpuType": "abc",
                            "RealGpu": 1,
                            "RealGpuDetailSet": [
                                {
                                    "Name": "abc",
                                    "Value": 1
                                }
                            ]
                        },
                        "TotalResource": {
                            "Cpu": 1,
                            "Memory": 1,
                            "Gpu": 1,
                            "GpuType": "abc",
                            "RealGpu": 1
                        },
                        "InstanceStatus": "abc",
                        "SubUin": "abc",
                        "CreateTime": "abc",
                        "ExpireTime": "abc",
                        "AutoRenewFlag": "abc",
                        "SpecId": "abc",
                        "SpecAlias": "abc",
                        "SpecFeatures": [
                            "abc"
                        ],
                        "CvmInstanceId": "abc"
                    }
                ],
                "TagSet": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

