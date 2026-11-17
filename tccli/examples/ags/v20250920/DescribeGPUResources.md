**Example 1: 查询GPU资源**

查询当前地域、当前租户的逐台 GPU 商业资源及占用状态。仅展示当前资源，不展示已销毁或补偿完成的失败资源；先筛选（含占用状态）再统计和分页。

Input: 

```
tccli ags DescribeGPUResources --cli-unfold-argument  \
    --ResourceGroupId gpug-example \
    --State Active \
    --AllocationState InUse \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Resources": [
            {
                "ResourceId": "ins-example-001",
                "ResourceGroupId": "gpug-example",
                "State": "Active",
                "AllocationState": "InUse",
                "InstanceId": "sandbox-example-001",
                "ActiveAt": "2026-10-21T10:00:00+08:00",
                "ExpireAt": "2026-11-21T10:00:00+08:00",
                "RenewFlag": 1,
                "StatusReason": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "request-example"
    }
}
```

