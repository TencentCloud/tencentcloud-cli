**Example 1: 查询资源组详情**



Input: 

```
tccli tione DescribeBillingResourceGroups --cli-unfold-argument  \
    --Filters.0.Name AvailableSort \
    --Filters.0.Values true \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --TagFilters.0.TagKey tag-a \
    --TagFilters.0.TagValues tag-a \
    --Offset 0 \
    --Limit 0 \
    --SearchWord hello-world \
    --DontShowInstanceSet True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ResourceGroupSet": [
            {
                "ResourceGroupId": "rsg-8c92bd27",
                "ResourceGroupName": "test-rsg-a",
                "FreeInstance": 1,
                "TotalInstance": 1,
                "UsedResource": {
                    "Cpu": 1,
                    "Memory": 1,
                    "Gpu": 1,
                    "GpuDetailSet": [
                        {
                            "Name": "A100",
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
                            "Name": "A100",
                            "Value": 1
                        }
                    ]
                },
                "InstanceSet": [],
                "TagSet": [
                    {
                        "TagKey": "tag-a",
                        "TagValue": "tag-b"
                    }
                ]
            }
        ],
        "RequestId": "a8410ded-4a5f-6ad1-6537-6a3462568017"
    }
}
```

