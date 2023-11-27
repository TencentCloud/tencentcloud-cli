**Example 1: 查询资源组节点列表**



Input: 

```
tccli tione DescribeBillingResourceGroup --cli-unfold-argument  \
    --ResourceGroupId abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --Offset 1 \
    --Limit 1 \
    --Order abc \
    --OrderField abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
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
                    "RealGpu": 1,
                    "RealGpuDetailSet": [
                        {
                            "Name": "abc",
                            "Value": 1
                        }
                    ]
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
                ]
            }
        ],
        "ResourceGroupSWType": "NORMAL",
        "RequestId": "abc"
    }
}
```

