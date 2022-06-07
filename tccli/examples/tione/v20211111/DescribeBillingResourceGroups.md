**Example 1: 查询资源组详情**



Input: 

```
tccli tione DescribeBillingResourceGroups --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values ems-dn6bqflh \
    --Filters.0.Name xx \
    --Filters.0.Negative True \
    --TagFilters.0.TagValues xx \
    --TagFilters.0.TagKey xx \
    --Limit 0 \
    --SearchWord xx \
    --Offset 0 \
    --Type xx
```

Output: 
```
{
    "Response": {
        "RequestId": "02be3c0f-d1f1-4a8e-97bd-38128985baa7",
        "TotalCount": 1,
        "ResourceGroupSet": [
            {
                "ResourceGroupId": "ersg-69q4tmjm",
                "ResourceGroupName": "hayescao_test",
                "TotalInstance": 1,
                "UsedResource": {},
                "TotalResource": {},
                "InstanceSet": [
                    {
                        "InstanceId": "eins-343vo66vf91c",
                        "UsedResource": {},
                        "TotalResource": {
                            "Cpu": 2000,
                            "Memory": 4096
                        },
                        "InstanceStatus": "RUNNING",
                        "AutoRenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                        "SpecId": "sv_tio_platform_cloud_pre_cpu_2c4g",
                        "SpecAlias": "2核4G"
                    }
                ]
            }
        ]
    }
}
```

