**Example 1: 按状态过滤 Version 列表**

Filter 支持 status、source_type；多值按 OR。

Input: 

```
tccli ags DescribeRegistryRecordVersionList --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name status \
    --Filters.0.Values APPROVED
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "VersionSet": [],
        "TotalCount": 0
    }
}
```

